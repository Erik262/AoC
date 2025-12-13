from __future__ import annotations

from pathlib import Path
import re


def _parse_input(text: str):
    lines = [ln.rstrip("\n") for ln in text.splitlines()]

    shapes = {}
    regions = []

    i = 0
    n = len(lines)

    shape_header = re.compile(r"^(\d+):\s*$")
    region_header = re.compile(r"^(\d+)x(\d+):\s*(.*)$")

    while i < n:
        ln = lines[i].strip()
        if not ln:
            i += 1
            continue

        m_shape = shape_header.match(ln)
        m_region = region_header.match(ln)

        if m_shape:
            idx = int(m_shape.group(1))
            i += 1
            grid = []
            
            while i < n and lines[i].strip() != "":
                grid.append(lines[i].strip())
                i += 1

            shapes[idx] = grid
            continue

        if m_region:
            w = int(m_region.group(1))
            h = int(m_region.group(2))
            rest = m_region.group(3).strip()
            counts = [int(x) for x in rest.split()] if rest else []
            regions.append((w, h, counts))
            i += 1
            continue

    if not regions:
        return [], []

    max_idx = max(shapes.keys())
    shape_list = [None] * (max_idx + 1)
    for k, v in shapes.items():
        shape_list[k] = v

    return shape_list, regions


def _cells_from_grid(grid):
    cells = []
    for y, row in enumerate(grid):
        for x, ch in enumerate(row):
            if ch == "#":
                cells.append((x, y))

    return tuple(cells)


def _normalize(cells):
    min_x = min(x for x, _ in cells)
    min_y = min(y for _, y in cells)
    out = sorted((x - min_x, y - min_y) for x, y in cells)
    return tuple(out)


def _orientations(cells):

    def rot90(x, y):
        return (y, -x)

    unique = set()
    res = []
    base = list(cells)

    for flip in (False, True):
        cur = [(-x, y) if flip else (x, y) for x, y in base]

        for _ in range(4):
            norm = _normalize(cur)

            if norm not in unique:
                unique.add(norm)
                res.append(norm)
            cur = [rot90(x, y) for x, y in cur]

    return res


def _placement_masks_for_region(orientations, W, H):

    masks = []
    for ori in orientations:
        max_x = max(x for x, _ in ori)
        max_y = max(y for _, y in ori)
        w = max_x + 1
        h = max_y + 1
        if w > W or h > H:
            continue

        for oy in range(H - h + 1):
            row_base = oy * W

            for ox in range(W - w + 1):
                m = 0

                for x, y in ori:
                    bit = (row_base + y * W + (ox + x))
                    m |= 1 << bit

                masks.append(m)

    return list(dict.fromkeys(masks))


def _can_pack(W, H, counts, placements_by_shape, areas):
    total_cells = W * H
    rem_area = 0
    counts = list(counts) + [0] * (len(areas) - len(counts))
    counts = tuple(counts[: len(areas)])

    for i, c in enumerate(counts):
        if c:
            if not placements_by_shape[i]:
                return False
            rem_area += c * areas[i]

    if rem_area > total_cells:
        return False
    
    if rem_area == 0:
        return True

    placement_lens = [len(p) for p in placements_by_shape]
    memo = {}

    def dfs(occ, cnts, rem):
        if rem == 0:
            return True
        
        free = total_cells - occ.bit_count()
        if rem > free:
            return False

        key = (occ, cnts)
        v = memo.get(key)
        if v is not None:
            return v

        best_i = -1
        best_len = 10**18
        for i, c in enumerate(cnts):
            if c:
                L = placement_lens[i]
                if L == 0:
                    memo[key] = False
                    return False
                if L < best_len:
                    best_len = L
                    best_i = i

        i = best_i
        new_cnts = list(cnts)
        new_cnts[i] -= 1
        new_cnts = tuple(new_cnts)

        for m in placements_by_shape[i]:
            if (m & occ) == 0:
                if dfs(occ | m, new_cnts, rem - areas[i]):
                    memo[key] = True
                    return True

        memo[key] = False

        return False

    return dfs(0, counts, rem_area)


def solve(input_path: Path) -> int:
    text = input_path.read_text(encoding="utf-8")
    shape_grids, regions = _parse_input(text)

    if not shape_grids:
        return 0

    shape_cells = [_cells_from_grid(g) for g in shape_grids]
    shape_oris = [_orientations(c) for c in shape_cells]
    areas = [len(c) for c in shape_cells]

    placement_cache = {}

    ok = 0
    for W, H, counts in regions:
        key = (W, H)

        if key not in placement_cache:
            placement_cache[key] = [
                _placement_masks_for_region(shape_oris[i], W, H) for i in range(len(shape_oris))
            ]

        placements_by_shape = placement_cache[key]

        if _can_pack(W, H, counts, placements_by_shape, areas):
            ok += 1

    return ok


if __name__ == "__main__":

    input_path = Path(__file__).parent / "test.txt"
    input_path = Path(__file__).parent / "input.txt"
    print(solve(input_path))
