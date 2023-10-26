class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        inn = {}
        def dfs(root):
            ans = 0
            if root.left:
                ans = max(ans, dfs(root.left))
            if root.right:
                ans= max(ans, dfs(root.right))
            inn[root] = ans + root.val
            return ans + root.val
        out = {root:0}
        def dfs2(root, par):
            if par == -1:
                if root.left:
                    dfs2(root.left, root)
                if root.right:
                    dfs2(root.right, root)
            else:
                if par.right == root:
                    try:
                        out[root] = max(0, par.val + out[par], par.val, par.val+ inn[par.left])
                    except:
                        out[root] = max(0, par.val + out[par], par.val)
                if par.left == root:
                    try:
                        out[root] = max(0, par.val + out[par], par.val, par.val+ inn[par.right])
                    except:
                        out[root] = max(0, par.val + out[par], par.val)
                if root.left:
                    dfs2(root.left, root)
                if root.right:
                    dfs2(root.right, root)
            
        dfs(root)
        dfs2(root, -1)
        ans = float('-inf')
        for i in inn:
            ans = max(ans, inn[i]+out[i]) 
        return ans
