# leetcode google interview problems


### 1. [Leetcode 939](https://leetcode.com/problems/minimum-area-rectangle/description/) : Minimum Area Rectangle
<pre>
You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

Return the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes. If there is not any such rectangle, return 0.

Example 1:

Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
Example 2:

Input: points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2
 
Constraints:

1 <= points.length <= 500
points[i].length == 2
0 <= xi, yi <= 4 * 104
All the given points are unique.
</pre>

Solution:

```python
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        min_area = float('inf')
        visited = set()
        for x1,y1 in points:
            for x2, y2 in visited:
                if (x1, y2) in visited and (x2, y1) in visited:
                    size = abs(x2-x1) * abs(y2-y1)
                    min_area = min(min_area, size)
            visited.add((x1,y1))
        return min_area if min_area != float('inf') else 0
```

### 2. [Leetcode 1293](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/) : Shortest Path in a Grid with Obstacles Elimination
<pre>
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

 

Example 1:


Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
Example 2:


Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
Output: -1
Explanation: We need to eliminate at least two obstacles to find such a walk.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 40
1 <= k <= m * n
grid[i][j] is either 0 or 1.
grid[0][0] == grid[m - 1][n - 1] == 0
</pre>

Solution:

```python
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        if rows + cols - 2 <= k:
            return rows + cols - 2
        queue = deque([(0,(0,0,k))])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set([(0,0,k)])
        while queue:
            steps, (r, c, eilimination_remaining) = queue.popleft()
            if r == rows-1 and c == cols-1:
                return steps
            for (r_inc, c_inc) in directions:
                new_row, new_col = r + r_inc, c + c_inc
                if 0 <= new_row and new_row < rows and 0 <= new_col and new_col < cols:
                    new_eiliminated = eilimination_remaining - grid[new_row][new_col]
                    if ((new_row,new_col, new_eiliminated) not in visited) and new_eiliminated >= 0:
                        visited.add((new_row, new_col, new_eiliminated))
                        queue.append((steps + 1, (new_row, new_col, new_eiliminated)))
        return -1
```