"""Small, runnable examples for the Jupyter Notebooks lesson.

Install the dependencies into the active environment before running this file:
    python -m pip install numpy pandas matplotlib

In a notebook, run the functions in separate cells to inspect their values and
render the returned DataFrame and plot inline.
"""

from __future__ import annotations

import random
import time
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def timing_comparison(size: int = 100_000) -> dict[str, float]:
    """Compare Python and NumPy random-number generation for the same size."""
    python_rng = random.Random(42)
    start = time.perf_counter()
    python_values = [python_rng.random() for _ in range(size)]
    python_seconds = time.perf_counter() - start

    numpy_rng = np.random.default_rng(42)
    start = time.perf_counter()
    numpy_values = numpy_rng.random(size)
    numpy_seconds = time.perf_counter() - start

    # Keep both results alive until after timing so both versions do the work.
    assert len(python_values) == len(numpy_values) == size
    return {"python_seconds": python_seconds, "numpy_seconds": numpy_seconds}


def model_dataframe() -> pd.DataFrame:
    """Return a small comparison table suitable for a notebook's rich display."""
    return pd.DataFrame(
        {
            "model": ["Linear", "Random Forest", "Neural Net"],
            "accuracy": [0.72, 0.89, 0.94],
            "training_time_seconds": [0.1, 2.3, 45.6],
        }
    )


def signal_plot(output_path: str | Path = "notebook_plot.png"):
    """Create a deterministic signal-versus-noise plot and save a copy."""
    rng = np.random.default_rng(42)
    x = np.linspace(0, 10, 200)
    signal = np.sin(x)
    noisy_signal = signal + rng.normal(0, 0.2, size=x.size)

    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    axes[0].plot(x, signal, label="signal")
    axes[0].plot(x, noisy_signal, alpha=0.6, label="noisy signal")
    axes[0].set_title("Signal and noise")
    axes[0].legend()
    axes[1].hist(noisy_signal - signal, bins=30, edgecolor="black")
    axes[1].set_title("Noise distribution")
    fig.tight_layout()
    fig.savefig(output_path, dpi=100)
    return fig, axes


def memory_report() -> dict[str, float]:
    """Report array payload sizes; this excludes Python and notebook overhead."""
    arrays = {
        "1K": np.zeros(1_000, dtype=np.float64),
        "100K": np.zeros(100_000, dtype=np.float64),
        "1M": np.zeros(1_000_000, dtype=np.float64),
    }
    return {name: array.nbytes / 1_000_000 for name, array in arrays.items()}


def main() -> None:
    timings = timing_comparison()
    print("Random-number generation for 100,000 values")
    print(f"Python list: {timings['python_seconds']:.4f} s")
    print(f"NumPy:       {timings['numpy_seconds']:.4f} s")

    frame = model_dataframe()
    print("\nModel comparison")
    print(frame.to_string(index=False))

    figure_path = Path("notebook_plot.png")
    signal_plot(figure_path)
    print(f"\nSaved plot to {figure_path}")
    print("Array payload sizes (MB):", memory_report())
    print("In Jupyter, use %timeit for repeated line timings and %%time for one cell run.")


if __name__ == "__main__":
    main()
