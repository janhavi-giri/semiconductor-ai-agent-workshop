# Semiconductor AI Agent Workshop

A public, vendor-neutral workshop for learning Agentic AI with synthetic semiconductor wafer analytics.

## Learning outcomes

- Generate reproducible synthetic wafer measurements.
- Compare K-means, DBSCAN, and hierarchical clustering.
- Wrap deterministic analytics as agent tools.
- Build a ReAct agent using a public OpenAI-compatible provider.
- Launch a Gradio UI locally or with Docker.


## Local setup

```powershell
Set-Location C:\GitHub\semiconductor-ai-agent-workshop
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
Copy-Item .env.example .env
notepad .env
python run_ui.py
```

Open [the local workshop UI](http://localhost:7860).

## Student setup
Follow the STUDENT_DOCKER_QUICKSTART.md to build the image, run the container, and launch the workshop UI.
## Docker setup

```powershell
Set-Location C:\GitHub\semiconductor-ai-agent-workshop
Copy-Item .env.example .env
notepad .env
docker build --tag semiconductor-ai-agent-workshop --file docker\Dockerfile .
docker run --name semiconductor-ai-workshop --publish 7860:7860 --env-file .env semiconductor-ai-agent-workshop
```

## Public provider configuration

```text
OPENAI_API_KEY=replace-with-your-own-key
OPENAI_MODEL=gpt-4o-mini
OPENAI_BASE_URL=https://api.openai.com/v1
```

Do not commit `.env`. The supplied data is synthetic and intended only for education.
