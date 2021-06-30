import sqlite3
def connect(dbname):
    conn = sqlite3.connect(dbname)
    conn.execute('CREATE TABLE IF NOT EXISTS OYO_HOTELS (NAME TEXT, ADDRESS TEXT, PRICE INT, AMENITIES TEXT, RATING TEXT)')
    print('Table created sucessfully!!')
    conn.close()

def insert_info_table(dbname,values):
    conn = sqlite3.connect(dbname)
    insert_sql = 'INSERT INTO OYO_HOTELS (NAME, ADDRESS, PRICE, AMENITIES, RATING) VALUES (?, ?, ?, ?, ?)'
    comm.execute(insert_sql,values)
    comm.commit()
    com.close()

def get_hotel_info(dbname):
    conn = sqlite3.connect(dbname)
    curs = comm.cursor()
    curs.execute('SELECT * FROM OYO_HOTELS')
    table_data = curs.fetchall()
    for record in table_data:
        print(record)
    comm.close()
