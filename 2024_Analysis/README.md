# Location Extraction and Geocoding for YC Job Posts (2024)

This project provides a script, `extract_job_details_loaction.py`, for extracting, normalizing, and geocoding location information from Y Combinator job posts. The script processes job post data, identifies valid locations, geocodes them using the Google Maps Geocoding API, and outputs a clean Excel file with all relevant location details.

## Features
- Extracts all valid locations (cities, states, countries, regions) from job post headers and bodies
- Expands common city abbreviations (e.g., SF → San Francisco)
- Normalizes location names for consistency
- Geocodes locations to obtain formatted addresses and coordinates (latitude, longitude) using the Google Maps Geocoding API
- Removes all case variations of the word "remote" from the final output
- Outputs a comprehensive Excel file for further analysis

## Requirements
- Python 3.7+
- Packages: `pandas`, `requests`, `geonamescache`, `pycountry`, `openpyxl`
- A Google Maps Geocoding API key

Install dependencies with:
```bash
pip install pandas requests geonamescache pycountry openpyxl
```

## Usage
1. Place your job post data file (e.g., `2024_job_posts.json`) in the same directory or update the script path.
2. Set your Google Maps Geocoding API key in the script (variable `API_KEY`).
3. Run the script:
   ```bash
   python extract_job_details_loaction.py
   ```
4. The output Excel file will be saved as `Location_2024_Final.xlsx` in the same directory.

## Output
The resulting Excel file contains the following columns for each job post:
- **Post #**: The post number
- **Original Extracted Location**: All extracted location strings
- **Normalized Location**: Cleaned and standardized location names
- **Formatted Address**: Google-formatted address (if geocoded)
- **Latitude**: Latitude (if geocoded)
- **Longitude**: Longitude (if geocoded)

All instances of "remote" (in any case) are removed from the output.

## Notes
- The script skips geocoding for major regions and the word "remote".
- If a location cannot be geocoded, the address and coordinates will be left blank.
- For best results, ensure your job post data is well-formatted and includes clear location information.

## License
This project is for educational and research purposes. Please respect the terms of use for the Google Maps Geocoding API. 
