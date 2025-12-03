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

def get_joltage2(bank: str) -> int:
    n = len(bank)
    k = 12

    if n <= k:
        return int(bank)
    
    to_remove = n - k
    stack = []

    for batt in bank:
        while to_remove > 0 and stack and stack[-1] < batt:
            stack.pop()
            to_remove -= 1

        stack.append(batt)

    if to_remove > 0:
        stack = stack[:-to_remove]

    return int("".join(stack))

def main():
    input_path = pathlib.Path(__file__).parent / "input.txt"
    # input_path = pathlib.Path(__file__).parent / "test.txt"
    banks = input_path.read_text(encoding='utf-8').splitlines()

    results = []
    for bank in banks:
        # results.append(get_joltage(bank))
        results.append(get_joltage2(bank))

    # print(results)
    print(sum(results))

if __name__ == "__main__":
    main()