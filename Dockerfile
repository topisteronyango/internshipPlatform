FROM python:3.10.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libcairo2-dev

RUN apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt 2>&1 | tee install.log


COPY . .


CMD ["gunicorn", "InternBoard.wsgi:application", "--log-file", "-", "--log-level", "debug"]
