# Hacker News Hiring Threads Scraper

This project contains a Python script that scrapes and analyzes the monthly "Who is hiring?" threads from Hacker News.

## Overview

The scraper collects data from Hacker News' monthly hiring threads, which are posted by the user "whoishiring". It extracts information about each thread including:
- Title
- URL
- Month
- Year

## Features

- Fetches all hiring threads from Hacker News API
- Extracts month and year information from thread titles
- Saves results to a JSON file
- Provides statistics about the collected threads
- Identifies missing months in the data
- Includes error handling and rate limiting

## Requirements

- Python 3.x
- Required Python packages:
  - requests
  - json
  - datetime
  - time
  - re

## Usage

1. Run the script:
```bash
python scrape_hiring_threads.py
```

2. The script will:
   - Fetch all hiring threads from Hacker News
   - Save them to `all_hiring_threads.json`
   - Print statistics about the collected threads
   - Show the most recent threads

## Output

The script generates a JSON file (`all_hiring_threads.json`) containing an array of thread objects, each with:
- `title`: The thread title
- `url`: The URL to the thread
- `month`: The month the thread was posted
- `year`: The year the thread was posted

## Statistics

The script provides the following statistics:
- Total number of threads found
- Number of threads per year
- Identification of years with missing months

## Notes

- The script includes a small delay (0.1 seconds) between API requests to be polite to the Hacker News API
- Threads from 2011 and 2025 are skipped
- The script handles various error cases and continues processing even if some threads fail to load 
