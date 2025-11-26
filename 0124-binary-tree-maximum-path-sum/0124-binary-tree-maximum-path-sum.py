class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_path = -inf
        def dfs(root):
            nonlocal max_path
            if not root:
                return 0

            l, r = max(0, dfs(root.left)), max(0, dfs(root.right))
            max_path = max(max_path, l+r+root.val)
            return root.val + max(l, r)
        dfs(root)
        return max_path
            