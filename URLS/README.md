# URLs Folder

This folder contains scraped job posting URLs from Hacker News "Who is Hiring" threads.

## Contents

- `All_URLs.txt`: Contains all unique job posting URLs collected from Hacker News
- `hacker_news_urls.txt`: Alternative collection of job posting URLs

## Purpose

The URLs in these files are collected from Hacker News' monthly "Who is Hiring" threads. These threads are a popular source for tech job postings, particularly for startups and tech companies.

## How to Use

1. Each URL in the files points to a specific job posting on Hacker News
2. URLs are sorted alphabetically for easy reference
3. Each URL is on a new line
4. URLs follow the format: `https://news.ycombinator.com/item?id=XXXXX`

## Data Collection

The URLs are collected using automated web scraping scripts that:
- Navigate through Hacker News "Who is Hiring" threads
- Extract unique job posting URLs
- Filter for relevant job-related content
- Save the results to text files

## Notes

- URLs are collected periodically and may not represent the most current job postings
- Some URLs may no longer be active
- The collection includes various types of job-related posts:
  - "Who is Hiring" posts
  - "Freelancer Seeking" posts
  - "Who Wants to be Hired" posts

## Maintenance

The URLs are automatically collected and updated by the scraping scripts. To update the collection:
1. Run the scraping script
2. New URLs will be added to the existing collection
3. Duplicate URLs are automatically filtered out 
