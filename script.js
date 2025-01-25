document.getElementById('send-btn').addEventListener('click', sendMessage);
document.getElementById('user-input').addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
});

// Event listener for the Send button
document.getElementById('send-btn').addEventListener('click', sendMessage);

// Event listener for the Enter key
document.getElementById('user-input').addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
        console.log("Enter key pressed!"); // Debug log
        sendMessage(); // Call sendMessage when Enter is pressed
    }
});

function sendMessage() {
    const userInput = document.getElementById('user-input').value.trim();
    if (userInput=== "") return; // Do nothing if input is empty

    // Display user message
    displayMessage(userInput, 'user');

   
    // Show the typing indicator
    const chatCharacter = document.getElementById('chat-character');
    chatCharacter.style.visibility = 'visible';

    console.log('User input:', userInput);
    
    // Simulate bot response (you can integrate this with your backend or API)
    fetch('http://127.0.0.1:5000/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            user_input: userInput, // Send the user's input to the backend
        }),
    })
        .then((response) => {
            console.log('Response status:', response.status);
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
        .then((data) => {
            // Display the bot's response
            const botResponse = data.bot_response;
            displayMessage(botResponse, 'bot');

            // Hide the typing indicator
            chatCharacter.style.visibility = 'hidden';
        })
        .catch((error) => {
            console.error('Error fetching bot response:', error);
            displayMessage("Oops! Something went wrong. Please try again later.", 'bot');

            // Hide the typing indicator
            chatCharacter.style.visibility = 'hidden';
        });

     // Clear input field
     document.getElementById('user-input').value = '';

}


function displayMessage(message, sender) {
    const chatBox = document.getElementById('chat-box');
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', sender);
    messageElement.innerHTML = `<p>${message}</p>`;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the latest message
}

function getBotResponse(userInput) {
    // Replace this with your backend API or hard-coded responses
    const responses = {
        greeting: "Hello! How can I help you today?",
        farewell: "Goodbye! Have a great day!",
        weather: "It's sunny outside today.",
    };

    if (userInput.includes("hello") || userInput.includes("hi")) {
        return responses.greeting;
    } else if (userInput.includes("bye")) {
        return responses.farewell;
    } else if (userInput.includes("weather")) {
        return responses.weather;
    } else {
        return "I'm sorry, I didn't understand that.";
    }
}


function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim() === "") return; // Do nothing if input is empty

    displayMessage(userInput, 'user');
    document.getElementById('user-input').value = '';

    fetch('http://127.0.0.1:5000/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_input: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        displayMessage(data.bot_response, 'bot');
    })
    .catch(error => console.error('Error:', error));
}
