The official cheat sheet is [here](https://pytorch.org/tutorials/beginner/ptcheat.html)

# Tensor
Tensors `x` are similar to NumPy’s ndarrays, with the addition being that Tensors can also be used on a GPU to accelerate computing.
## Properties
```python
x.Size() # tensor size, type->tuple
x[:, 1]  # NumPy-like indexing
```

## Methods
1. Resize/reshape `torch.view`:
	```python
	x = torch.randn(4, 4) # >> torch.Size([4, 4])
	y = x.view(16)        # >> torch.Size([16])
	z = x.view(-1, 8)     # >> torch.Size([2, 8])
	```
2. If you have a **one element** tensor, use `.item()` to get the value as a Python number:
	```python
	x = torch.randn(1)
	print(x)          # >> tensor([-0.3687])
	print(x.item())   # >> -0.3686990439891815
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
* Syntax 1:
	```python
	x = torch.rand(5, 3)
	y = torch.rand(5, 3)
	print(x + y)
	```
* Syntax 2:
	```python
	print(torch.add(x, y))
	```
* Syntax 3:

	providing an output tensor as argument
	```python
	result = torch.empty(5, 3)
	torch.add(x, y, out=result)
	print(result)
	```
* Syntax 4:

	in-place
	```python
	y.add_(x)
	print(y)
	```
	**NOTE**: Any operation that **mutates a tensor in-place** is post-fixed with an `_`. For example: `x.copy_(y)`, `x.t_()`, will change `x`.
	
	
	
