# Sorting algorithom in python
## 1 Bubble: *O(n<sup>2</sup>)*
```python
def bubble(a: list):
    N = len(a)
    for i in range(N-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a
```

## 2 Selection: *O(n<sup>2</sup>)*
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

## 3 Insersion: *O(n<sup>2</sup>)*
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

## 4 Shell:
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
