FROM python:3.7 AS build
COPY requirements.txt .
RUN pip install -r requirements.txt

FROM python:3.7-slim
COPY --from=build /usr/local/lib/python3.7 /usr/local/lib/python3.7
WORKDIR /app
COPY bot.py .
CMD ["python", "bot.py"]
