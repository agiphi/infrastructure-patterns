FROM python:3.12-slim

WORKDIR /app
COPY src ./src

ENV PYTHONUNBUFFERED=1
ENV APP_ENV=production

CMD ["python", "-m", "src.app"]
