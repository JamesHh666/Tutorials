[Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)

## O(N<sup>2</sup>)
```python
def lengthOfLIS(nums: List[int]) -> int:
  if not nums:
      return 0
  dp = [1] * len(nums)
  for i in range(1, len(nums)):
      for j in range(i):
          if nums[i] > nums[j]:
              dp[i] = max(dp[i], dp[j] + 1)
  return max(dp)
```

## O(NlogN)
Thanks to [this](https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation)
```python
def lengthOfLIS(nums: List[int]) -> int:
    if not nums:
        return 0
    dp = [nums[0]]
    for i in range(1, len(nums)):
        num = nums[i]
        if num > dp[-1]:
            dp.append(num)
        else:
            p1, p2 = 0, len(dp)-1
            while p1 != p2:
                m = (p1 + p2) // 2
                if dp[m] >= num:  # equal here is very important because we want increasing, cannot include the non-increasing number
                    p2 = m
                else:
                    p1 = m + 1
            dp[p1] = num
    return len(dp)
```
