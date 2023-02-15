import sqlite3

conn = sqlite3.connect("summary.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS links (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    link TEXT NOT NULL,
    published_date TEXT
)
""");

cursor.execute("""
CREATE TABLE IF NOT EXISTS passages (
    id INTEGER,
    summary TEXT NOT NULL,
    FOREIGN KEY (id) REFERENCES articles (id)
)
""");

conn.commit()
conn.close()
