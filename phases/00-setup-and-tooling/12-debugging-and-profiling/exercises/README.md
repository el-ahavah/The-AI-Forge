# Lesson 12 Practical Exercises

Complete these exercises after the quiz. Run commands from the root of `The-AI-Forge`.

## Before you start

Use the project's virtual environment when available:

```bash
source .venv/bin/activate
```

Check PyTorch:

```bash
python3 -c "import torch; print(torch.__version__)"
```

If PyTorch is unavailable in the active environment, do not install packages without checking first. The toolkit has a limited fallback for memory tracking and logging, but the tensor demonstrations require PyTorch.

## Exercise 1 — Run the debugging toolkit

```bash
python3 phases/00-setup-and-tooling/12-debugging-and-profiling/code/debug_tools.py
```

Read the output. Find the sections showing tensor details, shapes, NaN detection, device checks, and gradient health.

Then inspect the NaN demonstration in the script. It includes a simulated NaN loss to show how a detector reports the failure.

**Observed result:** The script ran. The memory-tracking and structured-logging demonstrations completed. PyTorch was not installed, so tensor diagnostics, NaN detection, and gradient demonstrations were skipped.

**Status:** Partially completed.

## Exercise 2 — Profile execution time

Create a small Python script with at least two functions that take noticeably different amounts of time. Run:

```bash
python3 -m cProfile -s cumtime your_script.py
```

Identify the slowest function you wrote. Do not assume that the GPU or model computation is the bottleneck; use the profiler output.

**Observed result:** `cProfile` reported 9,274 calls (8,982 primitive) in 0.026 seconds. `demo_memory_tracking()` was the slowest user-defined function at 0.010 seconds cumulative time; `main()` took 0.011 seconds cumulatively.

**Status:** Completed.

## Exercise 3 — Inspect Python memory allocations

Use `tracemalloc` to take a snapshot before and after creating a sizeable Python list or other data structure. Print the top five entries:

```python
import tracemalloc

tracemalloc.start()
data = [bytearray(1024) for _ in range(1000)]
snapshot = tracemalloc.take_snapshot()
for stat in snapshot.statistics("lineno")[:5]:
    print(stat)
tracemalloc.stop()
```

**Observed result:** The top allocation was reported at `<string>:6`: 1,064 KiB, 2,001 allocations, and 545 bytes average.

**Status:** Completed.

## Exercise 4 — Visualize training with TensorBoard

Use a small synthetic dataset and a simple model. Log both training and validation loss with `SummaryWriter`. Launch:

```bash
tensorboard --logdir=runs
```

Open the local address printed by TensorBoard. Identify whether the training and validation curves suggest overfitting. If TensorBoard or its dependencies are not installed, record the missing dependency rather than changing the environment without permission.

**Observed result:** `python3 -m tensorboard --version` returned `No module named tensorboard`. The PyTorch check also returned `ModuleNotFoundError: No module named 'torch'`. TensorBoard could not be run because both dependencies are unavailable. No installation was attempted.

**Status:** Blocked by unavailable dependencies.

## Exercise 5 — Use the Python debugger

Put `breakpoint()` inside a small Python loop or training step. Run the script and, at the `(Pdb)` prompt, try:

```text
p x.shape
p x.device
n
c
```

Use `q` to exit if needed. If your variable names differ, inspect variables that exist in your script.

**Observed result:** Used `p number` to inspect 10 and 20, `n` to step to the next line, and `p total` to inspect running totals of 10 and 30. Used `c` to continue through the loop. The program finished with `Total: 60`.

**Status:** Completed.

## Quiz result

**5/5 (100%) — passed.** All five questions were answered correctly. No formal review is required.

## Progress

| Exercise | Status |
|---|---|
| 1. Debugging toolkit | Partially completed — memory tracking and logging ran; PyTorch diagnostics unavailable |
| 2. cProfile | Completed |
| 3. tracemalloc | Completed |
| 4. TensorBoard | Blocked — TensorBoard and PyTorch are not installed |
| 5. breakpoint / pdb | Completed |

**Overall:** 3 completed, 1 partially completed, and 1 blocked by missing dependencies. No packages were installed.
