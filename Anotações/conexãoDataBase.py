'''
1. importar o driver cx_Oracle
2. Estabelecer uma conexão entre o Python e o DB
3. Criar um cursor (objeto para executar queries e obter resultados após execução)
'''
import cx_Oracle

# Create connection

conn = cx_Oracle.connect(user="rm98524", password="100603", host="oracle.fiap.com.br/orcl", port="1521", service_name="orcl")
# conn = cx_Oracle.connect(user="rm98524", password="100603", host="oracle.fiap.com.br/orcl", port="1521")
print(conn.version)

# Create Cursor
cursor = conn.cursor()

# Create Table
sql_create = """
CREATE TABLE CEO_DETAILS (
    FIRST_NAME VARCHAR2(50),
    LAST_NAME VARCHAR2(50),
    COMPANY VARCHAR2(50),
    AGE NUMBER
);
"""
#execute query
cursor.execute()
print("Tabela criada!")

#fechar conexão
conn.close()

#fechar cursor
cursor.close()