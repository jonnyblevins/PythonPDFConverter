document.getElementById('upload-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    
    const fileInput = document.getElementById('pdf-file');
    const messageDiv = document.getElementById('message');
    const downloadDiv = document.getElementById('download-link');
    const downloadBtn = document.getElementById('download-btn');
    const submitBtn = document.querySelector('.submit-btn');

    // Validate file
    const file = fileInput.files[0];
    if (!file) {
        messageDiv.innerHTML = 'Please select a file';
        return;
    }
    if (file.size > 16 * 1024 * 1024) {
        messageDiv.innerHTML = 'File size must be less than 16MB';
        return;
    }
    if (!file.name.toLowerCase().endsWith('.pdf')) {
        messageDiv.innerHTML = 'Please upload a PDF file';
        return;
    }

    // Prepare UI for conversion
    messageDiv.innerHTML = 'Converting your file...';
    submitBtn.disabled = true;
    downloadDiv.style.display = 'none';

    try {
        const formData = new FormData();
        formData.append('pdf-file', file);

        const response = await fetch('/convert', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();
        
        if (data.success) {
            messageDiv.innerHTML = 'Conversion complete!';
            downloadBtn.href = `/downloads/${data.file_name}`;
            downloadBtn.download = data.original_name;
            downloadDiv.style.display = 'block';
        } else {
            messageDiv.innerHTML = data.message || 'Conversion failed';
        }
    } catch (error) {
        messageDiv.innerHTML = 'An error occurred during conversion';
        console.error('Conversion error:', error);
    } finally {
        submitBtn.disabled = false;
    }
});