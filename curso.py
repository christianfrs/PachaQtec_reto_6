from conn1 import Connection
class Cursos:
    def __init__(self, nombre_curso=''):
        self.nombre = nombre_curso
        
    def fetchall_curso(self):
        try:
            conn = Connection()
            query = '''
                SELECT * FROM curso;
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchall()
            for row in rows:
                print(f'id = {row[0]}')
                print(f'nombre = {row[1]}')
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
            print(f'nombre = {row[1]}')
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

    def insert_curso(self):
        try:
            #[model, price] => model,price
            conn = Connection()
            query = f'''
                INSERT INTO curso (nombre) 
                VALUES('{self.nombre}');
            '''
            conn.execute_query(query)
            conn.commit()
            print(f'Se agrego un curso -> {self.nombre}')
        except Exception as e:
            print(f'{str(e)}')

    def update_curso(self, id):
        try:
            conn = Connection()
            query = f'''
                UPDATE curso SET nombre = '{self.nombre}' WHERE id = {id};
            '''
            conn.execute_query(query)
            conn.commit()

            print(f'Se actualizo el curso con el ID {id} por -> {self.nombre}')
        except Exception as e:
            print(f'{str(e)}')

    def delete_curso(self, id):
        try:
            conn = Connection()
            query = f'''
                DELETE FROM curso WHERE id = {id};
            '''
            conn.execute_query(query)
            conn.commit()

            print(f'Se elimino el curso con ID {id}')
        except Exception as e:
            print(f'{str(e)}')

B=Cursos('Lenguaje')
B.delete_curso(3)
#B.fetchone_curso()
#B.fetchall_curso()