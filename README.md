# Python ML Project Template

## Setup on single Machine

```shell
# setup conda env
conda env create -f environment.yml

# activate env
conda activate python-ml-project-template

# install dependencies
invoke pip-install

# install pre-commit
invoke precommit-install
```

## Setup using Remote Interpreter

### Remote machine

```shell
# create conda env
conda env create -f environment.yml

# activate env
conda activate python-ml-project-template

# install dependencies
invoke pip-install
```

### Local machine

One-time setup of `build-tools` env:
```shell
conda create -n build-tools python=3.8
conda activate build-tools
pip install pre-commit
pip install invoke
```

Install project pre-commit hooks:
```shell
conda activate build-tools

invoke precommit-install
```

## Code Formatting, Style and Type Checks

```shell
invoke code-check
# or
invoke cc
```

## Testing

```shell
# unit tests
invoke unit-test
# or
invoke ut

# integration tests
invoke integration-test
# or
invoke it

# all tests
invoke test
```

## Create a Distribution Package

To create a [distribution package](https://packaging.python.org/en/latest/tutorials/packaging-projects/) use the following command:

```shell
python -m build
```

After the build process has finished the `sdist` and `wheel` packages are available in the `/dist` folder.
