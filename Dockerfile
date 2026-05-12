FROM apache/superset:latest
USER root

# 1. Ставим системные пакеты для сборки и библиотеки PostgreSQL
RUN apt-get update && apt-get install -y curl gcc libpq-dev

# 2. Скачиваем чистый pip и внедряем его прямо в виртуальное окружение Superset
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | /app/.venv/bin/python

# 3. Ставим драйверы для Postgres и коннектор для Google Таблиц
RUN /app/.venv/bin/python -m pip install \
    psycopg2 \
    psycopg2-binary \
    "shillelagh[gsheetsapi]"

# Возвращаем права для безопасности
USER superset