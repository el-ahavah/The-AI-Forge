# Debugging and Profiling

> The worst AI bugs don't crash. They train silently on garbage and report a beautiful loss curve.

**Type:** Build  
**Language:** Python  
**Prerequisites:** Lesson 1 (Dev Environment), basic PyTorch familiarity  
**Time:** ~60 minutes

## Learning Objectives

- Use conditional `breakpoint()` and `debug_print` to inspect tensor shapes, dtypes, and NaN values mid-training
- Profile training loops with `cProfile`, `line_profiler`, and `tracemalloc` to find bottlenecks
- Detect common AI bugs: shape mismatches, NaN loss, data leakage, and wrong-device tensors
- Set up TensorBoard to visualize loss curves, weight histograms, and gradient distributions

## The Problem

AI code fails differently than regular code. A web app crashes with a stack trace. A misconfigured training loop runs for 8 hours, burns GPU time, and produces a model that predicts the mean of every input. The code never errored. The bug was a tensor on the wrong device, a forgotten `.detach()`, or labels leaking into features.

You need debugging tools that catch these silent failures before they waste time and compute.

## The Concept

AI debugging operates at three levels:

1. **Standard Python:** breakpoints, logging, profiling, and memory.
2. **Tensor operations:** shapes, dtypes, devices, and NaN/Inf values.
3. **Training dynamics:** loss curves, gradient norms, and activations.

Most AI bugs are easier to find at the first two levels than by staring at a dashboard.

## Build It

### 1. Print debugging

A targeted print statement can show a tensor's shape, data type, device, value range, and whether it contains NaNs.

```python
def debug_print(name, tensor):
    print(
        f"{name}: shape={tensor.shape}, dtype={tensor.dtype}, "
        f"device={tensor.device}, has_nan={tensor.isnan().any().item()}"
    )
```

Use it after suspicious operations, then remove temporary prints when the bug is found.

### 2. Python debugger

Put `breakpoint()` at a point where you need to inspect the program:

```python
if loss.item() > 100 or torch.isnan(loss):
    breakpoint()
```

Useful commands at the `(Pdb)` prompt:

- `p outputs.shape` — inspect a tensor's shape.
- `p loss.item()` — print the loss value.
- `p torch.isnan(outputs).sum()` — count NaNs.
- `c` — continue.
- `q` — quit the debugger.

### 3. Logging

Python's `logging` module adds timestamps and severity levels and can write to a file:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)
logger.info("Training started")
logger.warning("Loss spike detected")
logger.error("NaN loss; stopping")
```

Use logging for longer runs instead of relying only on terminal prints.

### 4. Timing code

Use `time.perf_counter()` to measure elapsed time. A context manager can time sections such as data loading, the forward pass, and the backward pass. If data loading takes most of the time, a faster GPU will not solve that bottleneck.

### 5. Profiling execution

Run:

```bash
python -m cProfile -s cumtime train.py
```

`cProfile` reports function-call timing, sorted here by cumulative time. `line_profiler` can measure individual lines when installed and configured.

### 6. Memory profiling

Python's `tracemalloc` tracks Python memory allocations:

```python
import tracemalloc

tracemalloc.start()
# Run the code being investigated.
snapshot = tracemalloc.take_snapshot()
for stat in snapshot.statistics("lineno")[:5]:
    print(stat)
tracemalloc.stop()
```

For PyTorch GPU memory, inspect `torch.cuda.memory_allocated()` and `torch.cuda.memory_reserved()` when CUDA is available. If GPU memory runs out, first try a smaller batch size. Other options include mixed precision and gradient checkpointing.

### 7. Common AI bugs

- **Shape mismatch:** input dimensions do not match what a layer expects. Print shapes at each stage.
- **NaN/Inf loss:** possible causes include an excessive learning rate, division by zero, or taking a logarithm of zero. Check the loss and gradients.
- **Data leakage:** training and test data overlap, or features contain information from the target. Check IDs and split logic.
- **Wrong device:** model parameters and input tensors are on different devices. Check each tensor's `.device`.
- **Unhealthy gradients:** gradients may be zero, excessively large, NaN, or infinite. Inspect gradient norms and values.

### 8. TensorBoard

TensorBoard visualizes metrics over training:

```python
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter("runs/experiment_1")
writer.add_scalar("loss/train", loss.item(), step)
writer.close()
```

Launch it with:

```bash
tensorboard --logdir=runs
```

A training loss that decreases while validation loss rises can indicate overfitting. A loss that becomes NaN suggests numerical instability.

### 9. VS Code debugger

VS Code can launch a Python script using a `launch.json` configuration. Set a breakpoint in the editor, start debugging, and inspect variables in the Variables and Debug Console panes.

## Use It

1. Before training, check sample input and output shapes.
2. During the first steps, inspect loss values and check for NaNs.
3. Log loss, learning rate, and gradient norms.
4. When a failure occurs, use `breakpoint()` to inspect the state.
5. Profile execution time and memory before attempting optimization.

## Ship It

Run the debugging toolkit:

```bash
python phases/00-setup-and-tooling/12-debugging-and-profiling/code/debug_tools.py
```

See `outputs/prompt-debug-ai-code.md` for a prompt to help diagnose AI-specific bugs.

## Exercises

1. Run `debug_tools.py`. Read each section and modify the dummy model to introduce a NaN, then observe the detector.
2. Profile a training loop with `cProfile` and identify its slowest function.
3. Use `tracemalloc` to find which line allocates the most Python memory.
4. Set up TensorBoard for a simple training run and compare training and validation loss.
5. Put `breakpoint()` inside a training loop and inspect tensor shapes, devices, and gradients.

### Hints

**Exercise 1:** Run `python3 phases/00-setup-and-tooling/12-debugging-and-profiling/code/debug_tools.py`. The script includes a simulated NaN detector example.

**Exercise 2:** Run `python -m cProfile -s cumtime your_script.py`. Look at the `cumtime` column and identify the slowest function in your own code.

**Exercise 3:** Start `tracemalloc` before the data-loading code and take a snapshot afterward. The first entries from `snapshot.statistics("lineno")` show the largest allocations.

**Exercise 4:** Log training and validation loss with a `SummaryWriter`, then launch TensorBoard with `tensorboard --logdir=runs`.

**Exercise 5:** Put `breakpoint()` inside the loop. At the `(Pdb)` prompt, inspect `x.shape`, `x.device`, and a model parameter's gradient. Use `c` to continue.

---
Source: official AI Engineering from Scratch Lesson 12, adapted into this repository's lesson documentation.
