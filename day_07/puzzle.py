from pathlib import Path

def count_splits(grid: list[str]) -> int:
    H, W = len(grid), len(grid[0])
    # Find S
    for r, row in enumerate(grid):
        c = row.find('S')
        if c != -1:
            start = (r, c)
            break

    beams = {start}
    splits = 0

    while beams:
        new = set()
        for r, c in beams:
            nr = r + 1
            if nr >= H:
                continue
            cell = grid[nr][c]

            if cell == '.':
                new.add((nr, c))
            elif cell == '^':
                splits += 1
                if c > 0:
                    new.add((nr, c - 1))
                if c + 1 < W:
                    new.add((nr, c + 1))
            else:
                # treat S as empty space
                new.add((nr, c))

        beams = new

    return splits

if __name__ == "__main__":
    input_path = Path(__file__).parent / "input.txt"
    # input_path = Path(__file__).parent / "test.txt"
    text = input_path.read_text().splitlines()
    print(count_splits(text))
