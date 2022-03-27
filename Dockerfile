FROM python:3.10

RUN apt-get update && apt-get install -y git build-essential libssl-dev libffi-dev && \
    pip install poetry

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt


COPY . .
RUN chmod +x ./scripts/entrypoint.sh
CMD ["./scripts/entrypoint.sh"]
