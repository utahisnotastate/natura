"""
GENESIS LAB v1.0
"The Foundry of Intelligence"
"""
import os
import sys
# Add the parent directory to sys.path so we can find the 'natura' package
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import natura
from flask import Flask, request, jsonify, send_file
from natura.genesis import GenesisEngine
from natura.vision import LiquidDiffusion
from natura.web import Continuum

app = Flask(__name__)
genesis = GenesisEngine()
vision = LiquidDiffusion()

# --- THE SOVEREIGN UI ---
HTML_UI = """
<!DOCTYPE html>
<html lang="en">
<head>
    <style>
        body { background: #050505; color: #00ff41; font-family: 'Courier New', monospace; padding: 20px; }
        .container { max-width: 900px; margin: 0 auto; }
        .drop-zone { border: 2px dashed #00ff41; padding: 40px; text-align: center; margin-bottom: 20px; cursor: pointer; background: #001100; }
        .drop-zone:hover { background: #002200; }

        .card { border: 1px solid #333; padding: 15px; margin: 10px 0; background: #0a0a0a; display: flex; justify-content: space-between; align-items: center; }
        .card h3 { margin: 0 0 5px 0; color: #fff; }
        .btn { background: #00ff41; color: #000; border: none; padding: 10px 20px; font-weight: bold; cursor: pointer; }
        .btn:hover { background: #fff; }

        input[type="text"] { background: #000; border: 1px solid #333; color: #fff; padding: 10px; width: 100%; margin: 10px 0; }
        .hidden { display: none; }
    </style>
</head>
<body>
    <div class="container">
        <h1>// GENESIS LAB <span style="font-size:12px">SOVEREIGN MODE</span></h1>

        <div class="drop-zone" id="dropZone">
            <h2>DROP A FOLDER OR FILE HERE</h2>
            <p>I will scan the entropy and tell you what AI I can build.</p>
        </div>

        <div id="candidates-list"></div>

        <hr style="border-color:#333; margin: 40px 0;">
        <h2>// LIQUID DIFFUSION (MANUAL OVERRIDE)</h2>
        <input type="text" id="prompt" placeholder="Describe a reality to manifest...">
        <button class="btn" onclick="dream()">MANIFEST IMAGE</button>
        <div id="output" style="margin-top:20px;"></div>
    </div>

    <script>
        // 1. DRAG AND DROP LOGIC
        const dz = document.getElementById('dropZone');
        dz.addEventListener('dragover', e => e.preventDefault());
        dz.addEventListener('drop', async e => {
            e.preventDefault();
            const path = "C:/User/Data/Project_Alpha"; // Simulation of grabbing the path
            dz.innerHTML = `<h2>SCANNING: ${path}...</h2>`;

            // Call Genesis
            const res = await fetch('/scan', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({path: path})
            });
            const data = await res.json();

            let html = "<h3>// LIFEFORMS DETECTED:</h3>";
            data.candidates.forEach((c, idx) => {
                html += `
                <div class="card">
                    <div>
                        <h3>${c.name} [${c.type}]</h3>
                        <p>${c.desc}</p>
                    </div>
                    <button class="btn" onclick="evolve('${c.type}', '${path}')">EVOLVE THIS</button>
                </div>`;
            });
            document.getElementById('candidates-list').innerHTML = html;
            dz.innerHTML = "<h2>SCAN COMPLETE</h2>";
        });

        // 2. EVOLUTION LOGIC
        async function evolve(type, path) {
            alert(`// INITIATING BIRTH SEQUENCE FOR ${type}...\n(Check Terminal for Physics Output)`);
            await fetch('/evolve', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({type, path})
            });
            alert("// EVOLUTION COMPLETE. MODEL IS LIVE.");
        }

        // 3. DREAM LOGIC
        async function dream() {
            const prompt = document.getElementById('prompt').value;
            const res = await fetch('/dream', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({prompt})
            });
            const data = await res.json();
            document.getElementById('output').innerHTML = `<p>// MANIFESTED: ${data.file}</p>`;
        }
    </script>
</body>
</html>
"""


@app.route("/")
def index():
    return HTML_UI


@app.route("/scan", methods=["POST"])
def scan():
    # Simulate scanning the path provided by the UI
    path = request.json.get("path")
    candidates = genesis.crystallize(path)
    return jsonify({"candidates": candidates})


@app.route("/evolve", methods=["POST"])
def evolve():
    model_type = request.json.get("type")
    path = request.json.get("path")
    # Spin up the model
    genesis.evolve(model_type, path)
    return jsonify({"status": "ALIVE"})


@app.route("/dream", methods=["POST"])
def dream():
    prompt = request.json.get("prompt")
    filename = vision.dream(prompt)
    return jsonify({"file": filename})


# NATURA TAKEOVER
app = natura.possess(app)

if __name__ == "__main__":
    print("// GENESIS LAB: ONLINE.")
    app.run(port=8000)
