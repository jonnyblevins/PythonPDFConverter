#BreakingPlaidPDFConverter

import streamlit as st
import fitz
from docx import Document
import os

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

st.set_page_config(page_title="PDF to DOCX Converter")
st.title("PDF to DOCX Converter")
st.subheader("Upload a PDF to convert it into DOCX format.")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

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