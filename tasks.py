from invoke import task


@task
def precommit_install(c):
    c.run("pre-commit install")


@task
def conda_install(c):
    c.run("conda env update --prune -f environment.yml")


@task
def pip_install(c):
    c.run("pip-compile requirements/prod.in")
    c.run("pip-compile requirements/dev.in")
    c.run("pip-sync requirements/prod.txt requirements/dev.txt")
    c.run("pip install -e .")


@task
def clean_cache(c):
    c.run("find . -name '*.pyc' -exec rm -f {} +")
    c.run("find . -name '*.pyo' -exec rm -f {} +")
    c.run("find . -name '*~' -exec rm -f {} +")
    c.run("find . -name '__pycache__' -exec rm -fr {} +")
    c.run("rm -fr .mypy_cache")


@task
def clean_test(c):
    c.run("rm -fr .tox/")
    c.run("rm -f .coverage")
    c.run("rm -fr htmlcov/")
    c.run("rm -fr .pytest_cache")


@task
def clean(c):
    clean_cache(c)
    clean_test(c)


@task
def lint(c):
    c.run("pre-commit run --all-files", pty=True)


@task(aliases=["ut"])
def unit_test(c):
    c.run("pytest tests/unit", pty=True)


@task(aliases=["it"])
def integration_test(c):
    c.run("pytest tests/integration", pty=True)


@task
def test(c):
    c.run("pytest tests", pty=True)
