from pathlib import Path
import re

def parse_machine(line):
    ind_match = re.search(r'\[([.#]+)\]', line)
    pattern = ind_match.group(1)
    target = 0

    for i, ch in enumerate(pattern):
        if ch == '#':
            target |= 1 << i

    before_curly = line.split('{', 1)[0]
    btn_strs = re.findall(r'\(([^()]*)\)', before_curly)
    buttons = []

    for s in btn_strs:
        s = s.strip()

        if not s:
            continue
        mask = 0

        for part in s.split(','):
            mask |= 1 << int(part)

        buttons.append(mask)

    return target, buttons

def subset_xor_arrays(buttons):
    n = len(buttons)
    size = 1 << n
    xs = [0] * size
    cs = [0] * size

    for s in range(1, size):
        lsb = s & -s
        i = lsb.bit_length() - 1
        prev = s ^ lsb
        xs[s] = xs[prev] ^ buttons[i]
        cs[s] = cs[prev] + 1

    return xs, cs

def min_presses(target, buttons):
    if target == 0:
        return 0
    
    m = len(buttons)
    mid = m // 2
    first = buttons[:mid]
    second = buttons[mid:]
    xs1, cs1 = subset_xor_arrays(first)
    best_first = {}

    for x, c in zip(xs1, cs1):
        if x not in best_first or c < best_first[x]:
            best_first[x] = c

    xs2, cs2 = subset_xor_arrays(second)
    best = 10**18
    for x2, c2 in zip(xs2, cs2):
        need = target ^ x2
        if need in best_first:
            t = c2 + best_first[need]
            if t < best:
                best = t

    return best

def main():
    input_path = Path(__file__).parent / "test.txt"
    input_path = Path(__file__).parent / "input.txt"
    lines = input_path.read_text().strip().splitlines()
    total = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue
        target, buttons = parse_machine(line)
        total += min_presses(target, buttons)

    print(total)

if __name__ == "__main__":
    main()
