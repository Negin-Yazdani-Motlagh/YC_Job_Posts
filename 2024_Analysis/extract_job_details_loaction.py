"""
Location Extraction and Geocoding Script for YC Job Posts (2024)

This script extracts valid location information from job post headers and bodies, normalizes and geocodes them, removes all case variations of 'remote', and outputs the results to an Excel file.
Output file: Location_2024_Final.xlsx
"""
import json
import re
import requests
import time
import geonamescache
import pycountry
import pandas as pd
from pathlib import Path

gc = geonamescache.GeonamesCache()
city_data = gc.get_cities()
city_names = set(city['name'].lower() for city in city_data.values())
country_names = {country.name.lower(): country.name for country in pycountry.countries}
country_codes = {country.alpha_2.lower(): country.name for country in pycountry.countries}

# US state code to state name
us_states = {
    'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California', 'CO': 'Colorado',
    'CT': 'Connecticut', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia', 'HI': 'Hawaii', 'ID': 'Idaho',
    'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa', 'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana',
    'ME': 'Maine', 'MD': 'Maryland', 'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi',
    'MO': 'Missouri', 'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey',
    'NM': 'New Mexico', 'NY': 'New York', 'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio', 'OK': 'Oklahoma',
    'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota',
    'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont', 'VA': 'Virginia', 'WA': 'Washington',
    'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming', 'DC': 'District of Columbia'
}

us_state_codes = {k.lower(): v for k, v in us_states.items()}

# Common city abbreviations
city_abbr = {
    'SF': 'San Francisco',
    'NYC': 'New York City',
    'LA': 'Los Angeles',
    'DC': 'Washington',
}

# Major regions to always include
major_regions = set([
    'remote', 'north america', 'south america', 'europe', 'asia', 'africa', 'australia', 'apac', 'emea', 'global'
])

# Helper to check if a city/state combo is valid (US only)
def is_valid_us_city_state(city, state):
    for city_id, city_info in city_data.items():
        if city_info['name'].lower() == city.lower() and city_info['admin1code'].lower() == state.lower():
            return True
    return False

def normalize_location(loc):
    loc = re.sub(r'^(hybrid|onsite|remote)?\s*in\s+', '', loc, flags=re.IGNORECASE).strip()
    if ',' in loc:
        city, rest = [x.strip() for x in loc.split(',', 1)]
        rest_upper = rest.upper()
        rest_lower = rest.lower()
        if rest_upper in us_states:
            state_full = us_states[rest_upper]
            if city.lower() in city_names:
                return f"{city}, {state_full}, USA"
        elif rest_lower in country_codes:
            country_full = country_codes[rest_lower]
            if city.lower() in city_names:
                return f"{city}, {country_full}"
        elif rest_lower in country_names:
            if city.lower() in city_names:
                return f"{city}, {country_names[rest_lower]}"
        elif rest_lower in (v.lower() for v in us_states.values()):
            if city.lower() in city_names:
                return f"{city}, {rest}, USA"
    else:
        loc_lower = loc.lower()
        if loc_lower in city_names:
            return loc.title()
        elif loc_lower in country_names:
            return country_names[loc_lower]
        elif loc_lower in country_codes:
            return country_codes[loc_lower]
        elif (loc_upper := loc.upper()) in us_states:
            return f"{us_states[loc_upper]}, USA"
        elif loc_lower in major_regions:
            return loc.title()
        elif loc_lower == 'remote':
            return 'Remote'
    return None

def expand_abbreviations(text):
    for abbr, full in city_abbr.items():
        text = re.sub(rf'\b{abbr}\b', full, text)
    return text

def debug_post_4(post):
    print('--- Debugging Post 4 ---')
    header = post.split('\n')[0]
    print('Header:', header)
    header = expand_abbreviations(header)
    print('Header after abbreviation expansion:', header)
    # Find the part with locations (the third |-separated part)
    parts = [p.strip() for p in header.split('|')]
    print('Header parts:', parts)
    if len(parts) > 2:
        loc_part = parts[2]
        print('Location part:', loc_part)
        # Extract parenthetical (e.g., (North America))
        parenthetical = re.findall(r'\(([^)]+)\)', loc_part)
        print('Parenthetical:', parenthetical)
        # Remove parenthetical from loc_part
        loc_part_clean = re.sub(r'\(.*?\)', '', loc_part)
        # Split on commas
        locs = [l.strip() for l in loc_part_clean.split(',') if l.strip()]
        # Add parenthetical as a separate location
        if parenthetical:
            locs.extend([p.strip() for p in parenthetical])
        print('Final extracted locations:', locs)
    print('----------------------')

