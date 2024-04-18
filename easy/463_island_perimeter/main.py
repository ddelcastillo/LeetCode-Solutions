class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        return self.solve_1(grid=grid)

    @staticmethod
    def solve_1(grid: list[list[int]]) -> int:
        """Approach is pretty simple and efficient: Once you're standing in an island grid, you want to check the
        neighbors, if there's ocean, sum it up!
        """
        perimeter: int = 0
        n: int = len(grid)
        for i in range(n):
            m = len(grid[i])
            for j in range(m):
                if grid[i][j]:
                    if (left := i - 1) < 0 or not grid[left][j]:
                        perimeter += 1
                    if (right := i + 1) >= n or not grid[right][j]:
                        perimeter += 1
                    if (up := j - 1) < 0 or not grid[i][up]:
                        perimeter += 1
                    if (down := j + 1) >= m or not grid[i][down]:
                        perimeter += 1
        return perimeter
