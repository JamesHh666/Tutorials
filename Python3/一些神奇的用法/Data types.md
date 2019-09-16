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
