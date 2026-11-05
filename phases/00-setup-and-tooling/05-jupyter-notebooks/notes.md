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

- [`notebooks/notebook_basics.ipynb`](notebooks/notebook_basics.ipynb) is the original lesson notebook and remains separate from the hands-on exercise notebook.
- [`notebooks/jupyter_exercises.ipynb`](notebooks/jupyter_exercises.ipynb) is the separate notebook used for the exercises.
- [`code/notebook_tips.py`](code/notebook_tips.py) provides the same examples as reusable Python functions and a script entry point.
- [`outputs/prompt-notebook-helper.md`](outputs/prompt-notebook-helper.md) is the notebook debugging helper prompt produced by this lesson.

## Exercise status

Ran the exercises locally in JupyterLab using the repository's `.venv`, which has JupyterLab, NumPy, pandas, and Matplotlib installed.

- **Timing comparison:** Python list generation took `11.1 ms ± 587 μs` per loop; NumPy generation took `1.27 ms ± 61.4 μs` per loop. NumPy was about 8.7× faster in this run. Timings vary by machine and session.
- **CSV and plot:** Completed the in-memory CSV exercise and confirmed the DataFrame and accuracy chart appeared.
- **Kernel state and clean rerun:** The initial cell reset `loss` to `4.0` on each run, so it returned `3.6` each time. The setup and update were then separated into cells to demonstrate retained kernel state. Restarted the local notebook kernel and ran all cells from the top; the run completed without errors.
- **Script/GPU exercise:** Ran `code/notebook_tips.py` in a Kaggle GPU notebook. PyTorch reported `2.11.0+cu130`, CUDA build `13.0`, and `torch.cuda.is_available() == True`. The script completed: Python random generation took `0.0142 s`, NumPy took `0.0011 s`; it displayed the model comparison table, saved `notebook_plot.png`, and reported array payloads of 0.008 MB, 0.8 MB, and 8.0 MB. These timings are specific to that Kaggle session.
- **Colab:** Not used because its homepage displayed a JavaScript JSON parsing error before notebook code could run.

No API credentials are needed for this lesson.
