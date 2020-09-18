from conn1 import Connection

class Alumno:
    def __init__(self, id='', nombre_alumno='', apellido_pat='', apellido_mat='', lista_alumno=[]):
        self.id = id
        self.nombres = nombre_alumno
        self.apellido_pat = apellido_pat
        self.apellido_mat = apellido_mat
        self.lista_alumno = lista_alumno


    def consultar_alumno_id(self):
        try:
            conn = Connection()
            query = f'''
                SELECT id, nombres, apellido_pat, apellido_mat
                FROM alumno
                WHERE id = {self.id};
            '''
            cursor = conn.execute_query(query)
            self.lista_alumno = cursor.fetchall()
            for alumno in self.lista_alumno:
                self.id = alumno[0]
                self.nombres = alumno[1]
                self.apellido_pat = alumno[2]
                self.apellido_mat = alumno[3]
        except Exception as e:
            print(f'Error -> {str(e)}')
        finally:
            conn.close_connection()

    def consultar_alumno_grado(self,idapertura):
        try:
            conn = Connection()
            query = f'''
                SELECT A.id, A.nombres, A.apellido_pat, A.apellido_mat
                FROM alumno A
                Inner join apertura_alumno_grado B on A.id = B.idalumno                
                WHERE B.idapertura={idapertura};
            '''
            cursor = conn.execute_query(query)
            self.lista_alumno = cursor.fetchall()
            for alumno in self.lista_alumno:
                self.id = alumno[0]
                self.nombres = alumno[1]
                self.apellido_pat = alumno[2]
                self.apellido_mat = alumno[3]
        except Exception as e:
            print(f'Error -> {str(e)}')
        finally:
            conn.close_connection()

    def consultar_alumno_nombre(self,nombre,anio):
        try:
            conn = Connection()
            query = f'''
                SELECT A.id, A.nombres, A.apellido_pat, A.apellido_mat
                FROM alumno A
                Inner join apertura_alumno_grado B on A.id = B.idalumno
                Inner join apertura_escolar C on B.idapertura=C.id  
                Inner join anio_escolar D on C.idanio=D.id             
                WHERE D.anio='{anio}' and A.nombres like '{nombre}';
            '''
            cursor = conn.execute_query(query)
            self.lista_alumno = cursor.fetchall()
            for alumno in self.lista_alumno:
                self.id = alumno[0]
                self.nombres = alumno[1]
                self.apellido_pat = alumno[2]
                self.apellido_mat = alumno[3]
        except Exception as e:
            print(f'Error -> {str(e)}')
        finally:
            conn.close_connection()

    def consultar_alumno_todos(self):
        try:
            conn = Connection()
            query = f'''
                SELECT id, nombres, apellido_pat, apellido_mat
                    FROM alumno;
            '''
            cursor = conn.execute_query(query)
            self.lista_alumno = cursor.fetchall()
        except Exception as e:
            print(f'Error -> {str(e)}')
        finally:
            conn.close_connection()

    def fetchall_alumno(self):
        try:
            conn = Connection()
            query = '''
                SELECT * FROM alumno;
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchall()
            for row in rows:
                print(f'id = {row[0]}')
                print(f'nombres = {row[1]}')
                print(f'apellido_pat = {row[2]}')
                print(f'apellido_mat = {row[3]}')
                print('=====================')
        except Exception as e:
            print(f'{str(e)}')

    def fetchone_alumno(self):
        try:
            conn = Connection()
            query = '''
                SELECT * FROM alumno;
            '''
            cursor = conn.execute_query(query)
            row = cursor.fetchone()
            print(f'id = {row[0]}')
            print(f'nombres = {row[1]}')
            print(f'apellido_pat = {row[2]}')
            print(f'apellido_mat = {row[3]}')
            print('=====================')
        except Exception as e:
            print(f'{str(e)}')

    def fetchmany_alumno(self):
        try:
            conn = Connection()
            query = '''
                SELECT * FROM alumno;
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchmany(2)
            print('First -> 2 rows')
            for row in rows:
                print(f'id = {row[0]}')
                print(f'nombres = {row[1]}')
                print(f'apellido_pat = {row[2]}')
                print(f'apellido_mat = {row[3]}')
                print('=====================')
            rows = cursor.fetchmany(3)
            print('Seconds -> 2 rows')
            for row in rows:
                print(f'id = {row[0]}')
                print(f'nombres = {row[1]}')
                print(f'apellido_pat = {row[2]}')
                print(f'apellido_mat = {row[3]}')
                print('=====================')
        except Exception as e:
            print(f'{str(e)}')

    def guardar_alumno(self):
        try:
            #[model, price] => model,price
            conn = Connection()
            query = f'''
                INSERT INTO alumno (nombres,apellido_pat,apellido_mat) 
                VALUES('{self.nombres}','{self.apellido_pat}','{self.apellido_mat}');
            '''
            conn.execute_query(query)
            conn.commit()
            print(f'Se agrego un alumno -> {self.nombres}')
        except Exception as e:
            print(f'{str(e)}')

    def update_alumno(self, id):
        try:
            conn = Connection()
            query = f'''
                UPDATE alumno SET nombres = '{self.nombres}', apellido_pat='{self.apellido_pat}', apellido_mat='{self.apellido_mat}' WHERE id = {id};
            '''
            conn.execute_query(query)
            conn.commit()
            print(f'Se actualizo el alumno con el ID {id} por -> {self.nombres}')
        except Exception as e:
            print(f'{str(e)}')

    def eliminar_alumno_id(self, id):
        try:
            conn = Connection()
            query = f'''
                DELETE FROM alumno WHERE id = {id};
            '''
            conn.execute_query(query)
            conn.commit()
            print(f'Se elimino el alumno con ID {id}')
        except Exception as e:
            print(f'{str(e)}')

    def aperturar_alumno_grado(self, id_apertura, id_alumno):
        try:
            conn = Connection()
            query = f'''
                INSERT INTO apertura_alumno_grado(idapertura, idalumno)
                    VALUES({id_apertura}, {id_alumno});
            '''
            conn.execute_query(query)
        except Exception as e:
            print(f'Error -> {str(e)}')
        finally:
            conn.close_connection()

    def registro_alumno_curso(self, idcursoprofesor, idalumnogrado, nota='' ):
        try:
            conn = Connection()
            query = f'''
                INSERT INTO registro_alumno_curso(idcursoprofesor, idalumnogrado)
                    VALUES({idcursoprofesor}, {idalumnogrado});
            '''
            conn.execute_query(query)
        except Exception as e:
            print(f'Error -> {str(e)}')
        finally:
            conn.close_connection()
    
    def registro_nota_periodo_alumno(self, idalumnocurso, idperiodoeval, nota='' ):
        try:
            conn = Connection()
            query = f'''
                INSERT INTO registro_nota_periodo_alumno(idalumnocurso, idperiodoeval,nota)
                    VALUES({idalumnocurso}, {idperiodoeval},{nota});
            '''
            conn.execute_query(query)
        except Exception as e:
            print(f'Error -> {str(e)}')
        finally:
            conn.close_connection()

#A=Alumno('','Carmen','Laos','Rios')
#A.guardar_alumno()
#A.fetchone_alumno()
#A.fetchall_alumno()