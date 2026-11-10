# Lesson 10 Practical Exercises

Run these from the repository root. Each script is safe to inspect before execution.

## Exercise 1 — tmux

Run:
```bash
bash phases/00-setup-and-tooling/10-terminal-and-shell/exercises/01-tmux-lab.sh
```
It creates a named three-pane tmux session: a system monitor, a live clock, and a harmless Python heartbeat. Detach with **Ctrl+B**, then **D**. Reattach with `tmux attach -t lesson10-lab`. Finish with `tmux kill-session -t lesson10-lab`. Requires tmux; the monitor uses htop if installed, otherwise top.

## Exercise 2 — shell aliases

Run the installer with the startup file for your active shell. For Bash:
```bash
bash phases/00-setup-and-tooling/10-terminal-and-shell/exercises/02-install-aliases.sh
source ~/.bashrc
```

For Zsh:
```bash
bash phases/00-setup-and-tooling/10-terminal-and-shell/exercises/02-install-aliases.sh ~/.zshrc
source ~/.zshrc
```

The installer itself runs with Bash, but its optional first argument selects which shell startup file receives the source line for the existing `code/shell_aliases.sh` file. It creates a backup and avoids duplicate entries. Use the startup file for your active shell (check with `echo "$SHELL"`). Review the alias file before loading it; do not invoke process-killing helpers unless you understand their effect.

## Exercise 3 — log analysis

Run:
```bash
bash phases/00-setup-and-tooling/10-terminal-and-shell/exercises/03-analyze-log.sh
```
The script creates a sample training log in the exercise directory, then uses grep, tail, and awk to inspect errors and extract loss values. It does not need a real training run.

## Exercise 4 — SSH configuration

Run:
```bash
bash phases/00-setup-and-tooling/10-terminal-and-shell/exercises/04-check-ssh-config.sh
```
It creates a temporary localhost SSH config and inspects the resolved values with `ssh -G`. It does not connect to a server or alter your personal SSH configuration. A reusable remote-host example is in `ssh_config.example`; replace placeholders only when you have a real host and credentials.

## Completion rule

These scripts and instructions are now stored in GitHub. That means the exercises are prepared, not that they have been executed on your computer. Mark each exercise complete in `../notes.md` only after running it locally and checking the result.
