import psycopg2
from psycopg2.sql import SQL, Identifier

conn = psycopg2.connect(database='netology_db', user='postgres', password='5021994Qwzc!')

# В данной функции мы создали таблицу test1 в базе netology_db
def create_table(conn):
    with conn.cursor() as cur:       
        cur.execute('''
                    DROP TABLE IF EXISTS phone_numbers;
                    DROP TABLE IF EXISTS clients;                   
                    ''')
        conn.commit()
        
        cur.execute('''
            CREATE TABLE clients(
            id_client SERIAL PRIMARY KEY,
            name_client VARCHAR(20) NOT NULL,
            firstname_client VARCHAR(20) NOT NULL,
            Email VARCHAR(40) UNIQUE NOT NULL);
            ''')
        conn.commit()

        cur.execute('''
            CREATE TABLE phone_numbers(
            id_phone_number INT REFERENCES clients(id_client),
            phone_number DECIMAL UNIQUE);
            ''')
        conn.commit()     

def add_new_client(conn, name_client, firstname_client, Email):
    with conn.cursor() as cur:
        cur.execute('''
            INSERT INTO clients(name_client, firstname_client, Email)
            VALUES(%s, %s, %s)RETURNING id_client, name_client, firstname_client, Email        
                    ''',(name_client, firstname_client, Email,))
        print(cur.fetchone())
    conn.commit() # если убрать эту строку, данные не будут фиксироваться в таблице    
           
def add_phone_number(conn, id_phone_number, phone_number):
    with conn.cursor() as cur:
        cur.execute('''
                    INSERT INTO phone_numbers
                    VALUES(%s, %s) RETURNING id_phone_number, phone_number
                    ''', (id_phone_number, phone_number,))
        print(cur.fetchone())
    conn.commit()
       
def update_values_client(conn, id_client, name_client=None, firstname_client=None, Email=None):
    arg_list = {'name_client':name_client, 'firstname_client':firstname_client, 'email':Email }
    for key, arg in arg_list.items():
        if arg:
            conn.cursor().execute(SQL("UPDATE clients SET {}=%s WHERE id_client=%s").format(Identifier(key)), (arg, id_client))
        conn.commit()

def update_phone_number(conn, new_phone_number, old_phone_number):
    with conn.cursor() as cur:
        cur.execute('''
                    UPDATE phone_numbers
                    SET phone_number = %s
                    WHERE phone_number = %s
                    ''', (new_phone_number, old_phone_number,))
    conn.commit()    

def del_phone_number(conn, phone_number):
    with conn.cursor() as cur:
        cur.execute('''
                    DELETE FROM phone_numbers
                    WHERE phone_number = %s
                    ''', (phone_number,))
    conn.commit()    

def del_client(conn, id_client):
    with conn.cursor() as cur:
        cur.execute('''
                    DELETE FROM phone_numbers
                    WHERE id_phone_number = %s
                    ''', (id_client,))
            
        cur.execute('''
                    DELETE FROM clients
                    WHERE id_client = %s
                    ''', (id_client,))
    conn.commit()

def find_client(conn, name_client=None, firstname_client=None, Email=None, phone_number=None):
    with conn.cursor() as cur:
        cur.execute("""
            SELECT * FROM clients c
            LEFT JOIN phone_numbers p ON c.id_client = p.id_phone_number
            WHERE (name_client = %(name_client)s OR %(name_client)s IS NULL)
            AND (firstname_client = %(firstname_client)s OR %(firstname_client)s IS NULL)
            AND (email = %(email)s OR %(email)s IS NULL)
            OR (phone_number = %(phone_number)s OR %(phone_number)s IS NULL);
            """, {'name_client':name_client, 'firstname_client':firstname_client, 'email':Email, 'phone_number':phone_number})
             
        print(cur.fetchone())
    conn.commit()

# create_table(conn)
# add_new_client(conn, 'Софья', 'Кильянова', 'vans-06@mail.ru')    
# add_phone_number(conn, 11, 89564711322)
# update_values_client(conn, 10, name_client='Томас', Email='Tomas@yandex.ru')
# update_phone_number(conn, 81111111111, 80000000000)
# del_phone_number(conn, 89564711333)
# del_client(conn, 10)
# find_client(conn, 'Елена')

conn.close() 