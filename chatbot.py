import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [r"(hi|hello|hey)", ["Hello! How can I help you?", "Hi there! How are you today?"]],
    [r"how are you (.*)", ["I'm just a chatbot, but I'm doing well! How about you?"]],
    [r"what is your name", ["I am a chatbot created to assist you. What's your name?"]],
    [r"my name is (.*)", ["Nice to meet you, %1! How can I assist you today?"]],
    [r"what can you do", ["I can chat with you, answer basic questions, and keep you company!"]],
    [r"thank you|thanks", ["You're welcome!", "No problem! Happy to help!"]],
    [r"bye|goodbye", ["Goodbye! Have a great day!", "Bye! Take care!"]],
    [r"(.*)", ["I'm sorry, I didn't quite understand that. Could you rephrase?"]]
]

# Reflections for dynamic responses
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "me": "you"
}

# Create chatbot instance
chatbot = Chat(pairs, reflections)

# Start the chatbot
def start_chat():
    print("ChatBot: Hi! I am your chatbot. Type 'bye' to exit.")
    chatbot.converse()

# Main program
if __name__ == "__main__":
    start_chat()