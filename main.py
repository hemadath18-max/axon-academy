from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os, uvicorn

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """<!DOCTYPE html><html><head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { font-family: sans-serif; background: #0b0f19; color: white; text-align: center; padding: 15px; }
        .box { background: #131c2e; padding: 15px; border-radius: 12px; border: 1px solid #1f2d4d; max-width: 500px; margin: 0 auto; }
        #screen { height: 300px; background: #070a12; border-radius: 12px; margin-top: 15px; position: relative; overflow: hidden; padding: 10px; }
        #bot { font-size: 60px; position: absolute; left: 40%; top: 20px; transition: all 0.5s ease; }
        #pic { width: 100%; height: 150px; object-fit: cover; border-radius: 8px; display: none; margin-top: 100px; }
        input { width: 90%; padding: 12px; border-radius: 8px; border: 1px solid #1f2d4d; background: #070a12; color: white; margin-top: 10px; }
        button { background: #00ff96; color: black; border: none; padding: 12px; width: 94%; border-radius: 8px; font-weight: bold; margin-top: 10px; }
    </style></head><body>
    <div class="box">
        <h2>Axon Academy AI 🤖</h2>
        <p id="msg">Hello Hemadath! Ask me anything (try: Heart, Rocket, or AI). I will move, talk, and show the image!</p>
        <input type="text" id="in" placeholder="Type your school question here...">
        <button onclick="ask()">Ask & Fly Bot! 🚀</button>
        <div id="screen"><div id="bot">🤖</div><img id="pic"></div>
    </div>
    <script>
        function speak(t) { window.speechSynthesis.cancel(); let u = new SpeechSynthesisUtterance(t); u.pitch = 1.3; window.speechSynthesis.speak(u); }
        function ask() {
            let q = document.getElementById('in').value.toLowerCase();
            let b = document.getElementById('bot');
            let m = document.getElementById('msg');
            let p = document.getElementById('pic');
            
            b.style.left = Math.floor(Math.random() * 70) + '%';
            b.style.top = Math.floor(Math.random() * 30) + 'px';
            
            if(q.includes('heart')) {
                m.innerHTML = "<b>🤖 Explaining Heart:</b><br>• Aorta: Main blood highway.<br>• Ventricles: Lower pump chambers.";
                p.src = "https://unsplash.com"; p.style.display = "block";
                speak("Look at the heart diagram! The aorta is the main artery, and ventricles are the lower pumps.");
            } else if(q.includes('rocket') || q.includes('space')) {
                m.innerHTML = "<b>🚀 Explaining Rockets:</b><br>• Nose Cone: Cuts air friction.<br>• Nozzle: Pushes gas down to go up.";
                p.src = "https://unsplash.com"; p.style.display = "block";
                speak("Launching to space! The nose cone cuts friction, and the nozzle pushes gas down to move up.");
            } else if(q.includes('ai') || q.includes('intelligence')) {
                m.innerHTML = "<b>🧠 Explaining AI:</b><br>• Artificial Intelligence uses networks like artificial brain cells to learn answers instantly.";
                p.src = "https://unsplash.com"; p.style.display = "block";
                speak("Artificial Intelligence uses networks that act like brain cells to study patterns and learn answers instantly.");
            } else {
                m.innerHTML = "<b>🤖 Searching Knowledge for '" + q + "':</b><br>Analyzing diagram. Focus on core parts for top marks!";
                p.src = "https://unsplash.com"; p.style.display = "block";
                speak("Searching global data for " + q + ". Study the main core layout labels carefully to get top marks!");
            }
        }
    </script></body></html>"""

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
    
