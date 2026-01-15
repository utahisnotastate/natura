"""
GPU KILLER: HOLOGRAPHIC RAG
Goal: Search 1GB of text without a Vector DB or GPU Index.
Method: Holographic Compression
"""
import sys
import os

# Add repo root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import natura  # noqa: F401

try:
    from natura.hologram import Hologram  # type: ignore
except Exception:
    # Fallback mock so the example still runs even if Hologram is unavailable
    class Hologram:  # type: ignore
        def __init__(self):
            self._docs = []
        def ingest(self, path: str):
            self._docs.append(f"[MOCK] Ingested path: {path}")
        def query(self, q: str) -> str:
            return f"[MOCK ANSWER] '{q}' → Intelligence emerges from liquid dynamics, not GPUs."


def main():
    print("=== VECTOR DBS ARE DEAD ===")

    # 1. Ingest Reality
    # Normal RAG: Chunks text, computes embeddings on GPU, stores in Pinecone.
    # Natura: Compresses folder into a single 'Hologram' object in RAM.
    kb = Hologram()
    kb.ingest("./")  # Ingest current folder

    # 2. Query
    query = "How does Natura replace GPUs?"
    answer = kb.query(query)

    print(f"\n[QUERY]: {query}")
    print(f"[HOLOGRAM]: {answer}")


if __name__ == "__main__":
    main()
