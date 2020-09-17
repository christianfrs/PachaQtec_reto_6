<<<<<<< HEAD
from conn1 import Connection
class Nivel_educativo:
    def __init__(self, nombre=''):
        self.nombre = nombre
        
    def fetchall_neduc(self):
        try:
            conn = Connection()
            query = '''
                SELECT * FROM nivel_educativo;
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchall()
            for row in rows:
                print(f'id = {row[0]}')
                print(f'nombre = {row[1]}')
                print('=====================')
        except Exception as e:
            print(f'{str(e)}')

    def fetchone_neduc(self):
        try:
            conn = Connection()
            query = '''
                SELECT * FROM nivel_educativo;
            '''
            cursor = conn.execute_query(query)
            row = cursor.fetchone()
            print(f'id = {row[0]}')
            print(f'nombre = {row[1]}')
            print('=====================')
        except Exception as e:
            print(f'{str(e)}')

    def fetchmany_neduc(self):
        try:
            conn = Connection()
            query = '''
                SELECT * FROM nivel_educativo;
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchmany(2)
            print('First -> 2 rows')
            for row in rows:
                print(f'id = {row[0]}')
                print(f'nombre = {row[1]}')
                print('=====================')
            rows = cursor.fetchmany(3)
            print('Seconds -> 2 rows')
            for row in rows:
                print(f'id = {row[0]}')
                print(f'nombre = {row[1]}')
                print('=====================')
        except Exception as e:
            print(f'{str(e)}')

    def insert_neduc(self):
        try:
            #[model, price] => model,price
            conn = Connection()
            query = f'''
                INSERT INTO nivel_educativo (nombre) 
                VALUES('{self.nombre}');
            '''
            conn.execute_query(query)
            conn.commit()
            print(f'Se agrego un nivel educativo -> {self.nombre}')
        except Exception as e:
            print(f'{str(e)}')

    def update_neduc(self, id):
        try:
            conn = Connection()
            query = f'''
                UPDATE nivel_educativo SET nombre = '{self.nombre}' WHERE id = {id};
            '''
            conn.execute_query(query)
            conn.commit()

            print(f'Se actualizo el nivel educativo con el ID {id} por -> {self.nombre}')
        except Exception as e:
            print(f'{str(e)}')

    def delete_neduc(self, id):
        try:
            conn = Connection()
            query = f'''
                DELETE FROM nivel_educativo WHERE id = {id};
            '''
            conn.execute_query(query)
            conn.commit()

            print(f'Se elimino el nivel_educativo con ID {id}')
        except Exception as e:
            print(f'{str(e)}')

C=Nivel_educativo('Primaria')
#C.insert_neduc()
C.fetchone_neduc()

=======
from connection import Connection

class Nivel_educativo:

    def __init__(self, id='', nombre='', lista_nivel=[]):
        self.id = id
        self.nombre = nombre
        self.lista_nivel = lista_nivel

    def consultar_nivel_id(self):

        select_table_query = f'''
            SELECT id, nombre 
                FROM nivel_educativo
                WHERE id = {self.id};
        '''
        try:
            db = Connection()
            cursor = db.execute_query(select_table_query)
            self.lista_nivel = cursor.fetchall()
            for nivel in self.lista_nivel:
                self.id = nivel[0]
                self.nombre = nivel[1]

        except Exception as e:
            print(f'Error -> {str(e)}')
        finally:
            db.close_connection()
            
    def consultar_nivel_todos(self):

        select_table_query = '''
            SELECT id, nombre FROM nivel_educativo;
        '''

        try:
            db = Connection()   
            cursor = db.execute_query(select_table_query)
            self.lista_nivel = cursor.fetchall()
        except Exception as e:
            print(f'Error -> {str(e)}')
        finally:
            db.close_connection()
        
    def inicializar_datos_constantes(self):

        self.consultar_nivel_todos()

        if not self.lista_nivel:

            create_table_query = '''
                CREATE TABLE IF NOT EXISTS  nivel_educativo(
                    id  SERIAL  PRIMARY KEY NOT NULL,
                    nombre varchar(100) NOT NULL
                );
            '''

            try:
                db = Connection()
                db.execute_query(create_table_query)
                db.commit()
            except Exception as e:
                print(f'Error -> {str(e)}')

            
            insert_data_query = '''
                INSERT INTO nivel_educativo 
                    VALUES  (1, 'Primaria'),
                            (2, 'Secundaria');
            '''
            try:
                db.execute_query(insert_data_query)
                db.commit()
            except Exception as e:
                print(f'Error -> {str(e)}')
            finally:
                db.close_connection()

        else:
            print(f'La tabla "nivel_educativo" y sus valores ya fueron inicializados correctamente')

# CONSULTAR TODOS LOS NIVELES
# Instanciar objeto
nivel = Nivel_educativo()
# ejecutar método de instancia
nivel.consultar_nivel_todos()
# listar niveles de la tupla
for nivel in nivel.lista_nivel:
    print(f'nivel -> {nivel[0]}', end=', ')
    print(f'nombre: -> {nivel[1]}')

# # CONSULTAR NIVEL POR ID
# #Instanciar objeto
# nivel = Nivel_educativo(2)
# nivel.consultar_nivel_id()
# print(f'nivel -> {nivel.id} nombre -> {nivel.nombre}')

# # INICIALIZAR TABLA Y VALORES POR DEFECTO
# # Instanciar objeto
# nivel = Nivel_educativo()
# nivel.inicializar_datos_constantes()
>>>>>>> 42ac9dbe08d540bc55d5a619f1ce250f21fc9ca0
