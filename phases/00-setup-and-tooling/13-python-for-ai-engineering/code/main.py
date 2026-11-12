"""Small standard-library toolkit for the Python for AI Engineering lesson."""

from __future__ import annotations

import csv
import json
import math
import random
import time
import tracemalloc
from collections.abc import Iterable, Iterator, Sequence
from dataclasses import dataclass, field
from itertools import islice
from pathlib import Path
from tempfile import TemporaryDirectory


@dataclass(frozen=True)
class Record:
    features: tuple[float, ...]
    label: int


@dataclass
class TrainingConfig:
    learning_rate: float = 0.01
    hidden_sizes: list[int] = field(default_factory=lambda: [64, 32])


def make_dataset(count: int, seed: int = 42) -> list[Record]:
    rng = random.Random(seed)
    records = []
    for index in range(count):
        label = index % 2
        center = 2.0 if label == 0 else 5.0
        features = (rng.gauss(center, 1.0), rng.gauss(center * 10, 5.0))
        records.append(Record(features, label))
    return records


def save_records(records: Sequence[Record], path: str | Path) -> Path:
    path = Path(path)
    rows = [{"x1": row.features[0], "x2": row.features[1], "label": row.label} for row in records]
    if not rows:
        raise ValueError("cannot save an empty dataset")
    if path.suffix == ".json":
        path.write_text(json.dumps(rows, indent=2), encoding="utf-8")
    elif path.suffix == ".csv":
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=["x1", "x2", "label"])
            writer.writeheader()
            writer.writerows(rows)
    else:
        raise ValueError(f"unsupported file type: {path.suffix}")
    return path


def load_records(path: str | Path) -> list[Record]:
    path = Path(path)
    if path.suffix == ".json":
        rows = json.loads(path.read_text(encoding="utf-8"))
    elif path.suffix == ".csv":
        with path.open("r", newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
    else:
        raise ValueError(f"unsupported file type: {path.suffix}")
    return [Record((float(row["x1"]), float(row["x2"])), int(row["label"])) for row in rows]


def train_test_split(
    items: Sequence, test_fraction: float = 0.2, seed: int = 42
) -> tuple[list, list]:
    if not 0 < test_fraction < 1:
        raise ValueError("test_fraction must be between 0 and 1")
    if len(items) < 2:
        raise ValueError("at least two items are required")
    indices = list(range(len(items)))
    random.Random(seed).shuffle(indices)
    test_count = min(max(1, round(len(items) * test_fraction)), len(items) - 1)
    test = [items[index] for index in indices[:test_count]]
    train = [items[index] for index in indices[test_count:]]
    return train, test


def batches(items: Iterable, batch_size: int, drop_last: bool = False) -> Iterator[list]:
    if batch_size < 1:
        raise ValueError("batch_size must be at least 1")
    iterator = iter(items)
    while batch := list(islice(iterator, batch_size)):
        if drop_last and len(batch) < batch_size:
            break
        yield batch


def mean(values: Sequence[float]) -> float:
    if not values:
        raise ValueError("mean requires at least one value")
    return sum(values) / len(values)


def std(values: Sequence[float]) -> float:
    average = mean(values)
    return math.sqrt(sum((value - average) ** 2 for value in values) / len(values))


def fit_standardizer(training_rows: Sequence[Sequence[float]]):
    if not training_rows:
        raise ValueError("training_rows cannot be empty")
    columns = list(zip(*training_rows, strict=True))
    means = [mean(column) for column in columns]
    scales = [std(column) or 1.0 for column in columns]

    def transform(row: Sequence[float]) -> list[float]:
        if len(row) != len(means):
            raise ValueError("row has an unexpected number of features")
        return [(value - avg) / scale for value, avg, scale in zip(row, means, scales, strict=True)]

    return transform


def dot(a: Sequence[float], b: Sequence[float]) -> float:
    return sum(x * y for x, y in zip(a, b, strict=True))


def best_time(function, *args, repeats: int = 5) -> float:
    if repeats < 1:
        raise ValueError("repeats must be at least 1")

    measurements = []
    for _ in range(repeats):
        start = time.perf_counter()
        function(*args)
        measurements.append(time.perf_counter() - start)
    return min(measurements)


def peak_memory(function) -> int:
    tracemalloc.start()
    try:
        function()
        return tracemalloc.get_traced_memory()[1]
    finally:
        tracemalloc.stop()


def sum_squares_list(count: int) -> int:
    return sum([number * number for number in range(count)])


def sum_squares_generator(count: int) -> int:
    return sum(number * number for number in range(count))


def run_demo() -> None:
    records = make_dataset(100)
    with TemporaryDirectory() as folder:
        csv_path = save_records(records, Path(folder) / "records.csv")
        json_path = save_records(records, Path(folder) / "records.json")
        csv_records = load_records(csv_path)
        json_records = load_records(json_path)

    train, test = train_test_split(records, seed=42)
    transform = fit_standardizer([record.features for record in train])
    scaled_train = [transform(record.features) for record in train]
    scaled_test = [transform(record.features) for record in test]

    print("Python for AI Engineering toolkit")
    print(f"CSV and JSON round-trip correct: {csv_records == records and json_records == records}")
    print(f"Training records: {len(train)}; test records: {len(test)}")
    print(f"Overlap between splits: {len(set(train) & set(test))}")
    print(f"Batch sizes: {[len(batch) for batch in batches(scaled_train, 16)]}")
    print(f"First standardized test row: {[round(value, 3) for value in scaled_test[0]]}")
    print(f"Dot product: {dot([1.0, 2.0], [3.0, 4.0])}")
    print(f"List and generator totals match: {sum_squares_list(1000) == sum_squares_generator(1000)}")
    print(f"Best list-sum time: {best_time(sum_squares_list, 100_000) * 1000:.2f} ms")
    print(f"Peak list memory: {peak_memory(lambda: sum_squares_list(100_000)):,} bytes")
    print(f"Peak generator memory: {peak_memory(lambda: sum_squares_generator(100_000)):,} bytes")


if __name__ == "__main__":
    run_demo()
