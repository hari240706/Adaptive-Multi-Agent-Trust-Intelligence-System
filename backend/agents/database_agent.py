import sqlite3

from datetime import datetime


# =========================
# Database Connection
# =========================

DATABASE_PATH = "amatis_memory.db"


# =========================
# Initialize Database
# =========================

def initialize_database():

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS analyses (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            text TEXT,

            prediction TEXT,

            trust_score REAL,

            timestamp TEXT
        )
        """
    )

    connection.commit()

    connection.close()


# Initialize DB on startup
initialize_database()


# =========================
# Save Analysis
# =========================

def save_analysis(

    text,

    prediction,

    trust_score
):

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO analyses (

            text,

            prediction,

            trust_score,

            timestamp

        )

        VALUES (?, ?, ?, ?)
        """,

        (

            text,

            prediction,

            trust_score,

            datetime.now().isoformat()
        )
    )

    connection.commit()

    connection.close()


# =========================
# Retrieve Recent Analyses
# =========================

def get_recent_analyses(

    limit=10
):

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT

            text,

            prediction,

            trust_score,

            timestamp

        FROM analyses

        ORDER BY id DESC

        LIMIT ?
        """,

        (limit,)
    )

    rows = cursor.fetchall()

    connection.close()

    analyses = []

    for row in rows:

        analyses.append({

            "text":
            row[0],

            "prediction":
            row[1],

            "trust_score":
            row[2],

            "timestamp":
            row[3]
        })

    return analyses


# =========================
# Database Statistics
# =========================

def get_database_stats():

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM analyses
        """
    )

    total_analyses = cursor.fetchone()[0]

    connection.close()

    return {

        "total_analyses":
        total_analyses
    }