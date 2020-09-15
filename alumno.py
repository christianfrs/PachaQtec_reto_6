from conn1 import Connection
class Alumno:
    def __init__(self, id_alumno='', nombre_alumno='',apellido_pat='',apellido_mat=''):
        self.id = id_alumno
        self.nombres = nombre_alumno
        self.apellido_pat = apellido_pat
        self.apellido_mat = apellido_mat


    def fetchall_alumno(self):
        try:
            conn = Connection()
            query = '''
                SELECT * FROM curso;
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchall()
            for row in rows:
                print(f'id = {row[0]}')
                print(f'nombres = {row[1]}')
                print(f'apellido_pat = {row[3]}')
                print(f'apellido_mat = {row[4]}')
                print('=====================')
        except Exception as e:
            print(f'{str(e)}')

    def fetchone_curso(self):
        try:
            conn = Connection()
            query = '''
                SELECT * FROM curso;
            '''
            cursor = conn.execute_query(query)
            row = cursor.fetchone()
            print(f'id = {row[0]}')
            print(f'nombres = {row[1]}')
            print(f'apellido_pat = {row[3]}')
            print(f'apellido_mat = {row[4]}')
            print('=====================')
        except Exception as e:
            print(f'{str(e)}')

    def fetchmany_curso(self):
        try:
            conn = Connection()
            query = '''
                SELECT * FROM curso;
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchmany(2)
            print('First -> 2 rows')
            for row in rows:
                print(f'id = {row[0]}')
                print(f'nombres = {row[1]}')
                print(f'apellido_pat = {row[3]}')
                print(f'apellido_mat = {row[4]}')
                print('=====================')
            rows = cursor.fetchmany(3)
            print('Seconds -> 2 rows')
            for row in rows:
                print(f'id = {row[0]}')
                print(f'nombres = {row[1]}')
                print(f'apellido_pat = {row[3]}')
                print(f'apellido_mat = {row[4]}')
                print('=====================')
        except Exception as e:
            print(f'{str(e)}')

    def insert_curso(self):
        try:
            #[model, price] => model,price
            conn = Connection()
            query = f'''
                INSERT INTO alumno (nombre) 
                VALUES('{self.nombres}','{self.apellido_pat}','{self.apellido_mat}')
            '''
            conn.execute_query(query)
            conn.commit()
            print(f'Se agrego un alumno -> {self.nombres}')
        except Exception as e:
            print(f'{str(e)}')

    def update_curso(self, id):
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