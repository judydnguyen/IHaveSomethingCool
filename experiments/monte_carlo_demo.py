"""Demo: Monte Carlo estimation of pi — randomness meets geometry."""

import os
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from src.monte_carlo import estimate_pi


def main():
    print("=" * 60)
    print("  MONTE CARLO PI DEMO")
    print("  Estimating pi by throwing random darts")
    print("=" * 60)

    # Show convergence across sample sizes
    print(f"\n{'Samples':>12}  {'Estimate':>12}  {'Error':>12}")
    print("-" * 40)

    for n in [100, 1_000, 10_000, 100_000, 1_000_000]:
        pi_est, _, _ = estimate_pi(n, seed=42)
        error = abs(pi_est - np.pi)
        print(f"{n:>12,}  {pi_est:>12.8f}  {error:>12.8f}")

    print(f"\n  True pi:   {np.pi:.8f}")

    # Generate the classic dart-board visualisation
    pi_est, inside, outside = estimate_pi(5_000, seed=42)

    fig, ax = plt.subplots(1, 1, figsize=(7, 7))
    ax.scatter(outside[:, 0], outside[:, 1], s=1, c="salmon", alpha=0.5, label="Outside")
    ax.scatter(inside[:, 0], inside[:, 1], s=1, c="steelblue", alpha=0.5, label="Inside")

    theta = np.linspace(0, 2 * np.pi, 200)
    ax.plot(np.cos(theta), np.sin(theta), "k-", linewidth=1.5)

    ax.set_xlim(-1.05, 1.05)
    ax.set_ylim(-1.05, 1.05)
    ax.set_aspect("equal")
    ax.set_title(f"Monte Carlo Pi = {pi_est:.4f}  (5,000 samples)", fontsize=14)
    ax.legend(loc="upper right")

    out_path = os.path.join("assets", "monte_carlo_pi.png")
    os.makedirs("assets", exist_ok=True)
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"\n  Saved visualisation to {out_path}")


if __name__ == "__main__":
    main()
