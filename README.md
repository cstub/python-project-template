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

## Code Formatting & Style Checks

```shell
invoke lint
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

To create a [distribution package](https://packaging.python.org/en/latest/tutorials/packaging-projects/) the `build` package must be added to `requirements/dev.in` file.

Afterwards the `sdist` and `wheel` packages can be built using the following command:

```shell
python -m build
```
