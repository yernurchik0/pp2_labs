import psycopg2

def update(nickname, score):
    """Обновляет счет пользователя или создает нового пользователя, если он не существует."""
    command = """
        UPDATE scores
        SET score =  %s 
        WHERE user_name = %s;
        """
    try:
        with psycopg2.connect(host="localhost", database="snake", user="postgres", password="123456789") as conn:
            with conn.cursor() as cur:
                cur.execute(command, (score, nickname))
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)