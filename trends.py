import requests
import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine

load_dotenv()
TOKEN = os.getenv("TOKEN")

# Настройки базы данных (локальный Docker на Mac)
DB_CONFIG = {
    "user": "admin",
    "password": "1212",
    "host": "localhost",
    "port": "5432",
    "database": "mpstats"
}

CATEGORY_PATH = "Товары для дома/Хозяйственные товары/Товары для ухода за одеждой и бельем/Вешалки напольные"
BASE_URL = "https://mpstats.io/api/ym/get/category/trends"

params = {
    "path": CATEGORY_PATH,
    "view": "itemsInCategory",
    "trends_by": "month"
}

headers = {
    "X-Mpstats-TOKEN": TOKEN,
    "Content-Type": "application/json"
}

response = requests.get(BASE_URL, params=params, json={}, headers=headers, timeout=30)

if response.status_code == 200:
    data = response.json()
    data_list = data.get("data", data) if isinstance(data, dict) else data
    df = pd.DataFrame(data_list)

    # 1. Сохраняем резервную копию в CSV
    df.to_csv("trends.csv", index=False, encoding="utf-8-sig")
    print("✅ CSV сохранен")

    # 2. Подготовка данных для БД
    # Здесь можно переименовать колонки, если API отдает другие имена
    # df = df.rename(columns={'api_name': 'db_name'})

    # 3. Подключение и загрузка в PostgreSQL
    try:
        engine = create_engine(
            f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}")

        # Загружаем данные в таблицу 'test'
        # if_exists='append' будет добавлять новые данные к старым
        df.to_sql('test', engine, if_exists='append', index=False)

        print(f"🚀 Данные успешно улетели в базу! Загружено строк: {len(df)}")
    except Exception as e:
        print(f"❌ Ошибка при работе с БД: {e}")
else:
    print(f"🛑 Ошибка API: {response.status_code}")