from pathlib import Path

def count_splits2(grid: list[str]) -> int:
    H, W = len(grid), len(grid[0])

    for r, row in enumerate(grid):
        c = row.find('S')
        if c != -1:
            sr, sc = r, c
            break

    dp = [[0] * W for _ in range(H)]
    dp[sr][sc] = 1

    finished = 0

    for r in range(sr, H):
        for c in range(W):
            k = dp[r][c]
            if k == 0:
                continue

            if r == H - 1:
                finished += k
                continue

            below = grid[r + 1][c]

            if below in ('.', 'S'):
                dp[r + 1][c] += k

            elif below == '^':
                if c > 0:
                    dp[r + 1][c - 1] += k
                else:
                    finished += k
                if c + 1 < W:
                    dp[r + 1][c + 1] += k
                else:
                    finished += k

    return finished

def count_splits(grid: list[str]) -> int:
    H, W = len(grid), len(grid[0])
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
                new.add((nr, c))

        beams = new

    return splits

if __name__ == "__main__":
    input_path = Path(__file__).parent / "input.txt"
    # input_path = Path(__file__).parent / "test.txt"
    text = input_path.read_text().splitlines()
    print(count_splits(text))
    print(count_splits2(text))