def is_location(val):
    val_lower = val.lower()
    if val_lower in city_names:
        return True
    if val_lower in country_names:
        return True
    if val_lower in country_codes:
        return True
    if val_lower in us_state_codes:
        return True
    if val_lower in (v.lower() for v in us_states.values()):
        return True
    if val_lower in major_regions:
        return True
    if val_lower == 'remote':
        return True
    # Check for city, state or city, country patterns
    if ',' in val:
        city, rest = [x.strip() for x in val.split(',', 1)]
        if city.lower() in city_names:
            if rest.lower() in us_state_codes or rest.lower() in (v.lower() for v in us_states.values()):
                return True
            if rest.lower() in country_names or rest.lower() in country_codes:
                return True
    return False

def extract_all_locations(post):
    header = post.split('\n')[0]
    header = expand_abbreviations(header)
    parts = [p.strip() for p in header.split('|')]
    locs = set()
    for part in parts:
        # Extract parentheticals
        parenthetical = re.findall(r'\(([^)]+)\)', part)
        part_clean = re.sub(r'\(.*?\)', '', part)
        # Split on commas
        comma_locs = [l.strip() for l in part_clean.split(',') if l.strip()]
        for l in comma_locs:
            if is_location(l):
                locs.add(l)
        for p in parenthetical:
            if is_location(p.strip()):
                locs.add(p.strip())
    # Also scan the body for City, Country/State patterns
    body = expand_abbreviations(post)
    for match in re.finditer(r'([A-Za-z .-]+,\s*[A-Za-z .-]+)', body):
        val = match.group(0).strip()
        if len(val) > 4 and len(val.split()) <= 4 and is_location(val):
            locs.add(val)
    return sorted(locs)

def geocode_location(location_text, api_key):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {'address': location_text, 'key': api_key}
    print(f"Querying: {base_url}?address={location_text.replace(' ', '+')}&key=API_KEY")
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        print(f"Full API response for '{location_text}':\n{json.dumps(data, indent=2)}\n")
        if data['status'] == 'OK':
            result = data['results'][0]
            formatted = result['formatted_address']
            lat = result['geometry']['location']['lat']
            lng = result['geometry']['location']['lng']
            return formatted, lat, lng
        else:
            return None, None, None
    except Exception as e:
        print(f"Error geocoding {location_text}: {str(e)}")
        return None, None, None

def remove_remote_from_df(df):
    import re
    return df.applymap(lambda x: re.sub(r'\bremote\b', '', x, flags=re.IGNORECASE).strip() if isinstance(x, str) else x)

def main():
    API_KEY = "Google Maps"
    with open("2024_Analysis/2024_job_posts.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    posts = data["YC"]["2024"]["comments"]
    debug_post_4(posts[3])
    results = []
    for idx, post in enumerate(posts):
        all_locs = extract_all_locations(post)
        origs, norms, addrs, lats, lngs = [], [], [], [], []
        for loc in all_locs:
            norm = normalize_location(loc)
            if norm and (norm.lower() in major_regions or norm.lower() == 'remote'):
                formatted, lat, lng = norm, '', ''
            elif norm:
                formatted, lat, lng = geocode_location(norm, API_KEY)
                time.sleep(0.1)
            else:
                formatted, lat, lng = '', '', ''
            origs.append(loc)
            norms.append(norm or loc)
            addrs.append(formatted or '')
            lats.append(str(lat) if lat else '')
            lngs.append(str(lng) if lng else '')
        results.append({
            'Post #': f'Post {idx+1}',
            'Original Extracted Location': ' | '.join(origs),
            'Normalized Location': ' | '.join(norms),
            'Formatted Address': ' | '.join(addrs),
            'Latitude': ' | '.join(lats),
            'Longitude': ' | '.join(lngs)
        })
    df = pd.DataFrame(results)
    df = remove_remote_from_df(df)
    output_file = Path('2024_Analysis/Location_2024_Final.xlsx')
    df.to_excel(output_file, index=False)
    print(f"Saved all geocoded locations to: {output_file}")

if __name__ == "__main__":
    main() 
