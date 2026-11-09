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

VS Code is already installed and its command-line launcher is available. Node.js and Git are also available. No installation was needed for these tools.

### Remaining practical checks

- [ ] Install and verify the eight core recommended VS Code extensions.
- [ ] Install optional recommended extensions if they are needed.
- [ ] Apply the repository's VS Code settings to the editor without overwriting unrelated existing settings.
- [ ] Verify Python interpreter selection and Pylance diagnostics.
- [ ] Verify Black formatting and Ruff linting.
- [ ] Open and run a Jupyter notebook in VS Code.
- [ ] Verify GitLens.
- [ ] Configure and test Remote SSH only if a remote machine is available.

## Artifacts

- [`code/vscode/extensions.json`](code/vscode/extensions.json) — recommended extensions for Python, notebooks, linting, Git, and remote development.
- [`code/vscode/settings.json`](code/vscode/settings.json) — Python analysis, formatting, notebook, terminal, and editor settings.

The lesson is not yet practically complete. Only the local tool installation check has been verified; extension installation and editor configuration checks remain pending.
