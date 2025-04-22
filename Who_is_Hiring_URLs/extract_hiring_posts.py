import json
import os
from bs4 import BeautifulSoup
from datetime import datetime
import re
from pathlib import Path

def extract_hiring_posts():
    # Create who_is_Hiring directory if it doesn't exist
    output_dir = Path("who_is_Hiring")
    output_dir.mkdir(exist_ok=True)
    
    # Read the HTML content
    with open("HTMLs/HTML_All_Titles.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Initialize dictionary to store posts by year
    posts_by_year = {}
    
    # Process each HTML content
    for entry in data:
        html_content = entry["html"]
        soup = BeautifulSoup(html_content, "html.parser")
        
        # Find all story links
        for story in soup.find_all("tr", class_="athing"):
            title_elem = story.find("span", class_="titleline")
            if not title_elem:
                continue
                
            title = title_elem.get_text()
            if "who is hiring" in title.lower():
                # Extract the date from the next row
                subtext = story.find_next_sibling("tr").find("span", class_="age")
                if not subtext:
                    continue
                    
                date_str = subtext.get("title", "")
                try:
                    date = datetime.fromisoformat(date_str.split()[0])
                    year = date.year
                    
                    # Extract URL
                    url = title_elem.find("a")["href"]
                    if not url.startswith("http"):
                        url = f"https://news.ycombinator.com/{url}"
                    
                    # Store post data
                    post_data = {
                        "title": title,
                        "url": url,
                        "date": date.isoformat(),
                        "points": story.find_next_sibling("tr").find("span", class_="score").get_text() if story.find_next_sibling("tr").find("span", class_="score") else "0 points",
                        "comments": story.find_next_sibling("tr").find("a", href=lambda x: x and "item?id=" in x).get_text() if story.find_next_sibling("tr").find("a", href=lambda x: x and "item?id=" in x) else "0 comments"
                    }
                    
                    if year not in posts_by_year:
                        posts_by_year[year] = []
                    posts_by_year[year].append(post_data)
                except (ValueError, AttributeError):
                    continue
    
    # Save posts by year
    for year, posts in posts_by_year.items():
        year_dir = output_dir / str(year)
        year_dir.mkdir(exist_ok=True)
        
        # Save posts to JSON file
        with open(year_dir / f"hiring_posts_{year}.json", "w", encoding="utf-8") as f:
            json.dump(posts, f, indent=2)
        
        # Create README for the year
        with open(year_dir / "README.md", "w", encoding="utf-8") as f:
            f.write(f"# Who is Hiring? Posts for {year}\n\n")
            f.write("| Date | Title | Points | Comments |\n")
            f.write("|------|-------|--------|----------|\n")
            for post in sorted(posts, key=lambda x: x["date"], reverse=True):
                date = datetime.fromisoformat(post["date"]).strftime("%Y-%m-%d")
                f.write(f"| {date} | [{post['title']}]({post['url']}) | {post['points']} | {post['comments']} |\n")
    
    # Create main README
    with open(output_dir / "README.md", "w", encoding="utf-8") as f:
        f.write("# Who is Hiring? Data Collection\n\n")
        f.write("This folder contains Hacker News \"Who is hiring?\" posts organized by year.\n\n")
        f.write("## Available Years\n\n")
        for year in sorted(posts_by_year.keys(), reverse=True):
            f.write(f"- [{year}]({year}/README.md) - {len(posts_by_year[year])} posts\n")

if __name__ == "__main__":
    extract_hiring_posts() 
