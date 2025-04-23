# Long Job Posts Analysis

This directory contains analysis of the longest job posts from Hacker News "Who is Hiring?" threads, organized by month and year.

## Contents

- `longest_posts.json`: Contains the longest job post for each month, with the following structure:
  ```json
  {
      "2012-December": {
          "length": 3550,
          "content": "longest post content..."
      },
      "2013-January": {
          "length": 6777,
          "content": "longest post content..."
      }
  }
  ```

## Key Findings

- **Longest Post**: May 2013 (343,459 characters) - Note: This appears to be an outlier and may contain data anomalies
- **Recent Trends**: 
  - 2022 had consistently long posts (6,500-6,800 characters)
  - 2023 posts were generally shorter (3,300-4,000 characters)
  - 2024 posts are showing a mix of lengths (2,600-4,600 characters)

## Notable Observations

1. **Length Variations**:
   - Early years (2012-2014) showed more variation in post lengths
   - Recent years (2021-2024) show more consistent lengths within each year
   - Average post length has generally increased over time

2. **Yearly Patterns**:
   - 2021-2022: Peak in post lengths (6,500-6,800 characters)
   - 2023: Significant decrease in average length
   - 2024: Moderate increase from 2023 levels

## Usage

This data can be used for:
- Analyzing trends in job posting length over time
- Studying the evolution of job descriptions
- Comparing posting styles across different periods
- Understanding changes in hiring communication patterns

## Notes

- All posts have been cleaned of HTML tags and formatting
- Length is measured in characters
- Only the longest post from each month is included
- Data spans from 2012 to 2024 
