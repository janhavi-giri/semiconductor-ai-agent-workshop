FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY src ./src
COPY run_ui.py .
EXPOSE 7860
CMD ["python","run_ui.py"]
