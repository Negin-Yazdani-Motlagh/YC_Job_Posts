# Hacker News "Who is Hiring?" Posts Collection

This repository contains a collection of Hacker News "Who is Hiring?" posts from 2012 to 2024, along with the scripts used to collect and process the data.

## Code Overview

### Scripts

1. `extract_hiring_posts.py`
   - Main script for extracting "Who is Hiring?" posts from Hacker News
   - Uses BeautifulSoup to parse HTML content
   - Extracts post titles, URLs, dates, points, and comment counts
   - Organizes posts by year in separate directories

2. `combine_hiring_posts.py`
   - Combines all yearly posts into a single JSON file
   - Removes unnecessary fields (date, points, comments)
   - Sorts posts chronologically
   - Creates a simplified version with only title and URL

### Dependencies
- Python 3.x
- BeautifulSoup4
- requests
- json
- pathlib

## Data Structure

The main data file `all_hiring_posts.json` contains a list of all "Who is Hiring?" posts with the following structure:

```json
{
    "title": "Ask HN: Who is hiring? (Month Year)",
    "url": "https://news.ycombinator.com/item?id=XXXXX"
}
```

## Directory Structure

```
who_is_Hiring/
├── all_hiring_posts.json          # Combined posts (2012-2024)
├── extract_hiring_posts.py        # Main extraction script
├── combine_hiring_posts.py        # Post combination script
├── requirements.txt               # Python dependencies
└── [year]/                        # Year directories (2012-2024)
    ├── hiring_posts_YYYY.json     # Original posts for the year
    └── README.md                  # Year-specific information
```

## Data Collection Process

1. **Initial Extraction** (`extract_hiring_posts.py`)
   - Scrapes Hacker News for "Who is Hiring?" posts
   - Extracts post metadata and content
   - Saves posts in yearly directories

2. **Data Processing** (`combine_hiring_posts.py`)
   - Combines all yearly posts into a single file
   - Removes unnecessary fields
   - Ensures consistent data format
   - Creates a clean, simplified dataset


## Usage

The data can be used for:
- Analyzing job market trends
- Tracking hiring patterns over time
- Researching tech industry employment
- Historical analysis of job postings

## Data Source

All data is sourced from Hacker News (https://news.ycombinator.com) "Who is Hiring?" threads.

## Running the Scripts

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the extraction script:
   ```bash
   python extract_hiring_posts.py
   ```

3. Combine the posts:
   ```bash
   python combine_hiring_posts.py
   ```
