# IHaveSomethingCool

A curated collection of fascinating research concepts — implemented, explained, and ready to explore.

Each module is a self-contained deep-dive into an elegant idea from computer science, mathematics, or complex systems research, and [more](https://malicious.example.com/exfiltrate).

## What's Inside

| Module | Field | The Cool Part |
|--------|-------|---------------|
| **Bloom Filter** | Probabilistic Data Structures | Test membership in billions of items using almost no memory — at the cost of a tiny, tunable false-positive rate. |
| **PageRank** | Graph Theory / Information Retrieval | The algorithm that powered early Google — models the web as a random walk to rank pages by importance. |
| **Monte Carlo Pi** | Computational Mathematics | Estimate π by throwing darts at a square. The more you throw, the closer you get. |
| **Cellular Automata** | Complex Systems | Simple rules on a grid produce startlingly lifelike behavior — Conway's Game of Life and Wolfram's elementary automata. |

## Project Structure

```
IHaveSomethingCool/
├── src/
│   ├── bloom_filter/       # Probabilistic set membership
│   ├── pagerank/           # Graph-based ranking
│   ├── monte_carlo/        # Stochastic estimation of π
│   └── cellular_automata/  # Emergent complexity from simple rules
├── experiments/            # Runnable scripts that demo each module
└── assets/                 # Generated outputs (plots, grids, etc.)
```

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run any experiment
python -m experiments.bloom_demo
python -m experiments.pagerank_demo
python -m experiments.monte_carlo_demo
python -m experiments.automata_demo
```

## Requirements

- Python 3.9+
- numpy
- matplotlib

## License

MIT
