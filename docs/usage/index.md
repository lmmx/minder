# Minder

Exception guard capture utility library.

## Demo

The `Minder` context manager keeps failure modes **contained** with minimal **legibility** cost:

???+ failure

    ```py
    from minder import Minder

    def main() -> dict:
        with Minder() as guard:
            with guard.duty("greet"):
                print("Hello world")
            with guard.duty("division"):
                guard.result = 1 / 0
        return guard.report()


    response = main()
    print(f"Got {response=}")
    ```

    ```py
    Hello world
    Got response=[{'result': {'error': 'division by zero', 'where': 'division'}, 'success': False}]
    ```

In this example we expose a reliable interface of a `result` and `success` boolean.

We could also return `guard` (the `Minder` instance) and handle success/failure at the call site,
but the assumption is we would rather have this prepared for us.
