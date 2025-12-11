from pathlib import Path


def area(points):
    n = len(points)
    best = 0

    for i in range(n):
        x1, y1 = points[i]

        for j in range(i + 1, n):
            x2, y2 = points[j]

            dx = abs(x1 - x2) + 1
            dy = abs(y1 - y2) + 1

            best = max(best, dx * dy)

    return best

def parse_input(lines):
    points = []

    for line in lines:
        x, y = map(int, line.split(","))
        points.append((x, y))

    return points

if __name__ == "__main__":

    input_path = Path(__file__).parent / "test.txt"
    input_path = Path(__file__).parent / "input.txt"

    lines = input_path.read_text().splitlines()
    points = parse_input(lines)

    print(area(points))