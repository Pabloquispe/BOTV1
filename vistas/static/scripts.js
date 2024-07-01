function toggleChat() {
    const chatContainer = document.getElementById('chat-container');
    chatContainer.classList.toggle('hidden');

    // Verificar si el chat se acaba de abrir
    if (!chatContainer.classList.contains('hidden')) {
        sendWelcomeMessage();
    }
}

function sendWelcomeMessage() {
    fetch('/conversacion', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: '' }), // Enviar un mensaje vacío para desencadenar la bienvenida
    })
    .then(response => response.json())
    .then(data => {
        appendMessage('bot', data.message);
    })
    .catch(error => {
        console.error('Error:', error);
        appendMessage('bot', 'Hubo un error al iniciar el chat. Por favor, inténtalo de nuevo.');
    });
}

function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim() === '') return;

    appendMessage('user', userInput);
    document.getElementById('user-input').value = '';

    fetch('/conversacion', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        appendMessage('bot', data.message);
    })
    .catch(error => {
        console.error('Error:', error);
        appendMessage('bot', 'Hubo un error al procesar tu mensaje. Por favor, inténtalo de nuevo.');
    });
}

function appendMessage(sender, message) {
    const chatWindow = document.getElementById('chat-window');
    const messageElement = document.createElement('div');
    messageElement.classList.add(sender === 'user' ? 'user-message' : 'bot-message');
    messageElement.textContent = message;
    chatWindow.appendChild(messageElement);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}

function checkEnter(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
}
