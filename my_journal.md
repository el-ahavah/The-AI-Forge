# My AI Engineering Learning Journal

This journal explains what I am learning in plain language and keeps the useful details close by. `LEARNING.md` remains the course tracker for lesson order, quiz scores, and review topics. This file adds explanations, setup instructions, and personal notes as I move through the course.

## Install the AI tutor for AI Engineering from Scratch

The tutor is a set of skills that teaches lessons, gives quizzes, and reads the course plan in `LEARNING.md`. The course recommends installing its skills with the Skills CLI. A course clone is optional for installing or reading lessons, but useful when I want to run lesson code and labs locally.

### Step 1: Open a terminal in the project

Open a terminal application. Check its current folder with:

```bash
pwd
```

For this workspace, the expected result is `/home/student/ai/The-AI-Forge`.

### Step 2: Check Node.js and `npx`

Run:

```bash
node --version
npx --version
```

Both commands should print version numbers. `npx` is included with npm, which is included with Node.js. No separate global installation of the Skills CLI is required.

### Step 3: Install Node.js if either check failed

For Linux or macOS using zsh, install `nvm` and the Node.js long-term support release:

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.8/install.sh | bash
source ~/.zshrc
nvm install --lts
```

Then verify again:

```bash
node --version
npx --version
```

If `source ~/.zshrc` reports that the file is missing, close and reopen the terminal, then run the checks. On Windows, install WSL 2 with Ubuntu from PowerShell:

```powershell
wsl --install -d Ubuntu-24.04
```

After Ubuntu opens, use the Linux commands above. The nvm command is from the [official nvm instructions](https://github.com/nvm-sh/nvm); update its version if that page publishes a newer install command.

### Step 4: Install the course tutor skills

Run this in the terminal:

```bash
npx skills add rohitg00/ai-engineering-from-scratch
```

When prompted, choose **Codex** as the agent. Choose **project** scope to install the skills for this repository, or **user/global** scope to use them across projects. Selecting those choices happens in the installer's interactive menu; there is no additional command to enter. Follow the displayed prompts and confirm the choices.

### Step 5: Confirm the skills are present

For a project installation in this repository, check for the tutor files:

```bash
ls .agents/skills/learn/SKILL.md .agents/skills/start-learning/SKILL.md
```

If the installer chose a different scope, it prints the destination. If Codex does not show newly installed skills, close and reopen the workspace or start a new Codex session.

The course skills are already present in this workspace under `.agents/skills/`, so I do not need to reinstall them here.

### Step 6: (Optional) Clone the course to run code and labs

Skip this step if a course checkout is already open. Otherwise run:

```bash
git clone https://github.com/rohitg00/ai-engineering-from-scratch.git
cd ai-engineering-from-scratch
```

### Step 7: Start or continue learning in Codex

Enter these skill names in the Codex chat, not in the terminal:

```text
start-learning
learn
course-guide dot products
```

Use `start-learning` to create a plan, `learn` to teach the next lesson from `LEARNING.md`, or `course-guide` with a topic to find a lesson. I already have a plan, so my next action is `learn`.

To update installed skills later, run this in the terminal:

```bash
npx skills update
```

### Step 8: Keep the learning files organized

- `LEARNING.md` tracks phase statuses, lesson progress, quiz scores, and review topics.
- `my_journal.md` keeps setup instructions and plain-language lesson explanations.
- `README.md` links to the learning files and summarizes current progress.

After every completed lesson, automatically update `LEARNING.md` with the score and review topics, add a plain-language summary here, and refresh the README progress summary when it changes. If a separate artifact or file is needed, explain its purpose and exact path before creating it.

## Where I am starting

My study plan starts at **Phase 0: Setup & Tooling**. Lessons 1–7 are studied: I set up the development environment, practiced Git collaboration, used a Colab T4 GPU, learned API keys and requests, completed the Jupyter notebook lesson, practiced Python environment isolation, and learned how Docker packages AI environments. The `uv` and GPU timing reviews are cleared. Lesson 4's live API request is pending an API key. Lesson 5's quiz score is 3/3; I ran its timing and CSV/plot exercises locally in a separate notebook, confirmed Restart & Run All completed without errors, then ran `notebook_tips.py` in Kaggle and confirmed PyTorch CUDA availability. Lesson 6's quiz score is 3/3 and all four listed exercises are complete; the local editable project uses CPU-only PyTorch, and the Kaggle GPU check from Lesson 5 confirmed CUDA access. Lesson 7's quiz score is 3/3. Its Dockerfile and Compose configuration are in `phases/00-setup-and-tooling/07-docker-for-ai/code/`, with exercise evidence tracked in that lesson's `notes.md`; Docker is unavailable in this workspace, so the container exercises remain pending. Next is **Editor Setup**, then the remaining Phase 0 lessons before Phase 1, **Math Foundations**.

## Learning record

### Phase 0 · Lesson 1: Dev Environment

**Started:** 2026-10-31

**Completed:** 2026-11-01
**Quiz:** 2/3  
**Review:** `uv` package management reviewed on 2026-11-02.

**Exercise status:** The Python virtual environment, NumPy dot-product check, course verifier, CPU PyTorch import, and Hello World examples in all four lesson languages are complete. The example files are under `phases/00-setup-and-tooling/01-dev-environment/codes/`; the output note is at `phases/00-setup-and-tooling/01-dev-environment/outputs/hello.txt` and records `hello world` for all four.

To rerun all four examples from the repository root:

```bash
.venv/bin/python phases/00-setup-and-tooling/01-dev-environment/codes/hello.py
npx tsx phases/00-setup-and-tooling/01-dev-environment/codes/hello.ts
rustc phases/00-setup-and-tooling/01-dev-environment/codes/hello.rs -o /tmp/hello-rust && /tmp/hello-rust
julia phases/00-setup-and-tooling/01-dev-environment/codes/hello.jl
```

Each example prints `hello world`. TypeScript uses `tsx` because Node.js does not run `.ts` files directly.

### Phase 0 · Lesson 2: Git & Collaboration

**Date:** 2026-11-02

**Quiz:** 3/3

**Review note:** Nothing flagged by this quiz. The earlier `uv` review from Lesson 1 was cleared on 2026-11-02.

Git moves selected changes from the working directory to the staging area with `git add`, saves a local snapshot with `git commit`, and sends committed changes to a remote with `git push`. A branch lets me make commits on an isolated line of work; merging applies those changes to another branch. `git log --oneline` gives a compact view of commit history.

**Checkpoint ignore patterns:** These are present in this repository's `.gitignore`:

```gitignore
*.pt
*.pth
*.safetensors
```

**Hands-on status:** All three practical exercises are complete. The `.gitignore` checkpoint patterns were checked with temporary `.pt`, `.pth`, and `.safetensors` files, and the temporary files were removed. Git history was reviewed with `git log` and `git show --stat`. In `/home/student/ai/ai-engineering-from-scratch`, `origin` points to my fork, `upstream` points to the maintainers' repository, and branch `my-progress` tracks `origin/my-progress`. The pushed commit is `e6a95f699 docs: record course progress`.

Detailed commands and evidence are in [Git & Collaboration notes](phases/00-setup-and-tooling/02-git-and-collaboration/notes.md).

Useful commands for the remaining practice:

```bash
git -C /home/student/ai/ai-engineering-from-scratch log --oneline
git -C /home/student/ai/ai-engineering-from-scratch log --oneline -- phases/00-setup-and-tooling
```

These display the course's complete compact history and then the commits affecting Phase 0.

I inspected commit `f6472e3cd` with:

```bash
git -C /home/student/ai/ai-engineering-from-scratch show --stat f6472e3cd
```

It changed `phases/00-setup-and-tooling/01-dev-environment/code/main.rs` with 19 insertions and 8 deletions. The commit message says it centralized repeated `Check` defaults in a constructor.

**PyTorch install and verification:** The CPU build installed and imported successfully. `CUDA available: False` is expected for this CPU-only build. The install command used was:

```bash
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

