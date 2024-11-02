import psycopg2

db_setup = {
    'dbname': 'using_sql_with_python',
    'user': 'postgres',
    'password': '1234',
    'host': 'localhost',
    'port': 5432
}

with open('seed.sql', 'r') as file:
    sql_commands = file.read()

try:
    with psycopg2.connect(**db_setup) as conn:
        with conn.cursor() as cur:
            cur.execute(sql_commands)
            conn.commit()
    print('Successfully created schema')
except Exception as e:
    print(f'Failed with error: {e}')