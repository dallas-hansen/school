import sqlite3

def initialize_db():
    con = sqlite3.connect('workout_log.db')
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        dob TEXT,
        gender TEXT,
        height REAL,
        weight REAL,
        email TEXT,
        password TEXT
        )""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS sessions (
        session_id INTEGER PRIMARY KEY,
        user_id INTEGER,
        date TEXT NOT NULL,
        time TEXT NOT NULL,
        sleep_quality INTEGER,
        mood TEXT,
        energy_level INTEGER,
        notes TEXT,
        FOREIGN KEY(user_id) REFERENCES users(user_id)
        )""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS exercises (
        exercise_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        equipment TEXT,
        notes TEXT
        )""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS session_exercises (
        session_exercise_id INTEGER PRIMARY KEY,
        session_id INTEGER,
        exercise_id INTEGER,
        variaton TEXT,
        notes TEXT,
        FOREIGN KEY(session_id) REFERENCES sessions(session_id),
        FOREIGN KEY(exercise_id) REFERENCES exercises(exercise_id)
        )""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS sets (
        set_id INTEGER PRIMARY KEY,
        session_exercise_id INTEGER,
        set_number INTEGER,
        reps INTEGER,
        weight REAL,
        rest_time INTEGER,
        rpe INTEGER,
        rir INTEGER,
        notes TEXT,
        FOREIGN KEY(session_exercise_id) REFERENCES session_exercises(session_exercise_id)
        )""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS cardio (
        cardio_id INTEGER PRIMARY KEY,
        session_id INTEGER,
        exercise_id INTEGER,
        distance REAL,
        duration INTEGER,
        starting_heart_rate INTEGER,
        ending_heart_rate INTEGER,
        avg_heart_rate INTEGER,
        calories_burned INTEGER,
        notes TEXT,
        FOREIGN KEY(session_id) REFERENCES sessions(session_id),
        FOREIGN KEY(exercise_id) REFERENCES exercises(exercise_id)
        )""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS body_stats (
        body_stat_id INTEGER PRIMARY KEY,
        user_id INTEGER,
        date TEXT NOT NULL,
        weight REAL,
        height REAL,
        bmi REAL,
        waist REAL,
        chest REAL,
        arms REAL,
        notes TEXT,
        FOREIGN KEY(user_id) REFERENCES users(user_id)
        )""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS pr (
        pr_id INTEGER PRIMARY KEY,
        user_id INTEGER,
        exercise_id INTEGER,
        date TEXT NOT NULL,
        weight REAL,
        reps INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(user_id),
        FOREIGN KEY(exercise_id) REFERENCES exercises(exercise_id)
        )""")
    
    
    con.commit()
    con.close()

if __name__ == "__main__":
    initialize_db()