# minder

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

```py
from minder import Minder


def risky_business() -> dict:
    with Minder() as guard:
        with guard.duty("greet"):
            print("Hello")
        with guard.duty("calculation"):
            guard.result = 1 / 0
    return guard.errors or guard.result


response = risky_business()
print(f"Got {response=}")
```

```
Hello
Got response=[{'error': 'division by zero', 'where': 'calculation'}]
```
