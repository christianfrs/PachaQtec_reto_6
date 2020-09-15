from conn1 import Connection
class Nivel_educativo:
    def __init__(self, id='', nombre=''):
        self.id = id
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
                VALUES('{self.nombre}')
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
