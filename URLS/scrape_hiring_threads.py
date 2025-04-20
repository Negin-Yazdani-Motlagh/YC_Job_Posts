import requests
import json
from datetime import datetime
import time
import re

def get_hiring_threads():
    """Get all hiring threads from Hacker News"""
    threads = []
    base_url = "https://hacker-news.firebaseio.com/v0"
    
    # Get user data for whoishiring
    user_url = f"{base_url}/user/whoishiring.json"
    try:
        print("Fetching whoishiring's submissions...")
        response = requests.get(user_url)
        response.raise_for_status()
        user_data = response.json()
        
        if 'submitted' not in user_data:
            print("No submissions found!")
            return threads
            
        total_submissions = len(user_data['submitted'])
        print(f"Found {total_submissions} total submissions")
        
        # Process all submissions
        for i, item_id in enumerate(user_data['submitted'], 1):
            try:
                print(f"\nProcessing submission {i}/{total_submissions} (ID: {item_id})")
                
                # Get thread data from API
                item_url = f"{base_url}/item/{item_id}.json"
                item_response = requests.get(item_url)
                item_response.raise_for_status()
                item_data = item_response.json()
                
                if not item_data:
                    print(f"  No data returned for {item_id}")
                    continue
                    
                if 'title' not in item_data:
                    print(f"  No title found for {item_id}")
                    continue
                    
                title = item_data['title']
                print(f"  Title: {title}")
                
                # Case-insensitive check for "Who is hiring?"
                if not re.search(r'who\s+is\s+hiring', title, re.IGNORECASE):
                    print(f"  Not a hiring thread")
                    continue
                    
                # Extract year and month from title
                year_match = re.search(r'\((\w+)\s+(\d{4})\)', title)
                if not year_match:
                    print(f"  Could not extract date from title")
                    continue
                    
                month, year = year_match.groups()
                year = int(year)
                
                # Skip 2011 and 2025
                if year == 2011 or year == 2025:
                    print(f"  Skipping year {year}")
                    continue
                    
                thread_data = {
                    'title': title,
                    'url': f"https://news.ycombinator.com/item?id={item_id}",
                    'month': month,
                    'year': year
                }
                threads.append(thread_data)
                print(f"  Added thread: {month} {year}")
                
                # Be polite to the API
                time.sleep(0.1)
                
            except requests.exceptions.RequestException as e:
                print(f"Error fetching item {item_id}: {e}")
                continue
            except Exception as e:
                print(f"Error processing item {item_id}: {e}")
                continue
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching user data: {e}")
    
    return threads

def analyze_threads(threads):
    """Analyze the threads and print statistics"""
    if not threads:
        return
        
    # Count threads by year
    year_counts = {}
    for thread in threads:
        year = thread['year']
        year_counts[year] = year_counts.get(year, 0) + 1
    
    # Print statistics
    print("\nStatistics:")
    print(f"Total threads found: {len(threads)}")
    print("\nThreads per year:")
    for year in sorted(year_counts.keys()):
        print(f"  {year}: {year_counts[year]} threads")
    
    # Find years with missing months
    print("\nYears with missing months:")
    for year in sorted(year_counts.keys()):
        year_threads = [t for t in threads if t['year'] == year]
        months = set(t['month'] for t in year_threads)
        if len(months) < 12:
            missing = sorted(set(['January', 'February', 'March', 'April', 'May', 'June', 
                                'July', 'August', 'September', 'October', 'November', 'December']) - months)
            print(f"  {year}: Missing {', '.join(missing)}")

def main():
    print("Fetching all hiring threads...")
    threads = get_hiring_threads()
    
    if threads:
        # Sort threads by year and month
        threads.sort(key=lambda x: (x['year'], datetime.strptime(x['month'], '%B').month))
        
        # Save the results to a JSON file
        with open('all_hiring_threads.json', 'w', encoding='utf-8') as f:
            json.dump(threads, f, indent=4, ensure_ascii=False)
        
        print("\nResults saved to all_hiring_threads.json")
        
        # Analyze threads
        analyze_threads(threads)
        
        # Print sample of most recent threads
        print("\nMost recent threads:")
        for thread in sorted(threads, key=lambda x: (x['year'], datetime.strptime(x['month'], '%B').month), reverse=True)[:5]:
            print(f"- {thread['title']}")
            print(f"  URL: {thread['url']}")
    else:
        print("\nNo threads were found!")

if __name__ == "__main__":
    main() 
