"""
NATURA TYCOON: BUSINESS LOGIC PROTOCOL
"""
from dataclasses import dataclass
import os


@dataclass
class BusinessIdea:
    name: str
    niche: str
    model: str


class TycoonProtocol:
    """A playful placeholder protocol that simulates a business generator.

    In a real implementation, this would orchestrate research agents, market
    scrapers, financial forecasters, and product generators.
    """

    def __init__(self):
        self.pipeline = [
            "Market Scan",
            "Competitor Map",
            "Value Prop Synthesizer",
            "Pricing Wizard",
            "Launch Plan"
        ]

    def deep_scan(self, source: str = "computer", root: str | None = None, max_items: int = 100):
        """
        Scan the filesystem to discover assets.

        - source="computer": scans the user's home folder (non-recursive beyond a soft cap)
        - source is a path: scans that path
        Returns a list of up to `max_items` relative file paths.
        """
        start = root or (os.path.expanduser("~") if source == "computer" else os.path.abspath(str(source)))
        results: list[str] = []
        try:
            for dirpath, _, filenames in os.walk(start):
                for fname in filenames:
                    path = os.path.join(dirpath, fname)
                    rel = os.path.relpath(path, start)
                    results.append(rel)
                    if len(results) >= max_items:
                        return results
        except Exception:
            # Fail-soft: return a small synthetic list so demos still run
            pass
        if not results:
            results = ["README.md", "main.py", "natura/__init__.py"]
        return results

    def launch_wizard(self):
        print("// TYCOON: Initializing wealth engine...")
        for step in self.pipeline:
            print(f"// TYCOON: {step} ✦ COMPLETE")
        idea = BusinessIdea(
            name="Natura Cloud",
            niche="AI-native creative tooling",
            model="SaaS + Usage Tiers",
        )
        print(f"// TYCOON: RECOMMENDED IDEA → {idea.name} [{idea.niche}] :: {idea.model}")
        print("// TYCOON: Deploy the demo with 'python main.py mirage' or prototype automations in 'genesis'.")
