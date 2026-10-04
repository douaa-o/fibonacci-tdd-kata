# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "fibonacci-tdd-kata",
#     "marimo",
#     "matplotlib",
# ]
# ///

import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")

with app.setup:
    from collections import Counter

    import marimo as mo
    import matplotlib.pyplot as plt

    from fibonacci_tdd_kata import fibonacci


@app.cell
def _():
    mo.md(r"""
    # Fibonacci Explorer
    Pick a range below and see how fibonacci classifies each number
    in it, both as a list and as a chart of the distribution of
    outputs. This notebook consumes the published fibonacci_tdd_kata
    package — it does not reimplement the function.
    """)
    return


@app.cell
def _():
    start = mo.ui.slider(1, 200, value=1, label="Range start")
    end = mo.ui.slider(1, 200, value=100, label="Range end")
    modulo = mo.ui.slider(1, 10, value=5, label="Modulo")
    mo.hstack([start, end, modulo])
    return end, modulo, start


@app.cell
def _(end, modulo, start):
    lo, hi = sorted((start.value, end.value))
    results = [fibonacci(n, modulo.value) for n in range(lo, hi + 1)]
    results
    return (results,)


@app.cell
def _(results):
    counts = Counter(results)

    fig, ax = plt.subplots()
    ax.bar(
        counts.keys(),
        counts.values(),
        color=["#4c72b0", "#dd8452", "#55a868", "#c44e52"],
    )
    ax.set_ylabel("Count")
    ax.set_title("Distribution of Fibonacci outputs over the selected range")
    fig
    return


if __name__ == "__main__":
    app.run()
