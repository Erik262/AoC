import pathlib
from collections import defaultdict, Counter
import heapq
from typing import List


def get_joltage(bank: str) -> int:
    l, r = 0, 1
    joltage = 0

    while l < r:
        if r >= len(bank):
            break
        
        d1 = bank[l]
        d2 = bank[r]

        if d1 < d2:
            l = r
            r += 1
        else:
            r += 1
        
        joltage = max(joltage, int(d1 + d2))

    return joltage


def main():
    input_path = pathlib.Path(__file__).parent / "input.txt"
    # input_path = pathlib.Path(__file__).parent / "test.txt"
    banks = input_path.read_text(encoding='utf-8').splitlines()

    results = []
    for bank in banks:
        results.append(get_joltage(bank))

    # print(results)
    print(sum(results))

if __name__ == "__main__":
    main()