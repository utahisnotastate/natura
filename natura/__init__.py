"""
NATURA v8.0: GENESIS EDITION
"Evolution is a function."
"""
import os
from .core import SovereignModel
from .evie import EvieAI
from .web import Continuum
from .genesis import GenesisEngine   # <--- NEW
from .vision import LiquidDiffusion  # <--- NEW
from .tycoon import TycoonProtocol  # <--- NEW
from . import tycoon  # expose module at package root for `from natura import tycoon`
from .scrolls import ScrollEngine  # <--- NEW

MODE = os.getenv("NATURA_MODE", "SOVEREIGN")

def GenerativeModel(model_name="evie"):
    # ... (Same as before)
    return SovereignModel(core=EvieAI())

def possess(app_instance):
    return Continuum(app_instance).possess()

# EXPOSE THE IDIOT-PROOF FUNCTIONS
def evolve(path):
    """
    The Single Function to rule them all.
    """
    engine = GenesisEngine()
    candidates = engine.crystallize(path)
    # Automatically pick the best one for the user (World-A style)
    best_option = candidates[0]
    return engine.evolve(best_option['type'], path)
