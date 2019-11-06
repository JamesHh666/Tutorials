## 1 Change cuda version:
put in ~/.bashrc (Ubuntu)
``` bash
export CUDA_HOME="/usr/local/cuda-10.0"
export PATH="$CUDA_HOME/bin:$PATH"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$CUDA_HOME/lib64"
```
