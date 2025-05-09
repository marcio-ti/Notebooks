import pymysql

def conectar_ao_banco():
    conexao = pymysql.connect(
        host='186.202.152.77',
        user='ceasars',
        password='F@44KeM78jCt23',
        database='ceasars'
    )
    return conexao

def mostrar_ips_conectados():
    conexao = conectar_ao_banco()
    try:
        with conexao.cursor() as cursor:
            cursor.execute("SELECT ID, USER, HOST, DB, COMMAND, TIME, STATE, INFO FROM information_schema.PROCESSLIST;")
            resultados = cursor.fetchall()
            print("Processos ativos e IPs conectados:")
            for linha in resultados:
                print(f"ID: {linha[0]}, User: {linha[1]}, Host: {linha[2]}, DB: {linha[3]}, Command: {linha[4]}, Time: {linha[5]}, State: {linha[6]}, Info: {linha[7]}")
    finally:
        conexao.close()

if __name__ == "__main__":
    mostrar_ips_conectados()
