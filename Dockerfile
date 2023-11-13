# web: gunicorn InternBoard.wsgi:application --log-file - --log-level debug

FROM python:3.10.12-slim

# install needed packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libcairo2-dev

# clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

CMD gunicorn InternBoard.wsgi