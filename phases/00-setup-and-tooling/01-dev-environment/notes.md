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
/home/student/ai/The-AI-Forge/.venv/bin/python
14
```

The Python path confirms the virtual environment was active. The dot product is `1×1 + 2×2 + 3×3 = 14`.

## Course verifier

Ran from the root of the full course checkout:

```bash
python3 phases/00-setup-and-tooling/01-dev-environment/code/verify.py --route beginner
```

Result: **2/2 required checks passed** — Python 3.12.3 at `/usr/bin/python3` and Git 2.43.0 at `/usr/bin/git`. The verifier skipped later tools because they are not required to start the beginner route.

## PyTorch

Installed the CPU build with:

```bash
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

Verified it with the project's interpreter:

```bash
/home/student/ai/The-AI-Forge/.venv/bin/python -c "import torch; print(torch.__version__); print('CUDA available:', torch.cuda.is_available())"
```

Output:

```text
2.15.0+cpu
CUDA available: False
```

`CUDA available: False` is expected because this is the CPU-only build.

## Lesson quiz

Score: **2/3**. Review how `uv` installs and resolves Python packages.

## Re-create after a reset

After restoring this repository from GitHub, run these commands from its root. Reopen the terminal after installing `uv` so the command is on `PATH`.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv --python 3.12
source .venv/bin/activate
uv pip install numpy matplotlib jupyter
```

The `.venv/` directory is already excluded by the repository's `.gitignore`; recreate it locally instead of pushing it.

## Exercise files and rerun commands

All four Hello World files are in `codes/`; `outputs/hello.txt` records `hello world` for each. From the repository root, rerun them with:

```bash
.venv/bin/python phases/00-setup-and-tooling/01-dev-environment/codes/hello.py
npx tsx phases/00-setup-and-tooling/01-dev-environment/codes/hello.ts
rustc phases/00-setup-and-tooling/01-dev-environment/codes/hello.rs -o /tmp/hello-rust && /tmp/hello-rust
julia phases/00-setup-and-tooling/01-dev-environment/codes/hello.jl
```

Node.js does not run `.ts` files directly, so the TypeScript example uses `tsx`.

## Follow-up

- Review `uv` package management, the topic missed in the quiz.
- GPU setup is optional; the CPU PyTorch build works for lessons that do not require GPU acceleration.

## Questions to revisit

- What does each layer of the environment stack provide?
