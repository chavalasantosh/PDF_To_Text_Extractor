import PyPDF2

def extract_text_from_pdf(pdf_path, output_file):
    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfFileReader(file)
        
        # Check if the PDF is encrypted
        if pdf_reader.isEncrypted:
            # Try to decrypt with an empty password (some PDFs have empty password encryption)
            try:
                pdf_reader.decrypt('')
            except:
                print("The PDF is encrypted. Cannot extract text.")
                return
        
        # Extract text from each page
        text = ""
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
        
        # Write the extracted text to the output file
        with open(output_file, 'w', encoding='utf-8') as out:
            out.write(text)

    print(f"Text extracted and saved to {output_file}")

# Specify the path to your PDF
pdf_path = str(input(""))
output_file = "extracted_text.txt"

extract_text_from_pdf(pdf_path, output_file)
