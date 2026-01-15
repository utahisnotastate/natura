"""
NATURA SCROLLS: THE LIVING DOCUMENT ENGINE
"Why think in cells when you can think in flow?"
"""
import io
import contextlib
from .evie import EvieAI


class ScrollEngine:
    def __init__(self):
        # Core intelligence (optional for future optimizations/advice)
        self.brain = EvieAI()
        # The Liquid State (variables and functions from executed blocks live here)
        self.context = {}

    def manifest(self, markdown_text: str) -> str:
        """
        Reads a Scroll (Markdown), executes Python code blocks, and injects results
        as Holographic Annotations right after each executed block.
        """
        lines = markdown_text.split('\n')
        output_scroll = []
        code_buffer = []
        in_code_block = False

        for line in lines:
            stripped = line.strip()

            # Open a python code block
            if stripped.startswith("```python") and not in_code_block:
                in_code_block = True
                output_scroll.append(line)
                # do not include the opener in the buffer; buffer only code
                continue

            # Close any code block
            if stripped.startswith("```") and in_code_block:
                in_code_block = False

                # 1) OPTIMIZE (placeholder)
                raw_code = "\n".join(code_buffer)
                # In the future, we could run AST transforms here for CPU efficiency.

                # 2) EXECUTE in the Liquid State
                result = self._run_liquid(raw_code)

                # 3) Render output: close block, then add an annotation block if any
                output_scroll.append(line)  # the closing ``` line
                if result:
                    output_scroll.append(f"\n> [NATURA RESULT]:\n> {result}\n")

                code_buffer = []
                continue

            # Accumulate code while inside a python block
            if in_code_block:
                code_buffer.append(line)
                output_scroll.append(line)
            else:
                # Pass-through normal markdown lines
                output_scroll.append(line)

        # If the document finished while still in a code block (unclosed),
        # we will execute it and append a synthetic closing fence and result.
        if in_code_block:
            raw_code = "\n".join(code_buffer)
            result = self._run_liquid(raw_code)
            output_scroll.append("```")
            if result:
                output_scroll.append(f"\n> [NATURA RESULT]:\n> {result}\n")

        return "\n".join(output_scroll)

    def _run_liquid(self, code: str) -> str:
        """
        Executes code in the shared `self.context` namespace while capturing stdout.
        Returns captured stdout, or an error description if execution fails.
        """
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            try:
                exec(code, self.context)
            except Exception as e:
                return f"[CRASH]: {e}"
        return buffer.getvalue().strip()

    def optimize_for_cpu(self, code: str) -> str:
        """
        Ask Evie to rewrite heavy pandas/numpy code to run fast on CPU.
        (Current version is a thin wrapper; may no-op if Evie lacks `think`).
        """
        try:
            return self.brain.think(f"Rewrite this for CPU efficiency: {code}")
        except Exception:
            return code
