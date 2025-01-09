document.getElementById('encryptBtn').addEventListener('click', function() {
    processInput('encrypt');
});

document.getElementById('decryptBtn').addEventListener('click', function() {
    processInput('decrypt');
});

function processInput(mode) {
    const message = document.getElementById('message').value;
    const shift = parseInt(document.getElementById('shift').value, 10); // Ensure shift is an integer

    fetch('/process', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message, shift, mode })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        document.getElementById('result').innerText = data.result;
    })
    .catch(error => {
        document.getElementById('result').innerText = 'Error: ' + error.message; // Display error message
    });
}
