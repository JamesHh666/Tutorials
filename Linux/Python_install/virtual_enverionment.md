# Set up virtual environment
## Install [pyenv](https://github.com/pyenv/pyenv) and [Install pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)
Prerequisities:
```
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
```

Download:
```
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
```

For ubuntu:
```
export PYENV_ROOT="$HOME/.pyenv" >> ~/.bashrc
export PATH="$PYENV_ROOT/bin:$PATH" >> ~/.bashrc
eval "$(pyenv init -)" >> ~/.bashrc
eval "$(pyenv virtualenv-init -)" >> ~/.bashrc
```

# Often used command:
