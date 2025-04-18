import pdfplumber
import os

def process_table_row(row):
    """Process a single row to handle inconsistencies."""
    if len(row) < 4:  # Ensure the row has at least 4 columns
        return None  # Skip rows with insufficient columns
    # Clean and normalize the data
    return [cell.strip() if cell else "" for cell in row]

# Store the extracted data
word_data = []

with pdfplumber.open('K:/WORK/saurabh/SSC CGL/App_/book.pdf') as pdf:
    for page in pdf.pages:
        table = page.extract_table()
        if table:
            for row in table:
                processed_row = process_table_row(row)
                if processed_row:
                    serial_number, word, meaning, hindi = processed_row
                    # Append the data as a dictionary
                    word_data.append({
                        "Word": word,
                        "Meaning": meaning,
                        "Hindi": hindi
                    })

# Print the structured data
for entry in word_data:
    print(f"Word: {entry['Word']}")
    print(f"Meaning: {entry['Meaning']}")
    print(f"Hindi: {entry['Hindi']}")
    print("-" * 40)





