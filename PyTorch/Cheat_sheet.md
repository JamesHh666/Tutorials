The official cheat sheet is [here](https://pytorch.org/tutorials/beginner/ptcheat.html)

# Tensor
Tensors `x` are similar to NumPy’s ndarrays, with the addition being that Tensors can also be used on a GPU to accelerate computing.
## Properties
```python
x[:, 1]     # NumPy-like indexing
tensor.data # returns a new tensor that shares storage with tensor. However, it always has requires_grad=False (even if the original tensor had requires_grad=True
```

## Methods
```python
x.Size()                # tensor size, type->tuple
x = x.view(-1, 8)       # Reshape/resize

x.item()                # Get a Python number from a tensor containing a SINGLE value
x.tolist()              # Returns the tensor as a (nested) list. For scalars, a standard Python number is returned, just like with item().

y = x.numpy()           # tensor -> ndarray. NOTE: if you change x, y is changed too!!
x = torch.from_numpy(y) # ndarray -> tensor

tensor.detach()         # creates a tensor that shares storage with tensor that does not require grad
tensor.clone()          # creates a copy of tensor that imitates the original tensor's requires_grad field
```
`detach` vs `clone`: Thanks to [this](https://discuss.pytorch.org/t/clone-and-detach-in-v0-4-0/16861/2?u=zxy)

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
