import sqlite3

# SQLite 데이터베이스 연결 (또는 생성)
conn = sqlite3.connect('sample.db')
cursor = conn.cursor()

# 샘플 테이블 생성
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    hire_date TEXT,
    salary REAL
)
''')

# 샘플 데이터 삽입
cursor.execute('INSERT INTO employees (first_name, last_name, hire_date, salary) VALUES (?, ?, ?, ?)',
               ('John', 'Doe', '2020-01-15', 60000))
cursor.execute('INSERT INTO employees (first_name, last_name, hire_date, salary) VALUES (?, ?, ?, ?)',
               ('Jane', 'Smith', '2019-03-10', 75000))
cursor.execute('INSERT INTO employees (first_name, last_name, hire_date, salary) VALUES (?, ?, ?, ?)',
               ('Emily', 'Jones', '2021-06-01', 50000))

conn.commit()
conn.close()
