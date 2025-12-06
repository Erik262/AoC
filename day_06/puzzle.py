import pathlib
import math


def calculate(rows: list) -> int:
    sign = rows[0]
    rows = list(map(int, rows[1:]))

    if sign == '+':
        return sum(rows)
    
    if sign == '*':
        return math.prod(rows)

def main():
    input_path = pathlib.Path(__file__).parent / "input.txt"
    # input_path = pathlib.Path(__file__).parent / "test.txt"
    lines = input_path.read_text(encoding='utf-8').splitlines()

    # rows = len(lines[0].split())
    # cols = len(lines)
    # print(rows, cols)

    lines = [line for line in lines if line.strip()]
    rows = [line.split() for line in lines]
    cols = list(map(list, zip(*reversed(rows))))

    result = 0
    for col in cols:
        result += calculate(col)

    print(result)

if __name__ == "__main__":
    main()