# config/mysqlconnection.py

import pymysql.cursors

class MySQLConnection:
    def __init__(self, db):
        conexion = pymysql.connect(host='localhost',
                                    user='root',  # Cambia por tu usuario de MySQL
                                    password='tazmania2316', # Cambia por tu contraseña de MySQL
                                    db=db,
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor,
                                    autocommit=True)
        self.conexion = conexion

    def query_db(self, consulta, data=None):
        with self.conexion.cursor() as cursor:
            try:
                if consulta.lower().find("insert") >= 0:
                    cursor.execute(consulta, data)
                    self.conexion.commit()
                    return cursor.lastrowid
                elif consulta.lower().find("select") >= 0:
                    cursor.execute(consulta, data)
                    resultado = cursor.fetchall()
                    return resultado
                else:
                    cursor.execute(consulta, data)
                    self.conexion.commit()
            except Exception as e:
                print(e)
                return False

def connectToMySQL(db):
    return MySQLConnection(db)