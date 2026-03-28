import numpy as np
from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        grid_np = np.array(grid)
        grid_t = grid_np.T

        column_counter = Counter(tuple(row) for row in grid_t)

        total_matches = 0
        for row in grid_np:
            row_tuple = tuple(row)
            count = column_counter.get(row_tuple, 0)
            total_matches += count
            
        return total_matches


        