from pathlib import Path
import math
from collections import Counter

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]

        return x

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        if ra == rb:
            return
        
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb

        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra

        else:
            self.parent[rb] = ra
            self.rank[ra] += 1

def read_points(path):
    pts = []

    for line in path.read_text().splitlines():
        x, y, z = map(int, line.split(','))
        pts.append((x, y, z))

    return pts

def all_pairwise_edges(points):
    n = len(points)
    edges = []

    for i in range(n):
        x1, y1, z1 = points[i]

        for j in range(i+1, n):
            x2, y2, z2 = points[j]
            dx = x1 - x2
            dy = y1 - y2
            dz = z1 - z2

            edges.append((math.sqrt(dx*dx + dy*dy + dz*dz), i, j))

    return edges

if __name__ == "__main__":
    # input_path = Path(__file__).parent / "test.txt"
    input_path = Path(__file__).parent / "input.txt"
    
    points = read_points(input_path)
    edges = all_pairwise_edges(points)
    edges.sort(key=lambda e: e[0])

    connections_needed = 1000

    dsu = DSU(len(points))
    for k in range(connections_needed):
        _, i, j = edges[k]
        dsu.union(i, j)

    roots = [dsu.find(i) for i in range(len(points))]
    counts = Counter(roots)
    sizes = sorted(counts.values(), reverse=True)

    result = sizes[0] * sizes[1] * sizes[2]
    print(result)
