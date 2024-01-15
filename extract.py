import os
import re
from PyPDF2 import PdfReader
from tqdm import tqdm

# Define a function to extract emails from a given text using regex
def extract_emails(text):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    return re.findall(email_regex, text)

# Get the current script's directory
script_directory = os.path.dirname(os.path.abspath(__file__))

# Output text file where the emails will be saved
output_file = 'extracted_emails.txt'

# Error log file
error_log_file = 'error_log.txt'

# Function to process each PDF file and extract emails
def process_pdf(pdf_file_path):
    try:
        pdf_reader = PdfReader(pdf_file_path)
        extracted_text = ''

        for page in pdf_reader.pages:
            extracted_text += page.extract_text()

        emails = extract_emails(extracted_text)

        return emails
    except Exception as e:
        # Log the error and the PDF filename to the error log file
        with open(error_log_file, 'a') as error_log:
            error_log.write(f"Error processing PDF: {pdf_file_path} - {str(e)}\n")
        return []

# Get a list of PDF files in the same directory as the script
pdf_files = [filename for filename in os.listdir(script_directory) if filename.endswith('.pdf')]

# Create a tqdm progress bar
progress_bar = tqdm(total=len(pdf_files), unit=' PDF')

# Initialize an in-memory cache for emails
email_cache = []

# Iterate through the PDF files and extract emails
for filename in pdf_files:
    pdf_path = os.path.join(script_directory, filename)
    emails = process_pdf(pdf_path)
    email_cache.extend(emails)

    # Update the progress bar
    progress_bar.update(1)

# Close the progress bar
progress_bar.close()

# Write the extracted emails from the cache to the output file
with open(output_file, 'w') as text_file:
    for email in email_cache:
        text_file.write(email + '\n')

# Print a message
print(f"Extracted {len(email_cache)} emails. Saved to {output_file}")
