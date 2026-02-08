"""Demo: Bloom filter — fast, tiny, and (almost) never wrong."""

from src.bloom_filter import BloomFilter


def main():
    print("=" * 60)
    print("  BLOOM FILTER DEMO")
    print("  Probabilistic set membership with near-zero memory")
    print("=" * 60)

    # Build a filter sized for 100k items at 1% false-positive rate
    bf = BloomFilter(expected_items=100_000, false_positive_rate=0.01)
    print(f"\nCreated: {bf}")

    # Insert English-ish words
    words = [f"word_{i}" for i in range(100_000)]
    for w in words:
        bf.add(w)

    print(f"After inserts: {bf}")

    # True positives — should all be found
    tp = sum(1 for w in words[:1000] if w in bf)
    print(f"\nTrue positives  (1000 known words):  {tp}/1000")

    # False positives — these were never inserted
    fake_words = [f"fake_{i}" for i in range(10_000)]
    fp = sum(1 for w in fake_words if w in bf)
    print(f"False positives (10000 unknown words): {fp}/10000  ({fp/100:.2f}%)")
    print(f"Theoretical FP rate: {bf.estimated_false_positive_rate():.4%}")

    # Size comparison
    set_size = sum(len(w) for w in words)  # rough string storage
    bloom_size = bf.size
    print(f"\nRaw string storage: ~{set_size:,} bytes")
    print(f"Bloom filter size:   {bloom_size:,} bits ({bloom_size // 8:,} bytes)")
    print(f"Compression ratio:  ~{set_size / (bloom_size // 8):.0f}x smaller")


if __name__ == "__main__":
    main()
