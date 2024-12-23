import streamlit as st
import fitz  # PyMuPDF
from docx import Document
import os

# Function to extract text from PDF and convert it to DOCX
def convert_pdf_to_docx(uploaded_file, save_dir):
    try:
        # Open the uploaded PDF file using PyMuPDF
        pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        
        # Create a new DOCX document
        doc = Document()

        # Extract text from each page and add it to the DOCX file
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            text = page.get_text("text")  # Extract plain text
            
            if text:
                doc.add_paragraph(text)
        
        # Save the DOCX document to the specified directory
        docx_path = os.path.join(save_dir, "converted_" + uploaded_file.name.replace('.pdf', '.docx'))
        doc.save(docx_path)

        return docx_path

    except Exception as e:
        st.error(f"Conversion error: {str(e)}")
        return None

# Streamlit UI setup
st.set_page_config(page_title="PDF to DOCX Converter")
st.title("PDF to DOCX Converter")
st.subheader("Upload a PDF to convert it into DOCX format.")

# File uploader widget
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

# Local directory where files will be saved (in the same directory as the script)
save_dir = os.path.join(os.getcwd(), "converted_files")

# Create the directory if it doesn't exist
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Convert the PDF to DOCX when the button is clicked
if uploaded_file:
    if st.button("Convert to DOCX"):
        with st.spinner("Converting..."):
            docx_path = convert_pdf_to_docx(uploaded_file, save_dir)
            if docx_path:
                st.success("✅ Conversion complete!")

                # Display the converted file's full path
                st.write(f"Converted file is saved at: {docx_path}")

                # Provide a download button for the converted file
                with open(docx_path, 'rb') as f:
                    docx_data = f.read()

                st.download_button(
                    label="⬇️ Download DOCX",
                    data=docx_data,
                    file_name=os.path.basename(docx_path),
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )