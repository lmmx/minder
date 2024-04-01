"""Test that a `Minder` works when no error is raised (trivial case)."""

from minder import Minder


__all__ = ["succeed", "test_succeed"]


def succeed():
    """Usage example showing an operation that succeeds."""
    with Minder() as guard:
        with guard.duty("processing"):
            my_value = 100
        with guard.duty("finalising"):
            guard.result = my_value
    return guard.report()


def test_succeed():
    """Confirm that the result was set on the `Minder` without issue."""
    assert succeed() == {"result": 100, "success": True}
