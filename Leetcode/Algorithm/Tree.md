# 1 Tree or Binary Tree:
## [Terminology](https://en.wikipedia.org/wiki/Tree_(data_structure)#Terminology)
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Binary_tree.svg/384px-Binary_tree.svg.png" alt="tree" height="200" width="240">

* **Node:** A structure which may contain a value or condition6
    * The topmost node in a tree is called the **root** node.
    * An **internal node** (also known as an inner node, inode for short, or **branch** node) is any node of a tree that has child nodes. 
    * An **external node** (also known as an outer node, **leaf** node, or terminal node) is any node that does not have child nodes.
* Each node in a tree has zero or more **child** nodes
* A node that has a child is called the child's **parent** node. A node has at most one parent.

## Tree traversal（遍历）
Traversing a tree involves iterating over all nodes in some manner.

Depth-first search: 
1. Inorder  : L-N-R
2. Preorder : N-(L-R) / N-children
3. Postorder: (L-R)-N / children-N
* **Recursively**
    * Inorder
        ```python
        def Inorder(root): 
            if root:  
                Inorder(root.left) 
                print(root.val)
                Inorder(root.right) 
        ```
    * Preorder
        * Binary tree
        ```python
        def Preorder(root): 
            if root: 
                print(root.val), 
                Preorder(root.left) 
                Preorder(root.right) 
        ```    
        * N-ary tree
        ```python
        def Postorder(root: 'Node') -> List[int]:
            def recur(root, res):
                 if root:
                    res.append(root.val)
                    for child in root.children:
                        Preorder(child, res)
            res = []
            recur(root, res)
            return res    
        ```
    
    * Postorder
        * Binary tree
        ```python
        def Postorder(root): 
            if root: 
                Postorder(root.left) 
                Postorder(root.right) 
                print(root.val)
        ```
        * N-ary tree
        ```python
        def recur(root, res):
            if root:
                for child in root.children:
                    recur(child, res)
                res.append(root.val)
        ```
        
* **Iteratively**
    `while` + `pop` + `list.extend/+=`
    * Preorder
        ```python
        def Preorder(root):
            res, nodes = [], root and [root]

            while nodes:
                node = nodes.pop()
                res.append(node.val)
                nodes += reversed([child for child in node.children if child])
            return res
        ```    
        
        **Notice:**
        1. `nodes = root and [root]`: very cool use of `and`, see [here](https://github.com/JamesHh666/Tutorials/blob/master/Python3/%E4%B8%80%E4%BA%9B%E7%A5%9E%E5%A5%87%E7%9A%84%E7%94%A8%E6%B3%95/Operators.md#logical-and-or-not)
        2. `reversed()` because the node is **poped** from list, so the leftmost child needs to go in last
        
    * Postorder
    
        If search by the order `child_left -> child_right -> node`,  the `node` needs to be preserved till all its children are traversed. 而且算法设计感觉会比较麻烦。
        逆向想想，倒过来遍历一遍，再把结果反过来，可能会方便很多。（不知道算不算小聪明？）
        ```python
        def Postorder(self, root: 'Node') -> List[int]:
            res, nodes = [], root and [root]

            while nodes:
                node = nodes.pop()
                res.append(node.val)
                nodes += [child for child in node.children if child]
            return reversed(res)
        ```    

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

> <img src="https://github.com/JamesHh666/Tutorials/blob/master/Images/58CCF8D69A16016315BAEA885A299233.png?raw=true" alt="Basic_block" width="500" height="300" />

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

## [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)
   * Version 1 (Iterative):
        Think from current node and its child
        ```python
        def invertTree(self, root: TreeNode) -> TreeNode:
            nodes = root and [root]

            while nodes:
               nodes_child = []
               for node in nodes:
                   node.left, node.right = node.right, node.left
                   if node.left:
                       nodes_child.append(node.left)
                   if node.right:
                       nodes_child.append(node.right)
               nodes = nodes_child
            return root
        ```
   * Version 2:
        Just think of the current node, similar idea as preorder traversal(见一个翻转一个)
        ```python
        def invertTree(self, root: TreeNode) -> TreeNode:
           nodes = root and [root]
           while nodes:
               node = nodes.pop()
               if node:
                node.left, node.right = node.right, node.left
                nodes += node.left, node.right
           return root
        ```

<br>
<br>
<br>
<br>

***

# 2 Binary Search Tree (BST)

[Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/solution/) is a binary tree where:

* the key in each node is greater than any key stored in the left sub-tree,

* and less than any key stored in the right sub-tree.

<img src="https://leetcode.com/problems/search-in-a-binary-search-tree/Figures/700/bst.png" alt="BST" width="350" height="200" />

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
