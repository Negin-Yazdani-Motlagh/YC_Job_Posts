# Hacker News "Who is Hiring?" Posts Collection

This repository contains a collection of Hacker News "Who is Hiring?" posts from 2012 to 2024.

## Data Structure

The main data file `all_hiring_posts.json` contains a list of all "Who is Hiring?" posts with the following structure:

```json
{
    "title": "Ask HN: Who is hiring? (Month Year)",
    "url": "https://news.ycombinator.com/item?id=XXXXX"
}
```

## Contents

- `all_hiring_posts.json`: Combined file containing all "Who is Hiring?" posts from 2012-2024
- Individual year directories (2012-2024) containing:
  - `hiring_posts_YYYY.json`: Original posts for that year
  - `README.md`: Year-specific information

## Statistics

- Total number of posts: 153
- Time range: 2012-2024
- Posts per year: Approximately 12 (one per month)

## Usage

The data can be used for:
- Analyzing job market trends
- Tracking hiring patterns over time
- Researching tech industry employment
- Historical analysis of job postings

## Data Source

All data is sourced from Hacker News (https://news.ycombinator.com) "Who is Hiring?" threads.
