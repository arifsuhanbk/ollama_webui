// Populate model dropdown
window.onload = async () => {
    try {
        const res = await fetch('/models');
        const models = await res.json();
        const modelSelect = document.getElementById('modelSelect');

        models.forEach(model => {
            const option = document.createElement('option');
            option.value = model;
            option.textContent = model;
            modelSelect.appendChild(option);
        });
    } catch (error) {
        console.error('Failed to fetch model list:', error);
    }
};

async function sendData() {
    const input = document.getElementById('inputText');
    const model = document.getElementById('modelSelect').value;
    const message = input.value.trim();
    if (!message) return;

    const resultDiv = document.getElementById('result');

    const userMessage = document.createElement('div');
    userMessage.className = 'message user';
    userMessage.textContent = message;
    resultDiv.appendChild(userMessage);
    input.value = '';

    const botMessage = document.createElement('div');
    botMessage.className = 'message bot';
    resultDiv.appendChild(botMessage);
    resultDiv.scrollTop = resultDiv.scrollHeight;

    try {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message, model })
        });

        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        let content = '';

        while (true) {
            const { done, value } = await reader.read();
            if (done) break;
            content += decoder.decode(value, { stream: true });
            botMessage.textContent = content;
            resultDiv.scrollTop = resultDiv.scrollHeight;
        }

    } catch (error) {
        console.error('Error:', error);
    }
}
