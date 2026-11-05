#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/../../../.." && pwd)"
VENV_DIR="$REPO_ROOT/.venv"
CORE_PACKAGES=(numpy matplotlib jupyter scikit-learn pandas)

cd "$REPO_ROOT"
echo "Repository: $REPO_ROOT"

if command -v uv >/dev/null 2>&1; then
    PYTHON_CMD=python3
else
    PYTHON_CMD=python3
    echo "uv not found; using Python's built-in venv and pip."
fi

if [ ! -d "$VENV_DIR" ]; then
    "$PYTHON_CMD" -m venv "$VENV_DIR"
fi

source "$VENV_DIR/bin/activate"
echo "Python: $(command -v python)"

if command -v uv >/dev/null 2>&1; then
    uv pip install "${CORE_PACKAGES[@]}"
else
    python -m pip install "${CORE_PACKAGES[@]}"
fi

python - <<'PY'
import importlib

modules = {
    "numpy": "numpy",
    "matplotlib": "matplotlib",
    "jupyter": "jupyter_core",
    "scikit-learn": "sklearn",
    "pandas": "pandas",
}
for package, module in modules.items():
    loaded = importlib.import_module(module)
    print(f"[PASS] {package}: {loaded.__version__}")

import numpy as np
a = np.random.randn(3, 3)
b = np.random.randn(3, 3)
print(f"[PASS] NumPy matrix multiply: {a.shape} @ {b.shape} = {(a @ b).shape}")

try:
    import torch
except ImportError:
    print("[INFO] PyTorch not installed; add it when a later lesson needs it.")
else:
    print(f"[INFO] PyTorch {torch.__version__}; CUDA available: {torch.cuda.is_available()}")
PY

echo "Environment setup checks passed. Activate it with: source .venv/bin/activate"
