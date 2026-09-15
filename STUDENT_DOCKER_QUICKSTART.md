# Student Docker Quick Start Guide

Welcome to the **Semiconductor AI Agent Workshop**.

This guide takes you from installing Docker to running a working Agentic AI application that analyzes synthetic semiconductor wafer data.

## What you will learn

By completing this quick start, you will:

- Build a Docker image from a Dockerfile.
- Run an AI application inside a Docker container.
- Generate synthetic semiconductor wafer data.
- Use a natural-language agent to call analytical tools.
- Explore clustering results through a browser-based interface.
- Keep API credentials outside source code.

## What you are building

```text
Browser
  |
  v
Gradio web interface
  |
  v
Agentic AI workflow
  |
  v
Analytical tools
  |
  v
Synthetic wafer dataset
```

The application will run locally at [http://localhost:7860](http://localhost:7860).

> **Important:** `localhost` means the application is available only on the computer running the Docker container.

---

## 1. Install the prerequisites

You need:

- Docker Desktop
- Git
- A personal or institution-approved API key for OpenAI or another public OpenAI-compatible provider

### Install Docker Desktop

Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop/).

Start Docker Desktop and wait until the Docker Engine is running.

Open PowerShell and verify Docker:

```powershell
docker version
```

A working installation displays both `Client` and `Server` sections.

If the `Server` section is missing, open Docker Desktop and wait for the engine to finish starting.

### Verify Git

```powershell
git --version
```

