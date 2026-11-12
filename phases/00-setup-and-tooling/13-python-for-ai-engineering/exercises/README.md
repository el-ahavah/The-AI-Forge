# Lesson 13 Practical Exercises

Run commands from the root of `The-AI-Forge`. These exercises use Python's standard library; NumPy is discussed as a concept but is not required for the core exercises.

## Check your Python version

```bash
python3 --version
```

The official lesson targets Python 3.11 or newer. Use the project's virtual environment if one is available.

## Exercise 1 — Run the toolkit

```bash
python3 phases/00-setup-and-tooling/13-python-for-ai-engineering/code/main.py
```

Observe the dataset round-trip, split sizes, mini-batch sizes, standardized feature means, timing comparison, and memory comparison.

## Exercise 2 — Run the tests

```bash
python3 -m unittest discover -s phases/00-setup-and-tooling/13-python-for-ai-engineering/code/tests -v
```

All tests should pass. If a test fails, copy the complete error output before changing anything.

## Exercise 3 — Reproducible split

In a Python shell, split the same list twice with the same seed. Confirm both training lists and both test lists are identical. Then change the seed and compare the result.

## Exercise 4 — Generator and batching

Create a generator that yields the squares of numbers from 0 to 9. Convert it to a list twice and observe that the second result is empty. Then create a fresh generator for a second pass.

Also run `batches(range(10), 4)` and confirm the batch sizes are `[4, 4, 2]`.

## Exercise 5 — Mutable default argument

Write a function with a list default, call it twice, and observe that the list is shared. Rewrite it using `None` as the default and verify that each call starts with a new list.

## Exercise 6 — Training-only standardization

Create a small two-feature training dataset and a separate test row. Calculate the training means and standard deviations, standardize the training data, and apply the same statistics to the test row. Do not calculate new statistics from the test row.

## Exercise 7 — Review a Python file

Use the prompt in `outputs/prompt-python-review.md` to review a Python file for shared mutable objects, exhausted generators, missing random seeds, data leakage, unsafe CSV parsing, and inefficient numerical loops.

## Completion record

**Date:** 2026-11-12  
**Status:** All 7 exercises completed and verified.

| Exercise | Result | Evidence |
|---|---|---|
| 1. Run the toolkit | Complete | Python 3.12.3; CSV/JSON round-trip correct; 80 training and 20 test records; zero split overlap; batch sizes of 16; numerical, timing, and memory demonstrations ran. |
| 2. Run the tests | Complete | Initial suite: 14 tests passed. After adding benchmark validation coverage: 15 tests passed. |
| 3. Reproducible split | Complete | Same seed reproduced both splits; a different seed produced a different test split. |
| 4. Generator and batching | Complete | Confirmed generator values 1, 2, 3 and `StopIteration` after exhaustion. Toolkit tests also verified batching behavior. |
| 5. Mutable default argument | Complete | Demonstrated shared-list behavior, then fixed it with a `None` default and a fresh list per call. |
| 6. Training-only standardization | Complete | Fitted the transformation on training rows and applied it unchanged to test data. |
| 7. Review a Python file | Complete | Reviewed `code/main.py` with `outputs/prompt-python-review.md`; added positive-repeat validation to `best_time()` and a regression test. |

**Final verification command:**

```bash
python3 -m unittest discover -s phases/00-setup-and-tooling/13-python-for-ai-engineering/code/tests -v
```

**Final result:** 15 tests passed. The user confirmed the test run passed.

**Review follow-up:** The review also suggested explicit record-shape and CSV/JSON required-field validation. Those additional suggestions remain potential improvements and are not recorded as implemented.

