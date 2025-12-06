import pathlib
import math

def calculate(rows: list) -> int:
    sign = rows[0]
    rows = list(map(int, rows[1:]))

    if sign == '+':
        return sum(rows)
    
    if sign == '*':
        return math.prod(rows)

def calculate2(lines: list[str]) -> int:
    lines = [l.rstrip("\n") for l in lines if l.strip()]
    w = max(len(l) for l in lines)
    grid = [l.ljust(w) for l in lines]
    h = len(grid)

    blocks = []
    cur = []
    for c in range(w):
        col = [grid[r][c] for r in range(h)]
        if all(ch == " " for ch in col):
            if cur:
                blocks.append(cur)
                cur = []
        else:
            cur.append(c)
    if cur:
        blocks.append(cur)

    total = 0
    for cols in blocks:
        op = next(grid[h-1][c] for c in cols if grid[h-1][c] in "+*")
        nums = []
        for c in reversed(cols):
            ds = [grid[r][c] for r in range(h-1) if grid[r][c] != " "]
            if ds:
                nums.append(int("".join(ds)))
        total += sum(nums) if op == "+" else math.prod(nums)

    return total

def main():
    input_path = pathlib.Path(__file__).parent / "input.txt"
    # input_path = pathlib.Path(__file__).parent / "test.txt"
    lines = input_path.read_text(encoding='utf-8').splitlines()

    new_lines = [line for line in lines if line.strip()]
    rows = [line.split() for line in new_lines]
    cols = list(map(list, zip(*reversed(rows))))

    result = 0
    for col in cols:
        result += calculate(col)

    print(result)
    print(calculate2(lines))

if __name__ == "__main__":
    main()