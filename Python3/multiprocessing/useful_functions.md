# Useful functions for multiprocessing
Here are some function and other things that might be helpful for mp :)
## 1 Split list into sub-lists:
From [Ned Batchelder](https://stackoverflow.com/a/312464/10551119) (stackoverflow)
```python
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
```
