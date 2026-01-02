# 🤖 Mini AI Chatbot

A Python-based AI chatbot with natural language processing using NLTK and a modern Flask web interface.

## Features

- **NLP Preprocessing**: Uses NLTK for tokenization and stopword removal
- **Context-Aware Responses**: Powered by OpenAI API (mock mode included for testing)
- **Modern Web Interface**: Beautiful gradient UI with smooth animations
- **Conversation Logging**: Saves all chats to JSON for analysis

## Tech Stack

- Python 3.14
- Flask (web framework)
- NLTK (natural language processing)
- OpenAI API
- HTML/CSS/JavaScript

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/MiniChatbot.git
cd MiniChatbot
```

2. Create a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Mac/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Download NLTK data:
```bash
python
>>> import nltk
>>> nltk.download('punkt_tab')
>>> nltk.download('stopwords')
>>> exit()
```

## Usage

### Mock Mode (Free - No API Key Needed)

Run the app as-is to test with mock responses:
```bash
python app.py
```

Visit `http://127.0.0.1:5000/` in your browser.

### Real AI Mode (Requires OpenAI API Key)

1. Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)
2. Open `chatbot.py` and replace `"your-api-key-here"` with your actual key
3. Uncomment the OpenAI API code in the `get_response` function
4. Add billing to your OpenAI account
5. Run the app!

## Project Structure
```
MiniChatbot/
├── app.py              # Flask web server
├── chatbot.py          # Chatbot logic (NLTK + OpenAI)
├── logs.json           # Conversation history
├── templates/
│   └── index.html      # Chat interface
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Screenshots

<img width="1919" height="904" alt="aichatbot" src="https://github.com/user-attachments/assets/f816cd09-bd1e-4e6c-bb8b-3b4453216f48" />


## Future Improvements

- Add user authentication
- Implement chat history viewer
- Add sentiment analysis
- Deploy to cloud (Heroku/Render/Railway)

## License

MIT License - feel free to use for learning and portfolio projects!
```

Save it. ✅

---

Your folder should look like:
```
MiniChatbot/
├── venv/
├── templates/
│   └── index.html
├── app.py
├── chatbot.py
├── logs.json
├── requirements.txt
├── .gitignore
└── README.md
