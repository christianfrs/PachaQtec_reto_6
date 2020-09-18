from connection import Connection

class Profesor:

    def __init__(self, id='', nombres='', apellido_pat='', apellido_mat='', lista_profesor=[]):
        
        self.id = id
        self.nombres = nombres
        self.apellido_pat = apellido_pat
        self.apellido_mat = apellido_mat
        self.lista_profesor = lista_profesor

    def consultar_profesor_id(self):

        select_table_query = f'''
        SELECT id, nombres, apellido_pat, apellido_mat
            FROM profesor
            WHERE id = {self.id};
        '''
        try:
            db = Connection()
            cursor = db.execute_query(select_table_query)
            self.lista_profesor = cursor.fetchall()
            
            if self.lista_profesor:
                for profesor in self.lista_profesor:
                    self.id = profesor[0]
                    self.nombres = profesor[1]
                    self.apellido_pat = profesor[2]
                    self.apellido_mat = profesor[3]
            else:
                self.id = ''

        except Exception as e:
            print(f'Error -> {str(e)}')
        finally:
            db.close_connection()

    def consultar_profesor_todos(self):

        select_table_query = f'''
            SELECT id, nombres, apellido_pat, apellido_mat
                FROM profesor;
        '''
        try:
            db = Connection()
            cursor = db.execute_query(select_table_query)
            self.lista_profesor = cursor.fetchall()
        except Exception as e:
            print(f'Error -> {str(e)}')
        finally:
            db.close_connection()
    
    def guardar_profesor(self):

        insert_table_query = f'''
            INSERT INTO profesor(nombres, apellido_pat, apellido_mat)
                VALUES('{self.nombres}', '{self.apellido_pat}', '{self.apellido_mat}');
        '''

        try:
            db = Connection()
            db.execute_query(insert_table_query)
            db.commit()
        except Exception as e:
            print(f'Error -> {str(e)}')
        finally:
            db.close_connection()

    def eliminar_profesor_id(self):

        delete_table_query = f'''
            DELETE FROM profesor WHERE id = {self.id};
        '''

        try:
            db = Connection()
            db.execute_query(delete_table_query)
            db.commit()
            db.close_connection()
        except Exception as e:
            print(f'Error -> {str(e)}')
        finally:
            print('proceso de eliminacion finalizado')#db.close_connection()

    def aperturar_curso_profesor(self, id_apertura, id_curso, id_profesor):

        insert_table_query = f'''
            INSERT INTO apertura_curso_profesor(id, idapertura, idcurso, idprofesor)
                VALUES({id_apertura}, {id_curso}, {id_profesor});
        '''

        try:
            db = Connection()
            db.execute_query(insert_table_query)
        except Exception as e:
            print(f'Error -> {str(e)}')
        finally:
            db.close_connection()


# nuevo_profesor = Profesor('', 'Pedro2', 'Ramirez', 'Rios')
# nuevo_profesor.guardar_profesor()
# profesor = Profesor(id = 10) #100, 'Pedro', 'Ramirez', 'Rios')
# profesor.consultar_profesor_id()

# print(f'id -> {profesor.id}, nombres -> {profesor.nombres}')

# for i in profesor.lista_profesor:
#     print(i)

#profesor.eliminar_profesor_id()