"""
PageRank — the algorithm that ranked the early web.

Published by Larry Page and Sergey Brin in 1998, PageRank models a
"random surfer" who follows hyperlinks at random:

  PR(p) = (1 - d)/N  +  d * Σ PR(q) / L(q)
                           q ∈ B(p)

Where:
  - d is the damping factor (probability of following a link vs. jumping
    to a random page; typically 0.85).
  - N is the total number of pages.
  - B(p) is the set of pages linking TO page p.
  - L(q) is the number of outgoing links FROM page q.

The algorithm iterates until convergence: a fixed point where every
page's rank stabilises. Pages that many important pages link to
accumulate high rank — a recursive definition of "importance."

This implementation uses the power-iteration method on a simple
adjacency-list graph.
"""

import numpy as np


def pagerank(
    edges: list[tuple[str, str]],
    damping: float = 0.85,
    max_iter: int = 100,
    tol: float = 1e-6,
) -> dict[str, float]:
    """Compute PageRank scores for a directed graph.

    Args:
        edges: List of (source, target) pairs.
        damping: Damping factor in [0, 1].
        max_iter: Maximum iterations.
        tol: Convergence threshold.

    Returns:
        Dict mapping node name to its PageRank score.
    """
    nodes = sorted({n for edge in edges for n in edge})
    idx = {node: i for i, node in enumerate(nodes)}
    n = len(nodes)

    # Build column-stochastic transition matrix
    M = np.zeros((n, n))
    out_degree = np.zeros(n)

    for src, tgt in edges:
        M[idx[tgt], idx[src]] += 1
        out_degree[idx[src]] += 1

    # Normalise columns (handle dangling nodes)
    for j in range(n):
        if out_degree[j] > 0:
            M[:, j] /= out_degree[j]
        else:
            M[:, j] = 1.0 / n  # dangling node distributes evenly

    rank = np.ones(n) / n

    for iteration in range(max_iter):
        new_rank = (1 - damping) / n + damping * M @ rank
        if np.linalg.norm(new_rank - rank, 1) < tol:
            break
        rank = new_rank

    return {node: float(rank[idx[node]]) for node in nodes}
