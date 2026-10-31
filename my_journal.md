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

My study plan starts at **Phase 0: Setup & Tooling**. I am working through its first lesson, **Dev Environment**: the verifier passed, PyTorch works, and the quiz is complete. Python Hello World is done; TypeScript, Rust, and Julia examples remain. Phase 1, **Math Foundations**, is marked `Do` in my plan and comes after the remaining Phase 0 lessons. This journal begins with my course setup and will continue as I reach Phase 1 and later phases.

## Learning record

### Phase 0 · Lesson 1: Dev Environment

**Date:** 2026-10-31  
**Quiz:** 2/3  
**Review next time:** What `uv` does.

**Exercise status:** The Python virtual environment, NumPy dot-product check, course verifier, and CPU PyTorch import are complete. Python Hello World is saved at `phases/00-setup-and-tooling/01-dev-environment/codes/hello.py`; it prints `hello world`, captured in `phases/00-setup-and-tooling/01-dev-environment/outputs/hello.txt`. TypeScript, Rust, and Julia Hello World examples remain.

To rerun the Python example from the repository root:

```bash
.venv/bin/python phases/00-setup-and-tooling/01-dev-environment/codes/hello.py
```

It prints `Hello, AI Engineering!`.

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

`uv` is a Python package and environment tool. I need to revisit that role because I missed the `uv` question in the lesson quiz.

**My setup evidence:** Python 3.12.3; `.venv` created; NumPy, Matplotlib, and Jupyter installed; dot product output `14`. My earlier setup notes are in [Dev Environment notes](phases/00-setup-and-tooling/01-dev-environment/notes.md).

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
