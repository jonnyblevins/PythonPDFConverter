# PDF to DOCX Converter with Streamlit

This app lets you convert PDFs into DOCX format using the libaries of Streamlit, `fitz` from PyMuPDF, and `python-docx`. You upload a PDF, it gets converted, and you can download the DOCX. Clear as mud, right?

## Libraries Used:
- `streamlit`: For the web app
- `fitz` PyMuPDF extracts text from PDFs
- `docx`: creates DOCX files
- `os`: handling file paths and directories (this one is new to me but Shifra says it's good, lol)

## Features:
- **Convert PDF to DOCX**: Upload your PDF and turn it into a DOCX with all the text extracted
- **Smooth Interface**: Streamlit gives you a neat, simple way to upload files. Hit convert and grab the result.

## Code Breakdown:

1. **Setting Up Streamlit Page**:
   - `st.set_page_config(page_title="PDF to DOCX Converter")` sets the browser tab title
   - `st.markdown()` adds custom CSS to give the page a bit of personality with colors and style for the title, buttons, and other elements

2. **File Upload and Save Directory**:
   - The uploader is handled by `st.file_uploader("Choose a PDF file", type="pdf")`—you pick a PDF to upload
   - The app automatically creates a directory (`converted_files`) to store your converted DOCX files

3. **Conversion Logic**:
   - `convert_pdf_to_docx()` is the heart of the app. It reads the uploaded PDF, grabs the text from each page, and throws it into a new DOCX file
   - The DOCX is saved in the `converted_files` folder with a `converted_` prefix

4. **Conversion Process**:
   - After uploading and clicking "Convert to DOCX", a spinner lets you know the app is working
   - When it's done, the path to the converted file shows up, and you can download it right from the app

5. **Download Button**:
   - `st.download_button()` gives you a button to download the newly created DOCX. Just click it and grab your file

## How to Use:
2. Click "Browse Files."
1. Upload your PDF.
2. Click "Convert to DOCX."
3. Once it's done, download your document. Let me know when it breaks, haha.

## Installation:
(HOW TO GET THIS TO WORK!)

I've provided you with the "requirements.txt" file. It's a neat tool that will install everything you need if you simply command line type:

```bash
pip install -r requirements.txt
```
It provides you with:
   streamlit
   pymupdf
   python-docx

After you've installed everything, to run the app on your computer 

streamlit run |REPLACE_WTIH_WHATEVER_YOU_NAMED_THIS_PROBABLY_"pdf_converter"|.py

So to run, it'll look something like this:
```bash
streamlit run pdf_converter.py
```
