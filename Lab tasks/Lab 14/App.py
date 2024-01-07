import sqlite3
import csv

# Create a SQLite database and a table
conn = sqlite3.connect('cricket.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cricket_data (
        Match_Id INTEGER,
        Innings_Id INTEGER,
        Over_Id INTEGER,
        Ball_Id INTEGER,
        Team_Batting_Id INTEGER,
        Team_Bowling_Id INTEGER,
        Striker_Id INTEGER,
        Striker_Batting_Position INTEGER,
        Non_Striker_Id INTEGER,
        Bowler_Id INTEGER,
        Batsman_Scored INTEGER,
        PRIMARY KEY (Match_Id, Innings_Id, Over_Id, Ball_Id)
    )
''')
conn.commit()

# Read CSV file and insert data into the database
with open('Ball_by_Ball.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        # Check if the data already exists in the table
        cursor.execute('''
            SELECT * FROM cricket_data
            WHERE Match_Id = ?, Innings_Id = ?, Over_Id = ?, Ball_Id = ?
        ''', (row[0], row[1], row[2], row[3]))
        existing_data = cursor.fetchone()

        if existing_data is None:
            # Insert the data into the table
            cursor.execute('''
                INSERT INTO cricket_data (
                    Match_Id, Innings_Id, Over_Id, Ball_Id, Team_Batting_Id,
                    Team_Bowling_Id, Striker_Id, Striker_Batting_Position,
                    Non_Striker_Id, Bowler_Id, Batsman_Scored
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
        else:
            # Skip inserting the data because it already exists
            pass

        conn.commit()
