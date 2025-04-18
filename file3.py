import pymupdf  # PyMuPDF
import json

# Open the PDF file
pdf_path = 'K:/WORK/saurabh/SSC CGL/App_/book.pdf'
doc = pymupdf.open(pdf_path)

# Select page #8 (zero-indexed, so page 8 is index 7)
page = doc[7]

# Extract text from the page
blocks = page.get_text("blocks", sort=True)  # Extract blocks of text
word_data = []

# Process each block to extract table-like data
for block in blocks:
    block_text = block[4]  # The actual text content of the block
    lines = block_text.split("\n")  # Split block into lines
    for line in lines:
        columns = line.split("\t")  # Split line into columns (assuming tab-separated data)
        if len(columns) == 5:  # Ensure the row has exactly 5 columns
            serial_number, word, meaning, hindi, repetition_count = columns
            word_data.append({
                "Serial Number": serial_number.strip(),
                "Word": word.strip(),
                "Meaning": meaning.strip(),
                "Hindi": hindi.strip(),
                "Repetition Count": repetition_count.strip()
            })

# Save the extracted data as a JSON file
json_file_path = 'K:/WORK/saurabh/SSC CGL/App_/flashcards_page8.json'
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(word_data, json_file, ensure_ascii=False, indent=4)

print(f"Data from page #8 has been saved as JSON: {json_file_path}")

# Close the PDF document
doc.close()