The successful import check used this project's interpreter:

```bash
/home/student/ai/The-AI-Forge/.venv/bin/python -c "import torch; print(torch.__version__); print('CUDA available:', torch.cuda.is_available())"
```

Output: `2.15.0+cpu`; `CUDA available: False`.

**Verifier command:** Run from the root of the full course checkout:

```bash
python3 phases/00-setup-and-tooling/01-dev-environment/code/verify.py --route beginner
```

**Verifier result:** 2/2 required checks passed — Python 3.12.3 at `/usr/bin/python3` and Git 2.43.0 at `/usr/bin/git`. The verifier skipped later-tool checks because they are not required to start the beginner route.

An AI development setup has layers. The system foundation (operating system, shell, and drivers) supports package managers; package managers support language runtimes and their packages; AI libraries such as NumPy and PyTorch sit on top. If Python itself is missing, the issue is with the language runtime. If Python is present but a package cannot be installed, the package manager and package compatibility may need checking.

A Python virtual environment, such as `.venv`, keeps one project's installed packages separate from other projects. The value of `sys.executable` tells me which Python interpreter is running. In my setup it pointed into `.venv`, which confirmed the project environment was active.

NumPy's `dot` function computes a vector dot product. For `[1, 2, 3]` with itself, it calculates `1×1 + 2×2 + 3×3`, giving `14`. This small check confirmed NumPy was installed and working in the environment.

