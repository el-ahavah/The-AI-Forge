# GPU Setup & Cloud

Course lesson: [GPU Setup & Cloud](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/03-gpu-setup-and-cloud/docs/en.md)

**Date:** 2026-11-02  
**Quiz:** 2/3

## What I learned

A CPU can handle general computing and small experiments. A GPU can perform many similar calculations in parallel, which often makes the matrix operations used in neural networks faster. NVIDIA GPUs can run these calculations through CUDA, and PyTorch can use CUDA when it is available.

VRAM is memory dedicated to the GPU. It limits how much model data and training data can fit on the GPU at once. With fp16, each parameter takes about 2 bytes, so dividing VRAM bytes by 2 gives a rough parameter-only estimate. Training also needs memory for gradients, optimizer state, and intermediate values, so the estimate is not a model-size guarantee.

GPU work is asynchronous: Python may continue before the GPU finishes an operation. `torch.cuda.synchronize()` waits for outstanding GPU work, which is needed for accurate timing.

## Colab setup and results

Selected a T4 GPU in Google Colab using **Runtime → Change runtime type → T4 GPU**. `nvidia-smi` reported a Tesla T4, driver version 580.82.07, CUDA 13.0, and 15,360 MiB of GPU memory.

PyTorch in the Colab runtime reported:

```text
PyTorch: 2.11.0+cu130
CUDA available: True
GPU: Tesla T4
```

Ran a 5000 × 5000 matrix multiplication on CPU and GPU. The first GPU run included startup overhead; the second run was used as the comparison:

| Device | Time |
|---|---:|
| CPU | 2.305 s |
| Tesla T4 GPU | 0.087 s |
| Speedup | 26× |

Measured GPU memory was 15.6 GB. The rough fp16 parameter-only estimate was 7.8 billion parameters. Actual training capacity is lower because other training data also uses VRAM.

These timings describe this Colab session and this matrix multiplication; they are not guaranteed speedups for other workloads. The benchmark times matrix multiplication after transferring inputs to the GPU, and synchronizes around the GPU measurement.

## Code

[`code/gpu_check.py`](code/gpu_check.py) checks PyTorch and CUDA availability, reports GPU memory, estimates fp16 parameter capacity, and benchmarks CPU versus GPU matrix multiplication. On a machine without CUDA, it reports that and exits without attempting the GPU benchmark.

## Review

Quiz score: **2/3**. Reviewed on 2026-11-02: CUDA operations are asynchronous, so `torch.cuda.synchronize()` makes Python wait for the GPU to finish before the benchmark timer stops.
