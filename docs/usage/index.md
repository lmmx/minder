---
title: Usage guide
---

The [`Minder`](../api/index.md#minder.minder.Minder) context manager keeps failure modes **contained**
with minimal **legibility** cost:

???+ failure

    ```py
    from minder import Minder

    def main() -> dict:
        with Minder() as guard:
            with guard.duty("greet"):
                print("Hello")
            with guard.duty("division"):
                guard.result = 1 / 0
        return guard.errors or guard.result


    response = main()
    print(f"Got {response=}")
    ```

    ```py
    Hello
    Got response=[{'error': 'division by zero', 'where': 'division'}]
    ```

In this example we simply use logical `or` to give the `errors` if any exist.
We could also return the `Minder` instance and handle success/failure at the call site.
