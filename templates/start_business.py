"""
TEMPLATE: TYCOON BUSINESS LAUNCHER
Use this to spin up a new income stream from your files.
"""
import sys
import os

# Fix import path so `import natura` works when running template directly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from natura.tycoon import TycoonProtocol


def launch():
    print(">> INITIALIZING TYCOON TEMPLATE...")
    tycoon = TycoonProtocol()

    # Step 1: Force Scan specific folder
    print(">> SCANNING ASSETS...")
    # Change this to your folder path (e.g., "C:/Users/me/Documents/Assets")
    assets = tycoon.deep_scan(source="computer")  # returns a summary list (simulated)
    print(f">> ASSETS FOUND: {len(assets)} item(s)")
    for a in assets[:10]:
        print(f" - {a}")

    # Step 2: Launch Wizard
    tycoon.launch_wizard()


if __name__ == "__main__":
    launch()
