# Lesson 11 Practical Exercises — Linux for AI

The original course lists five practical exercises. Run commands from your Ubuntu terminal. These exercises are prepared here; mark them complete in `../notes.md` only after you have run them and checked the result.

## Before starting

Confirm your environment:

```bash
pwd
whoami
echo "$SHELL"
uname -a
```

You are already using Ubuntu, so you can practise the Linux commands directly. You do not need to install WSL2.

## Exercise 1 — Navigate and create files

Create a practice directory inside your home directory, add three empty files, and list them:

```bash
mkdir -p ~/linux-ai-practice
cd ~/linux-ai-practice
touch notes.txt config.yaml train.py
ls -la
```

Check that all three files appear and have a size of zero bytes. This exercise does not modify the project repository.

## Exercise 2 — Inspect processes with htop

First check whether htop is installed:

```bash
command -v htop
```

If it is installed, run:

```bash
htop
```

Identify the process using the most memory. Press `q` to exit. If htop is missing and you have permission to install packages, ask before using `sudo apt update` or `sudo apt install htop`; on a managed machine, do not change system packages without authorization. You can use `top` as a read-only alternative.

## Exercise 3 — Detach and reattach a tmux session

Check whether tmux is installed:

```bash
command -v tmux
```

If available, create a session and run a harmless process:

```bash
tmux new -s lesson11
```

Inside tmux, run:

```bash
sleep 300
```

Detach with **Ctrl+B**, then **D**. Back in the normal terminal, list sessions and reattach:

```bash
tmux ls
tmux attach -t lesson11
```

The `sleep` command should still be running. Press **Ctrl+C** to stop it, then exit tmux with:

```bash
exit
```

If tmux is not installed, do not install it without permission. Record the dependency as pending.

## Exercise 4 — Inspect disk and cache usage

Run:

```bash
df -h
df -h ~
du -sh ~/.cache 2>/dev/null
```

If the cache directory exists, inspect its immediate subdirectories:

```bash
du -sh ~/.cache/* 2>/dev/null | sort -h
```

Identify the file system containing your home directory and note its available space. These commands inspect storage; they do not delete anything. Do not clear caches or remove checkpoints as part of this exercise.

## Exercise 5 — Compare scp and rsync

This exercise requires a remote Linux host that you own or are authorized to use, plus working SSH access. Do not guess a hostname or connect to a machine without permission.

On your local machine, create a small test file:

```bash
printf 'Linux file transfer practice\n' > ~/linux-ai-practice/transfer-test.txt
```

After you have a valid remote host and username, copy it with scp:

```bash
scp ~/linux-ai-practice/transfer-test.txt USER@HOST:~/
```

Then synchronize the same file with rsync:

```bash
rsync -avP ~/linux-ai-practice/transfer-test.txt USER@HOST:~/
```

Run the rsync command a second time and observe that an unchanged file usually requires little or no data transfer. Replace `USER` and `HOST` only with the real details of an authorized server.

If you do not have a remote host, mark this exercise **pending — remote host unavailable**. Do not treat a local copy as proof of an SSH transfer.

## Completion record

| Exercise | What to verify | Status |
|---|---|---|
| 1. Filesystem navigation | Three empty files appear in the practice directory | Pending |
| 2. Process monitoring | Identify the highest-memory process in htop or top | Pending |
| 3. tmux session | Detach, list, and reattach while sleep is still running | Pending |
| 4. Disk usage | Read available disk space and inspect cache size | Pending |
| 5. Remote transfer | Compare scp and rsync on an authorized remote host | Pending |

**Safety:** Avoid running `rm -rf` on paths you have not checked. Do not use `sudo` to bypass an unexplained permission error. Do not force-kill processes or change system services unless you understand the impact and are authorized to do so.
