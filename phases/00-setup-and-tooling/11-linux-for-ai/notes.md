# Linux for AI

Course lesson: [Linux for AI](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/11-linux-for-ai/docs/en.md)

**Lesson type:** Learn  
**Estimated time:** ~30 minutes  
**Status:** In progress

## Learning objectives

- Navigate the Linux file system and manage files from the terminal.
- Understand file ownership and permissions, including `chmod` and `chown`.
- Understand how Ubuntu installs system packages with `apt`.
- Inspect users, processes, services, memory, and disk usage.
- Transfer files between local and remote machines with `scp` and `rsync`.
- Recognize common differences between macOS, Windows, and Linux.

## 1. Linux file system

Linux has one directory tree that begins at the root directory, written as `/`. Unlike Windows, it does not normally use separate drive letters such as `C:\\`.

| Path | Purpose |
|---|---|
| `/` | Root of the entire file system |
| `/home/username` | A regular user's personal files |
| `~` | Shortcut for the current user's home directory |
| `/tmp` | Temporary files; contents may be cleared |
| `/etc` | System-wide configuration files |
| `/usr` | Many installed programs and shared resources |
| `/var/log` | System and application logs |
| `/mnt` | Common mount point for drives and other file systems |
| `/proc`, `/sys` | Virtual information about processes, the kernel, and hardware |

Most of my project work should live in my home directory, not in protected system directories.

### Navigation commands

```bash
pwd             # Print the current directory
ls              # List visible files and directories
ls -la          # Include hidden files and detailed information
cd /path/to/dir # Move to a directory
cd ~            # Go to my home directory
cd ..           # Move up one directory
```

## 2. Working with files and directories

```bash
mkdir project                 # Create a directory
mkdir -p project/data/raw     # Create nested directories
touch notes.txt               # Create an empty file
cp notes.txt notes-backup.txt # Copy a file
cp -r data data-backup        # Copy a directory and its contents
mv old.txt new.txt            # Rename or move a file
rm notes-backup.txt           # Delete a file
rmdir empty-folder            # Remove an empty directory
```

**Important:** `rm` deletes files without moving them to a graphical trash folder. `rm -rf` recursively deletes a directory without asking for confirmation. Always inspect the path carefully before using it; do not use broad or guessed paths.

## 3. Reading and searching files

```bash
cat notes.txt                    # Print the whole file
head -20 training.log            # Show the first 20 lines
tail -20 training.log            # Show the last 20 lines
tail -f training.log             # Follow new log lines until Ctrl+C
less training.log                # Read a long file page by page; press q to quit
grep -i "error" training.log     # Search without case sensitivity
grep -r "learning_rate" .        # Search recursively in the current directory
find . -name "*.py"              # Find Python files
find . -name "*.ckpt" -size +1G  # Find checkpoint files larger than 1 GB
```

## 4. Linux permissions and ownership

Linux records who owns a file and which users can read, write, or execute it. In `ls -l`, permission characters are grouped into owner, group, and everyone-else permissions.

- `r` means read.
- `w` means write.
- `x` means execute.

Examples:

```bash
ls -l train.sh
chmod +x train.sh       # Add execute permission
chmod 755 deploy.sh     # Owner: read/write/execute; others: read/execute
chmod 644 config.yaml   # Owner: read/write; others: read only
chown user:group file   # Change owner and group (usually requires sudo)
```

A `Permission denied` message does not automatically mean I should use `sudo`. First inspect the file path, ownership, and permissions with `ls -l`. Use `chmod` only when the permission change is appropriate. Use `sudo` only for a specific operation that genuinely requires administrator privileges.

## 5. Installing software with apt

Ubuntu and other Debian-based distributions use APT to manage system packages.

```bash
sudo apt update
sudo apt install htop
apt list --installed
sudo apt remove htop
```

- `apt update` refreshes the package index; it does not upgrade every installed package.
- `apt install` installs a package.
- `apt remove` uninstalls a package.
- `sudo` runs one command with administrator privileges when permitted.

Common tools on an AI workstation or remote GPU machine include `git`, `curl`, `wget`, `tmux`, `htop`, `unzip`, and `python3-venv`. I should check whether a tool is already installed before installing it. I should not run system-changing commands on a shared or managed machine without permission.

## 6. Users, processes, and services

```bash
whoami                  # Show the current username
id                      # Show user and group IDs
sudo command            # Run one administrator command
ps aux                  # List running processes
ps aux | grep python    # Search for Python processes
htop                    # Interactive process monitor
kill PID                # Ask a process to stop gracefully
kill -9 PID             # Force-stop a process; use only as a last resort
nvidia-smi              # Show NVIDIA GPU status, if supported
```

