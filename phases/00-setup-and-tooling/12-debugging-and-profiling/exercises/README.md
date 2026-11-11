# Lesson 12 Practical Exercises

Complete these exercises after the quiz. Run commands from the root of `The-AI-Forge`.

## Before you start

Use the project's virtual environment when available:

```bash
source .venv/bin/activate
```

Check PyTorch:

```bash
python -c "import torch; print(torch.__version__)"
```

If PyTorch is unavailable in the active environment, do not install packages without checking first. The toolkit has a limited fallback for memory tracking and logging, but the tensor demonstrations require PyTorch.

## Exercise 1 — Run the debugging toolkit

```bash
python phases/00-setup-and-tooling/12-debugging-and-profiling/code/debug_tools.py
```

Read the output. Find the sections showing tensor details, shapes, NaN detection, device checks, and gradient health.

Then inspect the NaN demonstration in the script. It includes a simulated NaN loss to show how a detector reports the failure.

**Record:** whether the script completed and which diagnostics it displayed.

## Exercise 2 — Profile execution time

Create a small Python script with at least two functions that take noticeably different amounts of time. Run:

```bash
python -m cProfile -s cumtime your_script.py
```

Identify the slowest function you wrote. Do not assume that the GPU or model computation is the bottleneck; use the profiler output.

**Record:** the slowest function and its cumulative time.

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

**Record:** the line responsible for the largest allocation.

## Exercise 4 — Visualize training with TensorBoard

Use a small synthetic dataset and a simple model. Log both training and validation loss with `SummaryWriter`. Launch:

```bash
tensorboard --logdir=runs
```

Open the local address printed by TensorBoard. Identify whether the training and validation curves suggest overfitting. If TensorBoard or its dependencies are not installed, record the missing dependency rather than changing the environment without permission.

**Record:** whether TensorBoard started and what the curves show.

## Exercise 5 — Use the Python debugger

Put `breakpoint()` inside a small Python loop or training step. Run the script and, at the `(Pdb)` prompt, try:

```text
p x.shape
p x.device
n
c
```

Use `q` to exit if needed. If your variable names differ, inspect variables that exist in your script.

**Record:** which values you inspected and whether you successfully continued execution.

## Progress

| Exercise | Status |
|---|---|
| 1. Debugging toolkit | Pending |
| 2. cProfile | Pending |
| 3. tracemalloc | Pending |
| 4. TensorBoard | Pending |
| 5. breakpoint / pdb | Pending |
