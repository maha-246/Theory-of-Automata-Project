function processString() {
    const inputString = document.getElementById('inputString').value;
    fetch('/process', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ inputString }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerHTML = data.result;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}





