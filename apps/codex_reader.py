"""
THE CODEX v1.0
"The Notebook Killer"
"""
import os
import sys

# Fix imports for app running (so `from natura ...` works when run directly)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, jsonify
from natura.scrolls import ScrollEngine
from natura.web import Continuum  # noqa: F401  (side-effect use via natura.possess)
import natura

app = Flask(__name__)
engine = ScrollEngine()
evie = natura.GenerativeModel("evie")

# --- THE CODEX UI ---
HTML_UI = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <title>THE CODEX</title>
    <style>
        body { background: #f4f4f4; color: #333; font-family: 'Georgia', serif; padding: 0; margin: 0; display: flex; height: 100vh; }
        #editor { width: 50%; height: 100%; border: none; padding: 40px; background: #2d2d2d; color: #ccc; font-family: 'Consolas', monospace; font-size: 14px; outline: none; resize: none; box-sizing: border-box; }
        #preview { width: 50%; height: 100%; padding: 40px; overflow-y: auto; box-sizing: border-box; background: #fff; line-height: 1.6; }
        pre { background: #eee; padding: 15px; border-radius: 5px; border-left: 5px solid #00ff41; white-space: pre-wrap; }
        blockquote { border-left: 4px solid #000; padding-left: 15px; color: #555; font-style: italic; background: #f9f9f9; padding: 10px; }
        h1, h2, h3 { color: #000; }
        .status-bar { position: fixed; bottom: 0; left: 0; width: 50%; background: #00ff41; color: #000; padding: 5px; font-family: sans-serif; font-size: 12px; font-weight: bold; text-align: right; box-sizing: border-box; }
    </style>
</head>
<body>
    <textarea id="editor" oninput="scheduleRender()"># The Fibonacci Sequence (Natura Scroll)

Define a function and compute a value below. Note how variables persist across blocks.

```python
print("// LOADING FIBONACCI...")

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print("Fibonacci Function Loaded.")
```

Now let's calculate the 10th number.

```python
result = fib(10)
print(f"The 10th number is: {result}")
```
</textarea>

<div class="status-bar" id="status">STATUS: SOVEREIGN</div>
<div id="preview"></div>

<script>
    let timeout = null;

    function scheduleRender() {
        document.getElementById('status').innerText = "STATUS: THINKING...";
        clearTimeout(timeout);
        timeout = setTimeout(render, 800); // Auto-run after typing stops
    }

    async function render() {
        const text = document.getElementById('editor').value;

        const res = await fetch('/manifest', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({text: text})
        });
        const data = await res.json();

        // Simple Markdown Parser for the View
        let html = data.result
            .replace(/\n/g, '<br>')
            .replace(/```python(.*?)```/gs, '<pre>$1</pre>')
            .replace(/> \[NATURA RESULT\]:<br>> (.*?)(?:<br>|$)/gs, '<blockquote><strong>⚡ REALITY OUTPUT:</strong> $1</blockquote>');

        document.getElementById('preview').innerHTML = html;
        document.getElementById('status').innerText = "STATUS: SYNCHRONIZED";
    }

    // Initial Run
    render();
</script>
</body>
</html>
"""


@app.route("/")
def index():
    return HTML_UI


@app.route("/manifest", methods=["POST"])
def manifest():
    # THE MAGIC: Execute the scroll
    text = request.json.get("text") or ""
    rendered_text = engine.manifest(text)
    return jsonify({"result": rendered_text})


# NATURA TAKEOVER
app = natura.possess(app)


if __name__ == "__main__":
    print("// THE CODEX: ONLINE.")
    print("// POINT BROWSER TO: http://localhost:9000")
    app.run(port=9000)
