import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pytest

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Fibonacci TDD with marimo
    """)
    return


@app.function
def fibonacci_v1(n): 
    if n == 0 : 
        return 0
    if n == 1 : 
        return 1
    return fibonacci_v1(n-1) + fibonacci_v1(n-2)


if __name__ == "__main__":
    app.run()
