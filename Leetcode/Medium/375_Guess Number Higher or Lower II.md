# Binary search:

```python
class Solution(object):
    def searchRange(self, nums, target):
        def binary_search_to_left(hi, nums, target):
            lo = 0
            mid = (lo+hi) // 2

            while lo <= hi:
                if nums[mid] == target:
                    hi = mid - 1
                elif nums[mid] > target:
                    hi = mid - 1
                elif nums[mid] < target:   
                    lo = mid + 1
                mid = (lo+hi) // 2
            return mid + 1
        
        def binary_search_to_right(lo, nums, target):
            hi = len(nums) - 1
            mid = (lo+hi) // 2

            while lo <= hi:
                if nums[mid] == target:
                    lo = mid + 1
                elif nums[mid] > target:
                    hi = mid - 1
                elif nums[mid] < target:   
                    lo = mid + 1
                mid = (lo+hi) // 2
            return mid

        if len(nums) == 0:
            return [-1, -1]

        lo = [0, 0, None]  # outer, left, right
        hi = [len(nums) - 1, None, len(nums) - 1]
        mid = (lo[0]+hi[0]) // 2
        
        # 1 Find target in nums
        while lo[0] <= hi[0]:
            if nums[mid] == target:
                lo[2] = mid + 1
                hi[1] = mid 
                break
            elif nums[mid] > target:
                hi[0] = mid - 1
            elif nums[mid] < target:   
                lo[0] = mid + 1
            mid = (lo[0]+hi[0]) // 2
            
        if lo[0] > hi[0]: 
            return [-1, -1]
            
        # 2 Find first and last position
        return [binary_search_to_left(hi[1], nums, target), binary_search_to_right(lo[2], nums, target)]
```

### Result:
**Runtime**: 64 ms, faster than 93.28% of Python online submissions for Find First and Last Position of Element in Sorted Array. 

**Memory Usage**: 13 MB, less than 79.41% of Python online submissions for Find First and Last Position of Element in Sorted Array.

### Coding problem:
1. **Not concise**, because I:
    * Firstly try to find **weather** target is **in** the nums and
    * Then find the first and the last index.
    
The first step can be improved to **directly** find the leftmost index

***
## The imporved version:

```python
class Solution(object):
def searchRange(self, nums, target):
    def binary_search(nums, target, lo, hi, left):
        while lo < hi:
            mid = (lo+hi) // 2
            if (nums[mid] > target) or (left and nums[mid] == target):
                hi = mid 
            else:   
                lo = mid + 1
        return lo

    if len(nums) == 0:
        return [-1, -1]

    lo = binary_search(nums, target, lo=0, hi=len(nums)-1, left=True)
    if nums[lo] != target:
        return [-1, -1]

    return [lo, binary_search(nums, target, lo=lo, hi=len(nums), left=False)-1]
```

### Result: (seems almost the same)
**Runtime**: 64 ms, faster than 93.28% of Python online submissions for Find First and Last Position of Element in Sorted Array.

**Memory Usage**: 12.9 MB, less than 94.12% of Python online submissions for Find First and Last Position of Element in Sorted Array.

Code notice:
1. Finding the leftmost one is easy and intuitive using the code above, but as for the rightmost one, it is a little bit tricky:
    * The `hi` boudary should be **len(nums)** instead of **len(nums) - 1**, because otherwise the `mid` cannot reach and check whether the value at `nums[len(nums) - 1]` equals to target.
    * The returned `lo` is 1 larger than the true value, need to **-1**
   
