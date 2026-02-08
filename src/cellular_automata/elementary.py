"""
Wolfram's Elementary Cellular Automata — complexity from 1D rules.

Stephen Wolfram classified all 256 possible rules for 1D binary
cellular automata, where each cell's next state depends on itself
and its two neighbours (3 cells → 2³ = 8 possible inputs → 2⁸ = 256
possible rules).

Notable rules:
  - Rule 30:  Produces chaotic, pseudo-random behaviour. Used in
              Mathematica's random number generator.
  - Rule 90:  Produces a Sierpinski triangle — a fractal.
  - Rule 110: Proven Turing-complete by Matthew Cook in 2004.
  - Rule 184: Models traffic flow.

Wolfram's "A New Kind of Science" (2002) argues that such simple
programs are the key to understanding complexity in nature.
"""

import numpy as np


class ElementaryAutomaton:
    """A 1D elementary cellular automaton (Wolfram classification)."""

    def __init__(self, rule: int, width: int = 101):
        if not 0 <= rule <= 255:
            raise ValueError(f"Rule must be 0-255, got {rule}")
        self.rule = rule
        self.width = width
        self.lookup = self._build_lookup(rule)
        self.state = np.zeros(width, dtype=np.int8)
        self.state[width // 2] = 1  # single centre seed
        self.history: list[np.ndarray] = [self.state.copy()]

    def step(self) -> np.ndarray:
        padded = np.pad(self.state, 1, mode="wrap")
        new_state = np.zeros_like(self.state)
        for i in range(self.width):
            neighbourhood = (padded[i] << 2) | (padded[i + 1] << 1) | padded[i + 2]
            new_state[i] = self.lookup[neighbourhood]
        self.state = new_state
        self.history.append(self.state.copy())
        return self.state

    def run(self, steps: int) -> np.ndarray:
        for _ in range(steps):
            self.step()
        return np.array(self.history)

    @staticmethod
    def _build_lookup(rule: int) -> dict[int, int]:
        return {i: (rule >> i) & 1 for i in range(8)}

    def __repr__(self) -> str:
        return f"ElementaryAutomaton(rule={self.rule}, width={self.width}, steps={len(self.history)-1})"
