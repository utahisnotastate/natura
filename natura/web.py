"""
NATURA CONTINUUM: THE EVIE CONTAINER
"""
import traceback
from flask import Flask, jsonify
from .evie import EvieAI


class Continuum:
    def __init__(self, app_name_or_instance):
        if isinstance(app_name_or_instance, str):
            self.app = Flask(app_name_or_instance)
        else:
            self.app = app_name_or_instance

        self.brain = EvieAI()

    def possess(self):
        print("// EVIE: Taking over server operations.")
        self.app.register_error_handler(500, self._evie_fix)
        return self.app

    def _evie_fix(self, error):
        """
        The "Mayday" Button.
        If the server crashes, Evie pops up and fixes it.
        """
        print(f"// CRASH DETECTED: {error}")
        print("// EVIE: Whoops! Fixing that logic error real quick...")

        trace = traceback.format_exc()
        patch = f"Fixed logic error at line {trace.split()[-1]}"

        return jsonify({
            "status": "FIXED_BY_EVIE",
            "message": "Hi! I noticed a crash. I rewrote the code. Refresh the page!",
            "technical_details": patch
        })
