# 1 Tree or Binary Tree:

## [104 Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

### DFS (recursively )
```python 
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        if not root.left and not root.right: return 1
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

```
### BFS (iteratively)
```python
class Solution(object):
    def maxDepth(self, root):
        depth = 0
        nodes = [root] if root else []
        
        while nodes:
            depth += 1
            next_nodes = []
            for node in nodes:
                if node.right:
                    next_nodes.append(node.right)
                if node.left:
                    next_nodes.append(node.left)            
            nodes = next_nodes
            
        return depth
```

## [111. Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
### DFS
> **The basic block**
> <img src="https://github.com/JamesHh666/Tutorials/blob/master/Images/58CCF8D69A16016315BAEA885A299233.png?raw=true" alt="Basic_block" width="400" height="300" />

```python
class Solution(object):   
    def minDepth(self, root):
        if not root: return 0  # blk 3
        if not root.left and not root.right: return 1 # blk 2
        
        d = map(self.minDepth, (root.left, root.right))
        if min(d) == 0:
            return max(d) + 1  # blk 1
        else:
            return min(d) + 1  # blk 0

```
### BFS
```python
class Solution(object):   
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        nodes = [root] if root else []
        
        while nodes:
            depth += 1
            next_nodes = []
            find_min = False
            for node in nodes:
                if not node.left and not node.right:
                    find_min = True
                    break
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            if find_min:
                break
            nodes = next_nodes
        return depth
```

## [559. Maximum Depth of N-ary Tree](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/)
```python
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
#         # v1:
#         if not root: return 0
#         depth = 0
#         for child in root.children:
#             depth = max(self.maxDepth(child), depth)
#         return depth + 1

        # v2:
        if not root: return 0
        if not root.children: return 1
        
        return max(self.maxDepth(child) for child in root.children) + 1
        
```

## [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)

* ### First version
**!!!! The input `[]` is actually not a list, but `None`, so I add `mark_layer = 0` **

```python
class Solution(object):
    mark_layer = 0
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # In case input root is "None" (not []!!!!!!)
        if root is None and not self.mark_layer: return True
        self.mark_layer += 1
        
        if root is None: return 0
        if not root.left and not root.right: return 1
        
        depth_left = self.isBalanced(root.left)
        depth_right = self.isBalanced(root.right)
        if depth_left is False or depth_right is False:
            return False
        
        if abs(depth_left - depth_right) >1:
            return False
        return max(depth_left, depth_right) + 1
```
**To be improved:**
> 代码层次不够明显，`计算层数`和`判断`堆叠在一起。 
 
* ### Improved version

```python
class Solution(object):
    def do(self, root):
        if root is None: return 0
        if not root.left and not root.right: return 1
        
        depth_left = self.do(root.left)
        depth_right = self.do(root.right)
        
        if abs(depth_left - depth_right) >1:
            self.is_balanced = False
            return 0  # 随便返回一个数，无所谓了
        
        return max(depth_left, depth_right) + 1
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # In case input root is "None" (not []!!!!!!)
        if root is None: return True
        self.is_balanced = True
        self.do(root)
        
        return self.is_balanced
```

## [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ############# iteratively #############
        nodes = [root] if root else []

        while nodes:
            next_nodes = []
            next_nodes_val = []
            
            for node in nodes:
                next_nodes.append(node.left)
                next_nodes.append(node.right)

            for node in next_nodes:
                if node == None:
                    next_nodes_val.append(None)
                else:
                    next_nodes_val.append(node.val)

            n = len(next_nodes_val) // 2 
            left = next_nodes_val[:n][::-1]  # !!!! Reverse part of list (.reverse() won't work)
            right = next_nodes_val[n:]

            if left == right:
                nodes = [i for i in next_nodes if i != None]
            else:
                return False
    
        return True
```
**Result:** 16 ms, faster than 93.26% of Python online submissions for Symmetric Tree.
**Memory Usage:** 11.9 MB, less than 91.30% of Python online submissions for Symmetric Tree.

**Notice:** To reverse *part* of list, `list[2:4].reverse()` won't work, it just return `None`. Thanks to [Reman at stackoverflow](https://stackoverflow.com/a/40823118/10551119), use `list[2:4][::-1]`

<br>
<br>
<br>
<br>

***

# 2 Binary Search Tree (BST)

[Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/solution/) is a binary tree where:

* the key in each node is greater than any key stored in the left sub-tree,

* and less than any key stored in the right sub-tree.

<img src="https://leetcode.com/problems/search-in-a-binary-search-tree/Figures/700/bst.png" alt="BST" width="300" height="200" />

## [700. Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/)
```python
class Solution(object):
    def searchBST(self, root, val):
        if not root: return None
        if root.val == val: return root
        if not root.left and not root.right: return None
        
        ! return self.searchBST(root.left, val) or self.searchBST(root.right, val)
```
**Result:** Runtime: 68 ms, faster than 64.21% of Python online submissions for Search in a Binary Search Tree.


### Need optimization:
It is a BST, so you can take advantage of its property:
* if `root.val < val` only search the right node
* if `root.val > val` only search the left node

```python
class Solution(object):
    def searchBST(self, root, val):
        if not root: return None
        if root.val == val: return root
        if not root.left and not root.right: return None
        
        if val > root.val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)
```
**Result:** Runtime: 60 ms, faster than 95.49% of Python online submissions for Search in a Binary Search Tree.
