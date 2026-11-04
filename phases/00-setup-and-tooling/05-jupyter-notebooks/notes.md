# Jupyter Notebooks

Course lesson: [Jupyter Notebooks](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/05-jupyter-notebooks/docs/en.md)

**Date:** 2026-11-04
**Quiz:** 3/3
**Review:** Nothing flagged by the lesson quiz.

## What I learned

A notebook is made of code cells and Markdown cells. A Python kernel runs the code and keeps variables in memory between cells, so a later cell can use a value from an earlier one. Running a cell again uses the current value in the kernel: starting with `loss = 4.0` and `rate = 0.1`, `loss = loss * (1 - rate)` gives `3.6` on the first run and `3.24` on the second.

That shared state makes experimentation quick, but it can hide dependencies. Before sharing a notebook, restart the kernel and run all cells from top to bottom. This reveals cells that depend on stale variables or on an execution order that is not visible in the notebook.

`%timeit` repeats one line and reports an average, which is useful for small benchmarks. `%%time` measures one whole cell run. A DataFrame written as the final expression in a cell appears as a formatted table. `%matplotlib inline` displays plots in notebook output; `!pip install package` runs a shell command from a cell.

Notebooks are useful for exploring data, prototyping, plotting, and explaining an experiment. Move reusable utilities, training pipelines, and production code into `.py` files. Colab provides a cloud notebook and can offer a T4 GPU, but its sessions can time out, so save work outside the session.

## Exercise artifacts

- [`notebooks/notebook_basics.ipynb`](notebooks/notebook_basics.ipynb) compares Python and NumPy timings, reads a small CSV string into a DataFrame, plots accuracy, and demonstrates kernel memory state.
- [`code/notebook_tips.py`](code/notebook_tips.py) provides the same examples as reusable Python functions and a script entry point.
- [`outputs/prompt-notebook-helper.md`](outputs/prompt-notebook-helper.md) is the notebook debugging helper prompt produced by this lesson.

The notebook and script are prepared but have not been executed in this workspace. The available system Python has no Jupyter, NumPy, pandas, or Matplotlib installed, and there is no local `.venv` here. Install those packages in the intended environment before running the exercises. No API credentials are needed for this lesson.
