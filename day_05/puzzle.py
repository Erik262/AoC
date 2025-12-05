import pathlib

def check(id: int, fresh_range) -> bool:
    for rang in fresh_range:
        l, r = map(int, rang.split('-'))
            
        if id in range(l, r + 1):
            return True
    
    return False

def check2(fresh_range) -> int:
    intervals = []

    for rang in fresh_range:
        l, r = map(int, rang.split('-'))
        intervals.append((l, r))

    intervals.sort()
    total = 0
    cur_l, cur_r = intervals[0]

    for l, r in intervals[1:]:
        if l <= cur_r + 1:
            cur_r = max(cur_r, r)
        else:
            total += cur_r - cur_l + 1
            cur_l, cur_r = l, r

    total += cur_r - cur_l + 1
    return total

def main():
    input_path = pathlib.Path(__file__).parent / "input.txt"
    # input_path = pathlib.Path(__file__).parent / "test.txt"
    fresh_range, ids = input_path.read_text(encoding='utf-8').split(" ")
    fresh_range = fresh_range.splitlines()
    ids = ids.splitlines()[1:]

    fresh_counter = 0
    for id_str in ids:
        id_ = int(id_str)

        if check(id_, fresh_range):
            fresh_counter += 1

    print(fresh_counter)
    print(check2(fresh_range))

if __name__ == "__main__":
    main()