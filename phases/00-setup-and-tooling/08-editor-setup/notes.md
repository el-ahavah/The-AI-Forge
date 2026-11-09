# Editor Setup

Course lesson: [Editor Setup](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/08-editor-setup/docs/en.md)

**Date studied:** 2026-11-09  
**Quiz:** 4/4

## What I learned

- Remote SSH lets VS Code edit files and run tools on a remote GPU machine.
- Notebook output scrolling keeps long training logs from overwhelming a notebook.
- Basic type checking with Pylance can flag mismatched types and incorrect arguments while editing.
- Format on save applies a consistent code style without requiring manual formatting.

## Practical setup progress

### Step 1: Verify the local development tools — complete

Verified on 2026-11-09 using the local terminal:

| Tool | Verified result | Status |
|---|---|---|
| Visual Studio Code | Version 1.100.2, x64 | Complete |
| VS Code executable | `/usr/bin/code` | Complete |
| Node.js | `v26.13.0` | Complete |
| Git | `2.43.0` | Complete |

Commands used:

```bash
code --version
which code
node --version
git --version
```

### Step 2: Install and verify core extensions — complete

Ran `code --list-extensions` on 2026-11-09. All eight core extensions recommended for this lesson are present:

| Extension | Status |
|---|---|
| `ms-python.python` — Python | Installed |
| `ms-python.vscode-pylance` — Pylance | Installed |
| `ms-toolsai.jupyter` — Jupyter | Installed |
| `ms-python.debugpy` — Debugpy | Installed |
| `ms-python.black-formatter` — Black Formatter | Installed |
| `charliermarsh.ruff` — Ruff | Installed |
| `eamodio.gitlens` — GitLens | Installed |
| `ms-vscode-remote.remote-ssh` — Remote SSH | Installed |

Other useful extensions already present include Go, Python Environments, Jupyter Keymap, Jupyter Renderers, Jupyter Cell Tags, Jupyter Slideshow, Remote SSH Edit, and Remote Explorer.

Optional extensions from the repository recommendation list that were not shown in the command output: Remote Containers, YAML, and Even Better TOML. These are not part of the eight-extension core verification.

### Remaining practical checks

- [x] Verify VS Code, Node.js, and Git.
- [x] Install and verify the eight core recommended VS Code extensions.
- [x] Apply the repository's VS Code workspace settings.
- [x] Create and select the project Python 3.12.3 virtual environment at `.venv/bin/python`.
- [x] Verify Pylance type diagnostics: the intentional `greet(25)` mismatch produced a warning.
- [x] Verify Black formatting: the deliberately unformatted function was formatted on save.
- [x] Verify Ruff linting: Ruff flagged the intentionally unused `os` import.
- [ ] Open and run a Jupyter notebook in VS Code.
- [ ] Verify GitLens behavior in the editor.
- [ ] Configure and test Remote SSH only if a remote machine is available.

### Verification evidence

Created `code/editor_setup_check.py` to test editor behavior. Pylance flagged the intentional string-versus-integer argument mismatch, Black automatically formatted the deliberately unformatted function on save, and Ruff flagged the intentionally unused `os` import. The project virtual environment uses Python 3.12.3 and was selected in VS Code.

## Artifacts

- [`code/vscode/extensions.json`](code/vscode/extensions.json) — recommended extensions for Python, notebooks, linting, Git, and remote development.
- [`code/vscode/settings.json`](code/vscode/settings.json) — Python analysis, formatting, notebook, terminal, and editor settings.

The editor setup is partially complete: local prerequisites, all eight core extensions, workspace settings, Python interpreter selection, Pylance diagnostics, and Black format-on-save are verified. Ruff, Jupyter, GitLens, and (if a remote machine is available) Remote SSH checks remain.
