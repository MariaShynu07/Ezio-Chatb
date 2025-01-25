from flask import Flask, request, jsonify
import pyttsx3
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Text-to-speech function
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Chatbot logic
def chatbot_response(user_input):
    responses = {
        "hello": "Hi there! How can I assist you today?",
        "hi": "Hello! What can I do for you?",
        "hey": "Hey! How's it going?",
        "good morning": "Good morning! Hope you have a great day!",
        "good night": "Good night! Take care.",
        "how are you": "I'm just a bot, but I'm doing great! Thanks for asking.",
        "what's up": "Not much, just here to help you!",
        "what are you doing": "Just waiting for you to ask something interesting!",
        "what's the weather like": "I currently can't check the weather, but it's always sunny in here!",
        "is it raining": "I don't have live updates, but you can check your local forecast.",
        "bye": "Goodbye! Have a great day!",
        "see you later": "See you later! Don't hesitate to chat again.",
        "goodbye": "Goodbye! It was nice talking to you.",
        "what is your name": "I'm a chatbot created to assist you with your questions.",
        "who created you": "I was created by a Python enthusiast!",
        "what can you do": "I can chat with you, provide information, and help you with your studies",
        "how to solve quadratic equations": "Use the quadratic formula: x = (-b ± √(b²-4ac)) / 2a.",
        "examples of quadratic equations": "x² + 5x + 6 = 0 or x² - 4x + 4 = 0.",
        "pythagoras theorem": "The Pythagorean Theorem states: a² + b² = c².",
        "can you say about newton's first law": "An object will remain at rest or in uniform motion unless acted upon by an external force.",
        "photosynthesis": "Photosynthesis is the process by which plants convert sunlight into energy, using water and carbon dioxide.",
        "chemical reaction example": "Combustion: CH₄ + 2O₂ → CO₂ + 2H₂O.",
        "who was napoleon": "Napoleon Bonaparte was a French military leader and emperor who rose to prominence during the French Revolution.",
        "wwii start date": "World War II started on September 1, 1939.",
        "indus valley civilization": "The Indus Valley Civilization was an ancient civilization that flourished in the Indus River basin from 3300 BCE to 1300 BCE.",
        "time management": "Use tools like calendars, to-do lists, and techniques like Pomodoro for better time management.",
        "stress relief": "Take breaks, exercise, and don't forget to sleep well. Deep breathing exercises also help.",
        "how can I focus": "Eliminate distractions, work in intervals, and set specific goals for each session.",
        "exam stress": "Believe in yourself! You are stronger than you think.",
        "procrastination": "The secret to getting ahead is getting started. – Mark Twain",
        "study motivation": "Success is the sum of small efforts repeated day in and day out.",

    }
    return responses.get(user_input.lower(), "I'm sorry, I don't understand that.")

# Flask route for chatbot
@app.route('/chat', methods=['POST'])
def chat():
    # # data = request.get_json()  # Get JSON data from the request
    # # user_input = data.get('user_input')  # Extract user input
    
    # # if not user_input:
    # #     return jsonify({"error": "User input is required"}), 400  # Return error if input is missing

    # user_input = request.data.decode('utf-8').strip().lower()
    # print(f"User input received: {user_input}")  # Debug log

    # # Generate chatbot response
    # response = chatbot_response(user_input)
    
    # # Optional: Enable text-to-speech for the response
    # speak(response)
    
    # # Return response as JSON
    # # return jsonify({"bot_response": response})
    # return response, 200
    try:
        # Parse JSON data from the request
        data = request.get_json()
        user_input = data.get('user_input', '').strip().lower()
        print(f"User input received: {user_input}")  # Debug log

        # Generate chatbot response
        response = chatbot_response(user_input)

        # Enable text-to-speech for the response (optional)
        speak(response)

        # Return response as JSON
        return jsonify({"bot_response": response}), 200
    except Exception as e:
        print(f"Error: {e}")  # Debugging log
        return jsonify({"bot_response": "An error occurred. Please try again later."}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
