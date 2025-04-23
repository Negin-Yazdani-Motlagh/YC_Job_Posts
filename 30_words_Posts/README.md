# 30 Words or Less Job Posts

This directory contains a filtered subset of Hacker News "Who is Hiring?" posts that are 30 words or less in length.

## Contents

- `0_30_words_posts.json`: Contains all job postings that are 30 words or less, organized by month and year
  - Structure:
  ```json
  {
      "YC": {
          "2012-December": {
              "comments": ["short job posting 1", "short job posting 2", ...],
              "numJobPost": 123
          },
          "2013-January": {
              "comments": [...],
              "numJobPost": ...
          }
      }
  }
  ```

## Statistics

- Total Short Posts: 2,168
- Time Range: 2012-2024
- Posts per Month: Varies
- Data Format: Cleaned and structured

## Purpose

This filtered dataset is useful for:
- Analyzing very brief job postings
- Studying the effectiveness of concise job descriptions
- Comparing short vs. long job postings
- Understanding minimal viable job descriptions

## Notes

- Only includes posts with 30 words or less
- Maintains the same structure as the original dataset
- Only includes months that have at least one short post
- Preserves the chronological organization of the original data 
