FROM python:3.7 AS build

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY bot bot
COPY run.py .

FROM python:3.7-slim

COPY --from=build /usr/local/lib/python3.7 /usr/local/lib/python3.7

WORKDIR /app
COPY --from=build /app .
CMD ["python", "run.py"]
