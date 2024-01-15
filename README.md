# PDF-Email-extractor
#### This Python script extracts email addresses from a collection of PDF files in a specified directory. It uses the PyPDF2 library for reading PDF content and the tqdm library for displaying a progress bar during extraction.

## Usage

1. Ensure you have the necessary dependencies installed:

   ```bash
   pip install PyPDF2 tqdm

2. Place your PDF files in the same directory as the script.
   
3. Run the script:

   ```bash
   python extract.py

## Output

1. Extracted emails will be saved to extracted_emails.txt.
2. Errors encountered during extraction will be logged in error_log.txt.


## Features

1. Cache Mechanism: The script implements an in-memory cache to optimize email extraction from multiple PDFs, reducing redundant processing.

2. Error Logging: Any errors encountered during the extraction process are logged in error_log.txt. This helps identify issues with specific PDF files.

3. Progress Bar: The script displays a progress bar using tqdm, providing real-time feedback on the extraction progress for better user experience.


#### Feel free to customize the script to suit your specific needs. If you encounter issues or have suggestions for improvements, please open an issue on GitHub.
