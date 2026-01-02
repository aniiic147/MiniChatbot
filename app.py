from flask import Flask, render_template, request, jsonify
from chatbot import get_response

print("Starting app...")

# Create Flask app
app = Flask(__name__)

print("Flask app created")

@app.route("/")
def index():
    """
    Show the main chat page
    """
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    """
    Receive message from user, get bot response, send it back
    """
    user_message = request.form["message"]
    bot_reply = get_response(user_message)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    print("About to run Flask...")
    app.run(debug=True)
    print("Flask finished")