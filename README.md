# Open Claw

Run a lightweight demo to visualize and operate the Open Claw interface.

## Run locally

```bash
python3 open_claw.py --port 8000
```

Then open [http://localhost:8000](http://localhost:8000) in your browser.

## Repository setup

```bash
# On Windows, open Ubuntu via WSL first
wsl -d ubuntu

# Clone the repository
git clone https://github.com/deepspace28/openclaw.git
cd openclaw
```

## Environment configuration

Create an environment file for secrets and runtime configuration:

```bash
cp .env.example .env
```

Populate `.env` with required values (tokens, API keys, etc.). If you do not yet have an `.env.example`, create one with the variables your deployment expects.
