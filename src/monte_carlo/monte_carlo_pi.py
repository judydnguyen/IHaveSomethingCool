"""
Monte Carlo estimation of π — randomness as a computational tool.

The idea (dating back to Buffon's needle problem, 1777):
  1. Inscribe a circle of radius 1 inside a 2×2 square.
  2. Throw N random darts uniformly at the square.
  3. Count how many land inside the circle (x² + y² ≤ 1).
  4. The ratio  (hits / total)  approximates  π/4.

Why it works:
  Area of circle   = π r²  = π
  Area of square   = (2r)² = 4
  Ratio            = π / 4

So  π ≈ 4 × (hits / total).

Convergence is O(1/√N) — you need 100× more samples to gain one extra
digit of precision. But the beauty is its simplicity: no calculus, no
series expansions, just random numbers and counting.

Monte Carlo methods are the backbone of computational physics,
financial modelling, Bayesian inference, and reinforcement learning.
"""

import numpy as np


def estimate_pi(
    n_samples: int = 1_000_000,
    seed: int | None = None,
) -> tuple[float, np.ndarray, np.ndarray]:
    """Estimate π via Monte Carlo dart-throwing.

    Args:
        n_samples: Number of random points to generate.
        seed: Random seed for reproducibility.

    Returns:
        (pi_estimate, inside_points, outside_points)
        where each points array has shape (k, 2).
    """
    rng = np.random.default_rng(seed)
    points = rng.uniform(-1, 1, size=(n_samples, 2))

    distances = np.sum(points**2, axis=1)
    inside_mask = distances <= 1.0

    pi_estimate = 4.0 * np.sum(inside_mask) / n_samples
    return pi_estimate, points[inside_mask], points[~inside_mask]
