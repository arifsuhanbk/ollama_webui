async function sendData() {
    const input = document.getElementById('inputText');
    const message = input.value.trim();
    if (!message) return;

    const resultDiv = document.getElementById('result');

    // Add user message
    const userMessage = document.createElement('div');
    userMessage.className = 'message user';
    userMessage.textContent = message;
    resultDiv.appendChild(userMessage);
    input.value = '';

    // Scroll down
    resultDiv.scrollTop = resultDiv.scrollHeight;

    try {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message })
        });

        const data = await response.json();

        const botMessage = document.createElement('div');
        botMessage.className = 'message bot';
        botMessage.textContent = data.response_data;  // <-- use response_data here
        resultDiv.appendChild(botMessage);
        resultDiv.scrollTop = resultDiv.scrollHeight;
    } catch (error) {
        console.error('Error:', error);
    }
}
