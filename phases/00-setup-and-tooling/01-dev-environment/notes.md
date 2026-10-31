# Dev Environment

Course lesson: [Dev Environment](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/01-dev-environment/docs/en.md)

## What I learned

A development environment includes system tools, package managers, language runtimes, and AI/ML libraries. A project-specific Python environment keeps its installed packages separate from other projects.

## Setup results

| Tool | Result |
|---|---|
| Git | 2.43.0 |
| Python | 3.12.3 |
| uv | 0.13.6 |
| NumPy | 2.5.4 |
| Matplotlib | 3.11.2 |
| Jupyter | 1.1.1 |

Created `.venv` with CPython 3.12.3. Activated it with `source .venv/bin/activate` and installed NumPy, Matplotlib, and Jupyter into it.

## Commands I ran

```bash
git --version
python3 --version
uv --version
uv venv --python 3.12
source .venv/bin/activate
uv pip install numpy matplotlib jupyter
python -c "import sys, numpy as np; print(sys.executable); a = np.array([1, 2, 3]); print(np.dot(a, a))"
```

## Verification output

```text
/home/student/The-AI-Forge/.venv/bin/python
14
```

The Python path confirms the virtual environment was active. The dot product is `1×1 + 2×2 + 3×3 = 14`.

## Re-create after a reset

After restoring this repository from GitHub, run these commands from its root. Reopen the terminal after installing `uv` so the command is on `PATH`.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv --python 3.12
source .venv/bin/activate
uv pip install numpy matplotlib jupyter
```

The `.venv/` directory is already excluded by the repository's `.gitignore`; recreate it locally instead of pushing it.

## Not done yet

- The course's official verifier was not run; its script is not in this learning repository.
- Install PyTorch and complete the lesson's language examples.
- Complete the lesson quiz.

## Questions to revisit

- What does each layer of the environment stack provide?
