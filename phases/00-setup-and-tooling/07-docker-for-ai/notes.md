# Docker for AI

Course lesson: [Docker for AI](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/07-docker-for-ai/docs/en.md)

**Date studied:** 2026-11-09  
**Quiz:** 3/3

## What I learned

- A Docker image packages an application environment; a container runs that image while sharing the host OS kernel.
- The CUDA runtime and libraries can be in the image, while the NVIDIA driver and physical GPU come from the host.
- Volume mounts keep code, models, and datasets available outside the container so they persist across container rebuilds.
- Docker Compose creates a shared network and DNS names, so one service can reach another by its service name (for example, `http://qdrant:6333`).

## Exercise evidence

Docker is not installed in this workspace, and no Docker socket or NVIDIA device is available. The commands below have not been run here; add their outputs and results when running the lesson on a Docker-capable machine.

| Exercise | Evidence to record | Status |
|---|---|---|
| Build image and check PyTorch | Build command, exit code, image tag, PyTorch version, and CUDA availability | Pending: Docker unavailable |
| Start Compose stack and check Qdrant | `docker compose up -d` result and response from `curl http://qdrant:6333/collections` inside `ai-dev` | Pending: Docker unavailable |
| Add Flask and run a simple API | Dockerfile change, rebuild result, port mapping, and successful request to `http://localhost:5000` | Pending: Docker unavailable |
| Compare base image sizes | `docker images` sizes for the `devel` and `runtime` builds | Pending: Docker unavailable |

## Artifacts

- [`code/Dockerfile`](code/Dockerfile) — CUDA, Python, PyTorch, and AI development tools.
- [`code/docker-compose.yml`](code/docker-compose.yml) — AI development container and Qdrant service.
