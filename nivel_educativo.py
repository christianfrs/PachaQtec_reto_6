from conn1 import Connection

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