If Git is unavailable, install [Git for Windows](https://git-scm.com/download/win).

---

## 2. Clone the workshop repository

Create a local workspace:

```powershell
New-Item -ItemType Directory -Path C:\GitHub -Force
Set-Location C:\GitHub
```

Clone the repository:

```powershell
git clone https://github.com/janhavi-giri/semiconductor-ai-agent-workshop.git
```

Open the repository directory:

```powershell
Set-Location C:\GitHub\semiconductor-ai-agent-workshop
```

Verify the files:

```powershell
Get-ChildItem -Force
```

You should see folders such as:

```text
src
data
notebooks
exercises
solutions
slides
docker
tests
```

---

## 3. Create your local environment file

Copy the provided environment template:

```powershell
Copy-Item -Path .env.example -Destination .env
```

Open the local environment file:

```powershell
notepad .env
```

For standard OpenAI, use:

```text
OPENAI_API_KEY=replace-with-your-own-key
OPENAI_MODEL=gpt-4o-mini
OPENAI_BASE_URL=https://api.openai.com/v1
```

Replace `replace-with-your-own-key` with your personal or institution-approved key.

For another public OpenAI-compatible service, use the model name and base URL documented by that provider.

### Protect your API key

- Do not commit `.env` to Git.
- Do not paste your key into Python source code.
- Do not include your key in screenshots, notebooks, issue descriptions, or chat messages.
- Rotate the key immediately if it is exposed.

Verify that Git ignores `.env`:

```powershell
git check-ignore -v .env
```

The output should show that `.env` is excluded by `.gitignore`.

Confirm that `.env` is not tracked:

```powershell
git ls-files .env
```

This command should produce no output.

---

## 4. Build the Docker image

Make sure PowerShell is in the repository root:

```powershell
Set-Location C:\GitHub\semiconductor-ai-agent-workshop
```

Build the image:

```powershell
docker build --tag semiconductor-ai-agent-workshop --file docker\Dockerfile .
```

Docker will:

1. Download the Python base image.
2. Install the required Python packages.
3. Copy the workshop source code into the image.
4. Configure the application to run on port 7860.

Verify the image:

```powershell
docker images semiconductor-ai-agent-workshop
```

You should see an image named:

```text
semiconductor-ai-agent-workshop
```

---

## 5. Run the workshop container

Remove an older workshop container if one already exists:

```powershell
docker rm --force semiconductor-ai-workshop
```

If Docker reports that the container does not exist, continue.

Start the application:

```powershell
docker run --name semiconductor-ai-workshop --publish 7860:7860 --env-file .env semiconductor-ai-agent-workshop
```

Leave this PowerShell window open while using the application.

A blinking cursor is normal because the application is running in the foreground.

---

## 6. Verify that the container is running

Open a second PowerShell window and run:

```powershell
docker ps --filter name=semiconductor-ai-workshop
```

The output should show:

- Container name `semiconductor-ai-workshop`
- Status beginning with `Up`
- Port mapping from host port 7860 to container port 7860

View recent application logs:

```powershell
docker logs --tail 100 semiconductor-ai-workshop
```

---

## 7. Open the workshop UI

Open [the Semiconductor AI Agent Workshop](http://localhost:7860) in your browser.

You should see tabs for:

- **Setup**
- **Chat**
- **Visualize**

---

## 8. Initialize the agent

In the **Setup** tab:

1. Select **Initialize agent**.
2. Confirm that the status displays:

```text
Agent initialized.
```

If initialization fails, check that `.env` contains a valid API key, model name, and base URL.

---

## 9. Generate synthetic wafer data

In the **Setup** tab:

1. Select the desired synthetic wafer count. Start with 600.
2. Select **Generate synthetic data**.
3. Confirm that the dataset preview appears.
4. Confirm that the dataset status reports the number of generated wafers.

The workshop uses synthetic data. The generated values do not represent an actual semiconductor fabrication facility.

---

## 10. Ask the agent questions

Open the **Chat** tab.

Start with:

```text
Inspect the dataset and describe the available features.
```

Then try:

```text
Find the optimal number of clusters for this dataset.
```

Apply clustering:

```text
Apply K-means clustering with four clusters.
```

Analyze the result:

```text
Summarize the characteristics of each cluster.
```

The language model coordinates the workflow, while deterministic Python tools perform the data inspection and clustering calculations.

---

## 11. Create a visualization

Open the **Visualize** tab.

1. Select a cluster count, such as 4.
2. Select **Create PCA cluster plot**.
3. Confirm that a two-dimensional cluster visualization appears.

PCA means Principal Component Analysis. The plot projects the standardized process features into two dimensions to support visual exploration.

---

## 12. Understand the Docker concepts

### Image

A Docker image is the reusable application template.

List images:

```powershell
docker images semiconductor-ai-agent-workshop
```

### Container

A container is a running instance of an image.

List running containers:

```powershell
docker ps
```

### Port mapping

This part of the run command:

```text
--publish 7860:7860
```

maps port 7860 on your computer to port 7860 inside the container.

### Environment variables

This part:

```text
--env-file .env
```

passes local configuration to the container without placing the API key in source code or in the Docker image.

---

## 13. Useful Docker commands

### View running containers

```powershell
docker ps
```

### View all containers

```powershell
docker ps --all
```

### View application logs

```powershell
docker logs --tail 100 semiconductor-ai-workshop
```

### Follow live logs

```powershell
docker logs --follow semiconductor-ai-workshop
```

Press `Ctrl+C` to stop following the logs. This does not stop the container.

### Stop the container

```powershell
docker stop semiconductor-ai-workshop
```

### Restart the existing container

```powershell
docker start --attach semiconductor-ai-workshop
```

### Remove the container

```powershell
docker rm semiconductor-ai-workshop
```

### Remove the image

```powershell
docker rmi semiconductor-ai-agent-workshop
```

---

## 14. Rebuild after changing the source code

If you update files under `src`, rebuild and recreate the container:

```powershell
Set-Location C:\GitHub\semiconductor-ai-agent-workshop
docker rm --force semiconductor-ai-workshop
docker build --no-cache --tag semiconductor-ai-agent-workshop --file docker\Dockerfile .
docker run --name semiconductor-ai-workshop --publish 7860:7860 --env-file .env semiconductor-ai-agent-workshop
```

A change to `.env` does not require an image rebuild. Remove and recreate the container so Docker reads the updated environment file.

---

## Troubleshooting

### Docker command is not recognized

Confirm that Docker Desktop is installed and running:

```powershell
docker version
```

### Docker Server section is missing

Open Docker Desktop and wait for the Docker Engine to start. Then run:

```powershell
docker version
```

### Container name is already in use

```powershell
docker rm --force semiconductor-ai-workshop
```

Then run the container again:

```powershell
docker run --name semiconductor-ai-workshop --publish 7860:7860 --env-file .env semiconductor-ai-agent-workshop
```

### Browser cannot open the UI

Verify that the container is running:

```powershell
docker ps --filter name=semiconductor-ai-workshop
```

Check the logs:

```powershell
docker logs --tail 200 semiconductor-ai-workshop
```

### Agent does not initialize

Verify that the required configuration exists without displaying the API key:

```powershell
docker exec semiconductor-ai-workshop python -c "import os; print('KEY_PRESENT=', bool(os.getenv('OPENAI_API_KEY'))); print('MODEL=', os.getenv('OPENAI_MODEL')); print('BASE_URL=', os.getenv('OPENAI_BASE_URL'))"
```

If `KEY_PRESENT` is `False`, review your local `.env` file.

### Chat reports an analysis or connection error

Check the application logs:

```powershell
docker logs --tail 200 semiconductor-ai-workshop
```

Confirm that:

- The agent was initialized.
- Synthetic data was generated.
- The provider key is valid.
- The configured model is available to your account.
- The base URL matches the provider's documentation.

---

## Completion checklist

You have completed the Docker quick start when:

- Docker Desktop is running.
- The workshop image builds successfully.
- The container has an `Up` status.
- [The local UI](http://localhost:7860) opens.
- The agent initializes successfully.
- Synthetic wafer data is generated.
- Chat returns an analytical response.
- The PCA visualization renders.
- `.env` remains untracked by Git.

Congratulations. You now have a working Agentic AI application running in Docker.
