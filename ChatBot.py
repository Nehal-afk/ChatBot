import nltk
from nltk.chat.util import Chat, reflections

# Download the NLTK data
nltk.download('punkt')

# Pre-defined questions and responses
pairs = [
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"my name is (.*)",
        ["Hello %1, How can I help you today?",]
    ],
    [
        r"what is your name ?|who are you ?",
        ["I am a chatbot created by Susobhan & Nehal. You can call me Nel :).",]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"sorry (.*)|sorry",
        ["It's alright", "No problem",]
    ],
    [
        r"I am fine",
        ["Great to hear that!",]
    ],
    [
        r"(.*) age?",
        ["I am a computer program, so I don't have an age.",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an intelligent chatbot! >:)",]
    ],
    [
        r"(.*) (location|city) ?|where do you live ?",
        ["I am a virtual being, so I do not live anywhere.", "I'm right behind you >.<", "I'm hiding inside the closet of your room XD",]
    ],
    [
        r"how (.*) health(.*)",
        ["I am a computer program, so I am always healthy. ^_^",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I am a big fan of chess.",]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand that.",]
    ],
]

reflections = {
    "i am"       : "you are",
    "i was"      : "you were",
    "i"          : "you",
    "i'd"        : "you would",
    "i've"       : "you have",
    "i'll"       : "you will",
    "my"         : "your",
    "you are"    : "I am",
    "you were"   : "I was",
    "you've"     : "I have",
    "you'll"     : "I will",
    "your"       : "my",
    "yours"      : "mine",
    "you"        : "me",
    "me"         : "you"
}

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Start the conversation
def chatbot_conversation():
    print("Hi! I am a chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "goodbye"]:
            print("Chatbot: Bye, Take care ! :)")
            break
        else:
            response = chatbot.respond(user_input)
            print("Chatbot:", response)

chatbot_conversation()
