import pandas as pd

# Read the Excel file
df = pd.read_excel('2024_Analysis/Location/Location_2024_Final.xlsx')

# Print column names to debug
print("Column names in the dataset:")
print(df.columns.tolist())

# Print first few rows to understand structure
print("\nFirst few rows:")
print(df.head())

# Find rows containing 'AI' in the second column (Original Extracted Location)
ai_rows = df[df.iloc[:, 1].str.contains(r'\bAI\b', case=True, na=False)]
print(f"\nFound {len(ai_rows)} entries containing 'AI':")
print(ai_rows)

# For each AI row, replace AI with appropriate location
for idx in ai_rows.index:
    original_loc = df.iloc[idx, 1]
    parts = [p.strip() for p in original_loc.split('|')]
    clean_parts = [p for p in parts if p.strip().upper() != 'AI']
    
    if clean_parts:
        # Keep other locations if they exist
        df.iloc[idx, 1] = ' | '.join(clean_parts)  # Original Location
        if 'NY' in original_loc or 'New York' in original_loc:
            df.iloc[idx, 2] = 'New York, NY, USA'  # Normalized Location
            df.iloc[idx, 3] = 'New York, NY, USA'  # Formatted Address
        else:
            df.iloc[idx, 2] = 'Unknown'  # Normalized Location
            df.iloc[idx, 3] = 'Unknown'  # Formatted Address
    else:
        # If only AI was present
        df.iloc[idx, 1] = 'Unknown'  # Original Location
        df.iloc[idx, 2] = 'Unknown'  # Normalized Location
        df.iloc[idx, 3] = 'Unknown'  # Formatted Address
    
    # Clear coordinates
    df.iloc[idx, 4] = None  # Latitude
    df.iloc[idx, 5] = None  # Longitude

# Save the updated file
output_file = '2024_Analysis/Location/Location_2024_Final_Fixed.xlsx'
df.to_excel(output_file, index=False)
print(f"\nSaved updated file to: {output_file}")

# Print the fixed entries
print("\nFixed entries:")
print(df.iloc[ai_rows.index, [0,1,2,3]]) 
