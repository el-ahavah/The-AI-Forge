# Git & Collaboration

Course lesson: [Git & Collaboration](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/02-git-and-collaboration/docs/en.md)

**Date:** 2026-11-02  
**Quiz:** 3/3

## What I learned

Git moves selected changes through four places:

1. The **working directory** contains the files I edit.
2. The **staging area** contains the changes I selected with `git add`.
3. The **local repository** stores snapshots created by `git commit`.
4. The **remote repository** is another copy, such as my GitHub repository; `git push` sends committed changes there.

The usual save-and-backup sequence is `git add` → `git commit` → `git push`. A branch gives experiments their own line of work. New commits advance the active branch; merging applies branch changes to another branch. A `.gitignore` file keeps selected files, such as large model checkpoints, out of Git's untracked-file list. `git log --oneline` gives a compact view of commit history.

## GitHub fork exercise

I forked the course into my GitHub account and configured the local course clone with my fork as `origin` and the official course repository as `upstream`.

```text
origin   https://github.com/el-ahavah/ai-engineering-from-scratch.git
upstream https://github.com/rohitg00/ai-engineering-from-scratch
```

I created the `my-progress` branch, added `my-progress.md`, committed it, and pushed the branch:

```bash
git checkout -b my-progress
git add my-progress.md
git commit -m "docs: record course progress"
git push -u origin my-progress
```

The pushed commit is `e6a95f699 docs: record course progress`. The branch tracks `origin/my-progress`.

## `.gitignore` exercise

The root `.gitignore` in my learning repository contains these checkpoint patterns:

```gitignore
*.pt
*.pth
*.safetensors
```

I created temporary files with each suffix and checked them with `git status --short`. They did not appear as untracked files, and I removed the temporary files afterward.

## Git history exercise

I listed recent commits and filtered the history to Phase 0 with:

```bash
git -C /home/student/ai/ai-engineering-from-scratch log --oneline -10
git -C /home/student/ai/ai-engineering-from-scratch log --oneline -10 -- phases/00-setup-and-tooling
```

I inspected commit `f6472e3cd` with:

```bash
git -C /home/student/ai/ai-engineering-from-scratch show --stat f6472e3cd
```

It changed `phases/00-setup-and-tooling/01-dev-environment/code/main.rs` with 19 insertions and 8 deletions. Its message says it centralized repeated `Check` defaults in a constructor.

## Commands to remember

```bash
git status
git add <file>
git commit -m "Describe the change"
git push origin <branch>
git checkout -b <new-branch>
git log --oneline
git remote -v
```

## Progress

Quiz and practical exercises are complete. The quiz score was **3/3**. Lesson 1's `uv` review was cleared on 2026-11-02. The next lesson at that point was **GPU Setup & Cloud**.
