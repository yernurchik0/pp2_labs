import psycopg2

def create_tables():
    
    commands = (
        """
        CREATE TABLE IF NOT EXISTS scores (
            id SERIAL PRIMARY KEY,
            user_name VARCHAR(32) NOT NULL,
            score INT NOT NULL
        )
        """,
    )
    try:
        with psycopg2.connect(host="localhost", database="snake", user="postgres", password="123456789") as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)