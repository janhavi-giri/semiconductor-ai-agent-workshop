# Semiconductor AI Agent Workshop

A public, vendor-neutral workshop for learning Agentic AI through synthetic semiconductor wafer analytics.

This repository combines synthetic data generation, clustering, deterministic analytical tools, a ReAct agent, a Gradio interface, guided notebooks, hands-on exercises, and Docker-based deployment.

> **Educational use only:** The supplied wafer data is synthetic and does not represent measurements from an actual semiconductor fabrication facility.

## Learning outcomes

By completing the workshop, students will be able to:

- Generate reproducible synthetic wafer measurements.
- Compare K-means, DBSCAN, and hierarchical clustering.
- Standardize process features and evaluate clusters with silhouette score.
- Wrap deterministic analytics as tools for an AI agent.
- Build a ReAct agent using a public OpenAI-compatible provider.
- Launch and use a Gradio web interface.
- Package and run the application with Docker.
- Keep API credentials outside source code and Git.

## Architecture

```text
Browser
  |
  v
Gradio web interface
  |
  v
ReAct agent
  |
  v
Deterministic analytical tools
  |
  v
Synthetic wafer dataset
```

The language model coordinates the workflow and selects tools. Python functions perform the data inspection, clustering, and cluster-summary calculations.

## Student setup

New to Docker or the workshop repository?

Follow the [Student Docker Quick Start Guide](docs/STUDENT_DOCKER_QUICKSTART.md).

The guide covers:

- Installing Docker Desktop and Git.
- Cloning the repository.
- Configuring a public OpenAI-compatible provider.
- Building the Docker image.
- Running and verifying the container.
- Initializing the agent.
- Generating synthetic wafer data.
- Using Chat and Visualize.
- Troubleshooting common setup issues.

## Public provider configuration

Create a local `.env` file from the included template:

```powershell
Copy-Item -Path .env.example -Destination .env
notepad .env
```

For standard OpenAI, configure:

```text
OPENAI_API_KEY=replace-with-your-own-key
OPENAI_MODEL=gpt-4o-mini
OPENAI_BASE_URL=https://api.openai.com/v1
```

For another public OpenAI-compatible provider, use the model name and base URL documented by that provider.

### Protect your credentials

- Do not commit `.env`.
- Do not place API keys in source code, notebooks, screenshots, issues, or documentation.
- Use a personal or institution-approved key.
- Rotate a key immediately if it is exposed.

Verify that `.env` is ignored:

```powershell
git check-ignore -v .env
```

Confirm that `.env` is not tracked:

```powershell
git ls-files .env
```

The second command should produce no output.

## Repository structure

```text
semiconductor-ai-agent-workshop/
├── README.md
├── WORKSHOP_GUIDE.md
├── SECURITY.md
├── LICENSE
├── requirements.txt
├── .env.example
├── run_ui.py
├── src/
│   ├── agent.py
│   ├── clustering.py
│   ├── synthetic_data.py
│   ├── tools.py
│   └── ui.py
├── data/
│   └── synthetic_wafer_data.csv
├── notebooks/
│   ├── 01_generate_dataset.ipynb
│   ├── 02_clustering.ipynb
│   ├── 03_agent_tools.ipynb
│   └── 04_gradio_interface.ipynb
├── exercises/
│   ├── 01_data_exploration.md
│   ├── 02_clustering.md
│   ├── 03_build_a_tool.md
│   ├── 04_agent_extension.md
│   └── 05_container_and_demo.md
├── solutions/
│   └── 03_build_a_tool_solution.py
├── slides/
│   └── Agentic_AI_Workshop.pptx
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── docs/
│   └── STUDENT_DOCKER_QUICKSTART.md
└── tests/
    └── test_clustering.py
```

## Workshop sequence

### 1. Generate synthetic data

Use `src/synthetic_data.py` or the first notebook to generate a reproducible dataset containing wafer yield, defect density, temperature, pressure, process time, and thickness measurements.

### 2. Explore clustering

Use `src/clustering.py` and the second notebook to compare:

- K-means
- DBSCAN
- Hierarchical clustering

### 3. Work with deterministic tools

Use `src/tools.py` and the third notebook to inspect the dataset, evaluate candidate cluster counts, apply K-means, and summarize cluster characteristics.

### 4. Run the agent

Use `src/agent.py` to connect the tools to a ReAct agent. The agent should call tools for computation and explain that the data is synthetic.

### 5. Use the web interface

Use `src/ui.py` and `run_ui.py` to initialize the agent, generate data, ask analytical questions, and create a PCA cluster visualization.

### 6. Complete the exercises

The `exercises` folder contains five progressive activities covering data exploration, clustering, tool creation, agent extension, and Docker deployment.

## Quick Docker commands

The detailed explanation is in the [Student Docker Quick Start Guide](docs/STUDENT_DOCKER_QUICKSTART.md). Experienced Docker users can use this condensed sequence:

```powershell
Set-Location C:\GitHub\semiconductor-ai-agent-workshop
Copy-Item -Path .env.example -Destination .env
notepad .env
docker build --tag semiconductor-ai-agent-workshop --file docker\Dockerfile .
docker rm --force semiconductor-ai-workshop
docker run --name semiconductor-ai-workshop --publish 7860:7860 --env-file .env semiconductor-ai-agent-workshop
```

If Docker reports that `semiconductor-ai-workshop` does not exist during the removal command, continue to the run command.

After the container starts, open [the local workshop UI](http://localhost:7860).

## Suggested agent questions

After initializing the agent and generating synthetic data, try:

```text
Inspect the dataset and describe the available features.
```

```text
Find the optimal number of clusters for this dataset.
```

```text
Apply K-means clustering with four clusters.
```

```text
Summarize the characteristics of each cluster.
```

## Run the tests

Create a Python environment and install the dependencies before running the tests:

```powershell
Set-Location C:\GitHub\semiconductor-ai-agent-workshop
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pytest -q
```

## Instructor resources

- `WORKSHOP_GUIDE.md` provides a suggested teaching sequence.
- `slides/Agentic_AI_Workshop.pptx` provides the workshop presentation.
- `notebooks` provides guided demonstrations.
- `exercises` provides student assignments.
- `solutions` provides instructor reference material.

## Security and responsible use

Review `SECURITY.md` before publishing changes or using the repository in a class.

Key requirements:

- Use synthetic data for public demonstrations.
- Do not commit API keys or `.env`.
- Do not add private, proprietary, or personally identifiable data.
- Keep TLS certificate verification enabled.
- Review staged changes before every commit.

```powershell
git status --short
git diff --cached
```

## License

This workshop is provided under the MIT License. See `LICENSE` for details.
