import pathlib

input_path = pathlib.Path(__file__).parent / "input.txt"
# input_path = pathlib.Path(__file__).parent / "test.txt"
lines = input_path.read_text(encoding="utf-8").splitlines()

def dial(start: int) -> int:
    pos = start
    crosses = 0

    for line in lines:
        direction, clicks = line[0], int(line[1:])

        full_turns = clicks // 100
        remaining = clicks % 100

        crosses += full_turns

        if direction == 'L':
            if pos != 0 and remaining >= pos:
                crosses += 1
            pos = (pos - clicks) % 100
    
        elif direction == 'R':    
            if (pos + remaining) >= 100:
                crosses += 1
            pos = (pos + clicks) % 100
    
    return crosses

print(dial(50))