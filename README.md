# Minder

[![PyPI](https://img.shields.io/pypi/v/minder?logo=python&logoColor=%23cccccc)](https://pypi.org/project/minder)
[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/lmmx/minder/master.svg)](https://results.pre-commit.ci/latest/github/lmmx/minder/master)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/minder.svg)](https://pypi.org/project/minder)

<!-- [![build status](https://github.com/lmmx/minder/actions/workflows/master.yml/badge.svg)](https://github.com/lmmx/minder/actions/workflows/master.yml) -->

Exception guard capture utility library.

## Installation

```sh
pip install minder
```

## Demo

The `Minder` context manager keeps failure modes **contained** with minimal **legibility** cost:

```py
from minder import Minder

def main() -> dict:
    with Minder() as guard:
        with guard.duty("greet"):
            print("Hello world")
        with guard.duty("division"):
            guard.result = 1 / 0
    return guard.errors or guard.result


response = main()
print(response)
```

```py
Hello world
[{'error': 'division by zero', 'where': 'division'}]
```

In this example we simply use logical `or` to give the `errors` if any exist.
We could also return the `Minder` instance and handle success/failure at the call site.
