import pathlib

def check(num: int) -> bool:
    str_num = str(num)
    half = len(str_num) // 2

    return str_num[:half] == str_num[half:]

def check_two(num: int) -> bool:
    str_num = str(num)

    for i in range(1, len(str_num) // 2 + 1):
        head = str_num[:i]
        tail = str_num[i: i + len(head)]
        # print(f"head: {head}, tail: {tail}")
        
        if head == tail:
            are_same = True

            if (len(str_num) % len(head)) != 0:
                continue

            for j in range(1, len(str_num) // len(head)):
                mov_tail = str_num[i*j: (i + len(head)*j)]
                # print(f"head: {head}, mov_tail: {mov_tail}")
                are_same = are_same and (head == mov_tail)

            return are_same
    return False

def product(start: int, end: int) -> list:
    results = []

    for n in range(start, end + 1):
        if check(n) or check_two(n):
            results.append(n)
    return results

def main():
    # input_path = pathlib.Path(__file__).parent / "test.txt"
    input_path = pathlib.Path(__file__).parent / "input.txt"
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

    # print(results)
    print(added_up)

if __name__ == "__main__":
    main()