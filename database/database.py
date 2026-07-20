import sqlite3
import bcrypt


def create_connection():
    conn = sqlite3.connect(
        "database/interview_assistant.db",
        check_same_thread=False
    )
    return conn


def create_users_table():

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT NOT NULL,

        email TEXT UNIQUE NOT NULL,

        password TEXT NOT NULL

    )
    """)

    conn.commit()
    conn.close()


def user_exists(email):

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=?",
        (email,)
    )

    user = cursor.fetchone()

    conn.close()

    return user


def insert_user(name, email, password):

    conn = create_connection()
    cursor = conn.cursor()

    hashed_password = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()

    cursor.execute(
        """
        INSERT INTO users(name,email,password)
        VALUES(?,?,?)
        """,
        (
            name,
            email,
            hashed_password
        )
    )

    conn.commit()
    conn.close()


def verify_user(email, password):

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=?",
        (email,)
    )

    user = cursor.fetchone()

    conn.close()

    if user:

        stored_password = user[3]

        if bcrypt.checkpw(
            password.encode(),
            stored_password.encode()
        ):
            return user

    return None