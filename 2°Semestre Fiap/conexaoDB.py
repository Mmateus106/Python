import cx_Oracle

#obter/criar conexao
def getConnection():
    try:
        conn = cx_Oracle.connect(user="rm98524", password="100603", 
        host="oracle.fiap.com.br/orcl", port="1521", service_name="orcl")
        print(f"Conexão: {conn.version}")
    except Exception as e:
        print("Erro ao obter uma conexão", e)
    return conn

def select():
    conn = getConnection()
    cursor = conn.cursor()
    sql_query = "SELECT * FROM CEO_DETAILS"
    cursor.execute(sql_query)
    for result in cursor:
        print(result)
    conn.commit()

def insert():
    conn = getConnection()
    cursor = conn.cursor()
    sql_query = "INSERT INTO CEO_DETAILS values('Steve', 'Jobs', 'Apple', 50)"
    cursor.execute(sql_query)
    conn.commit()

def update():
    try:
        conn = getConnection()
        cursor = conn.cursor()
        sql_query = "UPDATE CEO_DETAILS set AGE = 50 WHERE first_name= 'Steve'"
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Something went wrong - update {e}")

def delete():
    conn = getConnection()
    cursor = conn.cursor()
    sql_query = 'DELETE FROM CEO_DETAILS WHERE AGE=50'
    cursor.execute(sql_query)
    conn.commit()
    conn.close()
def close_connection(conn):
    try:
        conn.close()
        print(f"Connection closed!")
    except Exception as e:
        print(f"Something went wrong : {e}")

#Principal
print(f"Obtendo dados do BD")
conn = getConnection()
select()

conn.close()