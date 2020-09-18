from connection import Connection
 
class Grado_salon:

    def __init__(self, id='', idnivel='', nombre='',idsalon='', lista_grado=[]):
        self.id = id
        self.idnivel = idnivel
        self.nombre = nombre
        self.idsalon = idsalon
        self.lista_grado = lista_grado
        # self.create_table()
 
    def create_table(self):
        try:
            conn = Connection()
            query = '''
            CREATE TABLE IF NOT EXISTS  grado_salon(
            id  SERIAL  PRIMARY KEY NOT NULL,
            idnivel INTEGER,
            nombre varchar(50) NOT NULL,
            idsalon INTEGER,
            FOREIGN KEY (idnivel) REFERENCES nivel_educativo(id)
                );
             '''
            conn.execute_query(query)
            conn.commit()
            
        except Exception as e:
            raise print(e)
 
    def insert_grado_salon(self):
        try:
            conn = Connection()
            query = f'''
                INSERT INTO grado_salon (id,idnivel,nombre,idsalon) 
                VALUES('{self.id}', '{self.idnivel}', '{self.nombre}', '{self.idsalon}')
            '''
            
            conn.execute_query(query)
            conn.commit()
 
            print(f'Se agrego un grado_salon -> {self.id},{self.idnivel},{self.nombre},{self.idsalon}')
        except Exception as e:
            print(f'{str(e)}')

    def consultar_grado_id(self):

        select_table_query = f'''
            SELECT id, idnivel, nombre, idsalon
                FROM grado_salon
                WHERE id = {self.id};
        '''
        try:
            db = Connection()
            cursor = db.execute_query(select_table_query)
            self.lista_grado = cursor.fetchall()
            for i in self.lista_grado:
                self.id = i[0]
                self.idnivel = i[1]
                self.nombre = i[2]
                self.idsalon = i[3]

        except Exception as e:
            print(f'Error -> {str(e)}')
        finally:
            db.close_connection()
            
    def consultar_grado_todos(self):

        select_table_query = '''
            SELECT id, idnivel, nombre, idsalon 
                FROM grado_salon;
        '''

        try:
            db = Connection()   
            cursor = db.execute_query(select_table_query)
            self.lista_grado = cursor.fetchall()
        except Exception as e:
            print(f'Error -> {str(e)}')
        finally:
            db.close_connection()

    def consultar_grado_por_nivel(self):

        select_table_query = f'''
            SELECT id, idnivel, nombre, idsalon 
                FROM grado_salon
                WHERE idnivel = {self.idnivel};
        '''

        try:
            db = Connection()   
            cursor = db.execute_query(select_table_query)
            self.lista_grado = cursor.fetchall()
            
        except Exception as e:
            print(f'Error -> {str(e)}')
        finally:
            db.close_connection()