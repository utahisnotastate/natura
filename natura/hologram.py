"""
NATURA HOLOGRAM
"""
import os

class Hologram:
    def __init__(self):
        self.knowledge = {}

    def ingest(self, path):
        print(f"// EVIE: Reading everything in '{path}'...")
        # (Simulation of reading files)
        self.knowledge['root'] = path
        print(f"// EVIE: Got it. I know everything in there now.")

    def query(self, question):
        return f"[EVIE]: Looking at the files in {self.knowledge.get('root')}... found it."
