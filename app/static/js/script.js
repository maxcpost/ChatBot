async function sendQuery() {
    const query = document.getElementById('userInput').value;
    const chatLog = document.getElementById('chatLog');
    chatLog.innerHTML += `<div><strong>You:</strong> ${query}</div>`;
    const response = await fetch('/api/query', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query: query })
    });
    const data = await response.json();
    chatLog.innerHTML += `<div><strong>Bot:</strong> ${data.answer}</div>`;
    chatLog.scrollTop = chatLog.scrollHeight;
}