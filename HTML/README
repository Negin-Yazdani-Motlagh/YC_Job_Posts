# Hacker News "Who is Hiring?" HTML Content

This directory contains the raw HTML content of all "Who is Hiring?" threads from Hacker News, spanning from January 2012 to December 2024.

## Contents

- `hiring_thread_[Month]_[Year].html` - Individual HTML files for each thread
- `all_threads_combined.json` - Combined JSON file containing all threads
- `extract_html_content.py` - Script used to extract and process the HTML content

## File Details

### Individual HTML Files
- Format: `hiring_thread_[Month]_[Year].html`
- Size: Varies from ~1MB to ~2.5MB per file
- Content: Raw HTML of the entire thread page
- Encoding: UTF-8
- Total Files: 163 (one for each month from 2012-2024)

### Combined JSON File
- Name: `all_threads_combined.json`
- Size: ~238MB
- Format: Array of objects with the following structure:
  ```json
  {
    "month": "January",
    "year": "2012",
    "filename": "hiring_thread_January_2012.html",
    "content": "<html>...</html>"
  }
  ```

## Extraction Process

The HTML content was extracted using `extract_html_content.py`, which:

1. Loads thread URLs from `../URLs/all_hiring_threads.json`
2. For each thread:
   - Fetches the HTML content using a custom User-Agent
   - Saves the content to an individual HTML file
   - Includes a 1-second delay between requests
3. Combines all HTML files into a single JSON file
4. Saves the extraction script in this directory

## Usage Notes

- The HTML files contain the complete thread content, including all comments
- Files are named consistently for easy reference
- The combined JSON file makes it easy to process all threads programmatically
- All content is saved with UTF-8 encoding to handle special characters

## Technical Details

- Extraction Script: Python 3.x
- Required Libraries:
  - requests
  - beautifulsoup4
  - urllib3
- User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36

## Data Quality

- All threads from 2012-2024 are included
- Some threads may have missing or incomplete content due to:
  - Server errors during extraction
  - Deleted or removed content
  - Rate limiting restrictions

## Future Analysis

This data can be used for:
- Job posting analysis
- Technology trend tracking
- Company hiring pattern analysis
- Geographic distribution of job opportunities
- Salary and benefit trend analysis 
