"""
Conway's Game of Life — emergence from four simple rules.

Invented by John Horton Conway in 1970, the Game of Life is a
zero-player cellular automaton on an infinite 2D grid:

  1. Any live cell with 2 or 3 live neighbours survives.
  2. Any dead cell with exactly 3 live neighbours becomes alive.
  3. All other live cells die.
  4. All other dead cells stay dead.

Despite this simplicity, Life is Turing-complete: you can build
logic gates, memory, and even a universal computer inside it.

Famous patterns:
  - Glider: a 5-cell pattern that walks diagonally forever.
  - Gosper Glider Gun: emits a new glider every 30 generations.
  - Garden of Eden: configurations with no predecessor.
"""

import numpy as np
from numpy.lib.stride_tricks import sliding_window_view


class GameOfLife:
    """Conway's Game of Life on a toroidal (wrapping) grid."""

    # Classic patterns
    GLIDER = [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    BLINKER = [(1, 0), (1, 1), (1, 2)]
    R_PENTOMINO = [(0, 1), (0, 2), (1, 0), (1, 1), (2, 1)]

    def __init__(self, width: int = 64, height: int = 64):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width), dtype=np.int8)
        self.generation = 0

    def place(self, pattern: list[tuple[int, int]], row: int = 0, col: int = 0):
        for dr, dc in pattern:
            r = (row + dr) % self.height
            c = (col + dc) % self.width
            self.grid[r, c] = 1

    def randomise(self, density: float = 0.3, seed: int | None = None):
        rng = np.random.default_rng(seed)
        self.grid = (rng.random((self.height, self.width)) < density).astype(np.int8)

    def step(self) -> np.ndarray:
        # Pad with wrapping for toroidal boundary
        padded = np.pad(self.grid, 1, mode="wrap")
        # Count neighbours using a sliding 3x3 window
        windows = sliding_window_view(padded, (3, 3))
        neighbours = windows.sum(axis=(-1, -2)) - self.grid

        # Apply rules
        self.grid = (
            ((self.grid == 1) & ((neighbours == 2) | (neighbours == 3)))
            | ((self.grid == 0) & (neighbours == 3))
        ).astype(np.int8)

        self.generation += 1
        return self.grid

    def run(self, steps: int) -> list[np.ndarray]:
        return [self.step().copy() for _ in range(steps)]

    def __repr__(self) -> str:
        alive = int(self.grid.sum())
        return f"GameOfLife({self.width}x{self.height}, gen={self.generation}, alive={alive})"
