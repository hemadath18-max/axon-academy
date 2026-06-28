from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os
import uvicorn

app = FastAPI(title="Axon Academy Core Engine")

@app.get("/", response_class=HTMLResponse)
def load_animated_robot():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body { font-family: 'Segoe UI', sans-serif; background-color: #0b0f19; color: #ffffff; text-align: center; margin: 0; padding: 15px; }
            .header-panel { background: #131c2e; padding: 15px; border-radius: 12px; border: 1px solid #1f2d4d; margin-bottom: 15px; }
            h2 { color: #00ff96; margin: 0 0 5px 0; font-size: 22px; }
            #screen { position: relative; width: 100%; height: 50vh; background: #070a12; border: 2px dashed #1f2d4d; border-radius: 15px; overflow: hidden; margin-top: 15px; }
            #robot { position: absolute; width: 70px; height: 70px; font-size: 45px; text-align: center; line-height: 70px; transition: all 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
            .bubble { background: #1c283f; color: #ffffff; padding: 12px; border-radius: 10px; font-size: 14px; line-height: 1.5; border-left: 4px solid #00ff96; text-align: left; }
            .input-box { width: 90%; padding: 12px; border-radius: 8px; border: 1px solid #1f2d4d; background: #131c2e; color: white; font-size: 14px; margin-top: 10px; box-sizing: border-box; }
            .btn { background: #00ff96; color: #0b0f19; border: none; padding: 12px 20px; font-size: 15px; font-weight: bold; border-radius: 8px; margin-top: 10px; width: 90%; }
        </style>
    </head>
    <body>

        <div class="header-panel">
            <h2>Axon Academy AI 🤖</h2>
            <div id="dialogue">Welcome to Axon Academy, Hemadath! Type any exam topic below (try: Heart, Rocket, or Photosynthesis) and watch your AI guide fly to your help!</div>
        </div>

        <input type="text" id="userInput" class="input-box" placeholder="Ask your Axon guide a question...">
        <button class="btn" onclick="askRobot()">Ask & Fly Bot! 🚀</button>

        <div id="screen">
            <div id="robot">🤖</div>
        </div>

        <script>
            function askRobot() {
                var robot = document.getElementById('robot');
                var dialogue = document.getElementById('dialogue');
                var query = document.getElementById('userInput').value.toLowerCase();
                
                var maxX = document.getElementById('screen').clientWidth - 70;
                var maxY = document.getElementById('screen').clientHeight - 70;
                var randomX = Math.floor(Math.random() * maxX);
                var randomY = Math.floor(Math.random() * maxY);
                
                robot.style.left = randomX + 'px';
                robot.style.top = randomY + 'px';
                
                if (query.includes('heart')) {
                    dialogue.innerHTML = "<b>🤖 Axon Guide Explains the Heart:</b><br>• Labeled Part A (Aorta): Main highway sending oxygen-rich blood to your body.<br>• Labeled Part B (Ventricles): Lower chambers that pump blood hard. Memorize this for an A+!";
                } else if (query.includes('rocket') || query.includes('space')) {
                    dialogue.innerHTML = "<b>🚀 Axon Guide Explains Rockets:</b><br>• Nose Cone: Streamlined tip to cut air friction.<br>• Propulsion Nozzle: Expels hot gas downwards to create upward thrust!";
                } else if (query.includes('photo')) {
                    dialogue.innerHTML = "<b>🍃 Axon Guide Explains Photosynthesis:</b><br>• Chloroplasts trap solar light energy.<br>• Leaves combine Carbon Dioxide + Water to output Glucose food + Oxygen gas!";
                } else if (query === "") {
                    dialogue.innerText = "🤖 'Please type a school topic inside the box so I can fetch the exam details for you!'";
                } else {
                    dialogue.innerHTML = "<b>🤖 Searching diagrams for '" + query + "'...</b><br>Found a perfect match! Focus on the main center label and outer structures to score full marks in your test paper!";
                }
            }
            document.getElementById('robot').style.left = '30px';
            document.getElementById('robot').style.top = '30px';
        </script>

    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
  