`uv` installs and resolves Python packages, and it can create project environments with `uv venv`. I reviewed this role on 2026-11-02 after missing the `uv` question on the lesson quiz.

**My setup evidence:** Python 3.12.3; `.venv` created; NumPy, Matplotlib, and Jupyter installed; dot product output `14`. My earlier setup notes are in [Dev Environment notes](phases/00-setup-and-tooling/01-dev-environment/notes.md).

### Phase 0 · Lesson 3: GPU Setup & Cloud

**Date:** 2026-11-02
**Quiz:** 2/3
**Review:** Cleared on 2026-11-02; GPU operations are asynchronous, so synchronize before stopping the timer.

I used Google Colab's Tesla T4 and confirmed PyTorch could access it. On the second matrix multiplication run, the T4 was about 26× faster than the CPU. The 15.6 GB VRAM gives a rough fp16 parameter-only estimate of 7.8 billion; actual training also needs memory for gradients and other data.

**Artifact:** `phases/00-setup-and-tooling/03-gpu-setup-and-cloud/code/gpu_check.py` and `notes.md`.

### Phase 0 · Lesson 4: APIs & Keys

**Date:** 2026-11-03
**Quiz:** 3/3
**Review next time:** Nothing flagged. A live API request remains to try after setting up an API key.

An API key authenticates and authorizes requests, so I should keep it in an environment variable or an ignored `.env` file rather than source code. An SDK handles HTTP and JSON details; raw HTTP makes those steps visible. I learned to recognize authentication errors (401) and rate or spending limit errors (429). I do not have an Anthropic API key yet, so I did not send a live request.

**Artifacts:** `phases/00-setup-and-tooling/04-apis-and-keys/code/first_api_call.py`, `code/first_api_call.ts`, and `outputs/prompt-api-troubleshooter.md`.

### Phase 0 · Lesson 5: Jupyter Notebooks

**Date:** 2026-11-04
**Quiz:** 3/3
**Review next time:** Nothing flagged by the quiz. During recall, I needed a worked example to see that rerunning a cell changes the value kept by the kernel.

**Main idea in my own words:** A notebook is a lab bench: code cells run in a shared Python kernel, Markdown cells explain the experiment, and outputs stay beside the code. Shared state makes quick experiments convenient, but cells can accidentally depend on the order I happened to run them. Restarting the kernel and running every cell from the top checks that the notebook is reproducible. I can explore data and make plots in a notebook, then move reusable or production code into scripts.

**Example or evidence:** `%timeit` measured Python random-number list creation at `11.1 ms ± 587 μs` per loop and NumPy creation at `1.27 ms ± 61.4 μs` per loop (about 8.7× faster in this run). I loaded an in-memory CSV into a DataFrame and displayed its accuracy chart. A cell that initializes `loss = 4.0` before updating it returns `3.6` on each rerun; to observe retained kernel state, the initialization and update must be in separate cells. Restart & Run All completed without errors. I scored 3/3 on the lesson quiz.

**Exercise status:** Local timing and CSV/plot exercises ran in JupyterLab from `.venv`. Restart & Run All completed without errors. The script exercise ran in Kaggle; PyTorch 2.11.0+cu130 reported CUDA build 13.0 and GPU availability `True`. The script printed Python/NumPy timings (0.0142 s and 0.0011 s), displayed the model table, saved `notebook_plot.png`, and reported array payload sizes (0.008 MB, 0.8 MB, and 8.0 MB). Colab was unavailable due to a page-loading JSON parsing error, so Kaggle was used for the GPU exercise.

**Artifacts:** [`notebooks/notebook_basics.ipynb`](phases/00-setup-and-tooling/05-jupyter-notebooks/notebooks/notebook_basics.ipynb), [`notebooks/jupyter_exercises.ipynb`](phases/00-setup-and-tooling/05-jupyter-notebooks/notebooks/jupyter_exercises.ipynb), [`code/notebook_tips.py`](phases/00-setup-and-tooling/05-jupyter-notebooks/code/notebook_tips.py), [`outputs/prompt-notebook-helper.md`](phases/00-setup-and-tooling/05-jupyter-notebooks/outputs/prompt-notebook-helper.md), and [`notes.md`](phases/00-setup-and-tooling/05-jupyter-notebooks/notes.md).

### Phase 0 · Lesson 6: Python Environments

**Date:** 2026-11-05
**Quiz:** 3/3
**Review next time:** Nothing flagged by the quiz.

