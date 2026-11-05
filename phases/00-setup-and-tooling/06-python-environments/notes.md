# Python Environments

Course lesson: [Python Environments](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/06-python-environments/docs/en.md)

**Date:** 2026-11-05  
**Quiz:** 3/3  
**Review:** Nothing flagged by the lesson quiz.

## What I learned

A virtual environment keeps one project's Python packages separate from another project's. `pyproject.toml` declares the project's requirements; a lockfile records exact resolved versions, including transitive dependencies. `python -m pip` ties package installation to the selected Python interpreter. Conda environments should generally be managed with Conda so its resolver can track package changes.

## Exercise results

- **Environment setup:** Added and ran [`code/env_setup.sh`](code/env_setup.sh). It reused the repo `.venv` and passed checks for NumPy 2.5.4, Matplotlib 3.11.2, Jupyter 5.9.1, scikit-learn 1.9.1, pandas 3.1.1, and a NumPy matrix operation. `uv` was not on the repo environment's PATH, so the script used pip.
- **Isolation:** In `/tmp/lesson6-env`, NumPy was 1.26.4; in the repo `.venv`, it remained 2.5.4.
- **Project and lockfile:** [`exercise-project/pyproject.toml`](exercise-project/pyproject.toml) declares PyTorch and Anthropic. [`exercise-project/uv.lock`](exercise-project/uv.lock) pins the resolved dependencies and passed `uv lock --check`. `uv sync` installed the editable project into the temporary environment; imports reported `torch 2.15.0+cpu` and `anthropic 2.5.0`. The CPU-only PyTorch source avoids the large CUDA/cuDNN download; CUDA access was separately confirmed in Kaggle during Lesson 5.
- **User-site install:** Installed `pyfiglet 1.0.4` with `--user` into the isolated `/tmp/lesson6-userbase`, verified its location with `pip show`, uninstalled it, and confirmed `pip show` no longer found it.

The initial default PyTorch install timed out while downloading a 519 MB CUDA/cuDNN dependency. Using the official CPU-only PyTorch index completed the local import exercise without those CUDA packages. The global-install demonstration used a temporary user-site so it did not modify the actual system or home package sites.

## Artifacts

- [`code/env_setup.sh`](code/env_setup.sh) — creates or reuses the course `.venv`, installs core tools, and verifies imports.
- [`exercise-project/pyproject.toml`](exercise-project/pyproject.toml) — example project metadata and dependencies.
- [`exercise-project/uv.lock`](exercise-project/uv.lock) — exact dependency resolution for the project.
- [`exercise-project/src/lesson6_demo/__init__.py`](exercise-project/src/lesson6_demo/__init__.py) — minimal importable package for the editable-install exercise.
