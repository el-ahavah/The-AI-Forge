# Lesson 13: Python for AI Engineering

## Lesson goal

Learn the Python patterns that appear frequently in AI and data projects. We will use the Python standard library to prepare data, split datasets reproducibly, create mini-batches, and measure simple numerical operations.

## Learning objectives

By the end of this lesson, you should be able to:

- Work confidently with lists, tuples, dictionaries, sets, unpacking, slices, and comprehensions.
- Explain object references, shared mutable objects, and mutable default arguments.
- Use functions, type hints, dataclasses, and the `if __name__ == "__main__"` guard.
- Understand iterables, iterators, generators, and why generators are exhausted after use.
- Read and write CSV and JSON files safely.
- Create repeatable train/test splits with a fixed random seed.
- Generate mini-batches without loading all batches into memory.
- Explain why NumPy can process large numerical arrays faster than ordinary Python loops.
- Calculate basic statistics and standardize features without leaking test-set information into training.

## 1. Python objects and collections

A variable is a name that refers to an object. Assigning one list to another variable does not create a copy:

```python
weights = [1, 2, 3]
alias = weights
alias[0] = 99
print(weights)  # [99, 2, 3]
```

Use `list(weights)` or `weights.copy()` when you need a separate list.

Common collections:

| Type | Example | Main use |
|---|---|---|
| list | `[1, 2, 3]` | Ordered, changeable data |
| tuple | `(32, 784)` | Fixed values and records |
| dict | `{"lr": 0.01}` | Key/value configuration |
| set | `{"cat", "dog"}` | Unique values and membership checks |

Avoid creating a matrix with `[[0] * 3] * 2`: both rows refer to the same inner list. Use `[[0] * 3 for _ in range(2)]`.

## 2. Unpacking, slices, and comprehensions

Unpacking assigns several values at once:

```python
height, width = (28, 28)
first, *middle, last = [1, 2, 3, 4]
```

A slice uses `sequence[start:stop:step]`; the stop position is excluded.

Comprehensions provide a concise way to build collections:

```python
squares = [number ** 2 for number in range(5)]
even_squares = [number ** 2 for number in range(10) if number % 2 == 0]
```

A generator expression uses parentheses and produces values lazily:

```python
total = sum(number ** 2 for number in range(1_000_000))
```

## 3. Functions and mutable defaults

Python evaluates default argument values once, when it defines the function. This is dangerous when the default is a list or dictionary:

```python
def add_bad(item, bucket=[]):
    bucket.append(item)
    return bucket
```

Calls to `add_bad` share the same list. Use `None` and create a new list inside the function:

```python
def add_item(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket
```

Use keyword-only arguments when naming an option makes calls clearer. Type hints document expected inputs and outputs, but Python does not enforce them automatically.

## 4. Dataclasses

A dataclass generates common methods such as `__init__` and `__repr__`:

```python
from dataclasses import dataclass, field

@dataclass(frozen=True)
class Record:
    features: tuple[float, ...]
    label: int

@dataclass
class TrainingConfig:
    learning_rate: float = 0.01
    hidden_sizes: list[int] = field(default_factory=lambda: [64, 32])
```

Use `default_factory` for mutable dataclass fields so each instance gets its own list or dictionary.

## 5. Iterators and generators

An iterable can be used in a `for` loop. An iterator produces one item at a time through `next()`. A generator is a convenient way to create an iterator using `yield`.

```python
def countdown(start):
    while start > 0:
        yield start
        start -= 1

numbers = countdown(3)
print(next(numbers))  # 3
print(list(numbers)) # [2, 1]
print(list(numbers)) # []
```

A generator is normally exhausted after one pass. If a training loop needs a fresh pass for each epoch, create a new generator for each epoch.

Generators are useful for large datasets because they do not need to hold every item in memory at once.

## 6. Files, CSV, and JSON

Use `with open(...)` so files are closed automatically. Specify UTF-8 encoding. For CSV, use the `csv` module instead of splitting lines manually; quoted fields can contain commas.

CSV values are read as strings, so convert numeric fields explicitly. JSON supports Python dictionaries, lists, strings, numbers, booleans, and null-like values.

## 7. Reproducible train/test splits

A fixed seed makes a random operation repeatable:

```python
import random

rng = random.Random(42)
indices = list(range(10))
rng.shuffle(indices)
```

Prefer a local `random.Random(seed)` object over changing the global random state. Keep the original dataset unchanged when splitting it.

A correct split should have no overlap: a record must not appear in both training and test data.

## 8. Mini-batches

A mini-batch is a small group of examples processed together. Batching makes it possible to work with a dataset in manageable pieces.

For ten items and a batch size of four, the default result is batch sizes `[4, 4, 2]`. With `drop_last=True`, the final incomplete batch is discarded and the result is `[4, 4]`.

## 9. Statistics and standardization

For values (x_1, ..., x_n):

- Mean: sum of values divided by the number of values.
- Population standard deviation: square root of the mean squared distance from the mean.
- Standardized value: ((x - mean) / standard deviation).

**Important: calculate means and standard deviations from the training split only.** Then use those same training statistics to transform both training and test data. Calculating them using the test data leaks information from the test set into training and can make evaluation misleading.

If a feature has a standard deviation of zero, avoid division by zero; use a safe scale such as 1.

## 10. Why NumPy is faster for large numerical work

A Python list stores references to Python objects. A Python loop performs interpreter work for each element. NumPy arrays store numerical values in a compact block and perform many operations in compiled code.

Vectorization means expressing an operation over an entire array instead of writing a Python loop for every element. NumPy is not automatically better for every tiny task, but it is usually much faster for large numerical arrays.

## 11. Timing and memory

- Use `time.perf_counter()` for elapsed-time measurement.
- Repeat measurements and compare results; a single timing can be noisy.
- Use `tracemalloc` to inspect Python memory allocations.
- Compare equivalent work when benchmarking two implementations.

## Key reminders

1. Assignment does not copy mutable objects.
2. Never use a mutable list or dictionary as a function default.
3. A generator is consumed as you iterate over it.
4. Use a local seeded random generator for reproducibility.
5. Keep training and test data separate.
6. Fit preprocessing statistics on training data only.
7. Use generators to reduce memory use and NumPy for large numerical operations.
