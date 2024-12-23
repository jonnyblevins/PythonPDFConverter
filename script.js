document.getElementById('upload-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const formData = new FormData();
    formData.append("pdf-file", document.getElementById("pdf-file").files[0]);
    
    const messageDiv = document.getElementById("message");
    const downloadDiv = document.getElementById("download-link");
    const downloadBtn = document.getElementById("download-btn");

    // Show a loading message while the conversion is happening
    messageDiv.innerHTML = "Converting your file...";
    downloadDiv.style.display = "none";

    fetch('/convert', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            messageDiv.innerHTML = "Conversion complete!";
            downloadBtn.href = `/downloads/${data.file_name}`;
            downloadDiv.style.display = "block";
        } else {
            messageDiv.innerHTML = "An error occurred during conversion.";
        }
    })
    .catch(error => {
        messageDiv.innerHTML = "An error occurred during conversion.";
    });
});
