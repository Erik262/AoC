import pathlib

import torch
import torch.nn.functional as F

KERNEL = torch.tensor( # (N=1, C=1, H=3, W=3)
    [[1.,1.,1.],
        [1.,0.,1.],
        [1.,1.,1.]]
    ).unsqueeze(0).unsqueeze(0)

def step(grid: torch.Tensor) -> tuple[torch.Tensor, bool, int]:
    g = grid.unsqueeze(0).unsqueeze(0) # (N=1, C=1, H, W)
    n_count = F.conv2d(g, KERNEL, padding=1).squeeze()

    center = (grid == 1)
    mask = center & (n_count < 4)
    num_removed = int(mask.sum().item())

    if num_removed == 0:
        return grid, False, 0
    
    new_grid = grid.clone()
    new_grid[mask] = 0

    return new_grid, True, num_removed

def main():
    input_path = pathlib.Path(__file__).parent / "input.txt"
    # input_path = pathlib.Path(__file__).parent / "test.txt"
    lines = input_path.read_text(encoding='utf-8').splitlines()

    grid_replace = [[1 if c == '@' else 0 for c in row] for row in lines]
    grid = torch.tensor(grid_replace, dtype=torch.float32)
    # H, W = grid.shape

    total_removed = 0

    while True:
        grid, changed, num_removed = step(grid)
        total_removed += num_removed
        
        if not changed:
            break

    # final_ones = int(grid.sum().item())

    print(total_removed)

if __name__ == "__main__":
    main()