**Main idea in my own words:** A virtual environment gives a project its own Python interpreter and packages, keeping its versions separate from other projects. `pyproject.toml` records project metadata and dependency requirements; a lockfile records the exact resolved versions. Use the package manager associated with the active interpreter, and keep environment folders out of Git.

**Example or evidence:** Created `/tmp/lesson6-env` with `.venv/bin/python -m venv`; `which python` and `sys.prefix` pointed into the temporary environment. NumPy was `1.26.4` there and remained `2.5.4` in the repo `.venv`. The setup script passed checks for NumPy, Matplotlib, Jupyter, scikit-learn, pandas, and matrix multiplication. The sample editable project imported `torch 2.15.0+cpu` and `anthropic 2.5.0`; `uv lock --check` passed. The first CUDA-enabled PyTorch download timed out on a 519 MB cuDNN wheel, so the project uses the official CPU-only PyTorch index for this local import exercise. Kaggle had already reported CUDA available for the GPU exercise.

**Exercise status:** All four listed exercises are complete. For the global-scope demonstration, installed `pyfiglet 1.0.4` into an isolated temporary user-site at `/tmp/lesson6-userbase`, confirmed its install location with `pip show`, uninstalled it, and confirmed it was no longer found. The temporary user-site kept the actual system and home package sites unchanged.

**Artifacts:** [`code/env_setup.sh`](phases/00-setup-and-tooling/06-python-environments/code/env_setup.sh), [`exercise-project/pyproject.toml`](phases/00-setup-and-tooling/06-python-environments/exercise-project/pyproject.toml), [`exercise-project/uv.lock`](phases/00-setup-and-tooling/06-python-environments/exercise-project/uv.lock), and [`exercise-project/src/lesson6_demo/__init__.py`](phases/00-setup-and-tooling/06-python-environments/exercise-project/src/lesson6_demo/__init__.py).

### Phase 0 · Lesson 7: Docker for AI

**Date:** 2026-11-09
**Quiz:** 3/3
**Review next time:** Nothing flagged by this quiz.

**Main idea in my own words:** A Docker image packages an application's environment, including system libraries and Python packages; a container runs that image while sharing the host OS kernel. For GPU use, the image supplies CUDA libraries while the host supplies the NVIDIA driver and GPU. Mounts keep files outside the container, and Docker Compose lets services find each other by service name on a shared network.

**Example or evidence:** Explained why the Dockerfile uses a CUDA `devel` image, why it verifies the `get-pip.py` checksum, and why `python -m pip` ties package installation to the selected interpreter. Identified the host as the source of the NVIDIA driver and GPU, and explained how volumes persist data and Compose service DNS resolves `qdrant`.

**Exercise status:** Docker is not installed in this workspace; no Docker socket or NVIDIA device is available. The four container exercises (image build and PyTorch check, Compose/Qdrant check, Flask API, and image-size comparison) have not been run. Their evidence fields and pending status are recorded in [`notes.md`](phases/00-setup-and-tooling/07-docker-for-ai/notes.md).

**Artifacts:** [`code/Dockerfile`](phases/00-setup-and-tooling/07-docker-for-ai/code/Dockerfile), [`code/docker-compose.yml`](phases/00-setup-and-tooling/07-docker-for-ai/code/docker-compose.yml), and [`notes.md`](phases/00-setup-and-tooling/07-docker-for-ai/notes.md).

## Notes for future lessons

For each lesson, append a section to `my_journal.md` using this copyable template. The headings give me a place to explain the idea, preserve a small example, and record what I want to review:

```markdown
### Phase <number> · Lesson <number>: <lesson title>

**Date:** YYYY-MM-DD
**Quiz:** <score>
**Review next time:** <topic or "Nothing flagged">

**Main idea in my own words:**
<A short explanation I can understand later>

**Example or evidence:**
<Command, result, or small example from the lesson>

**Artifact:** <file path, or "None">
```

For the course tracker, append a table row to the `Progress log` in `LEARNING.md` using this format:

```markdown
| YYYY-MM-DD | <phase>/<lesson> | <score> | <one-line note> |
```

If the score is below 70%, add the lesson and missed topic under `Review queue` in `LEARNING.md`. These edits are plain Markdown, so there is no terminal command for them; I will update the files after we finish the lesson quiz.

Continue the course sequence from `LEARNING.md`; do not mark a phase complete until its lessons and course checks are complete.

## Sources

- [AI Engineering from Scratch course README](https://github.com/rohitg00/ai-engineering-from-scratch#choose-how-to-learn)
- [Skills CLI documentation](https://www.skills.sh/docs/cli)
