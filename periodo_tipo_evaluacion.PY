from connection import Connection

class Periodo_tipo_evaluacion:

    def __init__(self, id = '', descripcion = '', lista_periodo_tipo_evaluacion = []):

        self.id = id
        self.descripcion = descripcion
        self.lista_periodo_tipo_evaluacion = lista_periodo_tipo_evaluacion

    def consultar_periodo_tipo_evaluacion_id(self):
        select_table_query = f'''
            SELECT id, descripcion 
                FROM periodo_tipo_evaluacion
                WHERE id = {self.id};
        '''
        try:
            db = Connection()
            cursor = db.execute_query(select_table_query)
            self.lista_periodo_tipo_evaluacion = cursor.fetchall()
            for nivel in self.lista_periodo_tipo_evaluacion:
                self.id = nivel[0]
                self.descripcion = nivel[1]

        except Exception as e:
            print(f'Error -> {str(e)}')
        finally:
            db.close_connection()
    
    def consultar_periodo_tipo_evaluacion_todos(self):

        select_table_query = '''
            SELECT id, descripcion FROM periodo_tipo_evaluacion;
        '''

        try:
            db = Connection()   
            cursor = db.execute_query(select_table_query)
            self.lista_periodo_tipo_evaluacion = cursor.fetchall()
        except Exception as e:
            print(f'Error -> {str(e)}')
        finally:
            db.close_connection()

    def inicializar_datos_constantes(self):

        self.consultar_periodo_tipo_evaluacion_todos()

        if not self.lista_periodo_tipo_evaluacion:

            create_table_query = '''
                CREATE TABLE IF NOT EXISTS  periodo_tipo_evaluacion(
                    id  SERIAL  PRIMARY KEY NOT NULL,
                    descripcion varchar(50) NOT NULL
                );
            '''

            try:
                db = Connection()
                db.execute_query(create_table_query)
                db.commit()
            except Exception as e:
                print(f'Error -> {str(e)}')

            
            insert_data_query = '''
                INSERT INTO periodo_tipo_evaluacion 
                    VALUES  (1, '1er Bimestre'),
                            (2, '2do Bimestre'),
                            (3, '3er Bimestre'),
                            (4, '4to Bimestre');
            '''
            try:
                db.execute_query(insert_data_query)
                db.commit()
            except Exception as e:
                print(f'Error -> {str(e)}')
            finally:
                db.close_connection()

        else:
            print(f'La tabla "periodo_tipo_evaluacion" y sus valores ya fueron inicializados correctamente')



# periodo = Periodo_tipo_evaluacion()
# periodo.inicializar_datos_constantes()

# CONSULTA POR ID DE PERIODO TIPO EVALUACION
periodo = Periodo_tipo_evaluacion(2)
periodo.consultar_periodo_tipo_evaluacion_id()
print(f'Periodo -> {periodo.id}, Descripcion -> {periodo.descripcion}')