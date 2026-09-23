import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pytest

    return mo, pytest


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Fibonacci TDD with marimo
    """)
    return


@app.function
def fibonacci_v1(n):  
    return n


@app.cell
def _(pytest):
    @pytest.mark.parametrize(("n", "expected"), [(2, 1), (3,2), (4, 3)],)
    def test_cases(n, expected):
        assert fibonacci_v1(n) == expected

    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
