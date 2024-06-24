import sqlite3
import os
import sensitive_data as sd

def create_cur():
    con = sqlite3.connect(sd.DB_NAME)
    return con.cursor()
def create_tables():
    cur=create_cur()
    cur.execute("""
    CREATE TABLE games (
        id int NOT NULL CONSTRAINT games_pk PRIMARY KEY,
        Name nvarchar(50) NOT NULL,
        entry_fee int NOT NULL,
        minim_players int NOT NULL,
        max_players int NOT NULL
    );""")
    cur.execute("""
    CREATE TABLE games_played (
        session_id int NOT NULL CONSTRAINT games_played_pk PRIMARY KEY,
        game_id int NOT NULL,
        user_id int NOT NULL,
        guild_id int NOT NULL,
        bet int NOT NULL,
        result int NOT NULL,
        Users_user_id int NOT NULL,
        CONSTRAINT games_played_Games FOREIGN KEY (game_id)
        REFERENCES games (id),
        CONSTRAINT games_played_Users FOREIGN KEY (user_id)
        REFERENCES users (user_id)
    );""")
    cur.execute("""
    CREATE TABLE users (
        user_id int NOT NULL CONSTRAINT users_pk PRIMARY KEY,
        user_guild int NOT NULL,
        credits int NOT NULL
    );""")
def delete_db():
    db_path = 'casinodb.db'
    if os.path.exists(db_path):
        os.remove(db_path)
        print("Data base deleted")
        return True
    else:
        print("Data base not found")
        return False
def add_user():
    ...
def add_game():
    ...
def add_game_played():
    ...
def get_user():
    ...
def jakies_get_2():
    ...
def itd():
    ...