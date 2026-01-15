"""
TEMPLATE: CONTINUUM SERVER
A Flask app that rewrites its own code if it crashes.
"""
import sys
import os

# Ensure repo root is on path so `import natura` works
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from flask import Flask
import natura

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>My Sovereign App</h1><p>Running on Natura Continuum</p>"


# THE MAGIC LINE
# Wraps the app in Evie's self-healing logic
app = natura.possess(app)


if __name__ == "__main__":
    print(">> SERVER ONLINE (PORT 5000)")
    app.run(port=5000)
