from connection import Connection

class Cursos:
    def __init__(self, id='', nombre_curso='', lista_curso = []):
        self.id = id
        self.nombre = nombre_curso
        self.lista_curso = lista_curso

    def consultar_curso_id(self):
        try:
            conn = Connection()
            query = f'''
                SELECT id, nombre
                FROM curso
                WHERE id = {self.id};
            '''
            cursor = conn.execute_query(query)
            self.lista_curso = cursor.fetchall()
            for curso in self.lista_curso:
                self.id = curso[0]
                self.nombre = curso[1]
        except Exception as e:
            print(f'Error -> {str(e)}')
        finally:
            conn.close_connection()

    def consultar_curso_todos(self):
        try:
            conn = Connection()
            query = f'''
                SELECT id, nombre
                    FROM curso;
            '''
            cursor = conn.execute_query(query)
            self.lista_curso = cursor.fetchall()
        except Exception as e:
            print(f'Error -> {str(e)}')
        finally:
            conn.close_connection()

    def fetchall_curso(self):
        try:
            conn = Connection()
            query = '''
                SELECT * FROM curso;
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchall()
            self.lista_curso = rows #chches-170920+
            for row in rows:
                print(f'id = {row[0]}')
                print(f'nombre = {row[1]}')
                print('=====================')
        except Exception as e:
            print(f'{str(e)}')

    def fetchone_curso(self):
        try:
            conn = Connection()
            # query = '''
            #     SELECT * FROM curso;
            query = f'''
                SELECT * FROM curso WHERE id = {self.id};
            '''
            cursor = conn.execute_query(query)
            row = cursor.fetchall()
            self.lista_curso = row # chches-170920+
            
            if self.lista_curso:
                for c in self.lista_curso:
                    self.id = c[0]
                    self.nombre = c[1]
            else:
                self.id = 0

            # print(f'id = {row[0]}')
            # print(f'nombre = {row[1]}')
            # print('=====================')
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