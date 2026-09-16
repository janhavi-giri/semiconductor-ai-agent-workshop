# Daily Repository Refresh Workflow

Use this guide to update a local copy of the **Semiconductor AI Agent Workshop** repository and run the latest application version.

## What this workflow does

```text
GitHub repository
       |
       | git pull
       v
Local repository
       |
       | docker build
       v
Updated Docker image
       |
       | docker run
       v
Updated workshop UI
```

> **Important:** `git pull` updates the files in the local repository. It does not automatically update an existing Docker image or container.

---

## Quick daily refresh workflow

Open PowerShell and run:

```powershell
Set-Location C:\GitHub\semiconductor-ai-agent-workshop
git pull origin main
docker rm --force semiconductor-ai-workshop
docker build --tag semiconductor-ai-agent-workshop --file docker\Dockerfile .
docker run --name semiconductor-ai-workshop --publish 7860:7860 --env-file .env semiconductor-ai-agent-workshop
```

If Docker reports that the container `semiconductor-ai-workshop` does not exist during the removal command, continue to the build command.

Leave the PowerShell window open while the application is running.

Open [the local Semiconductor AI Agent Workshop UI](http://localhost:7860) in a browser.

---

## Step-by-step workflow

### 1. Open the local repository

```powershell
Set-Location C:\GitHub\semiconductor-ai-agent-workshop
```

### 2. Check for uncommitted local changes

```powershell
git status
```

If the output says:

```text
nothing to commit, working tree clean
```

continue to the pull command.

If files have local changes, either commit the changes or temporarily store them before pulling.

#### Option A: Commit local changes

```powershell
git add .
git commit -m "Save local workshop updates"
git pull origin main
```

#### Option B: Temporarily store local changes

```powershell
git stash push -m "Temporary changes before repository refresh"
git pull origin main
git stash pop
```

Review and resolve any merge conflicts before rebuilding the application.

### 3. Pull the latest version from GitHub

```powershell
git pull origin main
```

Possible results include:

```text
Already up to date.
```

or a list of files that were added, modified, or deleted.

### 4. Review what changed

Show the latest commits:

```powershell
git log --oneline -5
```

Show the files changed by the latest commit:

```powershell
git show --stat --oneline HEAD
```

Show the complete changes in the latest commit:

```powershell
git show HEAD
```

### 5. Decide whether Docker must be rebuilt

Rebuild the image when any of these files or folders changed:

```text
src/
run_ui.py
requirements.txt
docker/Dockerfile
docker/docker-compose.yml
```

A rebuild is normally not required when only these files changed:

```text
README.md
STUDENT_DOCKER_QUICKSTART.md
WORKSHOP_GUIDE.md
SECURITY.md
exercises/
notebooks/
slides/
```

If only documentation or teaching materials changed, the local files are already updated after `git pull`.

### 6. Remove the previous container

```powershell
docker rm --force semiconductor-ai-workshop
```

If Docker reports that the container does not exist, continue.

### 7. Rebuild the Docker image

```powershell
docker build --tag semiconductor-ai-agent-workshop --file docker\Dockerfile .
```

Use a full no-cache rebuild when dependencies, the Dockerfile, or the runtime environment changed:

```powershell
docker build --no-cache --tag semiconductor-ai-agent-workshop --file docker\Dockerfile .
```

### 8. Run the updated container

```powershell
docker run --name semiconductor-ai-workshop --publish 7860:7860 --env-file .env semiconductor-ai-agent-workshop
```

A blinking cursor is normal because the application is running in the foreground.

### 9. Verify that the application is running

Open a second PowerShell window and run:

```powershell
docker ps --filter name=semiconductor-ai-workshop
```

The container status should begin with:

```text
Up
```

Review recent logs:

```powershell
docker logs --tail 100 semiconductor-ai-workshop
```

### 10. Open the updated UI

Open [the local workshop UI](http://localhost:7860).

Confirm that:

- The Setup tab opens.
- The agent initializes.
- Synthetic wafer data can be generated.
- Chat returns a response.
- The PCA visualization renders.

---

## When a Docker rebuild is not needed

If `git pull` updates only documentation, notebooks, exercises, solutions, or workshop slides, a Docker rebuild is not required unless those files are intentionally copied into the image.

Examples:

```text
README.md
STUDENT_DOCKER_QUICKSTART.md
WORKSHOP_GUIDE.md
exercises/03_build_a_tool.md
slides/Agentic_AI_Workshop.pptx
```

Use the updated files directly from the local repository.

---

## When a Docker rebuild is required

Rebuild when the running application or its Python environment changed.

Examples:

```text
src/agent.py
src/clustering.py
src/synthetic_data.py
src/tools.py
src/ui.py
run_ui.py
requirements.txt
docker/Dockerfile
```

Use:

```powershell
docker rm --force semiconductor-ai-workshop
docker build --no-cache --tag semiconductor-ai-agent-workshop --file docker\Dockerfile .
docker run --name semiconductor-ai-workshop --publish 7860:7860 --env-file .env semiconductor-ai-agent-workshop
```

---

## If the local `.env` file is missing

Create it from the template:

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

Do not commit `.env`.

Verify that Git ignores it:

```powershell
git check-ignore -v .env
```

---

## Verify synchronization with GitHub

Fetch the latest remote information:

```powershell
git fetch origin
```

Check the current branch status:

```powershell
git status
```

A synchronized repository should report:

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

Compare the current local and remote commit identifiers:

```powershell
git rev-parse HEAD
git rev-parse origin/main
```

The two commit identifiers should match when the local `main` branch and `origin/main` are synchronized.

---

## Publishing local changes

Use `git push` only when local changes should be published to GitHub.

```powershell
git add .
git status --short
git diff --cached
git commit -m "Describe the workshop update"
git push origin main
```

Direction of the two commands:

```text
git pull: GitHub to the local repository
git push: local repository to GitHub
```

---

## Troubleshooting

### Pull is blocked by local changes

Check the affected files:

```powershell
git status
```

Commit or stash the local changes before pulling.

### Container name is already in use

```powershell
docker rm --force semiconductor-ai-workshop
```

Then run the container again.

### The UI still shows the previous version

Remove the old container and rebuild without cache:

```powershell
docker rm --force semiconductor-ai-workshop
docker build --no-cache --tag semiconductor-ai-agent-workshop --file docker\Dockerfile .
docker run --name semiconductor-ai-workshop --publish 7860:7860 --env-file .env semiconductor-ai-agent-workshop
```

Refresh [the local workshop UI](http://localhost:7860) after the new container starts.

### The container stops unexpectedly

```powershell
docker ps --all --filter name=semiconductor-ai-workshop
docker logs --tail 200 semiconductor-ai-workshop
```

### The agent does not initialize

Verify local configuration without displaying the API key:

```powershell
docker exec semiconductor-ai-workshop python -c "import os; print('KEY_PRESENT=', bool(os.getenv('OPENAI_API_KEY'))); print('MODEL=', os.getenv('OPENAI_MODEL')); print('BASE_URL=', os.getenv('OPENAI_BASE_URL'))"
```

---

## Recommended repository location

Add this document to the workshop repository as:

```text
DAILY_REPOSITORY_REFRESH.md
```

Link it from `README.md` with:

```markdown
## Keeping the workshop current

Use the [Daily Repository Refresh Workflow](DAILY_REPOSITORY_REFRESH.md) to pull updates and rebuild the Docker application when needed.
```
