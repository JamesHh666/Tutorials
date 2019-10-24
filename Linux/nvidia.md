# 1 GPU driver


# 2 CUDA
```
# Install development and runtime libraries (~4GB)
sudo apt-get install --no-install-recommends \
    cuda-10-0 \
    libcudnn7=7.6.2.24-1+cuda10.0  \
    libcudnn7-dev=7.6.2.24-1+cuda10.0
```
    
# 3 cuDNN
see [official web](https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html)

# Common question:
## 1. [Different CUDA versions shown by nvcc and NVIDIA-smi](https://stackoverflow.com/a/53504578/10551119)
