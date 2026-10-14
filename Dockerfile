FROM python:3.12-alpine3.24

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk upgrade --no-cache

COPY requirements.txt .
RUN python -m pip install --no-cache-dir --upgrade "pip==26.2.0" \
    && python -m pip install --no-cache-dir -r requirements.txt \
    && python -m pip install --no-cache-dir "gunicorn==26.2.0" \
    && python -m pip uninstall -y pip

RUN adduser -D -u 1000 appuser

COPY --chown=appuser:appuser . .

USER appuser

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]