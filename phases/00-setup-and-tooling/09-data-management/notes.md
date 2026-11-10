# Data Management

Course lesson: [Data Management](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/09-data-management/docs/en.md)

**Date studied:** 2026-11-10  
**Quiz:** Pending

## What I learned

- A dataset is a collection of examples used to develop or evaluate an AI system.
- The Hugging Face `datasets` library helps download, inspect, stream, cache, and convert datasets.
- Streaming reads examples as needed instead of downloading the entire dataset first.
- CSV is easy to read, JSON is useful for structured interchange, Parquet is efficient for analytical storage, and Arrow is used internally for fast in-memory data.
- Training data teaches the model, validation data helps guide choices, and test data is held back for final evaluation.
- A fixed random seed makes data splitting repeatable when the input data and procedure stay the same.
- Git should not store large generated datasets or model weights directly. Depending on the project, use `.gitignore`, Git LFS, or DVC.

## Practical work

The lesson utility is in `code/data_utils.py`. It includes functions for inspecting datasets, streaming rows, converting formats, making deterministic splits, loading saved formats, downloading a model file, and checking the local cache.

The course script downloads data from the Hugging Face Hub. Run it only when the environment has the required packages and internet access:

```bash
python -m pip install datasets huggingface_hub
python phases/00-setup-and-tooling/09-data-management/code/data_utils.py
```

## Exercise evidence

| Exercise | Evidence to record | Status |
|---|---|---|
| Load GLUE MRPC and inspect five examples | Dataset fields and five sample pairs | Pending |
| Stream C4 for ten seconds | Number of examples processed and elapsed time | Pending |
| Compare CSV and Parquet | File sizes and row count after reloading Parquet | Pending |
| Create 70/15/15 splits | Split sizes, total row count, and repeatability with the same seed | Pending |

## Quiz and review

- Quiz score: Pending
- Topics to review: To be determined from quiz answers.

## Artifacts

- `docs/en.md` — course lesson guide.
- `code/data_utils.py` — reusable dataset utilities.
- `outputs/prompt-data-helper.md` — prompt for choosing datasets.
