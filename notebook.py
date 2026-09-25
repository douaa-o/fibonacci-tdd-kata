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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Optimization
    """)
    return


@app.cell
def _(pytest):
    # As the numbers are very big, we will compare the length and the last digits for the unit tests 
    @pytest.mark.parametrize(("n", "expected_digits", "last_digits"), [(40, 9, "4155" )],)
    def test_large_values(n, expected_digits, last_digits):
        res = str(fibonacci_v3(n))
        assert len(res) == expected_digits
        assert res.endswith(last_digits)

    return


@app.function
def fibonacci_v4(n, dict=None):
    if dict is None : 
        dict = {0:0, 1:1} #initialize the dictionary 
    if n in dict : 
        return dict[n]
    dict[n] = fibonacci_v4(n-1, dict) + fibonacci_v4(n-2, dict)
    return dict[n]


@app.cell
def _(pytest):
    @pytest.mark.parametrize(("n", "expected_digits", "last_digits"), [(50, 11, "9025" ), (100, 21, "5075")],)
    def test_optimized(n, expected_digits, last_digits):
        res = str(fibonacci_v4(n))
        assert len(res) == expected_digits
        assert res.endswith(last_digits)

    return


if __name__ == "__main__":
    app.run()
