# CoopGT

A library for the study of cooperative game theory. It works with characteristic
function games and provides the Shapley value, checks of standard properties
(validity, monotonicity, superadditivity, convexity), and core membership.

## Documentation

Full documentation, including a theory section, is available here:
https://drvinceknight.github.io/coopgt/

## Installation

```bash
$ python -m pip install coopgt
```

## Development

This project uses [`uv`](https://docs.astral.sh/uv/) for environment management,
[`ruff`](https://docs.astral.sh/ruff/) for linting and formatting,
[`ty`](https://docs.astral.sh/ty/) for type checking, and
[`zensical`](https://zensical.org) for the documentation.

Clone the repository and install the development dependencies:

```bash
$ git clone https://github.com/drvinceknight/coopgt.git
$ cd coopgt
$ uv sync --group dev
```

Run the checks and the test suite:

```bash
$ uv run ruff check src/ tests/
$ uv run ruff format --check src/ tests/
$ uv run ty check src/
$ uv run pytest
```

Build and preview the documentation:

```bash
$ uv run zensical build
$ uv run zensical serve
```

## Code of conduct

In the interest of fostering an open and welcoming environment, all
contributors, maintainers and users are expected to abide by the Python code of
conduct: https://www.python.org/psf/codeofconduct/
