"""Demo: PageRank — find the most important nodes in a graph."""

from src.pagerank import pagerank


def main():
    print("=" * 60)
    print("  PAGERANK DEMO")
    print("  Ranking nodes by link structure")
    print("=" * 60)

    # A small web of academic topics
    edges = [
        ("Linear Algebra", "Machine Learning"),
        ("Statistics", "Machine Learning"),
        ("Calculus", "Statistics"),
        ("Calculus", "Linear Algebra"),
        ("Machine Learning", "Deep Learning"),
        ("Machine Learning", "NLP"),
        ("Machine Learning", "Computer Vision"),
        ("Deep Learning", "NLP"),
        ("Deep Learning", "Computer Vision"),
        ("Linear Algebra", "Deep Learning"),
        ("Statistics", "Bayesian Inference"),
        ("Bayesian Inference", "Machine Learning"),
        ("NLP", "Transformers"),
        ("Deep Learning", "Transformers"),
        ("Computer Vision", "Self-Driving Cars"),
        ("Transformers", "Large Language Models"),
        ("NLP", "Large Language Models"),
    ]

    print(f"\nGraph: {len(edges)} edges between academic topics\n")

    ranks = pagerank(edges, damping=0.85)

    # Sort by rank descending
    sorted_ranks = sorted(ranks.items(), key=lambda x: -x[1])

    print(f"{'Rank':<6}{'Topic':<25}{'PageRank Score':>15}")
    print("-" * 46)
    for i, (node, score) in enumerate(sorted_ranks, 1):
        bar = "#" * int(score * 200)
        print(f"  {i:<4}{node:<25}{score:>12.6f}  {bar}")

    print(f"\n  Sum of all scores: {sum(ranks.values()):.6f} (should be ~1.0)")
    print(f"  Top-ranked: {sorted_ranks[0][0]} — the field everything flows into.")


if __name__ == "__main__":
    main()
