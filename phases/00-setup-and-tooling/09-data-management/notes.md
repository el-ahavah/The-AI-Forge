# Data Management

Course lesson: [Data Management](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/09-data-management/docs/en.md)

**Date studied:** 2026-11-10  
**Quiz:** Completed — 4/5 (80%)  
**Practical progress:** Exercises 1 and 2 completed

## What I learned

- A dataset is a collection of examples used to develop or evaluate an AI system.
- The Hugging Face `datasets` library helps download, inspect, stream, cache, and convert datasets.
- The Hugging Face Hub hosts and shares datasets, models, and other machine-learning resources.
- Streaming reads examples as needed instead of downloading the entire dataset first.
- CSV is easy to read, JSON is useful for structured interchange, Parquet is efficient for analytical storage, and Arrow is used internally for fast in-memory data.
- Training data teaches the model, validation data helps guide choices, and test data is held back for final evaluation.
- A fixed random seed makes data splitting repeatable when the input data and procedure stay the same.
- Git should not store large generated datasets or model weights directly. Depending on the project, use `.gitignore`, Git LFS, or DVC.

## Quiz result

**Score: 4/5 (80%).**

| Question | Topic | Result |
|---|---|---|
| 1 | Purpose of train/validation/test splits | Correct |
| 2 | Purpose of the Hugging Face Hub | Incorrect |
| 3 | Parquet versus CSV | Correct |
| 4 | Dataset streaming | Correct |
| 5 | When to use DVC | Correct |

**Review point:** The Hugging Face Hub is for hosting and sharing datasets, models, and machine-learning resources. GitHub is primarily used for hosting and version-controlling source code.

## Practical work

The lesson utility is in `code/data_utils.py`. It includes functions for inspecting datasets, streaming rows, converting formats, making deterministic splits, loading saved formats, downloading a model file, and checking the local cache.

The course script downloads data from the Hugging Face Hub. Run it only when the environment has the required packages and internet access:

```bash
python -m pip install datasets huggingface_hub
python phases/00-setup-and-tooling/09-data-management/code/data_utils.py
```

## Exercise evidence

| Exercise | Evidence | Status |
|---|---|---|
| Load GLUE MRPC and inspect five examples | Loaded `nyu-mll/glue` with the `mrpc` configuration; inspected five sentence pairs and their labels | Completed |
| Inspect dataset structure | Confirmed columns `sentence1`, `sentence2`, `label`, `idx`; inspected feature types; verified 3,668 training examples; scored 3/3 on the understanding check | Completed |
| Stream C4 for ten seconds | Number of examples processed and elapsed time | Pending |
| Compare CSV and Parquet | File sizes and row count after reloading Parquet | Pending |
| Create 70/15/15 splits | Split sizes, total row count, and repeatability with the same seed | Pending |

**Environment note:** The short dataset identifier `glue` produced a Hugging Face repository-ID error in this environment. The fully qualified ID `nyu-mll/glue` loaded successfully. An unauthenticated Hub warning appeared, but it did not prevent the public dataset from loading.

## Artifacts

- `docs/en.md` — course lesson guide.
- `code/data_utils.py` — reusable dataset utilities.
- `outputs/prompt-data-helper.md` — prompt for choosing datasets.
