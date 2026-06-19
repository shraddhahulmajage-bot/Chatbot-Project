import random

responses = {
    "hello": ["Hello!", "Hi there!", "Welcome!"],
    "hi": ["Hello!", "Hi!"],
    "how are you": ["I am fine.", "Doing great!"],
    "what is your name": ["I am a Python Chatbot."],
    "bye": ["Goodbye!", "See you later!"]
}

def get_response(user_input):
    user_input = user_input.lower()

    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    return "Sorry, I don't understand that."