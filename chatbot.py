import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import json
from openai import OpenAI

# Your OpenAI API key (you'll add this)
client = OpenAI(api_key="your-api-key-here")

# Load English stopwords for filtering
stop_words = set(stopwords.words('english'))

def preprocess(text):
    """
    Clean up user input:
    - Convert to lowercase
    - Tokenize (split into words)
    - Remove punctuation and stopwords
    """
    # Tokenize and lowercase
    tokens = word_tokenize(text.lower())
    
    # Keep only actual words (no punctuation) and remove stopwords
    filtered = [word for word in tokens if word.isalnum() and word not in stop_words]
    
    # Join back into a string
    return " ".join(filtered)
def get_response(user_input):
    """
    Takes user input, processes it, gets AI response, and logs it
    """
    # Clean up the input with NLTK
    processed_input = preprocess(user_input)
    
    # MOCK RESPONSE (replace with real OpenAI later)
    # Simple rule-based responses for testing
    if "hello" in processed_input or "hi" in processed_input:
        answer = "Hello! How can I help you today?"
    elif "weather" in processed_input:
        answer = "I'm a mock chatbot, so I can't check real weather, but I hope it's nice where you are!"
    elif "name" in processed_input:
        answer = "I'm your friendly Mini AI Chatbot (currently in mock mode)."
    else:
        answer = f"You said: '{user_input}'. I processed it to: '{processed_input}'. (Mock response - add OpenAI billing to get real AI responses!)"
    
    # Log the conversation to logs.json
    log_entry = {"user": user_input, "bot": answer}
    
    try:
        with open("logs.json", "r") as f:
            logs = json.load(f)
    except:
        logs = []  # If file doesn't exist or is empty, start fresh
    
    logs.append(log_entry)
    
    with open("logs.json", "w") as f:
        json.dump(logs, f, indent=4)
    
    return answer