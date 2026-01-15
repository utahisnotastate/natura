# NATURA: The Biological AI Framework 🌿
**(N)atural (A)rtificial (T)ime-continuous (U)niversal (R)ecurrent (A)rchitecture**

> "Stop multiplying matrices. Start simulating reality."

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://zenodo.org/badge/latestdoi/XXXXXXX)
[![Powered By](https://img.shields.io/badge/Powered%20By-NCPs%20%7C%20S4%20%7C%20Diffrax-blue)](https://github.com/mlech26l/ncps)

## 🧠 What is NATURA?

NATURA is a high-level wrapper that unifies the most advanced "Post-TensorFlow" technologies into a single, easy-to-use API. It combines:
1.  **Liquid Neural Networks (NCPs):** For biological, sparse, interpretable brains.
2.  **State Space Models (S4):** For infinite memory and compression.
3.  **Differential Equations (Diffrax):** For continuous-time physics simulation.

**Why use this?**
Standard AI (TensorFlow/PyTorch) is **Static**. It takes a snapshot of the world, processes it, and forgets it.
NATURA is **Fluid**. It treats intelligence as a continuous flow of time, just like your brain does.

---

## 🚀 The "Red Pill" Guide (For Keras Users)

If you are coming from Keras `model.add(Dense(64))`, you need to unlearn "Layers" and learn "Dynamics."

### 1. The Philosophy Shift
| Feature | Old Way (Keras/TensorFlow) | New Way (NATURA) |
| :--- | :--- | :--- |
| **The Building Block** | A static "Layer" of math. | A dynamic "ODE" (Physics Equation). |
| **Time Handling** | Breaks time into jerky steps (t=1, t=2). | Solves time smoothly (t=1.453...). |
| **Memory** | Forgets after ~1000 words. | Remembers forever (Infinite Context). |
| **Noise Tolerance** | Breaks if you add 5% static. | Adapts and ignores noise (Low-pass filter). |
| **Hardware** | Needs a $2000 GPU. | Runs on a $100 Potato (Raspberry Pi/N5095). |

### 2. Code Translation Guide

#### Scenario A: The Robot Controller (CartPole/Drones)
*You want a small, fast brain that reacts instantly.*

**❌ The Keras Way (The "Fat" Brain):**
```python
# 20,000 Parameters. Heavy. Slow.
model = Sequential()
model.add(LSTM(64, return_sequences=True)) 
model.add(Dense(32, activation='relu'))
model.add(Dense(4)) # Motors


Feature,TensorFlow / Keras,NATURA
Philosophy,"""Multiply Matrices""","""Simulate Physics"""
Memory,"Forgets after ~1,000 steps",Remembers forever (S4)
Noise Tolerance,Fails at 5% Noise,Thrives at 50% Noise
Parameter Count,"20,000+ (Bloated)",~400 (Efficient)
Hardware,Needs NVIDIA GPU (RTX 4090),Runs on Intel N5095 (Potato)
Code Complexity,50 lines of boilerplate,"natura.create_life(10, 4)"

✅ The NATURA Way (The "Worm" Brain):Pythonimport natura

# 14 Neurons. 400 Parameters. Instant.
# "Create a lifeform with 10 eyes and 4 motors"
brain = natura.create_life(inputs=10, outputs=4, mode="liquid")
Scenario B: The Long Sequence (Audio/DNA/Stocks)You want to analyze 1 hour of audio (1 million steps).❌ The Keras Way (The "Crash"):Python# This will crash your RAM (OOM Error)
input = Input(shape=(1000000, 1))
x = Attention()(input, input) # Quadratic Memory Cost
✅ The NATURA Way (The "Infinite" Memory):Python# Compresses history into a polynomial. Zero RAM explosion.
brain = natura.create_life(inputs=1, outputs=1, mode="infinite")
🛠 InstallationNATURA sits on top of PyTorch.Bash# 1. Install PyTorch (CPU version is fine!)
pip install torch --index-url [https://download.pytorch.org/whl/cpu](https://download.pytorch.org/whl/cpu)

# 2. Install the Core Engines
pip install ncps s4 diffrax

# 3. Install NATURA
pip install natura-framework
🧬 Code TutorialsTutorial 1: The "Hello World" of Liquid AITask: Teach a brain to recognize a sine wave, but then confuse it with noise.Pythonimport torch
import natura
import matplotlib.pyplot as plt

# 1. GENERATE DATA (A simple sine wave)
# [Batch, Time, Features]
x = torch.linspace(0, 100, 1000).view(1, 1000, 1)
y = torch.sin(x)

# 2. CREATE THE BRAIN
# 1 Input (Time), 1 Output (Height)
brain = natura.create_life(inputs=1, outputs=1)

# 3. RUN IT
# Notice we don't need ".compile()" or complex loops.
prediction, fluid_state = brain(x)

# 4. PLOT
plt.plot(x.squeeze(), y.squeeze(), label="Reality")
plt.plot(x.squeeze(), prediction.detach().squeeze(), label="NATURA Brain")
plt.legend()
plt.show()
Tutorial 2: Visualizing the WiringOne of the coolest features of Liquid Networks is that you can SEE the brain structure.Pythonfrom ncps.wirings import AutoNCP
import matplotlib.pyplot as plt
import seaborn as sns

# Create a brain wiring diagram
wiring = AutoNCP(units=14, output_size=4)

# Draw it
plt.figure(figsize=(10, 10))
sns.heatmap(wiring.adjacency_matrix, cmap="viridis", cbar=False)
plt.title("The Synaptic Map of a 14-Neuron Liquid Brain")
plt.show()
If you see green dots, those are excitatory connections (Go!). If you see purple, they are inhibitory (Stop!). This is exactly how C. Elegans worms work.🔬 Under the Hood (For Nerds)NATURA is not magic. It is Math.Specifically, it solves the Liquid Time-Constant (LTC) equation:$$ \frac{dx(t)}{dt} = - \left[ \frac{1}{\tau} + f(x(t)) \right] x(t) + f(x(t)) A(t) $$$\tau$ (Tau): The "Time Constant." It decides how fast the neuron reacts. NATURA learns this for you.$f(x)$: The non-linear synapse function.$A(t)$: The input signal.Because this is a differential equation, we can run it on irregular time grids.Keras needs: t=1, t=2, t=3NATURA handles: t=1, t=5.4, t=99 (It adapts automatically).📜 Citation & CreditsThis framework is a wrapper around the pioneering work of:Ramin Hasani & Mathias Lechner (NCPs / Liquid Networks)Patrick Kidger (Diffrax / Neural ODEs)Hazy Research (S4 / State Spaces)If you use this in a paper, please cite the original authors.
