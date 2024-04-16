from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        return self.solve_3(root=root)

    @staticmethod
    def solve_1(root: TreeNode | None) -> int:
        """First approach is to run a BFS algorithm and check if the queue's current node has a left node and if so,
        check if it's a leaf node, and if so, sum the value.
        """
        queue: deque = deque([root])
        sum_: int = 0
        while queue:
            current_node: TreeNode = queue.popleft()
            if left := current_node.left:
                if left.left or left.right:
                    queue.append(left)
                else:
                    sum_ += left.val
            if right := current_node.right:
                queue.append(right)
        return sum_

    @staticmethod
    def solve_2(root: TreeNode | None) -> int:
        """Second approach, defining a recursive function that sums over an initial value of 0 and recursively adds
        based on the same logic as the previous approach (checking left nodes).
        """

        def _calculate_left_sum(node: TreeNode, cumulative_sum: int) -> int:
            if not node:
                return cumulative_sum
            if (left := node.left) and not left.left and not left.right:
                cumulative_sum += left.val
            cumulative_sum = _calculate_left_sum(node=left, cumulative_sum=cumulative_sum)
            return _calculate_left_sum(node=node.right, cumulative_sum=cumulative_sum)

        return _calculate_left_sum(node=root, cumulative_sum=0)

    def solve_3(self, root: TreeNode | None) -> int:
        """An improvement on the last approach by calling the function itself rather than defining a function within
        a function. The value is returned to avoid issues with immutable integers.
        """
        if not root:
            return 0
        sum_: int = 0
        if left := root.left:
            if not left.left and not left.right:
                sum_ += left.val
            else:
                sum_ += self.solve_3(root=left)
        sum_ += self.solve_3(root=root.right)
        return sum_
