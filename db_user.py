import sqlite3

def create_tables():
    conn = sqlite3.connect('fitness_tracker.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            weight REAL,
            height REAL,
            goals TEXT
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS workouts (
            user_id INTEGER,
            date TEXT,
            exercise TEXT,
            duration REAL,
            intensity TEXT,
            calories_burned REAL,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS nutrition (
            user_id INTEGER,
            date TEXT,
            meal TEXT,
            calories REAL,
            carbs REAL,
            protein REAL,
            fats REAL,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')
    conn.commit()
    conn.close()

create_tables()

def create_user(name, age, weight, height, goals):
    conn = sqlite3.connect('fitness_tracker.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO users (name, age, weight, height, goals)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, age, weight, height, goals))
    conn.commit()
    conn.close()

def get_user(name):
    conn = sqlite3.connect('fitness_tracker.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE name = ?', (name,))
    user = c.fetchone()
    conn.close()
    return user

def log_workout(user_id, date, exercise, duration, intensity, calories_burned):
    conn = sqlite3.connect('fitness_tracker.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO workouts (user_id, date, exercise, duration, intensity, calories_burned)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (user_id, date, exercise, duration, intensity, calories_burned))
    conn.commit()
    conn.close()

def log_nutrition(user_id, date, meal, calories, carbs, protein, fats):
    conn = sqlite3.connect('fitness_tracker.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO nutrition (user_id, date, meal, calories, carbs, protein, fats)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (user_id, date, meal, calories, carbs, protein, fats))
    conn.commit()
    conn.close()