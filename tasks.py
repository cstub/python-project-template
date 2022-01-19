from typing import Optional

from invoke import task


def _run_pytest(c, test_dir, cov=False, cov_report=None):
    c.run(f"pytest {test_dir} {_pytest_cov_options(cov, cov_report)}", pty=True)


def _pytest_cov_options(use_cov: bool, cov_reports: Optional[str]):
    if not use_cov:
        return ""

    cov_report_types = cov_reports.split(",") if cov_reports else []
    cov_report_types = ["term"] + cov_report_types
    cov_report_params = [f"--cov-report {r}" for r in cov_report_types]
    return f"--cov {' '.join(cov_report_params)}"


@task
def conda_install(c):
    c.run("conda env update --prune -f environment.yml")


@task
def pip_install(c):
    c.run("pip install --upgrade pip")
    c.run("pip-compile requirements/prod.in")
    c.run("pip-compile requirements/dev.in")
    c.run("pip-sync requirements/prod.txt requirements/dev.txt")
    c.run("pip install -e .")


@task
def precommit_install(c):
    c.run("pre-commit install")


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
def clean_build(c):
    c.run("rm -fr dist")


@task
def clean(c):
    clean_cache(c)
    clean_test(c)
    clean_build(c)


@task(aliases=["cc"])
def code_check(c):
    c.run("pre-commit run --all-files", pty=True)


@task(aliases=["ut"])
def unit_test(c, cov=False, cov_report=None):
    _run_pytest(c, "tests/unit", cov, cov_report)


@task(aliases=["it"])
def integration_test(c, cov=False, cov_report=None):
    _run_pytest(c, "tests/integration", cov, cov_report)


@task
def test(c, cov=False, cov_report=None):
    _run_pytest(c, "tests", cov, cov_report)
