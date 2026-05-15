# Intro

Attempting to run a self hosted github runner that connects with the self hosted instance https://github.com/thodkatz/DashVERSE within the LAN of INAB-CERTH.

## Self-hosted runner setup

A self-hosted runner is a process running on your own machine (or VM) that picks up GitHub Actions jobs. It connects outbound to GitHub over HTTPS, so no inbound ports or firewall rules are needed. This is the right choice when your DashVERSE instance is on a private LAN that GitHub-hosted runners cannot reach.

### Option 1: Repository-level runner

Scoped to a single repository. Go to:

**Repository → Settings → Actions → Runners → New self-hosted runner**

Follow the instructions GitHub provides to download, configure, and start the runner:

```bash
# Configure (use the token GitHub gives you)
./config.sh --url https://github.com/<org>/<repo> --token <token>

# Run interactively (for testing)
./run.sh

# Or install as a system service (for permanent use)
sudo ./svc.sh install
sudo ./svc.sh start
```

### Option 2: Organization-level runner (recommended)

Scoped to all repositories in the org. A single runner handles every repo without repeating the setup. Go to:

**Organization → Settings → Actions → Runners → New self-hosted runner**

The configuration and startup commands are identical — only the `--url` changes:

```bash
./config.sh --url https://github.com/<org> --token <token>
```

## Workflow setup

1. Create a `resqui` environment in your repository: **Settings → Environments → New environment**
2. Add `DASHVERSE_TOKEN` as a secret to that environment (obtain it from your DashVERSE instance via `make jwt`)
3. Push to the repository — the workflow in `.github/workflows/resqui.yml` triggers automatically on every push and pull request

## What the workflow checks

The workflow runs `configurations/basic.json`, which checks:

- `has_license` — a `LICENSE` file must exist in the repository root
- `has_citation` — a valid `CITATION.cff` file must exist in the repository root

Results are uploaded to your DashVERSE instance if `DASHVERSE_TOKEN` is provided.

