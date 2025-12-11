from pathlib import Path
from functools import lru_cache

def parse_graph(lines):
    graph = {}

    for line in lines:
        line = line.strip()

        left, right = line.split(":", 1)
        src = left.strip()
        dests = right.strip().split()

        graph[src] = dests

    return graph

def count_paths(graph, start, target):

    @lru_cache(None)
    def dfs(node):
        if node == target:
            return 1
        total = 0

        for nxt in graph.get(node, []):
            total += dfs(nxt)

        return total
    
    return dfs(start)

def main():
    input_path = Path(__file__).parent / "test.txt"
    input_path = Path(__file__).parent / "input.txt"
    lines = input_path.read_text().strip().splitlines()

    graph = parse_graph(lines)
    print(count_paths(graph, "you", "out"))

if __name__ == "__main__":
    main()
