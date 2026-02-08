"""Demo: Cellular automata — simple rules, emergent complexity."""

import os
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from src.cellular_automata import GameOfLife, ElementaryAutomaton


def demo_elementary():
    print("\n--- Elementary Cellular Automata (1D) ---\n")

    rules = [30, 90, 110, 184]
    fig, axes = plt.subplots(1, len(rules), figsize=(16, 5))

    for ax, rule_num in zip(axes, rules):
        automaton = ElementaryAutomaton(rule=rule_num, width=151)
        history = automaton.run(75)

        ax.imshow(history, cmap="binary", interpolation="nearest", aspect="auto")
        ax.set_title(f"Rule {rule_num}", fontsize=13, fontweight="bold")
        ax.set_xlabel("Cell")
        ax.set_ylabel("Time step")

        print(f"  Rule {rule_num}: {automaton}")

    fig.suptitle("Wolfram's Elementary Cellular Automata", fontsize=15, y=1.02)
    fig.tight_layout()

    out_path = os.path.join("assets", "elementary_automata.png")
    os.makedirs("assets", exist_ok=True)
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"\n  Saved to {out_path}")


def demo_game_of_life():
    print("\n--- Conway's Game of Life (2D) ---\n")

    life = GameOfLife(width=48, height=48)
    life.place(GameOfLife.R_PENTOMINO, row=22, col=22)

    snapshots = [0, 10, 50, 150]
    grids = {0: life.grid.copy()}

    for gen in range(1, max(snapshots) + 1):
        life.step()
        if gen in snapshots:
            grids[gen] = life.grid.copy()

    fig, axes = plt.subplots(1, len(snapshots), figsize=(16, 4.5))
    for ax, gen in zip(axes, snapshots):
        ax.imshow(grids[gen], cmap="binary", interpolation="nearest")
        alive = int(grids[gen].sum())
        ax.set_title(f"Gen {gen}  ({alive} alive)", fontsize=12)
        ax.axis("off")

    fig.suptitle("Game of Life — R-pentomino Evolution", fontsize=15, y=1.02)
    fig.tight_layout()

    out_path = os.path.join("assets", "game_of_life.png")
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  R-pentomino after 150 generations: {life}")
    print(f"  Saved to {out_path}")


def main():
    print("=" * 60)
    print("  CELLULAR AUTOMATA DEMO")
    print("  Simple rules, complex behaviour")
    print("=" * 60)

    demo_elementary()
    demo_game_of_life()


if __name__ == "__main__":
    main()
