# PDF_To_Text_Extractor

## PDF Text Extraction Script

This script utilizes the `PyPDF2` library to extract text from PDF files and save it to a text file. It's designed to handle both encrypted and unencrypted PDFs, providing a straightforward way to extract text data for further processing or analysis.

### How It Works

1. **Open the PDF File**: The script opens the PDF file in binary read mode.
   ```python
   with open(pdf_path, 'rb') as file:
   ```
Create a PDF Reader Object: Utilizes PyPDF2.PdfFileReader to create an object for reading the PDF.
```
pdf_reader = PyPDF2.PdfFileReader(file)
```
Check for Encryption: Before extracting text, it checks if the PDF is encrypted.
```
if pdf_reader.isEncrypted:
```
Attempt to Decrypt: Tries to decrypt the PDF using an empty password, as some PDFs are encrypted in a way that can be bypassed with no password.
```
pdf_reader.decrypt('')
```
If decryption fails or the PDF is encrypted in a way that requires a non-empty password, the script prints an error message and stops execution.
Extract Text from Each Page: Iterates through each page of the PDF, extracting the text and appending it to a string variable.
```
for page_num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(page_num)
    text += page.extractText()
```
Save the Extracted Text: Writes the concatenated text to an output file specified by the user.
```
with open(output_file, 'w', encoding='utf-8') as out:
    out.write(text)
```
Usage
To use the script, simply run it and provide the path to the PDF file when prompted. The script will then extract the text and save it to extracted_text.txt.
```
python extract_text_from_pdf.py
```
Enter the path to your PDF file when prompted, and the script will handle the rest, outputting the text to a file named extracted_text.txt in the same directory.

Dependencies
This script requires the PyPDF2 library, which can be installed via pip:
```
pip install PyPDF2
```
This tool is particularly useful for automating the extraction of text from a large number of PDF files or integrating PDF text extraction into larger Python projects.

