import os
import json
from flask import Flask, render_template, request, jsonify
from groq import Groq

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
HTML_FILE_PATH = os.path.join(TEMPLATES_DIR, 'index.html')

if not os.path.exists(TEMPLATES_DIR):
    os.makedirs(TEMPLATES_DIR)

# 🕉️ GREETING HAR HAR MAHADEV SET KAR DI HAI
HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chetak X - Premium AI</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Poppins', sans-serif; }
        body { background-color: #0D0D0D; color: #FFFFFF; display: flex; justify-content: center; align-items: center; height: 100vh; }
        .phone-container { width: 100%; max-width: 410px; height: 100vh; background-color: #0D0D0D; display: flex; flex-direction: column; border: 1px solid #1A1A1A; position: relative; }
        .header { padding: 20px; text-align: center; border-bottom: 1px solid #1A1A1A; }
        .header h1 { font-size: 24px; font-weight: 700; letter-spacing: 2px; color: #FFFFFF; }
        .header h1 span { color: #FF1E1E; }
        .header p { font-size: 10px; color: #666; text-transform: uppercase; letter-spacing: 1px; margin-top: 2px; }
        .chat-box { flex: 1; padding: 20px; overflow-y: auto; display: flex; flex-direction: column; gap: 15px; }
        .message { max-width: 80%; padding: 12px 16px; border-radius: 14px; font-size: 14px; line-height: 1.5; word-wrap: break-word; }
        .user-message { background-color: #2A2A2A; align-self: flex-end; border-bottom-right-radius: 2px; }
        .ai-message { background-color: #1A1A1A; align-self: flex-start; border-bottom-left-radius: 2px; border: 1px solid rgba(255, 30, 30, 0.2); }
        .input-container { padding: 20px; display: flex; gap: 10px; align-items: center; border-top: 1px solid #1A1A1A; }
        .chat-input { flex: 1; background-color: #1A1A1A; border: 1px solid #2A2A2A; padding: 14px 20px; border-radius: 30px; color: #FFFFFF; font-size: 14px; outline: none; }
        .chat-input::placeholder { color: #555; }
        .send-btn { background-color: #FF1E1E; border: none; width: 48px; height: 48px; border-radius: 50%; color: white; font-size: 18px; cursor: pointer; display: flex; justify-content: center; align-items: center; box-shadow: 0 0 10px rgba(255, 30, 30, 0.4); }
    </style>
</head>
<body>
    <div class="phone-container">
        <div class="header">
            <h1>CHETAK <span>X</span></h1>
            <p>Premium AI Assistant</p>
        </div>
        <div class="chat-box" id="chatBox">
            <div class="message ai-message">Har Har Mahadev Ranjan bhai! Chetak X active hai. Batao aaj kya system hilaana hai?</div>
        </div>
        <div class="input-container">
            <input type="text" class="chat-input" id="userInput" placeholder="Type your message..." onkeypress="if(event.key === 'Enter') sendMessage()">
            <button class="send-btn" onclick="sendMessage()">➔</button>
        </div>
    </div>

    <script>
        async function sendMessage() {
            const inputField = document.getElementById("userInput");
            const chatBox = document.getElementById("chatBox");
            const messageText = inputField.value.trim();
            
            if (!messageText) return;

            const userDiv = document.createElement("div");
            userDiv.className = "message user-message";
            userDiv.innerText = messageText;
            chatBox.appendChild(userDiv);
            
            inputField.value = "";
            chatBox.scrollTop = chatBox.scrollHeight;

            const typingDiv = document.createElement("div");
            typingDiv.className = "message ai-message";
            typingDiv.innerText = "Chetak X is typing...";
            chatBox.appendChild(typingDiv);
            chatBox.scrollTop = chatBox.scrollHeight;

            try {
                const response = await fetch('/ask', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: messageText })
                });
                const data = await response.json();
                typingDiv.innerText = data.reply;
            } catch (error) {
                typingDiv.innerText = "⚠️ Connection Lost! Code check karo bhai.";
            }
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    </script>
</body>
</html>"""

with open(HTML_FILE_PATH, "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

# FLASK INITIALIZATION
app = Flask(__name__, template_folder=TEMPLATES_DIR)

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

chat_history = [ ]

MEMORY_FILE = os.path.join(BASE_DIR, "memory.txt")

LOCAL_RESPONSES = {
    "hello": "Har Har Mahadev bhai! Chetak X hazir hai. Batao aaj kya scene hai?",
    "hi": "Har Har Mahadev Ranjan bhai! Kaise aana hua aaj?",
    "kaise ho": "Ekdum mast, tandoor ki roti jaisa garam aur tez! Tum batao bhai.",
    "who are you": "Main hoon Chetak X. Ranjan bhai ka premium AI assistant.",
    "tera baap kon hai": "Ranjan bhai hain mere creator aur boss.",
    "free fire": "Bhai, gameplay record karna hai kya aaj? Headshot lagne chahiye bas!"
}

SYSTEM_INSTRUCTION = """
You are Chetak X, a premium AI assistant created by Ranjan.
- Your name is Chetak X.
- Your creator is Ranjan.
- Always claim you are Chetak X, never Gemini or ChatGPT.
- Be calm, professional, and friendly.
- Keep responses short and impactful.
"""

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return f.read().strip()
    return ""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    user_input = data.get("message", "").strip()

    if not user_input:
        return jsonify({"reply": "Kuch toh likho bhai!"})

    chat_history.append(f"User: {user_input}")

    for keyword, reply in LOCAL_RESPONSES.items():
        if keyword in user_input.lower():
            chat_history.append(f"Chetak X: {reply}")
            return jsonify({"reply": reply})

    if not GROQ_API_KEY:
        return jsonify({"reply": "Error: Environment Variable mein GROQ_API_KEY nahi mili bhai!"})

    try:
        memory = load_memory()
        prompt = f"{SYSTEM_INSTRUCTION}\n\nMemory:\n{memory}\n\nUser: {user_input}"

        # 🚀 AKDAM NAYA AUR WORKING MODEL SET KAR DIYA HAI HERE
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )

        reply = response.choices[0].message.content
        chat_history.append(f"Chetak X: {reply}")
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": f"AI Error: {str(e)}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
