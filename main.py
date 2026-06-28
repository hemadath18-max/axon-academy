from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os
import uvicorn

app = FastAPI(title="Axon Academy Cross-Platform Core")

@app.get("/", response_class=HTMLResponse)
def load_responsive_platform():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Axon AGI Academy - Portal</title>
        <style>
            :root {
                --bg-deep: #060913;
                --bg-card: #0d1527;
                --bg-input: #121d36;
                --accent-neon: #00ff96;
                --accent-blue: #38bdf8;
                --text-main: #f8fafc;
                --text-muted: #94a3b8;
                --border-slate: #1e293b;
            }

            * {
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }

            body {
                font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
                background-color: var(--bg-deep);
                color: var(--text-main);
                min-height: 100vh;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                align-items: center;
                padding: 20px;
            }

            /* Responsive Main Grid Layout Frame */
            .main-container {
                width: 100%;
                max-width: 1200px;
                display: grid;
                grid-template-columns: 1fr;
                gap: 20px;
                margin: auto;
            }

            /* Tablet and Desktop Split Screen Frame */
            @media (min-width: 768px) {
                .main-container {
                    grid-template-columns: 1fr 1fr;
                    align-items: start;
                }
                .header-panel {
                    grid-column: span 2;
                }
            }

            .header-panel {
                background: linear-gradient(135deg, var(--bg-card) 0%, #111a30 100%);
                padding: 25px;
                border-radius: 16px;
                border: 1px solid var(--border-slate);
                text-align: center;
                box-shadow: 0 10px 30px rgba(0, 255, 150, 0.05);
            }

            h1 {
                color: var(--accent-neon);
                font-size: 28px;
                font-weight: 700;
                letter-spacing: 0.5px;
                margin-bottom: 8px;
            }

            .control-panel {
                background: var(--bg-card);
                border: 1px solid var(--border-slate);
                border-radius: 16px;
                padding: 24px;
                display: flex;
                flex-direction: column;
                gap: 16px;
                height: 100%;
            }

            .input-box {
                width: 100%;
                padding: 16px;
                border-radius: 12px;
                border: 1px solid var(--border-slate);
                background: var(--bg-input);
                color: var(--text-main);
                font-size: 16px;
                transition: all 0.3s ease;
                outline: none;
            }

            .input-box:focus {
                border-color: var(--accent-neon);
                box-shadow: 0 0 0 2px rgba(0, 255, 150, 0.1);
            }

            .btn {
                background: var(--accent-neon);
                color: var(--bg-deep);
                border: none;
                padding: 16px 24px;
                font-size: 16px;
                font-weight: 700;
                border-radius: 12px;
                cursor: pointer;
                transition: all 0.2s ease;
                display: flex;
                justify-content: center;
                align-items: center;
                gap: 8px;
                box-shadow: 0 4px 14px rgba(0, 255, 150, 0.2);
            }

            .btn:hover {
                transform: translateY(-2px);
                box-shadow: 0 6px 20px rgba(0, 255, 150, 0.3);
            }

            .btn:active {
                transform: translateY(0);
            }

            .output-panel {
                background: #020408;
                border: 1px solid var(--border-slate);
                border-radius: 16px;
                min-height: 400px;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                align-items: center;
                padding: 24px;
                position: relative;
            }

            #robot {
                font-size: 80px;
                transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
                margin: auto 0;
                z-index: 2;
                user-select: none;
            }

            #displayImage {
                width: 100%;
                max-width: 280px;
                height: 200px;
                border-radius: 12px;
                border: 1px solid var(--border-slate);
                object-fit: cover;
                display: none;
                margin-top: 20px;
                box-shadow: 0 8px 24px rgba(0,0,0,0.5);
            }

            .bubble {
                background: var(--bg-input);
                color: var(--text-main);
                padding: 16px;
                border-radius: 12px;
                font-size: 15px;
                line-height: 1.6;
                border-left: 4px solid var(--accent-neon);
                text-align: left;
                width: 100%;
            }

            .footer {
                margin-top: 40px;
                font-size: 12px;
                color: var(--text-muted);
                letter-spacing: 0.5px;
            }
        </style>
    </head>
    <body>

        <div class="main-container">
            <!-- Header Banner Section -->
            <div class="header-panel">
                <h1>AXON AGI ACADEMY</h1>
                <p style="color: var(--text-muted); font-size: 15px;">Enterprise Multi-Platform Educational Core</p>
            </div>

            <!-- Left Controls Section -->
            <div class="control-panel">
                <div class="bubble" id="dialogue">
                    AGI Node Online. Input any educational topic or core query parameters below to initiate standard knowledge compilation protocols.
                </div>
                <input type="text" id="userInput" class="input-box" placeholder="Type a subject question (e.g., Heart, Rocket, AI)..." autofocus>
                <button class="btn" onclick="triggerAGIBrain()">
                    <span>Query AGI Engine</span> ⚡
                </button>
            </div>

            <!-- Right Interactive Canvas Section -->
            <div class="output-panel">
                <div id="robot">🤖</div>
                <img id="displayImage" src="" alt="AGI Asset Distribution Layer">
            </div>
        </div>

        <div class="footer">
            Axon Academy Corporate Infrastructure • Secure System Matrix v1.2.0
        </div>

        <script>
            const voiceSynth = window.speechSynthesis;

            function robotSpeak(textToSay) {
                if (!voiceSynth) return;
                voiceSynth.cancel(); 
                const utterance = new SpeechSynthesisUtterance(textToSay);
                utterance.pitch = 1.25; 
                utterance.rate = 0.95;  
                voiceSynth.speak(utterance);
            }

            function triggerAGIBrain() {
                const robot = document.getElementById('robot');
                const dialogue = document.getElementById('dialogue');
                const imgContainer = document.getElementById('displayImage');
                const query = document.getElementById('userInput').value.trim();
                
                if (query === "") {
                    robotSpeak("Please submit an operational query topic.");
                    return;
                }

                // Multi-axis translation sequence matrix
                robot.style.transform = "translateY(-40px) rotate(360deg) scale(1.15)";
                dialogue.innerHTML = "✨ <b>Compiling target database matrix parameters... Please stand by...</b>";
                
                setTimeout(() => {
                    robot.style.transform = "translateY(0px) rotate(0deg) scale(1)";
                    processAGIResponse(query, dialogue, imgContainer);
                }, 1000);
            }

            function processAGIResponse(query, dialogue, imgContainer) {
                const cleanQuery = query.toLowerCase();
                let explanation = "";
                let speechText = "";
                let imageSrc = "";

                if (cleanQuery.includes('heart') || cleanQuery.includes('blood')) {
                    explanation = "<b>❤️ Core Analysis - Cardiovascular Matrix:</b><br>• <b>Atria Chambers</b>: Handle incoming fluid distribution pathways.<br>• <b>Ventricle Units</b>: High-pressure muscle engines driving vascular flow.<br>• <b>Aorta Network</b>: Primary distribution highway for target systemic routing.";
                    speechText = "Accessing human cardiovascular records. The heart utilizes upper atria units to route incoming fluid distribution pathways, and high pressure ventricle muscle engines to drive vascular flow. Ensure you diagram these components for full grading credit.";
                    imageSrc = "
