from conn1 import Connection

class Nivel_educativo:
    def __init__(self, id_ned='', descrip_ned=''):
        self.id_ned = id_ned
        self.descrip_ned = descrip_ned
        self.create_table()

    def create_table(self):
        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS nivel_educativo(
                    id_ned  SERIAL  PRIMARY KEY NOT NULL,
                    descrip_ned varchar(50) NOT NULL
                );
            '''
            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            raise print(e)
        
    def fetchall_neduc(self):
        try:
            conn = Connection()
            query = '''
                SELECT * FROM nivel_educativo;
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchall()
            for row in rows:
                print(f'id_ned = {row[0]}')
                print(f'descrip_ned = {row[1]}')
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
            print(f'id_ned = {row[0]}')
            print(f'descrip_ned = {row[1]}')
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
                print(f'id_ned = {row[0]}')
                print(f'descrip_ned = {row[1]}')
                print('=====================')
            rows = cursor.fetchmany(3)
            print('Seconds -> 2 rows')
            for row in rows:
                print(f'id_ned = {row[0]}')
                print(f'descrip_ned = {row[1]}')
                print('=====================')
        except Exception as e:
            print(f'{str(e)}')

    def insert_neduc(self):
        try:
            #[model, price] => model,price
            conn = Connection()
            query = f'''
                INSERT INTO nivel_educativo (descrip_ned) 
                VALUES('{self.descrip_ned}')
            '''
            conn.execute_query(query)
            conn.commit()
            print(f'Se agrego un nivel educativo -> {self.descrip_ned}')
        except Exception as e:
            print(f'{str(e)}')

    def update_neduc(self, id):
        try:
            conn = Connection()
            query = f'''
                UPDATE mobile SET model = '{self.descrip_ned}' WHERE id = {id};
            '''
            conn.execute_query(query)
            conn.commit()

            print(f'Se actualizo el nievel educativo con el ID {id} por -> {self.descrip_ned}')
        except Exception as e:
            print(f'{str(e)}')


class Cursos:
    def __init__(self, id_curso='', nombre_curso=''):
        self.id_curso = id_curso
        self.nombre_curso = nombre_curso
        self.create_table()

    def create_table(self):
        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS curso(
                    id_curso  SERIAL  PRIMARY KEY NOT NULL,
                    nombre_curso varchar(50) NOT NULL
                );
            '''
            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            raise print(e)

class Alumno:
    def __init__(self, id_alumno='', nombre_alumno=''):
        self.id_alumno = id_alumno
        self.nombre_alumno = nombre_alumno
        self.create_table()

    def create_table(self):
        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS alumno(
                    id_alumno  SERIAL  PRIMARY KEY NOT NULL,
                    nombre_alumno varchar(50) NOT NULL
                );
            '''
            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            raise print(e)

nivel = Nivel_educativo()
cursos = Cursos()
alumno = Alumno()
#mobile.fetchall_mobiles()
#mobile.fetchone_mobiles()
#nivel.fetchmany_neduc()
