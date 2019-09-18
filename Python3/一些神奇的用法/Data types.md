# Data types
## List
* ### Reverse part of list
  ```
  list[:n].reverse()
  ```
  does not work.
  According to [here](https://stackoverflow.com/a/40823118/10551119), use:
  ```
  list[:n][::-1]
  ```
  BUT, `reverse()` is much faster than `[::-1]` when it comes to reversing a list. [Source](https://leetcode.com/problems/n-ary-tree-preorder-traversal/discuss/148867/Python-short-iterative-solution-beats-100-66-ms-faster-than-fastest-!/198287)
