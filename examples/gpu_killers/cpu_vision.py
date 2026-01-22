"""
GPU KILLER: LIQUID VISION (LIVE KINETICS)
Goal: Upscale an image without a GPU using Fluid Dynamics.
Method: Laplacian Diffusion + Bicubic Metric Expansion
"""
import sys
import os
import time
from PIL import Image
import numpy as np

# BOILERPLATE: Add repo root to path so `import natura` works
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from natura.vision import MirageEngine

def create_sample_if_missing(filename):
    if not os.path.exists(filename):
        print(f"// INIT: Creating sample input '{filename}'...")
        # Create a tiny 64x64 image
        data = np.random.randint(0, 255, (64, 64, 3), dtype=np.uint8)
        img = Image.fromarray(data)
        img.save(filename)

def main():
    print("=== THE GPU IS OBSOLETE ===")
    print("Target: Upscale Low-Res -> High-Res")
    print("Hardware: CPU Only (Liquid State Physics)")

    # 1. Setup Data
    input_file = "low_res_sample.png"
    create_sample_if_missing(input_file)

    # 2. Initialize Mirage
    mirage = MirageEngine()

    start = time.time()

    # 3. Run Liquid Upscale
    # This now performs actual matrix math on the CPU
    output = mirage.upscale_liquid(input_file, factor=4)

    end = time.time()

    # Calculate effective "FPS" or speed
    print(f"\n[SUCCESS] Manifested in {end - start:.2f}s")
    print(f"VRAM Used: 0MB (Sovereign RAM Only)")
    print(f"Output: {output}")

if __name__ == "__main__":
    main()
