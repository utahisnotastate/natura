"""
MIRAGE STUDIO v1.0
"The Sovereign Video Foundry"
"""
import os
from flask import Flask, request, jsonify, send_file

import sys
# Add the parent directory to sys.path so we can find the 'natura' package
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from natura.vision import MirageEngine
from natura.web import Continuum
import natura

# 1. INITIALIZE REALITY ENGINES
app = Flask(__name__)
mirage = MirageEngine()
evie = natura.GenerativeModel("evie")

# 2. DEFINE THE UI (The "Continuum" serves this HTML)
# We inject a simple React-like interface directly via Python
HTML_UI = """
<!DOCTYPE html>
<html lang="en">
<head>
    <style>
        body { background: #0a0a0a; color: #00ff41; font-family: monospace; padding: 20px; }
        .drop-zone { border: 2px dashed #00ff41; padding: 50px; text-align: center; margin-bottom: 20px; cursor: pointer; }
        .drop-zone:hover { background: #001a05; }
        input[type="text"] { background: #000; border: 1px solid #00ff41; color: #fff; padding: 10px; width: 80%; }
        button { background: #00ff41; color: #000; border: none; padding: 10px 20px; font-weight: bold; cursor: pointer; margin-top: 10px; }
        .gallery { display: flex; gap: 10px; margin-top: 20px; }
        video { border: 1px solid #333; max-width: 300px; }
    </style>
</head>
<body>
    <h1>// MIRAGE STUDIO [PRIVATE_INSTANCE]</h1>

    <div class="drop-zone" id="dropZone">
        <h2>DRAG SOURCE VIDEO HERE</h2>
        <p>(Supports: .mp4, .mov, .mkv, .avi)</p>
    </div>

    <div id="controls">
        <h3>// REALITY CONTROLS</h3>
        <input type="text" id="prompt" placeholder="Describe the new reality (e.g., 'Cyberpunk 2077 style', 'Make them an Orc')">
        <br>
        <button onclick="process('upscale')">ENHANCE (4K LIQUID UPSCALER)</button>
        <button onclick="process('dream')">DREAM (GENERATE VIDEO)</button>
        <button onclick="process('identity')">SWAP IDENTITY (DEEPFAKE)</button>
    </div>

    <h3>// OUTPUT STREAM</h3>
    <div class="gallery" id="gallery"></div>

    <script>
        let selectedFile = null;

        document.getElementById('dropZone').addEventListener('dragover', (e) => e.preventDefault());
        document.getElementById('dropZone').addEventListener('drop', (e) => {
            e.preventDefault();
            selectedFile = e.dataTransfer.files[0];
            document.getElementById('dropZone').innerHTML = `<h2>LOCKED: ${selectedFile.name}</h2>`;
        });

        async function process(mode) {
            if (!selectedFile) return alert("FEED ME A FILE FIRST.");

            const formData = new FormData();
            formData.append('video', selectedFile);
            formData.append('prompt', document.getElementById('prompt').value);
            formData.append('mode', mode);

            document.getElementById('gallery').innerHTML += "<p>// RENDERING... PLEASE WAIT...</p>";

            const res = await fetch('/process', { method: 'POST', body: formData });
            const data = await res.json();

            document.getElementById('gallery').innerHTML += `
                <div>
                    <p>[${mode.toUpperCase()}] COMPLETE</p>
                    <video controls src="/download?path=${data.path}"></video>
                </div>
            `;
        }
    </script>
</body>
</html>
"""


@app.route("/")
def index():
    return HTML_UI


@app.route("/process", methods=["POST"])
def process_video():
    video = request.files['video']
    prompt = request.form.get('prompt')
    mode = request.form.get('mode')

    # Save Upload locally
    upload_path = f"./temp_{video.filename}"
    video.save(upload_path)

    output_path = ""

    # EVIE DECIDES THE WORKFLOW
    if mode == "upscale":
        output_path = mirage.upscale_liquid(upload_path, factor=4)
    elif mode == "dream":
        output_path = mirage.dream_transfer(upload_path, prompt)
    elif mode == "identity":
        # In a real app, you'd upload a face image too.
        # For the demo, Evie creates a synthetic face.
        output_path = mirage.identity_synthesis("synthetic_face", upload_path)

    return jsonify({"status": "MANIFESTED", "path": output_path})


@app.route("/download")
def download():
    return send_file(request.args.get('path'))


# 3. NATURA TAKEOVER (Auto-Healing Server)
app = natura.possess(app)

if __name__ == "__main__":
    print("// MIRAGE STUDIO: ONLINE.")
    print("// POINT BROWSER TO: http://localhost:5000")
    app.run(port=5000)
