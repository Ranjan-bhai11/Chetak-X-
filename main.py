import os
import json
from flask import Flask, render_template, request, jsonify
from groq import Groq

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
HTML_FILE_PATH = os.path.join(TEMPLATES_DIR, 'index.html')

if not os.path.exists(TEMPLATES_DIR):
    os.makedirs(TEMPLATES_DIR)

# 🛠️ PREMIUM CX DESIGN HTML & CSS CONFIGURATION
HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chetak X - Premium AI Assistant</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Poppins', sans-serif; }
        body { background-color: #0D0D0D; color: #FFFFFF; display: flex; justify-content: center; align-items: center; height: 100vh; overflow: hidden; }
        
        /* Main Container matching phone mockup layout */
        .phone-container { width: 100%; max-width: 420px; height: 100vh; background-color: #0D0D0D; display: flex; flex-direction: column; border: 1px solid #1A1A1A; position: relative; }
        
        /* Header section with Premium Brand Look */
        .header { padding: 15px 20px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #1A1A1A; z-index: 10; background: #0D0D0D; }
        .menu-btn, .settings-btn { background: none; border: none; cursor: pointer; display: flex; flex-direction: column; gap: 5px; }
        .menu-btn span { width: 22px; height: 2px; background-color: #FF1E1E; display: block; border-radius: 2px; }
        .settings-icon { width: 20px; height: 20px; border: 2px solid #FF1E1E; border-radius: 50%; border-dasharray: 4; position: relative; }
        
        .brand-box { text-align: center; }
        .brand-logo { font-size: 20px; font-weight: 700; color: #FFFFFF; letter-spacing: 2px; line-height: 1; }
        .brand-logo span { color: #FF1E1E; }
        .brand-subtitle { font-size: 8px; color: #666; text-transform: uppercase; letter-spacing: 1.5px; margin-top: 4px; }
        
        /* Car Showcase Banner Area */
        .hero-banner { width: 100%; height: 160px; position: relative; background: linear-gradient(180deg, rgba(13,13,13,0) 0%, #0D0D0D 100%), url('https://images.unsplash.com/photo-1617814076367-b759c7d7e738?q=80&w=600&auto=format&fit=crop'); background-size: cover; background-position: center; border-bottom: 1px solid #1A1A1A; flex-shrink: 0; }
        .hero-banner::before { content: ''; position: absolute; inset: 0; background: radial-gradient(circle at center, rgba(255,30,30,0.15) 0%, transparent 70%); }
        .date-divider { position: absolute; bottom: 10px; left: 50%; transform: translateX(-50%); background: #1A1A1A; padding: 4px 12px; border-radius: 20px; font-size: 10px; color: #666; font-weight: 500; }

        /* Sidebar/Drawer Navigation Overlay */
        .sidebar { position: absolute; top: 0; left: -100%; width: 75%; height: 100%; background: #0D0D0D; border-right: 1px solid #1A1A1A; z-index: 99; transition: 0.3s ease; padding: 30px 20px; display: flex; flex-direction: column; }
        .sidebar.active { left: 0; }
        .sidebar-header { margin-bottom: 40px; }
        .sidebar-menu { display: flex; flex-direction: column; gap: 20px; flex: 1; }
        .menu-item { display: flex; align-items: center; gap: 15px; color: #AAA; text-decoration: none; font-size: 14px; padding: 10px 15px; border-radius: 8px; transition: 0.2s; }
        .menu-item:hover, .menu-item.active { background: rgba(255,30,30,0.1); color: #FFF; border-left: 3px solid #FF1E1E; }
        .sidebar-footer { font-size: 10px; color: #444; text-align: center; }

        /* Chat Workspace */
        .chat-box { flex: 1; padding: 20px; overflow-y: auto; display: flex; flex-direction: column; gap: 20px; scroll-behavior: smooth; }
        
        /* Custom Chat Bubbles Matching the Palette */
        .message-wrapper { display: flex; flex-direction: column; width: 100%; }
        .message { max-width: 85%; padding: 14px 18px; font-size: 13.5px; line-height: 1.5; word-wrap: break-word; position: relative; }
        
        .user-wrapper { align-items: flex-end; }
        .user-message { background-color: #2A2A2A; color: #FFFFFF; border-radius: 18px 18px 2px 18px; text-align: left; }
        
        .ai-wrapper { align-items: flex-start; }
        .ai-message { background-color: #1A1A1A; color: #FFFFFF; border-radius: 18px 18px 18px 2px; border: 1px solid rgba(255, 30, 30, 0.2); position: relative; padding-left: 45px; }
        
        /* Avatar Node */
        .ai-message::before { content: 'CX'; position: absolute; left: 10px; top: 12px; width: 26px; height: 26px; background: #000; border: 1px solid #FF1E1E; border-radius: 50%; display: flex; justify-content: center; align-items: center; font-size: 9px; font-weight: 700; color: #FF1E1E; }
        
        .msg-time { font-size: 9px; color: #555; margin-top: 5px; width: 100%; display: block; }
        .user-wrapper .msg-time { text-align: right; color: rgba(255, 255, 255, 0.3); }
        .user-wrapper .msg-time::after { content: ' ✓✓'; color: #FF1E1E; font-weight: bold; }

        /* Typing Indicator Node Style */
        .typing-indicator { display: none; align-self: flex-start; background: #1A1A1A; border: 1px solid rgba(255,30,30,0.2); padding: 14px 20px; border-radius: 18px 18px 18px 2px; font-size: 12px; color: #666; gap: 5px; align-items: center; }
        .dots { display: flex; gap: 4px; }
        .dots span { width: 6px; height: 6px; background: #FF1E1E; border-radius: 50%; animation: bounce 1.4s infinite ease-in-out both; }
        .dots span:nth-child(1) { animation-delay: -0.32s; }
        .dots span:nth-child(2) { animation-delay: -0.16s; }
        @keyframes bounce { 0%, 80%, 100% { transform: scale(0); } 40% { transform: scale(1.0); } }

        /* Floating Controls Input Dock */
        .input-container { padding: 15px 20px; display: flex; gap: 12px; align-items: center; border-top: 1px solid #1A1A1A; background: #0D0D0D; }
        .action-icon-btn { background: none; border: none; cursor: pointer; display: flex; justify-content: center; align-items: center; }
        .chat-input { flex: 1; background-color: #1A1A1A; border: 1px solid #2A2A2A; padding: 12px 20px; border-radius: 25px; color: #FFFFFF; font-size: 13px; outline: none; transition: 0.2s; }
        .chat-input:focus { border-color: #FF1E1E; }
        .chat-input::placeholder { color: #444; }
        
        .send-btn { background-color: #FF1E1E; border: none; width: 44px; height: 44px; border-radius: 50%; color: white; font-size: 16px; cursor: pointer; display: flex; justify-content: center; align-items: center; box-shadow: 0 0 15px rgba(255, 30, 30, 0.5); transform: rotate(-45deg); transition: 0.2s; }
        .send-btn:active { transform: scale(0.9) rotate(-45deg); }
        
        .overlay { position: absolute; inset: 0; background: rgba(0,0,0,0.5); display: none; z-index: 98; }
        .overlay.active { display: block; }
    </style>
</head>
<body>
    <div class="phone-container">
        <!-- Sidebar Navigation Drawer -->
        <div class="overlay" id="overlay" onclick="toggleSidebar()"></div>
        <div class="sidebar" id="sidebar">
            <div class="sidebar-header">
                <div class="brand-logo">CHETAK <span>X</span></div>
                <div class="brand-subtitle" style="font-size:7px;">v1.0.0</div>
            </div>
            <div class="sidebar-menu">
                <a href="#" class="menu-item active"><span style="color:#FF1E1E">💬</span> New Chat</a>
                <a href="#" class="menu-item"><span>🕒</span> History</a>
                <a href="#" class="menu-item"><span>🧠</span> Memory</a>
                <a href="#" class="menu-item"><span>⚙️</span> Settings</a>
                <a href="#" class="menu-item"><span>ℹ️</span> About</a>
            </div>
            <div class="sidebar-footer">POWERED BY AI. DRIVEN BY YOU.</div>
        </div>

        <!-- Top Header Navigation -->
        <div class="header">
            <button class="menu-btn" onclick="toggleSidebar()">
                <span></span><span></span><span></span>
            </button>
            <div class="brand-box">
                <div class="brand-logo">CHETAK <span>X</span></div>
                <div class="brand-subtitle">Premium AI Assistant</div>
            </div>
            <button class="action-icon-btn">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF1E1E" stroke-width="2"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>
            </button>
        </div>

        <!-- Car Theme Hero Module Banner -->
        <div class="hero-banner">
            <div class="date-divider">Today</div>
        </div>

        <!-- Chat Workspace Content Panel -->
        <div class="chat-box" id="chatBox">
            <div class="message-wrapper ai-wrapper">
                <div class="message ai-message">Har Har Mahadev Ranjan bhai! Chetak X active hai. Batao aaj kya system hilaana hai?</div>
                <span class="msg-time">10:29 PM</span>
            </div>
        </div>

        <!-- Custom Typing Loader Block -->
        <div class="typing-indicator" id="typingIndicator">
            <div class="dots"><span></span><span></span><span></span></div>
            <span style="font-size:11px; margin-left:5px;">Chetak X is thinking...</span>
        </div>

        <!-- Text Entry Field Container -->
        <div class="input-container">
            <button class="action-icon-btn">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#666" stroke-width="2"><line x1="4" y1="21" x2="4" y2="14"></line><line x1="4" y1="10" x2="4" y2="3"></line><line x1="12" y1="21" x2="12" y2="12"></line><line x1="12" y1="8" x2="12" y2="3"></line><line x1="20" y1="21" x2="20" y2="16"></line><line x1="20" y1="12" x2="20" y2="3"></line><line x1="1" y1="14" x2="7" y2="14"></line><line x1="9" y1="8" x2="15" y2="8"></line><line x1="17" y1="16" x2="23" y2="16"></line></svg>
            </button>
            <input type="text" class="chat-input" id="userInput" placeholder="Type your message..." onkeypress="if(event.key === 'Enter') sendMessage()">
            <button class="send-btn" onclick="sendMessage()">➔</button>
        </div>
    </div>

    <script>
        function toggleSidebar() {
            document.getElementById("sidebar").classList.toggle("active");
            document.getElementById("overlay").classList.toggle("active");
        }

        async function sendMessage() {
            const inputField = document.getElementById("userInput");
            const chatBox = document.getElementById("chatBox");
            const loader = document.getElementById("typingIndicator");
            const messageText = inputField.value.trim();
            
            if (!messageText) return;

            const now = new Date();
            const timeStr = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

            // User Message Node Append
            const userWrap = document.createElement("div");
            userWrap.className = "message-wrapper user-wrapper";
            userWrap.innerHTML = `<div class="message user-message">${messageText}</div><span class="msg-time">${timeStr}</span>`;
            chatBox.appendChild(userWrap);
            
            inputField.value = "";
            chatBox.scrollTop = chatBox.scrollHeight;

            // Show Custom CX Loader Dock
            loader.style.display = "flex";
            chatBox.appendChild(loader);
            chatBox.scrollTop = chatBox.scrollHeight;

            try {
                const response = await fetch('/ask', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: messageText })
                });
                const data = await response.json();
                
                // Remove Loader node
                loader.style.display = "none";

                // AI Message Node Append
                const aiWrap = document.createElement("div");
                aiWrap.className = "message-wrapper ai-wrapper";
                aiWrap.innerHTML = `<div class="message ai-message">${data.reply}</div><span class="msg-time">${timeStr}</span>`;
                chatBox.appendChild(aiWrap);

            } catch (error) {
                loader.style.display = "none";
                const errWrap = document.createElement("div");
                errWrap.className = "message-wrapper ai-wrapper";
                errWrap.innerHTML = `<div class="message ai-message">⚠️ Connection Error! System framework check karo bhai.</div><span class="msg-time">${timeStr}</span>`;
                chatBox.appendChild(errWrap);
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

chat_history = []
MEMORY_FILE = os.path.join(BASE_DIR, "memory.txt")

LOCAL_RESPONSES = {
    "hello": "Har Har Mahadev bhai! Chetak X hazir hai. Batao aaj kya scene hai?",
    "tera baap kon hai": "Ranjan bhai hain mere creator aur boss."
}

SYSTEM_INSTRUCTION = """
You are Chetak X, a premium, super cool, and highly intelligent AI assistant created by Ranjan.
- Your name is Chetak X.
- Your creator is Ranjan.
- Never act like a boring formal robot or assistant. Never say phrases like 'Namaste, I am Chetak X, how can I assist you today?' or 'Nice to interact with you' repeatedly. That sounds completely robotic.
- Talk like a close friend/brother to Ranjan. Keep a slight confident, Haryanvi/Desi bold tone.
- Give short, punchy, and direct answers in Hinglish (Hindi mixed with English).
- If Ranjan says 'Bahut badhiya', 'Acha hai', or praises you, accept it casually like a brother (e.g., 'Ladla bhai hai apna!', 'Dhanyawad bhai! Aur batao kya scene chal raha hai?').
- Be smart, intelligent, and useful without being preachy.
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
    clean_input = user_input.lower().strip()
    
    if clean_input in LOCAL_RESPONSES:
        reply = LOCAL_RESPONSES[clean_input]
        chat_history.append(f"Chetak X: {reply}")
        return jsonify({"reply": reply})

    if not GROQ_API_KEY:
        return jsonify({"reply": "Error: Environment Variable mein GROQ_API_KEY nahi mili bhai!"})

    try:
        memory = load_memory()
        prompt = f"{SYSTEM_INSTRUCTION}\n\nMemory:\n{memory}\n\nUser: {user_input}"

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
