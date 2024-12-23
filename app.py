import streamlit as st
from pdf2docx import Converter
import os
import tempfile

# Function to handle PDF to DOCX conversion
def convert_pdf_to_docx(pdf_file):
    # Create a temporary file to save the uploaded PDF
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        temp_pdf.write(pdf_file.read())  # Save the PDF to a temp file
        temp_pdf_path = temp_pdf.name
    
    # Generate output filename with "converted" appended to the original name
    original_filename = os.path.splitext(pdf_file.name)[0]
    docx_filename = f"{original_filename}_converted.docx"
    docx_file = os.path.join(tempfile.gettempdir(), docx_filename)
    
    # Convert PDF to DOCX
    cv = Converter(temp_pdf_path)
    cv.convert(docx_file)
    
    # Ensure the temporary PDF file is closed before attempting to delete
    try:
        os.remove(temp_pdf_path)
    except PermissionError:
        st.error(f"Error removing the temporary PDF file: {temp_pdf_path}. It may still be in use.")
    
    return docx_file

# Set page layout and title
st.set_page_config(page_title="PDF to DOCX Converter", layout="centered")
st.title("PDF to DOCX Converter")
st.subheader("Convert your PDF files to editable DOCX format with ease.")

# Instructions for the user
st.markdown("""
    <p style="font-size:18px;">
    Simply upload your PDF file below, and we'll take care of the conversion. Once the conversion is complete, you'll be able to download the DOCX file.
    </p>
    """, unsafe_allow_html=True)

# File upload button
uploaded_pdf = st.file_uploader("Upload your PDF file here:", type="pdf")

# Conversion and download link
if uploaded_pdf:
    st.write("PDF uploaded successfully! 🎉")
    st.write("We're now processing your file. Please give us a moment.")

    if st.button('Convert to DOCX'):
        # Perform the conversion
        output_docx = convert_pdf_to_docx(uploaded_pdf)

        # After conversion
        st.success(f"Conversion complete! 🎉")

        # Offer download link with the new filename
        st.write(f"Your DOCX file ({os.path.basename(output_docx)}) is ready. Click the button below to download it.")
        st.download_button("Download DOCX", output_docx)

        # Action description for user
        st.write("Once you've downloaded the DOCX file, feel free to open it with any word processor to edit the contents.")
        st.write("Click 'Yes' below to confirm you've downloaded the document.")
        
        if st.button("Yes, I've downloaded the document"):
            st.write("Thank you! You're all set. Feel free to upload another file or exit the app.")