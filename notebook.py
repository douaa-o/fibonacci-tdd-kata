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


@app.function
def fibonacci_v3(n): 
    if n <= 1 :  
        return n 
    return fibonacci_v3(n-1) + fibonacci_v3(n-2)


@app.cell
def _(pytest):
    @pytest.mark.parametrize(("n", "expected"), [(2, 1), (3,2), (4, 3)],)
    def test_cases3(n, expected):
        assert fibonacci_v3(n) == expected

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Marimo widget to display result
    """)
    return


@app.cell
def _(mo):
    n_input = mo.ui.number(start=1, stop=1000, step=1, value=15, label="n")
    n_input
    return (n_input,)


@app.cell
def _(mo, n_input):
    try:
        result = fibonacci_v3(n_input.value)
        output = mo.md(f"`fibonacci({n_input.value})` → **{result}**")
    except ValueError as e:
        output = mo.md(f"⚠️ Error: {e}")
    output
    return


if __name__ == "__main__":
    app.run()
