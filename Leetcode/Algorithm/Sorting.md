# Sorting algorithom in python
## *O(n<sup>2</sup>)*
### 1 Bubble: 
```python
def bubble(a: list):
    N = len(a)
    for i in range(N-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a
```

### 2 Selection:
```python
def selection(a: list):
    N = len(a)
    for i in range(N-1, 0, -1):
        idx_max = 0
        for j in range(1, i+1):
            if a[j] > a[idx_max]:
                idx_max = j
        a[idx_max], a[i] = a[i], a[idx_max]
    
    return a
```

### 3 Insersion: 
```python
def insertion(a: list):
    N = len(a)
    for i in range(N):
        num_to_insert = a[i]
        j = i 
        while j > 0 and a[j - 1] > num_to_insert:
            a[j] = a[j - 1]
            j -= 1
        a[j] = num_to_insert
    return a
```
## *O(nlogn)*
### 4 Shell:
```python
def shell(a: list):
    N = len(a)
    gap = N // 2
    while gap > 0:
        for i in range(gap, N):
            num_to_insert = a[i]
            j = i 
            while j >= gap and a[j - gap] > num_to_insert:
                a[j] = a[j - gap]
                j -= gap
            a[j] = num_to_insert
        gap //= 2
    return a
```

### 5 Merge Sort:
Thanks to [this answer](https://stackoverflow.com/a/31453147/10551119) :laughing:
```python 
def merge(left, right):
    i, j = 0, 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res

def devide(a: list):
    if len(a) < 2:
        return a[:]
    else:
        mid = len(a) // 2
        left = devide(a[:mid])
        right = devide(a[mid:])
    return merge(left, right)

def merge_sort(a: list):
    return devide(a)
```

### 6 Quick Sort:
```python
def quick_sort(a: list):
    less = []
    greater = []
    equal = []
    
    if len(a) > 1:
        pivot = a[0]
        for i in a:
            if i > pivot:
                greater.append(i)
            elif i < pivot:
                less.append(i)
            else:
                equal.append(i)
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return a
```

### 7 Heapsort:
See [this](https://brilliant.org/wiki/heap-sort/#implementation-of-heapsort)
```python
def min_heapify_node(a: list, heap_size:int, i: int):
    left = i * 2
    right = i * 2 + 1
    min_index = i
    if left <= heap_size and a[left - 1] > a[min_index - 1]:  # The result is modified on the original list, so here use > for ascending sort
        min_index = left
    if right <= heap_size and a[right - 1] > a[min_index - 1]:
        min_index = right
    if min_index != i:
        a[min_index - 1], a[i - 1] = a[i - 1], a[min_index - 1]  # swap root and the last node

def min_heapify(a: list, heap_size: int):
    for i in range(heap_size//2, 0, -1):
        min_heapify_node(a, heap_size, i)
    
def heap_sort(a: list):
    heap_size = len(a)
    for i in range(len(a), 0, -1):
        min_heapify(a, heap_size)
        a[0], a[i - 1] = a[i - 1], a[0]
        heap_size -= 1
    return a
```

## *Linear Sort*
### 8 Counting sort: *O(n+k)*
```python
def counting_sort(a: list):
    # prepare c for # of occurrence
    length = max(a) + 1 
    c = [0] * length
    for item in a:
        c[item] += 1
    for i in range(1, length):
        c[i] += c[i-1]
        
    # Get result
    res = [None] * len(a)
    for item in a:
        res[c[item] - 1] = item
        c[item] -= 1
    return res
```

### 9 Bucket Sort

### 10 Radix Sort
Thanks to [this](https://github.com/hustcc/JS-Sorting-Algorithm/blob/master/10.radixSort.md#4-python-%E4%BB%A3%E7%A0%81%E5%AE%9E%E7%8E%B0)
```python
def find_radix(num: int, digit: int):
    return (num // 10 ** digit) % 10

def radix_sort(a: list):
    max_digit = 0
    max_value = max(a)
    while 10 ** max_digit < max_value:
        max_digit += 1  # max=99, max_digit=3
    for digit in range(max_digit):
        buckets = [[] for _ in range(10)]
        for num in a:
            radix = find_radix(num, digit)
            buckets[radix].append(num)
        a = []    
        for bucket in buckets:
            for num in bucket:
                a.append(num)
    return a
```

## A small test function :poop:
```python
import random
import time

def test(func):
    N = random.randint(24, 81)
    a = [random.randrange(60) for _ in range(N)]
    start = time.time()
    res = func(a)
    end = time.time()
    print(f"Time used: {start - end:.2f} s")
    
    if res == sorted(a):
        return True
    else:
        return False
```
