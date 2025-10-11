from typing import Self


class TreeNode:
    def __init__(self: Self, val: int = 0, left: Self | None = None, right: Self | None = None) -> None:
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


class Solution:
    def levelOrder(self: Self, root: TreeNode | None = None) -> list[list[int]]:
        values: list[list[int]] = []
        if root:
            self._levelOrder(node=root, depth=0, values=values)
        else:
            return []
        return values

    def _levelOrder(self, node: TreeNode, depth: int, values: list[list[int]]) -> None:
        if depth >= len(values):
            values.append([node.val])
        else:
            values[depth].append(node.val)
        if node.left:
            self._levelOrder(node=node.left, depth=depth + 1, values=values)
        if node.right:
            self._levelOrder(node=node.right, depth=depth + 1, values=values)


if __name__ == "__main__":
    print(Solution().levelOrder(root=TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
