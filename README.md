# 📝 PDF to DOCX Converter

I'm the kind of person who Googles "PDF to DocX free" so I was pumped to find this tool. This python program converts PDF files to DOCX format, using the `pdf2docx` library. It’s designed to take an input PDF file and produce a fully formatted DOCX file. 

`TLDR: you'll find it under the PDFConverter.ipynb (Jupyter notebook format). You can copy and paste that, then save a PDF to the same file and run.`

---

## 🚀 Features
- Converts any PDF file to DOCX format
- Maintains formatting and structure
- Quick and easy to use with minimal setup

---

## 🛠️ Requirements

To use this program, make sure you have:
- Python 3.x installed (I've got 3.12)
- The `pdf2docx` library (install with `pip install pdf2docx`)

---

## 📂 How to Use

1. Place the PDF file you want to convert in the same directory as the PDFConverter.ipynb file.
2. Update the `pdf_file` and `docx_file` variables with the filename of your PDF and make up an output DOCX file name (e.g., `"YourResume.pdf"` matched with what you have saved and `"ConvertedYourResume.docx"` will be the file to be created).
3. Run the script with:
   ```bash
   python your_script_name.py
4. Once completed, you will see the message: Conversion complete!
