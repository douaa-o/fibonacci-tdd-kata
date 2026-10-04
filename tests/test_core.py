import pytest

from fibonacci_tdd_kata.core import fibonacci


@pytest.mark.parametrize(
    ("n", "m", "expected"),
    [(50, 10_000, 9025), (100, 10_000, 5075), (1_000, 1_000_000, 228875)],
)
def test_optimized(n, m, expected):
    assert fibonacci(n, m) == expected


def test_fibonacci_zero():
    assert fibonacci(0, 10) == 0
