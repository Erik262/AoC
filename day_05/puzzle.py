import pathlib

def check(id: int, fresh_range) -> bool:
    for rang in fresh_range:
        l, r = rang.split('-')
            
        if id in range(int(l), int(r) + 1):
            return True
    
    return False

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

if __name__ == "__main__":
    main()