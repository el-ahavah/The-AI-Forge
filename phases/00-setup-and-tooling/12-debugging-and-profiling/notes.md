# Lesson 12: Debugging & Profiling

## Lesson goal

Learn to find errors and performance problems in Python and AI training code before they waste time or computing resources.

## Key ideas

### 1. Debugging versus profiling

- **Debugging** means finding and fixing incorrect behavior.
- **Profiling** means measuring where a program spends time or memory.
- AI bugs can be silent: a script may finish successfully while producing incorrect predictions or learning nothing useful.

### 2. Inspect tensors

When working with PyTorch tensors, inspect:

- `shape`: dimensions of the data.
- `dtype`: the kind of numbers stored, such as float32.
- `device`: CPU or GPU location.
- Minimum and maximum values.
- Whether any values are NaN or infinite.

A shape mismatch means the dimensions supplied to an operation do not match what it expects.

### 3. Use breakpoints

`breakpoint()` pauses Python and opens the built-in debugger (`pdb`). At the prompt:

| Command | Meaning |
|---|---|
| `p expression` | Print a value |
| `n` | Run the next line |
| `s` | Step into a function |
| `c` | Continue running |
| `q` | Quit the debugger |

A conditional breakpoint stops only when a condition is true, for example when loss becomes too large or NaN.

### 4. Use logging

The `logging` module records messages with levels such as DEBUG, INFO, WARNING, and ERROR. It can add timestamps and save messages to a log file. This is more useful than temporary print statements for long-running jobs.

### 5. Measure time

- `time.perf_counter()` measures elapsed time accurately.
- `cProfile` reports which functions consume the most execution time.
- `line_profiler` can inspect time spent on individual lines.

Do not optimize by guessing. Measure first, identify the bottleneck, then change the code and measure again.

### 6. Measure memory

`tracemalloc` tracks Python memory allocations. PyTorch has separate tools for inspecting GPU memory, such as `torch.cuda.memory_allocated()` and `torch.cuda.memory_reserved()`. CPU memory tracking and GPU memory tracking are not the same thing.

### 7. Recognize common AI bugs

- **NaN loss:** can come from unstable calculations, division by zero, log of zero, or a learning rate that is too high.
- **Data leakage:** information from the test set or target accidentally appears in training.
- **Device mismatch:** model and input tensors are on different devices.
- **Gradient problems:** gradients may be zero, too large, NaN, or infinite.
- **Shape mismatch:** tensors do not have the dimensions expected by a layer or operation.

### 8. TensorBoard

TensorBoard displays training metrics over time. Compare training loss with validation loss. If training loss falls while validation loss rises, the model may be overfitting.

## Important commands

```bash
python -m cProfile -s cumtime train.py
tensorboard --logdir=runs
```

## Lesson 12 checklist

- [ ] Read the official lesson.
- [x] Complete the five-question quiz (5/5, 100%).
- [ ] Run and inspect `code/debug_tools.py`.
- [ ] Complete or document each practical exercise.
- [x] Update the lesson tracker and journal with the quiz result; practical work remains pending.

## Quiz result

**5/5 (100%) — passed.** All five quiz questions were answered correctly. No formal review topic was flagged. Practical exercises have not yet been completed.
