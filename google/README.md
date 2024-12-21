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

### 3. [Leetcode 442](https://leetcode.com/problems/find-all-duplicates-in-an-array/description/) : Find All Duplicates in an Array
<pre>
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears at most twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output. O(1) space complexity.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
Example 2:

Input: nums = [1,1,2]
Output: [1]
Example 3:

Input: nums = [1]
Output: []
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
Each element in nums appears once or twice.
</pre>

Solution:

```python
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            num = abs(nums[i])
            if nums[num-1] < 0:
                res.append(num)
            else:
                nums[num-1] *= -1
        return res
```

### 4. [Leetcode 1091](https://leetcode.com/problems/shortest-path-in-binary-matrix/description/) : Shortest Path in Binary Matrix
<pre>
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

 

Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
</pre>

Solution:

```python
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        if grid[0][0] or grid[rows-1][cols-1]:
            return -1
        queue = deque([(0,0,1)])
        res = (rows*cols) + 1
        visited = set([(0,0)])
        directions = [(0, 1), (1, 1), (1, 0),(1,-1), (0, -1), (-1, -1), (-1,0), (-1, 1)]
        while queue:
            r, c, steps = queue.popleft()
            if r == rows-1 and c == cols-1:
                res = min(res, steps)
            for r_inc, c_inc in directions:
                new_row = r + r_inc
                new_col = c + c_inc
                if 0 <= new_row and new_row < rows and 0 <= new_col and new_col < cols and not grid[new_row][new_col]:
                    new_steps = steps + 1
                    if (new_row, new_col) not in visited:
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col, new_steps))
        return res if res < (rows*cols) + 1 else -1
```

### 3. [Leetcode 224](https://leetcode.com/problems/basic-calculator/description/) : Basic Calculator
<pre>
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
 

Constraints:

1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.
</pre>

Solution:

```python
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        cur, res = 0, 0
        sign = 1
        for ch in s:
            if ch.isdigit():
                cur = cur * 10 + int(ch)
            elif ch == '+' or ch == '-':
                res += cur * sign
                cur = 0
                sign = 1 if ch == '+' else -1
            elif ch == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif ch == ')':
                res += cur * sign
                cur = res
                sign = stack.pop()
                res = stack.pop()
        res += cur * sign
        return res
```

### 3. [Leetcode 68](https://leetcode.com/problems/text-justification/description/) : Text Justification
<pre>
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
 

Constraints:

1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth

</pre>

Solution:

```python
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        queue = deque([])
        charsCount, spaceCount = 0, -1
        res = []
        for i in range(len(words)):
            word = words[i]
            if charsCount + spaceCount + len(word) >= maxWidth:
                line = ""
                spaceSize = 0 if spaceCount <= 0 else (maxWidth - charsCount) // spaceCount
                extraSpaces = 0 if spaceCount <= 0 else (maxWidth - charsCount) % spaceCount
                spaceString = " " * spaceSize
                while queue:
                    chunk = queue.popleft()
                    if line != "":                        
                        line += spaceString + (" " if extraSpaces > 0 else "")
                        extraSpaces -= 1
                    line += chunk
                    if len(queue) == 0:
                        spaceString = " " * (maxWidth - len(line))
                        line += spaceString
                res.append(line)
                charsCount, spaceCount = 0, -1
            charsCount += len(word)
            spaceCount += 1
            queue.append(word)
        line = ""
        spaceString = " "
        while queue:
            chunk = queue.popleft()
            if line != "":
                line += spaceString
            line += chunk
            if len(queue) == 0:
                 spaceString = " " * (maxWidth - len(line))
                 line += spaceString
        res.append(line)
        return res
```

### 3. [Leetcode 721](https://leetcode.com/problems/accounts-merge/description/) : Accounts Merge
<pre>
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

 

Example 1:

Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Example 2:

Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
 

Constraints:

1 <= accounts.length <= 1000
2 <= accounts[i].length <= 10
1 <= accounts[i][j].length <= 30
accounts[i][0] consists of English letters.
accounts[i][j] (for j > 0) is a valid email.
</pre>

Solution:

```python
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = {}
        email_to_name = {}
        for account in accounts:
            name = account[0]
            if account[1] not in graph:
                graph[account[1]] = set()
            for email in (account[1:]):
                if email not in graph:
                    graph[email] = set()
                graph[email].add(account[1])
                graph[account[1]].add(email)
                email_to_name[email] = name
        
        res = []
        visited = set()
        for email in graph:
            if email in visited:
                continue
            local_res = []
            name = email_to_name[email]
            stack = [email]
            while stack:
                email = stack.pop()
                if email not in visited:
                    visited.add(email)
                    local_res.append(email)
                    for child in graph[email]:
                       stack.append(child)
            res.append([name] + sorted(local_res))
        return res
```

### 3. [Leetcode ]() : 
<pre>

</pre>

Solution:

```python

```

### 3. [Leetcode ]() : 
<pre>

</pre>

Solution:

```python

```

### 3. [Leetcode ]() : 
<pre>

</pre>

Solution:

```python

```

### 3. [Leetcode ]() : 
<pre>

</pre>

Solution:

```python

```

### 3. [Leetcode ]() : 
<pre>

</pre>

Solution:

```python

```

### 3. [Leetcode ]() : 
<pre>

</pre>

Solution:

```python

```

### 3. [Leetcode ]() : 
<pre>

</pre>

Solution:

```python

```

### 3. [Leetcode ]() : 
<pre>

</pre>

Solution:

```python

```

### 3. [Leetcode ]() : 
<pre>

</pre>

Solution:

```python

```

### 3. [Leetcode ]() : 
<pre>

</pre>

Solution:

```python

```

### 3. [Leetcode ]() : 
<pre>

</pre>

Solution:

```python

```

### 3. [Leetcode ]() : 
<pre>

</pre>

Solution:

```python

```

### 3. [Leetcode ]() : 
<pre>

</pre>

Solution:

```python

```