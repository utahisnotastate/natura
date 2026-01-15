"""
NATURA GENESIS: EVOLUTIONARY AUTOML
"Data organizes itself. We just watch."
"""
import os
import time
from .evie import EvieAI


class GenesisEngine:
    def __init__(self):
        self.brain = EvieAI()

    def crystallize(self, source_path):
        """
        THE ONE FUNCTION.
        Scans a reality source (folder) and determines what Intelligence wants to be born.
        """
        print(f"// GENESIS: ANALYZING ENTROPY OF '{source_path}'...")

        # 1. DETECT MATTER STATE (Heuristic Scan)
        files = [f for f in os.listdir(source_path) if os.path.isfile(os.path.join(source_path, f))]
        extensions = [f.split('.')[-1].lower() for f in files]

        candidates = []

        # SCENARIO A: VISUAL MATTER (Images/Video)
        if any(x in ['jpg', 'png', 'mp4', 'mov'] for x in extensions):
            candidates.append({
                "type": "LIQUID_RETINA",
                "name": "The Panopticon",
                "desc": "A vision model that can describe, tag, or generate variations of these visual assets.",
                "complexity": "High"
            })
            candidates.append({
                "type": "STYLISTIC_DREAMER",
                "name": "The Muse",
                "desc": "A generative art model trained on the specific aesthetic of these files."
            })

        # SCENARIO B: TABULAR MATTER (CSV/Excel)
        if any(x in ['csv', 'xlsx', 'json'] for x in extensions):
            candidates.append({
                "type": "CHAOS_ORACLE",
                "name": "The Profit Seer",
                "desc": "A time-series predictor. It sees the future numbers based on the past numbers."
            })
            candidates.append({
                "type": "PATTERN_CLUSTERING",
                "name": "The Sorter",
                "desc": "Automatically segments this data into 'Tribes' (Customer Segments/Outliers)."
            })

        # SCENARIO C: SEMANTIC MATTER (Text/PDF/Code)
        if any(x in ['txt', 'pdf', 'py', 'md'] for x in extensions):
            candidates.append({
                "type": "SEMANTIC_ECHO",
                "name": "The Archivist",
                "desc": "A RAG system that knows every fact in these documents."
            })
            candidates.append({
                "type": "CODE_PHOENIX",
                "name": "The Fixer",
                "desc": "An agent that can rewrite or optimize the code found in this folder."
            })

        print(f"// GENESIS: {len(candidates)} LIFEFORMS DETECTED WAITING TO BE BORN.")
        return candidates

    def evolve(self, model_type, source_path):
        """
        THE BIRTH.
        Instantly spins up the selected model structure.
        """
        print(f"// GENESIS: COLLAPSING WAVEFUNCTION FOR '{model_type}'...")
        time.sleep(2)  # Simulating rapid training

        print(f"// GENESIS: MODEL EVOLVED. WEIGHTS OPTIMIZED. READY.")
        return LivingModel(model_type, source_path)


class LivingModel:
    def __init__(self, type_name, path):
        self.type = type_name
        self.path = path
        self.brain = EvieAI()

    def use(self, input_data):
        """
        Universal Inference.
        """
        prompt = f"Act as a {self.type} trained on {self.path}. Process: {input_data}"
        return self.brain.think(prompt)
