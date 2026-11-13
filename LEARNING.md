# My AI Engineering Path
<!-- Managed by the ai-engineering-from-scratch learning skills.
     Repo: https://github.com/rohitg00/ai-engineering-from-scratch -->

## Mission
Become competent in AI engineering and build my personal model.

## Placement
- Date: 2026-10-30
- Score: 3/10 (Math & Statistics: 1/2; Classical ML: 2/2; Deep Learning: 0/2; NLP & Transformers: 0/2; Applied AI: 0/2)
- Entry point: Phase 0: Setup & Tooling
- Pace: ~30 hours/week

## Path
| Phase | Name | Status | Est. hours |
|-------|------|--------|------------|
| 0 | Setup & Tooling | Do | 16 |
| 1 | Math Foundations | Do | 23 |
| 2 | ML Fundamentals | Do | 26 |
| 3 | Deep Learning Core | Do | 15 |
| 4 | Computer Vision | Do | 27 |
| 5 | NLP — Foundations to Advanced | Do | 30 |
| 6 | Speech & Audio | Do | 18 |
| 7 | Transformers Deep Dive | Do | 14 |
| 8 | Generative AI | Do | 14 |
| 9 | Reinforcement Learning | Do | 13 |
| 10 | LLMs from Scratch | Do | 26 |
| 11 | LLM Engineering | Do | 19 |
| 12 | Multimodal AI | Do | 65 |
| 13 | Tools & Protocols | Do | 76 |
| 14 | Agent Engineering | Do | 55 |
| 15 | Autonomous Systems | Do | 20 |
| 16 | Multi-Agent & Swarms | Do | 28 |
| 17 | Infrastructure & Production | Do | 34 |
| 18 | Ethics, Safety & Alignment | Do | 31 |
| 19 | Capstone Projects | Do | 620 |

## Progress log
| Date | Lesson | Quiz | Note |
|------|--------|------|------|
| 2026-11-01 | 00-setup-and-tooling/01-dev-environment | 2/3 | Python environment, NumPy check, verifier, CPU PyTorch import, and Hello World examples in Python, TypeScript, Rust, and Julia are complete. Reviewed `uv` on 2026-11-02 and recalled its package install/resolve role. |
| 2026-11-02 | 00-setup-and-tooling/02-git-and-collaboration | 3/3 | Quiz and practical exercises complete: course fork/branch pushed, Git history reviewed, and checkpoint ignore patterns verified with temporary files. |
| 2026-11-02 | 00-setup-and-tooling/03-gpu-setup-and-cloud | 2/3 | Verified Colab Tesla T4 with PyTorch, benchmarked matrix multiplication (26x on second run), and estimated 7.8B fp16 parameters; reviewed GPU asynchrony and timing synchronization. |
| 2026-11-03 | 00-setup-and-tooling/04-apis-and-keys | 3/3 | Learned to keep API keys in environment variables, compared SDK and raw HTTP requests, and identified authentication and rate-limit errors. No live request made because no API key is set up. |
| 2026-11-04 | 00-setup-and-tooling/05-jupyter-notebooks | 3/3 | Quiz complete; locally ran the timing and CSV/plot exercises and confirmed Restart & Run All succeeds. Ran `notebook_tips.py` in Kaggle with CUDA available. |
| 2026-11-05 | 00-setup-and-tooling/06-python-environments | 3/3 | Setup checks passed; verified NumPy isolation (1.26.4 vs 2.5.4), installed the editable PyTorch/Anthropic project with a CPU wheel and checked its lockfile, then installed and removed a package in a temporary user-site. |
| 2026-11-09 | 00-setup-and-tooling/07-docker-for-ai | 3/3 | Explained Docker images versus Python environments, image layers, host GPU drivers, volume mounts, and Compose service DNS; container exercises remain unrun because Docker is unavailable in this workspace. |
| 2026-11-09 | 00-setup-and-tooling/08-editor-setup | 4/4 | Verified VS Code 1.100.2, Node.js v26.13.0, Git 2.43.0, all eight core extensions, workspace settings, and Python 3.12.3 virtual environment; Pylance, Black, Ruff, Jupyter kernel execution/state, GitLens file history, and Source Control checks passed. Remote SSH connection test remains optional without a remote host. |
| 2026-11-10 | 00-setup-and-tooling/09-data-management | 4/5 | Completed all five practical exercises: GLUE MRPC loading and schema inspection; C4 streaming (4,436 examples in 18.36 seconds); CSV vs Parquet comparison (608.71 KB vs 893.77 KB, with all 3,668 rows restored); and reproducible 70/15/15 splits (2,567/550/551) using seed 42. Reviewed the Hugging Face Hub's role in hosting and sharing datasets, models, and ML resources. |
| 2026-11-10 | 00-setup-and-tooling/10-terminal-and-shell | 5/5 | Quiz (100%) and all four practical exercises passed: tmux multi-pane lab, shell aliases loaded and verified in Zsh, training-log analysis with grep/tail/awk, and safe SSH configuration inspection with ssh -G. The aliases installer initially targeted Bash; configured the aliases in ~/.zshrc after confirming Zsh is the active shell. |
| 2026-11-11 | 00-setup-and-tooling/11-linux-for-ai | 4/5 | Linux for AI quiz passed (80%). Completed filesystem/file creation, process monitoring with top, and disk/cache inspection. tmux remains pending because it is not installed and the account has no sudo privileges; remote scp/rsync exercise was skipped. Missed quiz topic: sudo runs commands with administrator privileges. |
| 2026-11-11 | 00-setup-and-tooling/12-debugging-and-profiling | 5/5 | Debugging & Profiling quiz passed (100%). Completed cProfile, tracemalloc, and pdb exercises; debugging toolkit partially ran (PyTorch diagnostics unavailable); TensorBoard blocked because TensorBoard and PyTorch are not installed. |
| 2026-11-12 | 00-setup-and-tooling/13-python-for-ai-engineering | 6/6 | Quiz passed (100%); completed all seven practical exercises; verified reproducible splits, generator exhaustion, safe mutable defaults, and training-only standardization. Added positive-repeat validation to `best_time()` with a regression test; final suite passed all 15 tests. |
| 2026-11-13 | 01-math-foundations/01-linear-algebra-intuition | Pre-lesson: 0/2 | Began Segment 1: learned vector components, 2D vectors, direction, and magnitude. Corrected the magnitude calculation for [6, 8] from 5.29 to 10. Sample magnitude function ran successfully in the user's local environment and printed 5.0, 10.0, and 13.0 for [3, 4], [6, 8], and [5, 12]. Official practical and post-lesson quiz remain pending. |

## Review queue
<empty for now; no lesson currently requires a formal review based on the below-70% threshold>
