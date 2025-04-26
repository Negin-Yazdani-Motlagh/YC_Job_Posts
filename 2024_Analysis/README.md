# 2024 YC Job Posts Analysis

This folder contains scripts and data for analyzing Y Combinator job postings from 2024. The analysis extracts key information such as salary ranges, experience levels, locations, work types, and role types from job posts.

## Files Structure

- `2024_job_posts.json` - Raw job posting data scraped from Y Combinator
- `2024_job_details.xlsx` - Processed job details in Excel format
- `extract_job_details.py` - Python script for extracting and analyzing job details

## Code Structure

### Data Extraction (`extract_job_details.py`)

```python
# Key functions:
def extract_salary(text):
    # Extracts salary information using regex patterns
    # Handles formats like $100k-$200k, 100k USD, etc.
    # Returns standardized format or "Not specified"

def format_salary_to_k(salary_str):
    # Converts salary numbers to K format
    # Example: $100000 -> $100K
    # Handles ranges: $100000-$200000 -> $100K-$200K

def extract_work_type_and_location(text):
    # Separates work type (Remote/Hybrid/On-site) from physical locations
    # Returns tuple of (work_type, location_string)
```

### Excel Data Handling

```python
# Creating DataFrame
df = pd.DataFrame({
    'Salary Range': salary_ranges,
    'Experience Level': experience_levels,
    'Location': locations,
    'Work Type': work_types,
    'Role Type': role_types
})

# Saving to Excel
output_file = Path("2024_Analysis/2024_job_details.xlsx")
df.to_excel(output_file, index=False)
```

## Excel File Structure (`2024_job_details.xlsx`)

### Columns
1. **Salary Range**
   - Format: `$XXXK-$XXXK` or `$XXXK`
   - Examples: `$100K-$200K`, `$150K`
   - Implementation:
     ```python
     def format_salary_to_k(salary_str):
         # Converts raw salary to K format
         amount = int(salary)
         return f"${amount//1000}K"
     ```

2. **Experience Level**
   - Categories: Senior, Junior, Mid-level, Entry-level, etc.
   - Extraction pattern:
     ```python
     patterns = {
         'experience': r'(?:senior|junior|mid-level|entry-level|experienced|lead|principal|staff)'
     }
     ```

3. **Location**
   - Physical locations only (cities and countries)
   - Extraction patterns:
     ```python
     patterns = {
         'city_state': r'([A-Z][a-z]+(?: [A-Z][a-z]+)*),?\s+([A-Z]{2})',
         'city_only': r'(?:New York|San Francisco|...)',
         'country': r'(?:USA|United States|Canada|...)'
     }
     ```

4. **Work Type**
   - Categories: Remote, Hybrid, On-site
   - Extraction pattern:
     ```python
     patterns = {
         'work_arrangement': r'(?:remote|hybrid|on-site|in-office)'
     }
     ```

5. **Role Type**
   - Categories: Full-time, Part-time, Contract, etc.
   - Extraction pattern:
     ```python
     patterns = {
         'role_type': r'(?:full-time|part-time|contract|freelance|internship)'
     }
     ```

### Data Processing Pipeline

1. **Raw Data Loading**
   ```python
   with open("2024_job_posts.json", 'r', encoding='utf-8') as f:
       data = json.load(f)
   ```

2. **Information Extraction**
   - Process each post through extraction functions
   - Store results in respective lists

3. **DataFrame Creation**
   - Convert lists to pandas DataFrame
   - Organize data into structured columns

4. **Excel Generation**
   - Save DataFrame to Excel without index
   - Maintain data types and formatting

## Usage

To run the analysis:

```bash
python extract_job_details.py
```

This will:
1. Read job posts from `2024_job_posts.json`
2. Extract relevant information using regex patterns
3. Generate `2024_job_details.xlsx` with the analyzed data

## Excel Data Analysis Tips

1. **Filtering**
   - Use Excel filters to analyze specific categories
   - Filter by Work Type to see distribution of remote vs. on-site jobs
   - Filter by Location to analyze geographical distribution

2. **Salary Analysis**
   - Sort by Salary Range to see compensation trends
   - Use Excel formulas to calculate average ranges
   - Create pivot tables for salary distribution by experience level

3. **Experience Level Analysis**
   - Create pivot tables to see most common experience requirements
   - Cross-reference with salary ranges
   - Analyze by location and work type

4. **Location Analysis**
   - Use Excel's text functions to analyze city/country distribution
   - Create pivot tables for geographical clustering
   - Analyze salary ranges by location

5. **Work Type Analysis**
   - Calculate percentage distribution of remote/hybrid/on-site roles
   - Cross-reference with experience levels and salaries
   - Analyze trends by location

## Data Quality Notes

- Salary ranges are standardized to K format for consistency
- Location data separates physical locations from work arrangements
- Missing data is marked as "Not specified"
- Regular expressions are case-insensitive for better matching 
