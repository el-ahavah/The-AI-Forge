# My AI Engineering Journey

This repository documents my journey toward becoming an AI engineer.

## Learning approach

I study concepts, implement them in code, test my understanding, document mistakes, and build projects that apply what I have learned.

## Learning progress

See [LEARNING.md](LEARNING.md) for my curriculum, progress log, and topics that need further review.

Current progress: Phase 0 Lessons 1–9 studied. Lesson 9 Data Management quiz: 4/5 (80%); all five practical exercises completed. Loaded and inspected GLUE MRPC, examined its schema, streamed C4, compared CSV and Parquet storage, and created reproducible 70/15/15 dataset splits with seed 42. See [Lesson 9 notes](phases/00-setup-and-tooling/09-data-management/notes.md) for measured results. Lesson 8 quiz score: 4/4; verified VS Code 1.100.2 (x64), Node.js v26.13.0, Git 2.43.0, and all eight core recommended VS Code extensions. Workspace settings are applied and Python 3.12.3 is selected from the project virtual environment. Pylance diagnostics, Black format-on-save, Ruff linting, Jupyter execution and kernel state, GitLens file history, and VS Code Source Control checks passed. Lesson 8 notes and test notebook are committed and pushed; the working tree is clean. Remote SSH connection testing remains optional without a remote host. Lesson 7 quiz score: 3/3; added the Dockerfile and Docker Compose configuration. Container exercises remain pending because Docker is not installed in this workspace. Lesson 6 quiz score: 3/3; setup checks, NumPy environment isolation, editable PyTorch/Anthropic install, lockfile check, and temporary user-site install/uninstall exercise are complete. The local project uses CPU-only PyTorch; Kaggle previously confirmed CUDA access. Lesson 5's local exercises and Kaggle GPU run are complete. Lesson 4's live API request is pending an API key. Reviews for uv and GPU timing synchronization are cleared. See [my_journal.md](my_journal.md) for setup instructions and lesson notes.

## Repository contents

- `LEARNING.md` — My learning plan and course progress.
- `my_journal.md` — Tutor setup and plain-language notes from my lessons.
- `notes/` — Explanations written in my own words.
- `implementations/` — My lesson implementations.
- `tests/` — Tests for my code.
- `projects/` — Projects built using what I learn.
- `phases/00-setup-and-tooling/` — Phase 0 lesson notes, code, notebooks, and outputs. Lesson 5 artifacts are under `05-jupyter-notebooks/`.

## Learning principle

Understand the concept, implement it, test it, and document the evidence.