A process is a running program. Prefer a normal termination signal before using `kill -9`, because force-killing can prevent cleanup or saving work.

`systemd` manages background services on many Linux systems. For a service I am authorized to manage:

```bash
systemctl status SERVICE
sudo systemctl start SERVICE
sudo systemctl stop SERVICE
sudo systemctl restart SERVICE
```

Do not start, stop, or enable system services just to experiment on a shared machine.

## 7. Checking disk space

AI models, datasets, checkpoints, and caches can use many gigabytes.

```bash
df -h                 # Available and used space on mounted file systems
df -h ~               # File system containing my home directory
du -sh ~/some-folder  # Total size of one folder
du -sh ~/.cache       # Size of my user cache, if it exists
du -sh ./*            # Sizes of items in the current directory
```

- `df` reports free and used space on file systems.
- `du` estimates how much space files and directories use.

Inspect a cache or checkpoint directory before deleting anything. Cache contents may be useful and may take time or bandwidth to download again.

## 8. Networking and file transfer

```bash
wget https://example.com/file.zip
curl -O https://example.com/file.zip
curl -s https://example.com/health
```

For a remote machine that I am authorized to access:

```bash
scp report.csv user@server:~/         # Copy local file to remote home
scp user@server:~/result.csv ./       # Copy remote file to local folder
scp -r user@server:~/outputs/ ./      # Copy a remote directory
rsync -avP ./data/ user@server:~/data/ # Synchronize a directory
```

- `scp` securely copies files over SSH.
- `rsync` synchronizes files and directories and can avoid retransferring unchanged data.
- The trailing slash in an `rsync` source path affects whether the directory itself or its contents are copied.

Never put passwords or private SSH keys in commands, scripts, or GitHub. Remote transfer exercises require a real host and valid access; do not invent a host or attempt an unauthorized connection.

## 9. Keeping remote work running with tmux

An SSH connection can disconnect. A normal foreground process tied to that terminal may stop when the session ends. `tmux` provides a terminal session that can remain alive after detaching.

```bash
tmux new -s training     # Start a named session
tmux ls                  # List sessions
tmux attach -t training  # Reattach
```

Inside tmux, press `Ctrl+B`, release the keys, then press:

- `d` to detach.
- `%` to split the window vertically.
- `"` to split the window horizontally.
- An arrow key to move between panes.

Detaching leaves the session running. Ending the session or stopping its processes is different from detaching.

## 10. Windows Subsystem for Linux (WSL2)

WSL2 provides a Linux environment on Windows without requiring a traditional dual-boot setup. From an administrator PowerShell window, Windows users can install Ubuntu with:

```powershell
wsl --install -d Ubuntu-24.04
```

Inside WSL, Windows drives are commonly available under `/mnt/`, such as `/mnt/c/`. NVIDIA GPU support in WSL requires a supported Windows NVIDIA driver and compatible setup; do not install a separate Linux display driver inside WSL as if it were a normal Linux GPU machine.

This section is reference material. My current learning environment is already Ubuntu, so I do not need to install WSL2.

## 11. macOS and Linux differences

| Task | macOS | Ubuntu/Linux |
|---|---|---|
| Install packages | `brew install package` | `sudo apt install package` |
| Open a file in a desktop app | `open file` | Often `xdg-open file` (not usually available on headless servers) |
| Edit in-place with sed | `sed -i '' 's/a/b/' file` | `sed -i 's/a/b/' file` |
| Common default shell | Zsh | Often Bash on servers; this varies |
| File name case | Often case-insensitive by default | Usually case-sensitive |

Linux treats `Model.py` and `model.py` as different file names. Windows text files may use CRLF line endings, while Linux scripts normally use LF; CRLF can cause shell-script problems.

## Quick reference

| Need | Commands |
|---|---|
| Navigate | `pwd`, `ls -la`, `cd` |
| Create and move files | `mkdir`, `touch`, `cp`, `mv`, `rm` |
| Read and search | `cat`, `less`, `head`, `tail`, `grep`, `find` |
| Permissions | `ls -l`, `chmod`, `chown` |
| Packages | `apt update`, `apt install`, `apt remove` |
| Processes | `ps`, `htop`, `kill`, `nvidia-smi` |
| Disk | `df -h`, `du -sh` |
| Transfer | `scp`, `rsync`, `curl`, `wget` |
| Persistent terminal | `tmux new`, `tmux ls`, `tmux attach` |

## Practical exercise checklist

The five source-course exercises and their safe execution notes are in [exercises/README.md](exercises/README.md). Record completion only after running an exercise and checking its result.

## Quiz record

**Status:** Not attempted  
**Score:** Pending  
**Review topics:** To be recorded after the quiz.
