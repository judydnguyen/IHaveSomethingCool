"""
Bloom Filter — a space-efficient probabilistic data structure.

Invented by Burton Howard Bloom in 1970, a Bloom filter can tell you:
  - "Definitely NOT in the set"  (always correct)
  - "Probably in the set"        (small, tunable chance of being wrong)

How it works:
  1. Start with a bit array of size m, all zeros.
  2. To ADD an element, hash it with k independent hash functions,
     each producing an index in [0, m). Set those k bits to 1.
  3. To QUERY an element, hash it the same way. If ALL k bits are 1,
     the element is "probably" present. If ANY bit is 0, it is
     definitely absent.

The false-positive rate is approximately (1 - e^(-kn/m))^k,
where n is the number of inserted elements.

Use cases: spell checkers, network routers, database query optimizers,
blockchain SPV clients, and anywhere you need fast set-membership
tests on massive datasets without storing the data itself.
"""

import hashlib
import math
from typing import Any


class BloomFilter:
    """A classic Bloom filter with configurable size and hash count."""

    def __init__(self, expected_items: int, false_positive_rate: float = 0.01):
        self.fp_rate = false_positive_rate
        self.size = self._optimal_size(expected_items, false_positive_rate)
        self.hash_count = self._optimal_hash_count(self.size, expected_items)
        self.bit_array = bytearray(self.size)
        self.item_count = 0

    def add(self, item: Any) -> None:
        for i in range(self.hash_count):
            idx = self._hash(item, i) % self.size
            self.bit_array[idx] = 1
        self.item_count += 1

    def __contains__(self, item: Any) -> bool:
        return all(
            self.bit_array[self._hash(item, i) % self.size] == 1
            for i in range(self.hash_count)
        )

    def estimated_false_positive_rate(self) -> float:
        n = self.item_count
        m = self.size
        k = self.hash_count
        return (1 - math.exp(-k * n / m)) ** k

    @staticmethod
    def _optimal_size(n: int, p: float) -> int:
        return int(-n * math.log(p) / (math.log(2) ** 2))

    @staticmethod
    def _optimal_hash_count(m: int, n: int) -> int:
        return max(1, int((m / n) * math.log(2)))

    @staticmethod
    def _hash(item: Any, seed: int) -> int:
        h = hashlib.sha256(f"{seed}:{item}".encode()).hexdigest()
        return int(h, 16)

    def __repr__(self) -> str:
        fill = sum(self.bit_array) / self.size * 100
        return (
            f"BloomFilter(size={self.size}, hashes={self.hash_count}, "
            f"items={self.item_count}, fill={fill:.1f}%)"
        )
