The official cheat sheet is [here](https://pytorch.org/tutorials/beginner/ptcheat.html)

# Tensor
Tensors `x` are similar to NumPy’s ndarrays, with the addition being that Tensors can also be used on a GPU to accelerate computing.
## Properties
```python
x.Size() # tensor size, type->tuple
x[:, 1]  # NumPy-like indexing
```

## Methods
```python
x = x.view(-1, 8)       # Reshape/resize
x.item()                # Get the value as a Python number
y = x.numpy()           # tensor -> ndarray. NOTE: if you change x, y is changed too!!
x = torch.from_numpy(y) # ndarray -> tensro
```

## Creation
1. Common type:
	```python
	x = torch.empty(5, 3)
	x = torch.rand(5, 3)
	x = torch.zeros(5, 3, dtype=torch.long)  # Specify dtype
	```
2. Directly from data:
	```python
	x = torch.tensor([5.5, 3])
	```
3. Directly from existing tensor:

	These methods will **reuse** properties of the input tensor, e.g. dtype, unless new values are provided by user
	```python
	x = torch.tensor([5.5, 3])
	```
	
# Operations	
```python
x = torch.rand(5, 3)
y = torch.rand(5, 3)
# 1
print(x + y)
# 2
print(torch.add(x, y))
# 3 providing an output tensor as argument
torch.add(x, y, out=result) 
print(result)
# 4 in-place
y.add_(x) 
print(y)
```
**NOTE**: Any operation that **mutates a tensor in-place** is post-fixed with an `_`. For example: `x.copy_(y)`, `x.t_()`, will change `x`.
	
	
	
