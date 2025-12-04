import pathlib
from collections import defaultdict, Counter
import heapq
from typing import List

import torch
import torch.nn.functional as F

def main():
    input_path = pathlib.Path(__file__).parent / "input.txt"
    # input_path = pathlib.Path(__file__).parent / "test.txt"
    lines = input_path.read_text(encoding='utf-8').splitlines()

    grid_replace = [[1 if c == '@' else 0 for c in row] for row in lines]
    grid = torch.tensor(grid_replace, dtype=torch.float32)
    H, W = grid.shape

    grid = grid.unsqueeze(0).unsqueeze(0) # (N=1, C=1, H, W)

    kernel = torch.tensor(
        [[1.,1.,1.],
         [1.,0.,1.],
         [1.,1.,1.]]
        )
    
    kernel = kernel.unsqueeze(0).unsqueeze(0) # (N=1, C=1, H=3, W=3)
    n_count = F.conv2d(grid, kernel, padding=1).squeeze()

    mask = n_count < 4
    num_pos = mask.sum().item()

    center = (grid == 1)

    mask_active = center & mask
    num_active = mask_active.sum().item()
    print(num_active)

if __name__ == "__main__":
    main()