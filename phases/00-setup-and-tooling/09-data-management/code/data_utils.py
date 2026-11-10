"""Small reusable helpers for loading, inspecting, and saving Hugging Face datasets.

Install dependencies with:
    python -m pip install datasets huggingface_hub
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

try:
    from datasets import Dataset, load_dataset
    from huggingface_hub import hf_hub_download
except ImportError as exc:
    raise SystemExit(
        "Lesson 9 needs the Hugging Face packages. Install them with: "
        "python -m pip install datasets huggingface_hub"
    ) from exc


CACHE_DIR = Path.home() / ".cache" / "huggingface" / "datasets"


def load_and_inspect(
    dataset_name: str, config: str | None = None, split: str = "train"
) -> Any:
    """Load one dataset split and print a useful summary."""
    kwargs: dict[str, Any] = {"path": dataset_name}
    if config:
        kwargs["name"] = config
    if split:
        kwargs["split"] = split

    dataset = load_dataset(**kwargs)
    print(f"Dataset: {dataset_name}")
    print(f"Split: {split}")
    print(f"Rows: {len(dataset)}")
    print(f"Columns: {dataset.column_names}")
    print(f"Features: {dataset.features}")
    if len(dataset):
        print(f"First row: {dataset[0]}")
    return dataset


def stream_dataset(
    dataset_name: str, config: str | None = None, max_rows: int = 5
) -> list[dict[str, Any]]:
    """Read at most max_rows examples without downloading the full dataset."""
    if max_rows < 0:
        raise ValueError("max_rows cannot be negative")

    kwargs: dict[str, Any] = {
        "path": dataset_name,
        "split": "train",
        "streaming": True,
    }
    if config:
        kwargs["name"] = config

    stream = load_dataset(**kwargs)
    rows = []
    for example in stream:
        rows.append(example)
        if len(rows) >= max_rows:
            break

    print(f"Streamed {len(rows)} rows from {dataset_name}")
    return rows


def convert_format(dataset: Any, output_dir: str | Path, name: str) -> dict[str, Path]:
    """Save a dataset as CSV, JSON, and Parquet and report file sizes."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    paths = {
        "csv": output_path / f"{name}.csv",
        "json": output_path / f"{name}.json",
        "parquet": output_path / f"{name}.parquet",
    }
    dataset.to_csv(str(paths["csv"]))
    dataset.to_json(str(paths["json"]))
    dataset.to_parquet(str(paths["parquet"]))

    sizes = {key: path.stat().st_size for key, path in paths.items()}
    print(f"Format comparison for {name}:")
    for format_name, size in sizes.items():
        print(f"  {format_name.upper():8} {size:>10,} bytes")
    if sizes["parquet"]:
        print(f"Parquet/CSV size ratio: {sizes['parquet'] / sizes['csv']:.2%}")
    return paths


def make_splits(
    dataset: Any,
    train_ratio: float = 0.8,
    val_ratio: float = 0.1,
    seed: int = 42,
) -> dict[str, Any]:
    """Create deterministic train/validation/test splits."""
    test_ratio = 1.0 - train_ratio - val_ratio
    if not (0 < train_ratio < 1 and 0 < val_ratio < 1 and test_ratio > 0):
        raise ValueError("train_ratio and val_ratio must be positive and sum to less than 1")

    holdout_ratio = val_ratio + test_ratio
    first = dataset.train_test_split(test_size=holdout_ratio, seed=seed)
    holdout = first["test"]

    # Split the holdout so its validation/test proportions match the requested ratios.
    test_fraction_of_holdout = test_ratio / holdout_ratio
    second = holdout.train_test_split(test_size=test_fraction_of_holdout, seed=seed)
    splits = {"train": first["train"], "val": second["train"], "test": second["test"]}

    total = len(dataset)
    print(f"Splits (seed={seed}):")
    for name, subset in splits.items():
        print(f"  {name:5} {len(subset):>6} ({len(subset) / total:.1%})")
    assert sum(len(part) for part in splits.values()) == total
    return splits


def download_model_file(repo_id: str, filename: str) -> Path:
    """Download one file from a Hugging Face model repository into the HF cache."""
    path = Path(hf_hub_download(repo_id=repo_id, filename=filename))
    print(f"Downloaded {filename} from {repo_id}")
    print(f"Path: {path}")
    print(f"Size: {path.stat().st_size:,} bytes")
    return path


def cache_summary() -> None:
    """Print a summary of the local Hugging Face dataset cache, if present."""
    if not CACHE_DIR.exists():
        print("No Hugging Face dataset cache found yet.")
        return

    files = [path for path in CACHE_DIR.rglob("*") if path.is_file()]
    total_size = sum(path.stat().st_size for path in files)
    print(f"Dataset cache: {CACHE_DIR}")
    print(f"Files: {len(files)}")
    print(f"Total size: {total_size / (1024 * 1024):.1f} MB")


def load_from_parquet(path: str | Path) -> Any:
    dataset = Dataset.from_parquet(str(path))
    print(f"Loaded {len(dataset)} rows from {path}")
    return dataset


def load_from_csv(path: str | Path) -> Any:
    dataset = Dataset.from_csv(str(path))
    print(f"Loaded {len(dataset)} rows from {path}")
    return dataset


def load_from_json(path: str | Path) -> Any:
    dataset = Dataset.from_json(str(path))
    print(f"Loaded {len(dataset)} rows from {path}")
    return dataset


def fingerprint(dataset: Any, num_rows: int = 100) -> str:
    """Return a short SHA-256 digest for a deterministic sample of rows."""
    if num_rows < 0:
        raise ValueError("num_rows cannot be negative")
    sample = dataset.select(range(min(num_rows, len(dataset))))
    encoded = json.dumps(list(sample), sort_keys=True, default=str).encode("utf-8")
    digest = hashlib.sha256(encoded).hexdigest()[:16]
    print(f"Dataset fingerprint (first {min(num_rows, len(dataset))} rows): {digest}")
    return digest


if __name__ == "__main__":
    print("=" * 60)
    print("Lesson 9: Data Management Utility")
    print("=" * 60)

    dataset = load_and_inspect(
        "cornell-movie-review-data/rotten_tomatoes", split="train"
    )
    rows = stream_dataset(
        "cornell-movie-review-data/rotten_tomatoes", max_rows=3
    )
    for row in rows:
        print(f"  {row['text'][:80]}...")

    sample = dataset.select(range(min(500, len(dataset))))
    paths = convert_format(sample, "/tmp/data_utils_demo", "rotten_tomatoes_sample")
    splits = make_splits(sample, train_ratio=0.8, val_ratio=0.1, seed=42)
    restored = load_from_parquet(paths["parquet"])
    print(f"Reloaded columns: {restored.column_names}")
    print(f"Fingerprint: {fingerprint(dataset)}")
    cache_summary()

    print("\nAll data management checks completed.")
