FROM python:3.9

WORKDIR /app

COPY ./app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY alembic.ini /app/alembic.ini
COPY alembic /app/alembic

COPY app /app

EXPOSE 8000

CMD ["sh", "-c", " uvicorn app.main:app --host 0.0.0.0 --port 8000"]
