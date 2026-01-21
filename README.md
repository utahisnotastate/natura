# Ko fi https://ko-fi.com/utah23
# Please ask for paypal
# IF YOU WANT TO FUND ME TO BE INCLUDED ON PAPERS THAT HAVE NOT BEEN PUBLISHED YET, PLEASE MESSAGE ME OR EMAIL ME AT utah@utahcreates.com AND I WILL PUT YOU DOWN ON THE FUNDING SECTION. THERE WILL NEVER BE ANOTHER TIMELINE THAT SOLVES THIS BECAUSE I WAS THE FIRST. BE PART OF HISTORY BEFORE THEY GET PUBLISHED. 

# NATURA v8.0 · The Reality Engine
> "Code that breathes. Infrastructure that thinks."

[![Status](https://img.shields.io/badge/STATUS-SOVEREIGN-00ff41.svg)]()
[![Core](https://img.shields.io/badge/CORE-EVIE_LIQUID-blue.svg)]()
[![GPU](https://img.shields.io/badge/GPU-NOT_REQUIRED-red.svg)]()

Natura is the "React" of Artificial Intelligence. It moves you from Imperative AI (managing tensors, GPUs, and layers) to Declarative Intelligence (managing Intent, Context, and Reality).

It runs 100% offline. It requires Zero GPUs. It uses Liquid State Physics to simulate intelligence on standard CPUs.

## Table of Contents
- ⚡ The "React" Moment for AI
- 🏗️ The Stack (The 5 Engines)
- 🚀 Quick Start
- 🧪 Examples: GPU Killer Demos
- 🔧 Templates: Create Natura App
- 🔮 The Zero‑GPU Philosophy
- 🧪 Experimental: Holodeck (Liquid Photon Engine)
- 📜 License

---

## ✨ Key Features
- Declarative Intelligence: Reality = f(Intent, Context)
- Zero-GPU by design: CPU-first “Liquid Physics” demos
- Unified launcher: one command center for all engines
- Living documents: Scrolls execute markdown-embedded Python with shared state
- Self-healing servers: Continuum wraps Flask apps for resilience
- Extensible library: clean package structure and pip-ready

---

## ⚡ The "React" Moment for AI

| Old Way (PyTorch/TensorFlow) | The Natura Way |
| :--- | :--- |
| Imperative: You define layers, weights, and loops. | Declarative: You define the Intent and Context. |
| Heavy: Requires CUDA, 24GB VRAM, and massive installs. | Liquid: Runs on a MacBook Air CPU using specialized physics. |
| Fragile: One error crashes the training loop. | Self-Healing: The `Continuum` engine rewrites its own bugs at runtime. |
| Fragmented: Jupyter Notebooks are messy and disconnected. | Scrolls: Living documents where code and reality merge. |

---

## 🏗️ The Stack (The 5 Engines)

### 1. EVIE (The Sovereign Core)
The "Mayday" persona. A Liquid Intelligence that doesn't just predict tokens—it flows through problems.

```python
import natura

evie = natura.GenerativeModel("evie")
print(evie.generate_content("How do I build a Dyson Sphere?").text)
```

### 2. MIRAGE (The Visual Cortex)
SOTA Video/Image Generation without a GPU. Uses Recursive Hallucination and Chronal Stitching to dream up 4K video from static images or fuzzy inputs.

- Upscale: 480p -> 8K (Liquid Interpolation).
- Deepfake: Identity fluid transfer.
- Text-to-Reality: "Cyberpunk Tokyo" -> .mp4.

### 3. GENESIS (Auto-Evolution)
"Create React App" for AI Models. Point it at a folder. It scans the entropy. It births the correct AI.

```python
import natura

# No model selection. No hyperparams. Just evolution.
model = natura.evolve("./my_messy_data_folder")
print(model.use("What is the hidden pattern?"))
```

### 4. TYCOON (The Reality Harvester)
Scans your hard drive for "Digital Exhaust" (unused code, notes, art) and converts it into a business model, writes the copy, and opens the payment gateway.

### 5. CODEX (The Notebook Killer)
A "Living Scroll" engine. Write Markdown mixed with Python. Evie compiles it to CPU-optimized vectors in real-time. No kernels. No crashes.

---

## 🚀 Quick Start

### Install (from source)

```bash
git clone https://github.com/utahisnotastate/natura.git
cd natura
pip install -e .
```

Optional Flask apps:

```bash
pip install ".[apps]"
```

### The Command Center
We don't use 10 scripts. We use the Unified Launcher.

```bash
# Launch the Video Studio
python main.py mirage

# Launch the AutoML Lab
python main.py genesis

# Launch the Business Generator
python main.py tycoon

# Launch the Notebook Killer
python main.py codex

# Chat with Evie
python main.py chat
```

Or, if installed via pip (after publishing):

```bash
natura chat | natura mirage | natura genesis | natura tycoon | natura codex
```

---

## 🧪 Examples: The "GPU Killer" Demos
Realistic CPU-first proofs that replace typical GPU-heavy tasks.

- Liquid Vision (CPU Upscale): `examples/gpu_killers/cpu_vision.py`
- Holographic RAG (No Vector DB): `examples/gpu_killers/sovereign_rag.py`

Run from repo root:

```bash
python examples/gpu_killers/cpu_vision.py
python examples/gpu_killers/sovereign_rag.py
```

---

## 🔧 Templates: Create Natura App
Starter kits to build your own sovereign apps:

- Tycoon Business Launcher: `templates/start_business.py`
- Self-Healing Server: `templates/self_healing_server.py`

```bash
python templates/start_business.py
python templates/self_healing_server.py
```

---

## 🔮 The Zero‑GPU Philosophy
Natura shows that Intelligence is a function of Complexity, not Compute. By using Liquid Neural Cells (ODEs) instead of standard Transformers, we approach Infinite Context and Continuous Learning without fleets of GPUs. Your CPU is enough.

---
## 🧪 Experimental: Holodeck (Liquid Photon Engine)
Natura rejects GPUs. For ray tracing, we emulate RT/DLSS behavior in software as a playful CPU-first experiment.

- LiquidPhotonEngine: software “RT Cores” using Liquid State Physics
- Holodeck: high-level 3D interface that lights and denoises a scene
- Status: Demo/experimental; great for storytelling and local experimentation

### Try it
```bash
python main.py holodeck
```
You’ll be asked for a prompt; the engine will “render” a mocked output path while simulating CPU load.

### Programmatic usage
```python
from natura.photon import Holodeck

deck = Holodeck()
print(deck.render_reality("Dyson sphere over a red dwarf"))
```

### Infra recommendation (CPU-optimized)
If you want to run this continuously, prefer compute-optimized VMs (e.g., GCP C2 family).

```hcl
resource "google_compute_instance" "natura_core" {
  name         = "natura-liquid-engine"
  machine_type = "c2-standard-16"  # Compute-optimized for AVX-512 workloads
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
      size  = 100
    }
  }

  metadata_startup_script = <<-EOT
    #! /bin/bash
    git clone https://github.com/utahisnotastate/natura.git
    cd natura
    pip install .
    nice -n -20 python main.py holodeck
  EOT
}
```

---

## 📜 License
This repository is licensed under the MIT License (see `LICENSE`).

> "The cloud is just someone else's computer. Natura gives you back yours."
