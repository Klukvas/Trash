FROM python:3.10.5-slim-buster
RUN pip install pipenv
RUN pip install aiohttp
RUN apt-get update && apt-get install -y --no-install-recommends gcc
COPY . .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --system --deploy