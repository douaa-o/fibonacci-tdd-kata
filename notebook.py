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


@app.function
def fibonacci_v2(n): 
    if n == 0 : 
        return 0
    if n == 1 : 
        return 1 
    return fibonacci_v2(n-1) + fibonacci_v2(n-2)


@app.cell
def _(pytest):
    @pytest.mark.parametrize(("n", "expected"), [(2, 1), (3,2), (4, 3)],)
    def test_cases2(n, expected):
        assert fibonacci_v2(n) == expected

    return


if __name__ == "__main__":
    app.run()
