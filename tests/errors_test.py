"""Test that `Duty` failures are reported to the `Minder`."""
from minder import Minder


__all__ = ["fail_early", "test_fail_early"]


def fail_early(event: dict):
    """Usage example showing an operation that fails at the first hurdle (ingestion)."""
    with Minder() as guard:
        with guard.duty("ingestion"):
            if not event:
                raise ValueError("Input was empty")  # This error is caught and reported
        with guard.duty("processing"):
            print(f"Received {event}")
        with guard.duty("finalising"):
            guard.result = {"result": "Success"}
    return guard.errors or guard.result


def test_fail_early():
    """Confirm that the error message was stringified in the error key at ingestion."""
    assert fail_early({}) == [{"error": "Input was empty", "where": "ingestion"}]
