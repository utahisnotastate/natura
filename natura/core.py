"""
NATURA CORE: THE WRAPPER
"""


class SovereignModel:
    def __init__(self, core):
        self.brain = core

    def generate_content(self, prompt: str):
        """
        The Universal Interface.
        Redirects the user's prompt to the specific Brain (Evie, Omni, etc).
        """
        # 1. Process the thought
        result_text = self.brain.think(prompt)

        # 2. Return in a Google-compatible wrapper (The Skin Suit)
        return GenerationResponse(text=result_text)


class GenerationResponse:
    def __init__(self, text):
        self.text = text
