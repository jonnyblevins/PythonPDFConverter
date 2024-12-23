import streamlit as st
import fitz
from docx import Document
import os

# Set page configuration (must be first in the script)
st.set_page_config(page_title="PDF to DOCX Converter")

# Inject custom CSS to change background and text color
st.markdown("""
    <style>
        /* Set background color and gradient for the page */
        .reportview-container {
            background: linear-gradient(to right, #E2725B, #F1C6A4);  /* Terracotta gradient */
            color: black !important;  /* Set text color to black */
        }

        /* Style the title and subtitle */
        .css-1v0mbdj {
            color: #FFFFFF !important; /* Title color to make it stand out */
        }

        /* Style the button background */
        .css-1v0mbdj button {
            background-color: #E2725B !important; /* Button color */
            color: white !important;  /* Button text color */
        }

        /* Style the uploaded file input field */
        .css-1gb49k4 {
            background-color: #F1C6A4 !important;
            border-radius: 10px;
            color: #3E3E3E !important;
        }

        /* Ensure proper font color in elements */
        .css-18e3th9 {
            color: black !important;  /* Override text color for specific elements */
        }
    </style>
""", unsafe_allow_html=True)

def convert_pdf_to_docx(uploaded_file, save_dir):
    try:
        pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        
        doc = Document()

        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            text = page.get_text("text")
            
            if text:
                doc.add_paragraph(text)
        

        docx_path = os.path.join(save_dir, "converted_" + uploaded_file.name.replace('.pdf', '.docx'))
        doc.save(docx_path)

        return docx_path

    except Exception as e:
        st.error(f"Conversion error: {str(e)}")
        return None

# Title and subtitle
st.title("Breaking Plaid PDF Converter")
st.subheader("🌱 Upload a PDF to convert it into DOCX format. 🌿")

# File uploader widget
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

# Directory where converted files will be saved
save_dir = os.path.join(os.getcwd(), "converted_files")

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

if uploaded_file:
    if st.button("Convert to DOCX"):
        with st.spinner("Converting..."):
            docx_path = convert_pdf_to_docx(uploaded_file, save_dir)
            if docx_path:
                st.success("✅ Conversion complete!")

                st.write(f"Converted file is saved at: {docx_path}")

                with open(docx_path, 'rb') as f:
                    docx_data = f.read()

                st.download_button(
                    label="⬇️ Download DOCX",
                    data=docx_data,
                    file_name=os.path.basename(docx_path),
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )