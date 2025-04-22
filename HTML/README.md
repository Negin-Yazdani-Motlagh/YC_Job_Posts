# HTMLs Folder

This folder contains the HTML content scraped from Hacker News "Who is Hiring" posts.

## Contents

- `html_content.json`: Contains the raw HTML content of Hacker News "Who is Hiring" posts, along with metadata such as URLs and timestamps.
- `html_save.log`: Log file containing information about the HTML scraping process, including success/failure status and any errors encountered.
- `save_html_content.py`: Script used to fetch and save the HTML content from Hacker News.

## URLs Being Scraped

The following URLs are being scraped for "Who is Hiring" posts:

1. https://news.ycombinator.com/submitted?id=whoishiring
2. https://news.ycombinator.com/submitted?id=whoishiring&next=39562986&n=31
3. https://news.ycombinator.com/submitted?id=whoishiring&next=35773707&n=61
4. https://news.ycombinator.com/submitted?id=whoishiring&next=31947297&n=91
5. https://news.ycombinator.com/submitted?id=whoishiring&next=28380661&n=121
6. https://news.ycombinator.com/submitted?id=whoishiring&next=24969524&n=151
7. https://news.ycombinator.com/submitted?id=whoishiring&next=22225313&n=181
8. https://news.ycombinator.com/submitted?id=whoishiring&next=19543939&n=211
9. https://news.ycombinator.com/submitted?id=whoishiring&next=17205866&n=241
10. https://news.ycombinator.com/submitted?id=whoishiring&next=14901314&n=271
11. https://news.ycombinator.com/submitted?id=whoishiring&next=12627853&n=301
12. https://news.ycombinator.com/submitted?id=whoishiring&next=10655741&n=331
13. https://news.ycombinator.com/submitted?id=whoishiring&next=8822808&n=361
14. https://news.ycombinator.com/submitted?id=whoishiring&next=7162197&n=391
15. https://news.ycombinator.com/submitted?id=whoishiring&next=4857717&n=421
16. https://news.ycombinator.com/submitted?id=whoishiring&next=2949790&n=451

## Data Structure

The `html_content.json` file contains an array of objects with the following structure:
```json
{
    "url": "https://news.ycombinator.com/...",
    "html": "<raw HTML content>",
    "timestamp": "ISO format timestamp",
    "error": "Error message (if any)"
}
```

## Usage

The HTML content in this folder is used as the source data for extracting job postings from Hacker News. The content is saved in JSON format for easy processing and analysis.

## Logging

The `html_save.log` file tracks:
- Success/failure of each HTML fetch
- Timestamps of operations
- Error messages and retry attempts
- Overall progress of the scraping process

## Related Files

- `URLs/hiring_urls.json`: Contains the list of URLs that were scraped
- `URLs/hiring_urls.log`: Contains logs from the URL extraction process 
