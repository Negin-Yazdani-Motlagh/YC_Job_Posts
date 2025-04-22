# Hacker News "Who is Hiring?" HTML Content Collection

This directory contains the raw HTML content of all "Who is Hiring?" posts from Hacker News (2012-2024).

## Contents

- `hiring_posts_html.json`: A JSON file containing the HTML content of all "Who is Hiring?" posts

## Data Structure

The `hiring_posts_html.json` file contains an array of objects with the following structure:

```json
{
    "title": "Ask HN: Who is hiring? (Month Year)",
    "url": "https://news.ycombinator.com/item?id=XXXXX",
    "html_content": "<full HTML content of the post>"
}
```

## Collection Process

The HTML content was collected using the following process:
1. Reading URLs from `who_is_Hiring/all_hiring_posts.json`
2. Fetching HTML content from each URL using Python's requests library
3. Parsing the HTML using BeautifulSoup
4. Storing the content in a structured JSON format

## Technical Details

- **Data Source**: Hacker News (https://news.ycombinator.com)
- **Time Range**: 2012-2024
- **Total Posts**: 153
- **Collection Method**: Automated web scraping with rate limiting
- **HTML Parser**: BeautifulSoup4
- **Encoding**: UTF-8

## Usage

This HTML content can be used for:
- Detailed analysis of job postings
- Extracting specific information from posts
- Studying the evolution of job posting formats
- Training machine learning models
- Historical research of tech job market

## Notes

- The HTML content is stored in its original form
- Each request included a 2-second delay to be respectful to the server
- Error handling was implemented for failed requests
- User-Agent headers were used to mimic browser behavior

## Data Source

All HTML content is sourced from Hacker News (https://news.ycombinator.com) "Who is Hiring?" threads. 
