# Python Project Template

A Python project template using [conda](https://docs.conda.io/en/latest/) to manage virtual environments
and [Poetry](https://python-poetry.org/) to manage project dependencies and create Python packages.

The template uses [pre-commit hooks](https://pre-commit.com/) to run code style and code quality checks for each Git commit and
provides several [invoke](https://www.pyinvoke.org/) commands for common development [tasks](tasks.py).

The following tools are used for project development:

* [black](https://github.com/psf/black) for code formatting,
* [flake8](https://flake8.pycqa.org/en/latest/) for code style checks,
* [mypy](http://mypy-lang.org/) for type checking,
* [pytest](https://docs.pytest.org/en/7.0.x/) for test execution.

*Note*: A version of this project template using [pip-tools](https://github.com/jazzband/pip-tools) is available on the corresponding [branch](https://github.com/cstub/python-project-template/tree/pip-tools).

## Prerequisites

### Install Anaconda / Miniconda

Install [Anaconda](https://docs.anaconda.com/anaconda/install/index.html)
or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) by following the instructions outlined
in the respective documentation.

### Install Poetry

Install Poetry using the official [installer](https://python-poetry.org/docs/master/#installing-with-the-official-installer).

## Setup

### Setup on a local machine

To set up the development environment on a single machine run the following commands:

```shell
# setup conda environment
conda env create -f environment.yml

# activate conda environment
conda activate python-project-template

# install dependencies
poetry install

# install pre-commit hook
invoke precommit-install
```

This sequence of commands creates the project environment using conda and installs the Python dependencies specified in the [pyproject.toml](pyproject.toml) file into the newly created environment.
Afterwards the pre-commit hooks are installed and registered for automatic execution on each Git commit.

### Setup using Remote Interpreter

If a remote interpreter is employed (e.g. by using a [PyCharm SSH interpreter](https://www.jetbrains.com/help/pycharm/configuring-remote-interpreters-via-ssh.html)), the project environment can be installed on the remote machine using the following commands:

```shell
# create conda environment
conda env create -f environment.yml

# activate environment
conda activate python-project-template

# install dependencies
poetry install
```

To run the Git pre-commit hooks in a local environment, the following commands can be used locally:

```shell
# create and activate build tools environment
conda create -n build-tools python=3.9
conda activate build-tools

# install build tool dependencies
pip install pre-commit
pip install invoke
```

Install project pre-commit hooks using:
```shell
invoke precommit-install
```

## Usage

The project template provides [invoke](https://www.pyinvoke.org/) [tasks](tasks.py) to execute common development tasks.

Execute code formatting, style and type checks using:

```shell
invoke code-check
# or
invoke cc
```

Run the unit tests using:

```bash
invoke unit-test
# or
invoke ut
```

Run the integration tests using:

```bash
invoke integration-test
# or
invoke it
```

The complete test suite can be executed by running:

```bash
invoke test
```

To create a [distribution package](https://packaging.python.org/en/latest/tutorials/packaging-projects/) use the following command:

```shell
invoke build
```

After the build process has finished the `sdist` and `wheel` packages are available in the `/dist` folder.
