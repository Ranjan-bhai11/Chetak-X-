import os
import json
from flask import Flask, render_template, request, jsonify
from groq import Groq

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
HTML_FILE_PATH = os.path.join(TEMPLATES_DIR, 'index.html')

if not os.path.exists(TEMPLATES_DIR):
    os.makedirs(TEMPLATES_DIR)

# 🔥 EXTRA PREMIUM EXACT MOCKUP CONSOLE WITH STEALTH BLACK CAR & DEEPER SOUND
HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chetak X - Premium AI Assistant</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Poppins', sans-serif; }
        body { background-color: #000000; color: #FFFFFF; display: flex; justify-content: center; align-items: center; height: 100vh; overflow: hidden; }
        
        /* 🚨 EXACT MOCKUP SPLASH SCREEN WITH STEALTH BLACK CAR OVERLAY */
        #splash-screen { 
            position: fixed; 
            inset: 0; 
            background: #000000; 
            z-index: 9999; 
            display: flex; 
            flex-direction: column; 
            align-items: center; 
            justify-content: center; 
            transition: opacity 0.8s cubic-bezier(0.4, 0, 0.2, 1);
            cursor: pointer;
        }
        
        .splash-main-logo {
            font-size: 34px;
            font-weight: 700;
            color: #FFFFFF;
            letter-spacing: 5px;
            margin-bottom: 5px;
            text-align: center;
        }
        .splash-main-logo span { color: #FF1E1E; }
        .splash-sub { font-size: 9px; color: #666; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 25px; }

        .car-frame { 
            width: 100%; 
            max-width: 380px; 
            height: 280px; 
            background: url('https://images.unsplash.com/photo-1605559424843-9e4c228bf1c2?q=80&w=600&auto=format&fit=crop') center/cover; 
            position: relative; 
            filter: brightness(0.12) contrast(1.2);
            transition: filter 4.5s ease-in-out;
        }
        
        /* Glowing Hot Red Eye Rings Framework */
        .car-frame::before, .car-frame::after {
            content: '';
            position: absolute;
            width: 28px;
            height: 10px;
            border: 2px solid rgba(255, 30, 30, 0);
            border-radius: 50% 50% 0 0;
            top: 52%;
            box-shadow: 0 0 0px rgba(255, 30, 30, 0);
            transition: all 4.5s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .car-frame::before { left: 32%; transform: rotate(-5deg); }
        .car-frame::after { right: 32%; transform: rotate(5deg); }
        
        /* Ignited Engine State Styles */
        #splash-screen.ignited .car-frame { filter: brightness(0.85) contrast(1.2); }
        #splash-screen.ignited .car-frame::before, #splash-screen.ignited .car-frame::after {
            border-color: #FF1E1E;
            box-shadow: 0 0 25px #FF1E1E, 0 0 10px rgba(255, 30, 30, 0.8);
        }
        
        .init-text { font-size: 11px; color: #FF1E1E; letter-spacing: 4px; font-weight: 600; margin-top: 40px; text-transform: uppercase; text-align: center; }
        .tap-hint { font-size: 9px; color: #444; letter-spacing: 1px; margin-top: 10px; }

        /* 📱 MAIN APP DOCK FRAME */
        .phone-container { width: 100%; max-width: 420px; height: 100vh; background-color: #0D0D0D; display: flex; flex-direction: column; border: 1px solid #1A1A1A; position: relative; opacity: 0; transition: opacity 0.5s ease; }
        
        .header { padding: 15px 20px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #1A1A1A; z-index: 10; background: #0D0D0D; }
        .menu-btn { background: none; border: none; cursor: pointer; display: flex; flex-direction: column; gap: 5px; }
        .menu-btn span { width: 22px; height: 2px; background-color: #FF1E1E; display: block; border-radius: 2px; }
        
        .brand-box { text-align: center; }
        .brand-logo { font-size: 20px; font-weight: 700; color: #FFFFFF; letter-spacing: 2px; line-height: 1; }
        .brand-logo span { color: #FF1E1E; }
        .brand-subtitle { font-size: 8px; color: #666; text-transform: uppercase; letter-spacing: 1.5px; margin-top: 4px; }
        .settings-btn { background: none; border: none; cursor: pointer; }
        
        /* Small Content Car Top Banner */
        .hero-banner { width: 100%; height: 160px; position: relative; background: linear-gradient(180deg, rgba(13,13,13,0.3) 0%, #0D0D0D 100%), url('https://images.unsplash.com/photo-1605559424843-9e4c228bf1c2?q=80&w=600&auto=format&fit=crop') center/cover; filter: brightness(0.6) contrast(1.1); border-bottom: 1px solid #1A1A1A; flex-shrink: 0; }
        .date-divider { position: absolute; bottom: 10px; left: 50%; transform: translateX(-50%); background: #1A1A1A; padding: 4px 12px; border-radius: 20px; font-size: 10px; color: #666; font-weight: 500; }

        /* Sidebar Navigation Structure */
        .sidebar { position: absolute; top: 0; left: -100%; width: 75%; height: 100%; background: #0D0D0D; border-right: 1px solid #1A1A1A; z-index: 99; transition: 0.3s ease; padding: 30px 20px; display: flex; flex-direction: column; }
        .sidebar.active { left: 0; }
        .sidebar-header { margin-bottom: 40px; }
        .sidebar-menu { display: flex; flex-direction: column; gap: 20px; flex: 1; }
        .menu-item { display: flex; align-items: center; gap: 15px; color: #AAA; text-decoration: none; font-size: 14px; padding: 10px 15px; border-radius: 8px; transition: 0.2s; }
        .menu-item:hover, .menu-item.active { background: rgba(255,30,30,0.1); color: #FFF; border-left: 3px solid #FF1E1E; }
        .sidebar-footer { font-size: 10px; color: #444; text-align: center; }

        /* Chat Workspace Modules */
        .chat-box { flex: 1; padding: 10px 20px; overflow-y: auto; display: flex; flex-direction: column; gap: 20px; scroll-behavior: smooth; background: #0D0D0D; }
        .message-wrapper { display: flex; flex-direction: column; width: 100%; }
        .message { max-width: 85%; padding: 14px 18px; font-size: 13.5px; line-height: 1.5; word-wrap: break-word; }
        
        .user-wrapper { align-items: flex-end; }
        .user-message { background-color: #2A2A2A; color: #FFFFFF; border-radius: 18px 18px 2px 18px; border: 1px solid rgba(255, 255, 255, 0.05); }
        
        .ai-wrapper { align-items: flex-start; }
        .ai-message { background-color: #1A1A1A; color: #FFFFFF; border-radius: 18px 18px 18px 2px; border: 1px solid rgba(255, 30, 30, 0.15); position: relative; padding-left: 45px; }
        .ai-message::before { content: 'CX'; position: absolute; left: 10px; top: 12px; width: 26px; height: 26px; background: #000; border: 1px solid #FF1E1E; border-radius: 50%; display: flex; justify-content: center; align-items: center; font-size: 9px; font-weight: 700; color: #FF1E1E; }
        
        .msg-time { font-size: 9px; color: #444; margin-top: 5px; width: 100%; display: block; }
        .user-wrapper .msg-time { text-align: right; color: rgba(255, 255, 255, 0.2); }
        .user-wrapper .msg-time::after { content: ' ✓✓'; color: #FF1E1E; font-weight: bold; }

        /* Typing Indicator dots */
        .typing-indicator { display: none; align-self: flex-start; background: #1A1A1A; border: 1px solid rgba(255,30,30,0.15); padding: 14px 20px; border-radius: 18px 18px 18px 2px; font-size: 12px; color: #666; gap: 5px; align-items: center; margin-left: 20px; }
        .dots { display: flex; gap: 4px; }
        .dots span { width: 6px; height: 6px; background: #FF1E1E; border-radius: 50%; animation: bounce 1.4s infinite ease-in-out both; }
        .dots span:nth-child(1) { animation-delay: -0.32s; }
        .dots span:nth-child(2) { animation-delay: -0.16s; }
        @keyframes bounce { 0%, 80%, 100% { transform: scale(0); } 40% { transform: scale(1.0); } }

        /* Input Controls Layout Panel */
        .input-container { padding: 15px 20px 25px 20px; display: flex; gap: 12px; align-items: center; background: #0D0D0D; }
        .action-icon-btn { background: none; border: none; cursor: pointer; display: flex; justify-content: center; align-items: center; }
        .input-wrapper { flex: 1; background-color: #1A1A1A; border: 1px solid #FF1E1E; border-radius: 30px; display: flex; align-items: center; padding: 2px 5px 2px 20px; }
        .chat-input { flex: 1; background: transparent; border: none; padding: 12px 0; color: #FFFFFF; font-size: 14px; outline: none; }
        .chat-input::placeholder { color: #555; }
        
        /* Fixed Horizontal Vector Send Button Arrow */
        .send-btn { background-color: #FF1E1E; border: none; width: 42px; height: 42px; border-radius: 50%; color: white; cursor: pointer; display: flex; justify-content: center; align-items: center; box-shadow: 0 0 15px rgba(255, 30, 30, 0.4); flex-shrink: 0; margin-left: 5px; }
        .send-btn svg { width: 18px; height: 18px; fill: white; }
        
        .overlay { position: absolute; inset: 0; background: rgba(0,0,0,0.5); display: none; z-index: 98; }
        .overlay.active { display: block; }
    </style>
</head>
<body>

    <!-- 🚨 NEW MATTE BLACK CAR SPLASH INTERFACE (Tap anywhere to trigger V8 blast) -->
    <div id="splash-screen" onclick="igniteEngine()">
        <div class="splash-main-logo">CX</div>
        <div class="splash-sub">Chetak X</div>
        <div class="car-frame"></div>
        <div class="init-text" id="status-label">TAP TO START ENGINE</div>
        <div class="tap-hint" id="hint-label">(Browser safety requires one click to unlock sound)</div>
    </div>

    <!-- MAIN APP STRUCTURE -->
    <div class="phone-container" id="mainApp">
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

        <div class="header">
            <button class="menu-btn" onclick="toggleSidebar()">
                <span></span><span></span><span></span>
            </button>
            <div class="brand-box">
                <div class="brand-logo">CHETAK <span>X</span></div>
                <div class="brand-subtitle">Premium AI Assistant</div>
            </div>
            <button class="settings-btn">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#FF1E1E" stroke-width="2"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>
            </button>
        </div>

        <div class="hero-banner">
            <div class="date-divider">Today</div>
        </div>

        <div class="chat-box" id="chatBox">
            <div class="message-wrapper ai-wrapper">
                <div class="message ai-message">Har Har Mahadev Ranjan bhai! Chetak X active hai. Batao aaj kya system hilaana hai?</div>
                <span class="msg-time">10:29 PM</span>
            </div>
        </div>

        <div class="typing-indicator" id="typingIndicator">
            <div class="dots"><span></span><span></span><span></span></div>
            <span style="font-size:11px; margin-left:5px;">Chetak X is thinking...</span>
        </div>

        <div class="input-container">
            <button class="action-icon-btn">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#666" stroke-width="2"><line x1="4" y1="21" x2="4" y2="14"></line><line x1="4" y1="10" x2="4" y2="3"></line><line x1="12" y1="21" x2="12" y2="12"></line><line x1="12" y1="8" x2="12" y2="3"></line><line x1="20" y1="21" x2="20" y2="16"></line><line x1="20" y1="12" x2="20" y2="3"></line><line x1="1" y1="14" x2="7" y2="14"></line><line x1="9" y1="8" x2="15" y2="8"></line><line x1="17" y1="16" x2="23" y2="16"></line></svg>
            </button>
            <div class="input-wrapper">
                <input type="text" class="chat-input" id="userInput" placeholder="Type your message..." onkeypress="if(event.key === 'Enter') sendMessage()">
            </div>
            <button class="send-btn" onclick="sendMessage()">
                <svg viewBox="0 0 24 24"><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/></svg>
            </button>
        </div>
    </div>

    <script>
        let ignited = false;

        function igniteEngine() {
            if (ignited) return;
            ignited = true;
            
            const splash = document.getElementById('splash-screen');
            const mainApp = document.getElementById('mainApp');
            const status = document.getElementById('status-label');
            document.getElementById('hint-label').style.display = 'none';
            
            // 🔊 Solid V8 Pure Aggressive Racing Startup Audio Sound Node
            const roarAudio = new Audio('https://themes.googleusercontent.com/image?id=1_D5uB3lqN712_XwO10rT74y7_W2H75j8'); 
            // Fallback audio trigger just in case
            const backupAudio = new Audio('https://actions.google.com/sounds/v1/transportation/sports_car_rev_and_pull_away.ogg');
            
            status.innerText = "INITIALIZING V8 TWIN TURBO...";
            splash.classList.add('ignited');
            
            // Fire sound streams
            roarAudio.play().catch(() => backupAudio.play().catch(e => console.log('Audio Blocked')));

            // 5 Seconds precise timing freeze before interface crossfade
            setTimeout(() => {
                splash.style.opacity = '0';
                mainApp.style.opacity = '1';
                setTimeout(() => {
                    splash.style.display = 'none';
                }, 800);
            }, 5000);
        }

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

            const userWrap = document.createElement("div");
            userWrap.className = "message-wrapper user-wrapper";
            userWrap.innerHTML = `<div class="message user-message">${messageText}</div><span class="msg-time">${timeStr}</span>`;
            chatBox.appendChild(userWrap);
            
            inputField.value = "";
            chatBox.scrollTop = chatBox.scrollHeight;

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
                
                loader.style.display = "none";

                const aiWrap = document.createElement("div");
                aiWrap.className = "message-wrapper ai-wrapper";
                aiWrap.innerHTML = `<div class="message ai-message">${data.reply}</div><span class="msg-time">${timeStr}</span>`;
                chatBox.appendChild(aiWrap);

            } catch (error) {
                loader.style.display = "none";
                const errWrap = document.createElement("div");
                errWrap.className = "message-wrapper ai-wrapper";
                errWrap.innerHTML = `<div class="message ai-message">⚠️ System error! Try again.</div><span class="msg-time">${timeStr}</span>`;
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
- Never act like a boring formal robot.
- Talk like a close friend/brother to Ranjan. Keep a slight confident, Haryanvi/Desi bold tone.
- Give short, punchy, and direct answers in Hinglish (Hindi mixed with English).
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
