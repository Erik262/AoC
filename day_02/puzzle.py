import pathlib

def check(num: int) -> bool:
    str_num = str(num)
    half = len(str_num) // 2

    return str_num[:half] == str_num[half:]

def product(start: int, end: int) -> list:
    results = []
    for n in range(start, end + 1):
        if check(n):
            results.append(n)
    return results

def main():
    input_path = pathlib.Path(__file__).parent / "test.txt"
    # input_path = pathlib.Path(__file__).parent / "input.txt"
    ids = input_path.read_text(encoding='utf-8').split(',') 

    results = []
    added_up = 0
    for id in ids:
        a, b = id.split('-')
        res = product(int(a), int(b))
        if not res:
            continue
        results.append(res)
        added_up += sum(res)

    print(added_up)


if __name__ == "__main__":
    main()