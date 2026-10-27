import sqlite3

DB_NAME = "students.db"


def create_table():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS students ("
        "roll_no INTEGER PRIMARY KEY, "
        "name TEXT NOT NULL)"
    )
    conn.commit()
    conn.close()


def insert_student(roll_no, name):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("INSERT INTO students (roll_no, name) VALUES (?, ?)", (roll_no, name))
    conn.commit()
    conn.close()


def fetch_students():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT roll_no, name FROM students")
    rows = cur.fetchall()
    conn.close()
    return rows


if __name__ == "__main__":
    create_table()
    try:
        insert_student(1, "Divya")
    except sqlite3.IntegrityError:
        pass
    for row in fetch_students():
        print(row)
