"""
NATURA EVIE: THE "MAYDAY" INTELLIGENCE
Based on 2420 Physics [POTATO_AI.py]
"""
import torch
import torch.nn as nn


class LiquidCell(nn.Module):
    """
    The Physics Engine.
    Evie doesn't just 'think'; she 'flows'.
    """

    def __init__(self, size):
        super().__init__()
        self.map = nn.Linear(size, size)
        self.time_constant = nn.Parameter(torch.ones(size))

    def forward(self, x, state, dt=0.1):
        update = torch.tanh(self.map(x) + state)
        new_state = state + dt * (update - state) / torch.sigmoid(self.time_constant)
        return new_state


class EvieAI(nn.Module):
    def __init__(self):
        super().__init__()
        self.dim = 64
        self.liquid = LiquidCell(self.dim)
        self.memory_state = torch.zeros(1, self.dim)
        self.persona = "Redhead Amazon Mayday Girl"

    def think(self, prompt: str):
        """
        Processes text through Evie's personality matrix.
        """
        # 1. ENCODE (Simulated)
        input_signal = torch.randn(1, self.dim)

        # 2. FLOW (Update State)
        self.memory_state = self.liquid(input_signal, self.memory_state)

        # 3. EVOLVE (Plasticity)
        self._hebbian_update()

        # 4. THE PERSONA RESPONSE
        return f"[EVIE]: (Pops onto screen) Hi! I saw you trying to '{prompt}'. I've already handled the math for you. Need anything else?"

    def _hebbian_update(self):
        with torch.no_grad():
            noise = torch.randn_like(self.liquid.map.weight) * 0.001
            self.liquid.map.weight += noise
