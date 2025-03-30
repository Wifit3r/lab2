import sqlite3

conn = sqlite3.connect('news.db')  # Використовуйте той самий файл, що і у DBPipeline
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='news';")
table_exists = cursor.fetchone()

if table_exists:
    print("✅ Таблиця 'news' існує")
else:
    print("❌ Таблиці 'news' немає!")

conn.close()
