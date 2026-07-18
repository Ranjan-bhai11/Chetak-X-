import os
import json
from flask import Flask, render_template, request, jsonify
from groq import Groq

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
HTML_FILE_PATH = os.path.join(TEMPLATES_DIR, 'index.html')

if not os.path.exists(TEMPLATES_DIR):
    os.makedirs(TEMPLATES_DIR)

# 🚀 V8 ENGINE SOUND BYPASS + MAHADEV TILAK HUD + FULL SIDE BORDERS (15 SECONDS)
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
        
        /* 🚨 CYBER SPLASH OVERLAY WITH SIDE HUD GRAPHICS */
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
            padding: 20px;
            cursor: pointer;
        }

        /* THE EXACT MOCKUP SIDE BORDERS & HUD CORNERS */
        .cyber-border-frame {
            position: absolute;
            inset: 15px;
            border: 1px solid rgba(255, 30, 30, 0.08);
            pointer-events: none;
            box-shadow: 0 0 20px rgba(0,0,0,0.8) inset;
        }
        
        /* Glowing Tech Corners */
        .cyber-border-frame::before, .cyber-border-frame::after {
            content: '';
            position: absolute;
            width: 25px;
            height: 25px;
            border-color: rgba(255, 30, 30, 0.2);
            border-style: solid;
            transition: all 0.5s ease;
        }
        .cyber-border-frame::before { top: -2px; left: -2px; border-width: 3px 0 0 3px; }
        .cyber-border-frame::after { bottom: -2px; right: -2px; border-width: 0 3px 3px 0; }

        /* Activated State for Borders */
        #splash-screen.active-core .cyber-border-frame::before { border-color: #FF1E1E; box-shadow: 0 0 15px rgba(255, 30, 30, 0.4); }
        #splash-screen.active-core .cyber-border-frame::after { border-color: #FF1E1E; box-shadow: 0 0 15px rgba(255, 30, 30, 0.4); }

        /* HUD Side Brackets */
        .side-bracket {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            width: 4px;
            height: 120px;
            background: linear-gradient(180deg, transparent, #222, transparent);
            transition: all 1s ease;
        }
        .side-bracket.left { left: 8px; border-radius: 0 4px 4px 0; }
        .side-bracket.right { right: 8px; border-radius: 4px 0 0 4px; }
        
        #splash-screen.active-core .side-bracket {
            background: linear-gradient(180deg, transparent, #FF1E1E, transparent);
            box-shadow: 0 0 10px #FF1E1E;
            opacity: 0.4;
        }

        /* 🔱 PURE CSS MAHADEV TRIPUNDRA TILAK ACCENT */
        .mahadev-tilak-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            position: relative;
            width: 120px;
            height: 45px;
            margin-bottom: 20px;
            z-index: 10;
        }
        .tilak-line {
            width: 85px;
            height: 3px;
            background: linear-gradient(90deg, transparent, #333 50%, transparent);
            margin: 2.5px 0;
            border-radius: 10px;
            transition: all 1s ease;
        }
        .tilak-line.mid { width: 100px; }
        .tilak-line.bot { width: 75px; }
        
        .center-red-bindu {
            position: absolute;
            width: 8px;
            height: 24px;
            background: #220000;
            border-radius: 50% 50% 50% 50% / 40% 40% 60% 60%;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            z-index: 12;
            transition: all 0.6s ease;
        }

        /* Glowing Active State for Tilak */
        #splash-screen.active-core .tilak-line {
            background: linear-gradient(90deg, transparent, #888 20%, #FFF 50%, #888 80%, transparent);
            box-shadow: 0 0 8px rgba(255, 255, 255, 0.2);
        }
        #splash-screen.active-core .center-red-bindu {
            background: linear-gradient(180deg, #FF0000, #FF1E1E);
            box-shadow: 0 0 15px #FF0000, 0 0 30px #FF1E1E;
        }

        .splash-main-logo { font-size: 38px; font-weight: 700; color: #FFFFFF; letter-spacing: 6px; margin-bottom: 5px; text-align: center; z-index: 10; }
        .splash-main-logo span { color: #FF1E1E; }
        .splash-sub { font-size: 10px; color: #444; letter-spacing: 4px; text-transform: uppercase; margin-bottom: 50px; z-index: 10; }

        /* Glowing Cyber Core Ring Loader */
        .core-container {
            position: relative;
            width: 170px;
            height: 170px;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 10;
        }
        .outer-ring {
            position: absolute;
            width: 100%;
            height: 100%;
            border: 3px solid #111;
            border-radius: 50%;
            box-shadow: none;
        }
        #splash-screen.active-core .outer-ring {
            border-top: 3px solid #FF1E1E;
            animation: rotateCore 1.8s linear infinite;
            box-shadow: 0 0 25px rgba(255, 30, 30, 0.3);
        }
        
        .inner-core {
            width: 130px;
            height: 130px;
            background: radial-gradient(circle, #0c0c0e 0%, #020202 100%);
            border: 1px solid #1c1c1c;
            border-radius: 50%;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            box-shadow: 0 0 35px rgba(0,0,0,0.9) inset;
        }
        .center-brand-logo {
            font-size: 26px;
            font-weight: 800;
            color: #444;
            letter-spacing: 2px;
            line-height: 1;
            transition: all 0.8s ease;
        }
        .center-brand-logo span { color: #222; transition: all 0.8s ease; }
        #splash-screen.active-core .center-brand-logo { color: #FFFFFF; text-shadow: 0 0 15px rgba(255, 30, 30, 0.8); }
        #splash-screen.active-core .center-brand-logo span { color: #FF1E1E; }
        
        .core-counter { font-size: 11px; font-weight: 500; color: #333; margin-top: 6px; letter-spacing: 1px; }
        #splash-screen.active-core .core-counter { color: #666; }

        @keyframes rotateCore {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .init-text { font-size: 11px; color: #444; letter-spacing: 4px; font-weight: 600; margin-top: 50px; text-transform: uppercase; text-align: center; min-height: 20px; z-index: 10; transition: color 0.5s; }
        #splash-screen.active-core .init-text { color: #FF1E1E; }
        .tap-hint { font-size: 9px; color: #666; letter-spacing: 1px; margin-top: 10px; z-index: 10; }

        /* 📱 MAIN CONSOLE DASHBOARD */
        .phone-container { width: 100%; max-width: 420px; height: 100vh; background-color: #0D0D0D; display: flex; flex-direction: column; border: 1px solid #1A1A1A; position: relative; opacity: 0; transition: opacity 0.5s ease; }
        .header { padding: 15px 20px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #1A1A1A; z-index: 10; background: #0D0D0D; }
        .menu-btn { background: none; border: none; cursor: pointer; display: flex; flex-direction: column; gap: 5px; }
        .menu-btn span { width: 22px; height: 2px; background-color: #FF1E1E; display: block; border-radius: 2px; }
        .brand-box { text-align: center; }
        .brand-logo { font-size: 20px; font-weight: 700; color: #FFFFFF; letter-spacing: 2px; line-height: 1; }
        .brand-logo span { color: #FF1E1E; }
        .brand-subtitle { font-size: 8px; color: #666; text-transform: uppercase; letter-spacing: 1.5px; margin-top: 4px; }
        .settings-btn { background: none; border: none; cursor: pointer; }
        
        .top-deck-banner { width: 100%; height: 140px; background: linear-gradient(180deg, #000 0%, #0D0D0D 100%); border-bottom: 1px solid #1A1A1A; display: flex; align-items: center; justify-content: center; flex-shrink: 0; position: relative; }
        .mini-brand { font-size: 11px; letter-spacing: 6px; font-weight: 700; color: rgba(255,255,255,0.03); text-transform: uppercase; }
        .date-divider { position: absolute; bottom: 10px; left: 50%; transform: translateX(-50%); background: #1A1A1A; padding: 4px 12px; border-radius: 20px; font-size: 10px; color: #666; font-weight: 500; }

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

        .typing-indicator { display: none; align-self: flex-start; background: #1A1A1A; border: 1px solid rgba(255,30,30,0.15); padding: 14px 20px; border-radius: 18px 18px 18px 2px; font-size: 12px; color: #666; gap: 5px; align-items: center; margin-left: 20px; }
        .dots { display: flex; gap: 4px; }
        .dots span { width: 6px; height: 6px; background: #FF1E1E; border-radius: 50%; animation: bounce 1.4s infinite ease-in-out both; }
        .dots span:nth-child(1) { animation-delay: -0.32s; }
        .dots span:nth-child(2) { animation-delay: -0.16s; }
        @keyframes bounce { 0%, 80%, 100% { transform: scale(0); } 40% { transform: scale(1.0); } }

        .input-container { padding: 15px 20px 25px 20px; display: flex; gap: 12px; align-items: center; background: #0D0D0D; }
        .action-icon-btn { background: none; border: none; cursor: pointer; display: flex; justify-content: center; align-items: center; }
        .input-wrapper { flex: 1; background-color: #1A1A1A; border: 1px solid #FF1E1E; border-radius: 30px; display: flex; align-items: center; padding: 2px 5px 2px 20px; }
        .chat-input { flex: 1; background: transparent; border: none; padding: 12px 0; color: #FFFFFF; font-size: 14px; outline: none; }
        .chat-input::placeholder { color: #555; }
        
        .send-btn { background-color: #FF1E1E; border: none; width: 42px; height: 42px; border-radius: 50%; color: white; cursor: pointer; display: flex; justify-content: center; align-items: center; box-shadow: 0 0 15px rgba(255, 30, 30, 0.4); flex-shrink: 0; margin-left: 5px; }
        .send-btn svg { width: 18px; height: 18px; fill: white; }
        
        .sidebar { position: absolute; top: 0; left: -100%; width: 75%; height: 100%; background: #0D0D0D; border-right: 1px solid #1A1A1A; z-index: 99; transition: 0.3s ease; padding: 30px 20px; display: flex; flex-direction: column; }
        .sidebar.active { left: 0; }
        .sidebar-header { margin-bottom: 40px; }
        .sidebar-menu { display: flex; flex-direction: column; gap: 20px; flex: 1; }
        .menu-item { display: flex; align-items: center; gap: 15px; color: #AAA; text-decoration: none; font-size: 14px; padding: 10px 15px; border-radius: 8px; transition: 0.2s; }
        .menu-item:hover, .menu-item.active { background: rgba(255,30,30,0.1); color: #FFF; border-left: 3px solid #FF1E1E; }
        .sidebar-footer { font-size: 10px; color: #444; text-align: center; }
        .overlay { position: absolute; inset: 0; background: rgba(0,0,0,0.5); display: none; z-index: 98; }
        .overlay.active { display: block; }
    </style>
</head>
<body>

    <!-- 🚨 NEW DYNAMIC CORE SPLASH SCREEN WITH HUD CORNER BORDERS & V8 ENGINE TRIGGER -->
    <div id="splash-screen" onclick="igniteEngineCore()">
        <div class="cyber-border-frame"></div>
        <div class="side-bracket left"></div>
        <div class="side-bracket right"></div>
        
        <!-- 🔱 PURE CSS FUTURISTIC TRIPUNDRA TILAK ACCENT -->
        <div class="mahadev-tilak-container">
            <div class="tilak-line top"></div>
            <div class="tilak-line mid"></div>
            <div class="tilak-line bot"></div>
            <div class="center-red-bindu"></div>
        </div>

        <div class="splash-main-logo">CHETAK <span>X</span></div>
        <div class="splash-sub">Premium AI Assistant</div>
        
        <div class="core-container">
            <div class="outer-ring"></div>
            <div class="inner-core">
                <div class="center-brand-logo">C<span>X</span></div>
                <div class="core-counter" id="percentage-node">0%</div>
            </div>
        </div>
        
        <div class="init-text" id="status-label">TAP TO IGNITE CORE</div>
        <div class="tap-hint" id="hint-label">(Unlocks V8 Exhaust Sports Roar)</div>
    </div>

    <!-- MAIN CONSOLE DOCK -->
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

        <div class="top-deck-banner">
            <div class="mini-brand">CHETAK X CORE</div>
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
        let coreIgnited = false;

        function igniteEngineCore() {
            if (coreIgnited) return;
            coreIgnited = true;

            const splash = document.getElementById('splash-screen');
            const mainApp = document.getElementById('mainApp');
            const pctNode = document.getElementById('percentage-node');
            const statusLabel = document.getElementById('status-label');
            document.getElementById('hint-label').style.display = 'none';

            // 🔊 Bypassed HTML5 Verified Audio Asset Stream (Sports V8 Rev and acceleration sequence)
            const v8Audio = new Audio('https://actions.google.com/sounds/v1/transportation/sports_car_rev_and_pull_away.ogg');
            v8Audio.volume = 1.0;
            v8Audio.play().catch(e => console.log('Audio Context Bypass active'));

            // Turn on design grid glow states instantly
            splash.classList.add('active-core');
            statusLabel.innerText = "LOADING SECURE ENGINES...";

            let currentPct = 0;
            const targetTime = 15000; // 15 Seconds Matrix
            const intervalTime = targetTime / 100;

            const loaderInterval = setInterval(() => {
                currentPct++;
                pctNode.innerText = `${currentPct}%`;
                
                if (currentPct === 25) statusLabel.innerText = "TUNING TWIN TURBO PIPES...";
                if (currentPct === 50) statusLabel.innerText = "INJECTING SYSTEM INSTRUCTIONS...";
                if (currentPct === 75) statusLabel.innerText = "ESTABLISHING STEALTH PROTOCOLS...";
                if (currentPct === 95) statusLabel.innerText = "CORE ACTIVE. DEPLOYING WORKSPACE...";

                if (currentPct >= 100) {
                    clearInterval(loaderInterval);
                    setTimeout(() => {
                        splash.style.opacity = '0';
                        mainApp.style.opacity = '1';
                        setTimeout(() => { splash.style.display = 'none'; }, 800);
                    }, 500);
                }
            }, intervalTime);
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
- Talk like a close friend/brother to Ranjan with a bold Haryanvi/Desi tone.
- Give short, punchy answers in Hinglish.
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
