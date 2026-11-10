# Data Management

Course lesson: [Data Management](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/09-data-management/docs/en.md)

**Date studied:** 2026-11-10  
**Quiz:** Completed — 4/5 (80%)  
**Practical progress:** Exercises 1, 2, 3, and 4 completed

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
| Stream C4 for ten seconds | Streamed `allenai/c4` English training split; processed 4,436 examples in 18.36 seconds (about 242 examples/second) after retrieving the first example before timing | Completed, with timing caveat |
| Compare CSV and Parquet | Saved the 3,668-row MRPC training split as CSV (893.77 KB) and Parquet (608.71 KB); Parquet was 285.06 KB (about 31.9%) smaller; reloaded Parquet and verified all 3,668 rows were preserved | Completed |
| Create 70/15/15 splits | Split sizes, total row count, and repeatability with the same seed | Pending |

**CSV/Parquet comparison note:** In this experiment, Parquet used about 31.9% less storage than CSV for the same MRPC training data. Reloading the Parquet file returned 3,668 rows, matching the original dataset. This confirms row-count integrity; it does not by itself compare every field value.

**Streaming timing note:** The target was 10 seconds, but the observed elapsed time was 18.36 seconds. Streaming retrieval can block on remote I/O, and the timer is checked between yielded examples, so the measured duration can exceed the target. The result demonstrates successful streaming, not a strict ten-second benchmark.

**Environment note:** The short dataset identifier `glue` produced a Hugging Face repository-ID error in this environment. The fully qualified ID `nyu-mll/glue` loaded successfully. An unauthenticated Hub warning appeared, but it did not prevent the public dataset from loading.

## Artifacts

- `docs/en.md` — course lesson guide.
- `code/data_utils.py` — reusable dataset utilities.
- `outputs/prompt-data-helper.md` — prompt for choosing datasets.
- `exercises/stream_c4.py` — C4 streaming experiment.
- `exercises/compare_formats.py` — CSV and Parquet comparison experiment.
