from conn1 import Connection

class anio_escolar:
    def __init__(self, id='', anio='',descripcion='', lista_anio=[]):
        self.id = id
        self.anio = anio
        self.descripcion = descripcion
        self.lista_anio = lista_anio
        
    def consultar_anio_id(self):
        try:
            conn = Connection()
            query = f'''
                SELECT id, anio, descripcion
                FROM anio_escolar
                WHERE id = {self.id};
            '''
            cursor = conn.execute_query(query)
            self.lista_anio = cursor.fetchall()
            for anio in self.lista_anio:
                self.id = anio[0]
                self.anio = anio[1]
                self.descripcion = anio[2]               
        except Exception as e:
            print(f'Error -> {str(e)}')
        finally:
            conn.close_connection()

    def consultar_anio_todos(self):
        try:
            conn = Connection()
            query = f'''
                SELECT id, anio, descripcion
                    FROM anio_escolar;
            '''
            cursor = conn.execute_query(query)
            self.lista_anio = cursor.fetchall()
        except Exception as e:
            print(f'Error -> {str(e)}')
        finally:
            conn.close_connection()

    def fetchall_anio_escolar(self):
        try:
            conn = Connection()
            query = '''
                SELECT * FROM anio_escolar;
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchall()
            for row in rows:
                print(f'id = {row[0]}')
                print(f'anio = {row[1]}')
                print(f'descripcion = {row[2]}')
                print('=====================')
        except Exception as e:
            print(f'{str(e)}')

    def fetchone_anio_escolar(self):
        try:
            conn = Connection()
            query = '''
                SELECT * FROM anio_escolar;
            '''
            cursor = conn.execute_query(query)
            row = cursor.fetchone()
            print(f'id = {row[0]}')
            print(f'anio = {row[1]}')
            print(f'descripcion = {row[2]}')
            print('=====================')
        except Exception as e:
            print(f'{str(e)}')

    def fetchmany_anio_escolar(self):
        try:
            conn = Connection()
            query = '''
                SELECT * FROM anio_escolar;
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchmany(2)
            print('First -> 2 rows')
            for row in rows:
                print(f'id = {row[0]}')
                print(f'anio = {row[1]}')
                print(f'descripcion = {row[2]}')
                print('=====================')
            rows = cursor.fetchmany(3)
            print('Seconds -> 2 rows')
            for row in rows:
                print(f'id = {row[0]}')
                print(f'anio = {row[1]}')
                print(f'descripcion = {row[2]}')
                print('=====================')
        except Exception as e:
            print(f'{str(e)}')

    def guardar_anio_escolar(self):
        try:
            #[model, price] => model,price
            conn = Connection()
            query = f'''
                INSERT INTO anio_escolar (anio,descripcion) 
                VALUES('{self.anio}','{self.descripcion}');
            '''
            conn.execute_query(query)
            conn.commit()
            print(f'Se agrego un año escolcar -> {self.anio}')
        except Exception as e:
            print(f'{str(e)}')

    def update_anio_escolar(self, id):
        try:
            conn = Connection()
            query = f'''
                UPDATE anio_escolcar SET anio = '{self.anio}', descripcion='{self.descripcion}' WHERE id = {id};
            '''
            conn.execute_query(query)
            conn.commit()

            print(f'Se actualizo el año escolar con el ID {id} por -> {self.anio}')
        except Exception as e:
            print(f'{str(e)}')

    def delete_anio_escolar(self, id):
        try:
            conn = Connection()
            query = f'''
                DELETE FROM anio_escolar WHERE id = {id};
            '''
            conn.execute_query(query)
            conn.commit()

            print(f'Se elimino el año con ID {id}')
        except Exception as e:
            print(f'{str(e)}')

    def aperturar_anio_escolar(self, idanio, idgrado):
        try:
            conn = Connection()
            query = f'''
                INSERT INTO apertura_alumno_grado(idanio, idgrado)
                    VALUES({idanio}, {idgrado});
            '''
            conn.execute_query(query)
        except Exception as e:
            print(f'Error -> {str(e)}')
        finally:
            conn.close_connection()

#A=anio_escolar('2020','Dos mil veinte')
#A.guardar_anio_escolar()
#A.fetchone_alumno()
#A.fetchall_anio_escolar()