document.getElementById('send-btn').addEventListener('click', function() {
  let userInput = document.getElementById('user-input').value;
  if (userInput.trim() !== "") {
      addMessage(userInput, 'user');
      document.getElementById('user-input').value = '';

      setTimeout(() => {
          let aiResponse = generateAIResponse(userInput);
          addMessage(aiResponse, 'ai');
      }, 1000);
  }
});

function addMessage(message, sender) {
  let chatBox = document.getElementById('chat-box');
  let messageElement = document.createElement('p');
  messageElement.textContent = message;
  
  if (sender === 'user') {
      messageElement.style.textAlign = 'right';
      messageElement.style.backgroundColor = '#007bff';
      messageElement.style.color = 'white';
  } else {
      messageElement.style.textAlign = 'left';
      messageElement.style.backgroundColor = 'rgba(255, 255, 255, 0.2)';
      messageElement.style.color = '#fff';
  }
  
  chatBox.appendChild(messageElement);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function generateAIResponse(userInput) {
  const responses = [
      "I'm here to help you.",
      "Could you tell me more about that?",
      "That sounds interesting!",
      "Let's explore this further.",
      "I'm here to support you."
  ];
  return responses[Math.floor(Math.random() * responses.length)];
}
