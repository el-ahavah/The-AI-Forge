# My AI Engineering Journey

This repository documents my journey toward becoming an AI engineer.

## Learning approach

I study concepts, implement them in code, test my understanding, document mistakes, and build projects that apply what I have learned.

## Learning progress

See [LEARNING.md](LEARNING.md) for my curriculum, progress log, and topics that need further review.

Current progress: Phase 0 Lessons 1–12 studied. Lesson 12 Debugging & Profiling quiz: 5/5 (100%, passed); practical exercises are pending. Covered silent AI bugs, Python's pdb debugger, NaN loss, execution-time measurement with time, and TensorBoard. See the [Lesson 12 notes](phases/00-setup-and-tooling/12-debugging-and-profiling/notes.md) and [practical exercise guide](phases/00-setup-and-tooling/12-debugging-and-profiling/exercises/README.md). Lesson 11 Linux for AI quiz: 4/5 (80%, passed). Reviewed Linux filesystem navigation, file operations, permissions, APT package management, processes, disk usage, networking and file transfer, tmux, WSL2, and macOS/Linux differences. Three of five practical exercises are complete: filesystem navigation/file creation, process monitoring with `top`, and disk/cache inspection. The tmux exercise remains pending because tmux is not installed and this account has no sudo privileges; the remote scp/rsync exercise was skipped. See the [Lesson 11 practical exercise guide](phases/00-setup-and-tooling/11-linux-for-ai/exercises/README.md) for evidence and status. See [Lesson 11 notes](phases/00-setup-and-tooling/11-linux-for-ai/notes.md), the [official lesson](phases/00-setup-and-tooling/11-linux-for-ai/docs/en.md), and the [exercise guide](phases/00-setup-and-tooling/11-linux-for-ai/exercises/README.md). Lesson 10 Terminal & Shell quiz: 5/5 (100%); all four practical exercises passed locally (tmux panes, Zsh aliases, training-log analysis, and safe SSH configuration inspection). The quiz covered pipes and redirects, SIGHUP when a terminal closes, persistent tmux sessions, redirecting stdout and stderr to one log, and SSH local port forwarding for remote Jupyter. See [Lesson 10 notes](phases/00-setup-and-tooling/10-terminal-and-shell/notes.md). Lesson 9 Data Management quiz: 4/5 (80%); all five practical exercises completed. Loaded and inspected GLUE MRPC, streamed C4, compared CSV and Parquet storage, and created reproducible 70/15/15 dataset splits with seed 42. See [Lesson 9 notes](phases/00-setup-and-tooling/09-data-management/notes.md) for measured results. Lesson 8 quiz score: 4/4; verified VS Code 1.100.2 (x64), Node.js v26.13.0, Git 2.43.0, and all eight core recommended VS Code extensions. Workspace settings are applied and Python 3.12.3 is selected from the project virtual environment. Pylance diagnostics, Black format-on-save, Ruff linting, Jupyter execution and kernel state, GitLens file history, and VS Code Source Control checks passed. Lesson 7 quiz score: 3/3; Dockerfile and Docker Compose configuration are present, but container exercises remain pending because Docker is not installed. Lesson 6 quiz score: 3/3; environment isolation, editable installation, lockfile check, and temporary user-site package exercise are complete. Lesson 5's local exercises and Kaggle GPU run are complete. Lesson 4's live API request is pending an API key. Reviews for uv and GPU timing synchronization are cleared. See [LEARNING.md](LEARNING.md) for the full progress log and [my_journal.md](my_journal.md) for setup instructions and lesson notes.

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
