from psycopg2 import connect

class Connection:
    def __init__(self, server='127.0.0.1', user='postgres', 
                        password='R0s@N3gr@', database='colegio_reto_6_g2_prueba', port=5432):

        self.db = connect(host=server, user=user, password=password, 
                        database=database, port=port)
        self.cursor = self.db.cursor()
        # print(f'Conexión a la base de datos {database}, exitosa')
 
    def execute_query(self, sql):
        self.cursor.execute(sql)
        return self.cursor
 
    def close_connection(self):
        self.db.close()
        print("Se ha desconectado de la base de datos")
 
    def commit(self):
        self.db.commit()
        return True


# connection = Connection()