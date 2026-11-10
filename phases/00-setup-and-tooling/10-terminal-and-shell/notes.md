# Terminal & Shell

Course lesson: [Terminal & Shell](https://aiengineeringfromscratch.com/lesson?path=phases/00-setup-and-tooling/10-terminal-and-shell)

**Lesson type:** Learn  
**Estimated time:** ~35 minutes  
**Quiz:** 5/5 (100%) — completed 2026-11-10  
**Practical exercises:** 4/4 passed locally — completed 2026-11-10

## Learning objectives

- Use pipes, redirects, `grep`, `tail`, and `awk` to inspect training logs.
- Understand foreground and background processes, `nohup`, and persistent `tmux` sessions.
- Monitor system and GPU resources with `htop`, `nvtop`, and `nvidia-smi`.
- Understand remote access and file transfer with SSH, `scp`, and `rsync`.

## Core ideas

### 1. The shell

The shell is the command interpreter (for example, Bash or Zsh). The terminal is the application window where I interact with the shell.

Useful commands:

```bash
echo "$SHELL"   # Show the configured login shell
pwd             # Show the current directory
ls -la          # List files, including hidden files
history         # Show command history
clear           # Clear the terminal
```

### 2. Pipes and redirects

A pipe sends one command's standard output (stdout) to the next command's standard input (stdin).

| Operator | Meaning |
|---|---|
| `|` | Send stdout to another command |
| `>` | Write stdout to a file, replacing its previous contents |
| `>>` | Append stdout to a file |
| `2>` | Write standard error (stderr) to a file |
| `2>&1` | Send stderr to the same destination as stdout |

Examples:

```bash
grep "loss" train.log
grep "loss" train.log | wc -l
grep "loss:" train.log | awk '{print $NF}' > losses.txt
python train.py > output.log 2> errors.log
python train.py > train_full.log 2>&1
tail -f train.log | grep --line-buffered "ERROR"
```

### 3. Background jobs and persistent sessions

- `command &` starts a background job in the current shell, but it is not a reliable way to survive closing the terminal.
- `nohup command > run.log 2>&1 &` makes a process ignore the hangup signal and saves its output to a log. It does not provide an interactive session to reattach to.
- `tmux` keeps a terminal session alive so I can detach and reconnect while commands continue running.

Useful job commands:

```bash
jobs
ps aux | grep train.py
fg %1
kill %1
```

### 4. tmux essentials

```bash
tmux new -s training       # Create a named session
tmux ls                   # List sessions
tmux attach -t training   # Reattach
tmux kill-session -t training
```

Inside tmux, the prefix is `Ctrl+B`:

- `Ctrl+B`, then `"`: split into horizontal panes.
- `Ctrl+B`, then `%`: split into vertical panes.
- `Ctrl+B`, then an arrow key: move between panes.
- `Ctrl+B`, then `d`: detach without stopping the session.

### 5. Monitoring resources

```bash
htop
nvidia-smi
watch -n1 nvidia-smi
nvtop
df -h
du -sh ./data
```

`htop` monitors CPU, memory, and processes. `nvidia-smi` reports NVIDIA GPU state. `nvtop` provides an interactive GPU monitor when supported and installed. A machine without an NVIDIA GPU may not have `nvidia-smi` or `nvtop`; that is not a shell failure.

### 6. Remote access and file transfer

```bash
ssh user@gpu-box
scp model.pt user@gpu-box:~/models/
scp user@gpu-box:~/results/metrics.json ./
rsync -avz ./data/ user@gpu-box:~/data/
ssh -L 8888:localhost:8888 user@gpu-box
```

SSH opens an encrypted remote shell. `scp` copies files. `rsync` efficiently synchronizes directories. Local port forwarding (`ssh -L`) lets a local browser reach a service running on the remote machine.

A host alias can be stored in `~/.ssh/config`:

```sshconfig
Host gpu
    HostName your-server-address
    User your-username
    IdentityFile ~/.ssh/your-key
```

Replace the placeholders with real values. Never publish private SSH keys or passwords.

## Exercises

| # | Task | Status |
|---|---|---|
| 1 | `exercises/01-tmux-lab.sh`; displayed system monitor, live clock, and Python heartbeat in three panes | Passed — all three panes ran |
| 2 | `exercises/02-install-aliases.sh`; loaded and verified aliases in the active Zsh shell | Passed — `ll`, `gpu`, `checkenv`, and `ta` verified |
| 3 | `exercises/03-analyze-log.sh`; inspected the generated training log with `grep`, `tail`, and `awk` | Passed — one warning, one error, seven loss values identified |
| 4 | `exercises/04-check-ssh-config.sh`; inspected temporary localhost settings with `ssh -G` | Passed — no remote connection; `~/.ssh/config` unchanged |

**Shell configuration note:** This workspace uses Zsh (`/usr/bin/zsh`). The alias installer initially added its source line to `~/.bashrc`, which is not the active shell configuration. I added the alias-file source line to `~/.zshrc` and verified the aliases there. Sourcing the Bash startup file from Zsh produced Bash-specific `shopt` and completion errors; do not source `~/.bashrc` from Zsh.

**Safety note:** Review every alias before sourcing it. In particular, `killtraining` and `killtrain` can terminate matching Python processes. Do not run destructive commands or connect to a remote host unless you understand the target.

## Quiz record

Completed 2026-11-10.

- Score: 5/5 (100%)
- Questions missed: None
- Review topics: None flagged by the quiz
- Correct concepts: pipe operator (`|`), SIGHUP on terminal closure, tmux detach/reattach and panes, combined stdout/stderr redirection (`> output.log 2>&1`), and SSH local port forwarding (`ssh -L 8888:localhost:8888 user@gpu-box`).
