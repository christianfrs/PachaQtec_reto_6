from conn1 import Connection

class Database:
    def __init__ (self, conn):
        self.conn = conn

    def crear_profesor(self):
        
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  profesor(
                id  SERIAL   PRIMARY KEY NOT NULL,
                nombres varchar(100) NOT NULL,
                apellido_pat varchar(50) NOT NULL,
                apellido_mat varchar(60) NOT NULL
            );
        '''
        conn.execute_query(create_table_query)
        conn.commit()
        
    def crear_salon(self):

        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  salon(
                id  SERIAL  PRIMARY KEY NOT NULL,
                nrosalon varchar(4) NOT NULL,
                descripción varchar(100) NOT NULL
            );
        '''
        conn.execute_query(create_table_query)
        conn.commit()
        
    def crear_nivel_educativo(self):

        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  nivel_educativo(
                id  SERIAL  PRIMARY KEY NOT NULL,
                nombre varchar(100) NOT NULL
            );
        '''
        conn.execute_query(create_table_query)
        conn.commit()
        
    def crear_grado_salon(self):

        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  grado_salon(
                id  SERIAL  PRIMARY KEY NOT NULL,
                idnivel INTEGER NOT NULL,
                nombre varchar(50) NOT NULL,
                idsalon INTEGER,
                FOREIGN KEY (idnivel) REFERENCES nivel_educativo(id)
            );
        '''
        conn.execute_query(create_table_query)
        conn.commit()
        
    def crear_alumno(self):

        create_table_query = '''

            CREATE TABLE IF NOT EXISTS alumno(
                id SERIAL PRIMARY KEY NOT NULL,
                nombres varchar(100) NOT NULL,
                apellido_pat varchar(50) NOT NULL,
                apellido_mat varchar(60) NOT NULL
            );
        '''
        conn.execute_query(create_table_query)
        conn.commit()
        
    def crear_curso(self):

        create_table_query = '''

            CREATE TABLE IF NOT EXISTS curso(
                id SERIAL PRIMARY KEY NOT NULL,
                nombre varchar(100) NOT NULL
            );
        '''
        conn.execute_query(create_table_query)
        conn.commit()
        
    def crear_periodo_tipo_evaluacion(self):

        create_table_query = '''

            CREATE TABLE IF NOT EXISTS periodo_tipo_evaluacion(
                id SERIAL PRIMARY KEY NOT NULL,
                descripcion varchar(50) NOT NULL
            );
        '''
        conn.execute_query(create_table_query)
        conn.commit()
    
    def crear_anio_escolar(self):

        create_table_query = '''

            CREATE TABLE IF NOT EXISTS anio_escolar(
                id SERIAL PRIMARY KEY NOT NULL,
                anio VARCHAR(4) NOT NULL,
                descripcion VARCHAR(4) NOT NULL
            );
        '''
        conn.execute_query(create_table_query)
        conn.commit()
    
    def crear_apertura_escolar(self):

        create_table_query = '''

            CREATE TABLE IF NOT EXISTS apertura_escolar(
                id SERIAL PRIMARY KEY NOT NULL,
                idanio INTEGER NOT NULL,
                idgrado INTEGER NOT NULL,
                FOREIGN KEY (idanio) REFERENCES anio_escolar(id),
                FOREIGN KEY (idgrado) REFERENCES grado_salon(id)
            );

        '''
        conn.execute_query(create_table_query)
        conn.commit()
    
    def crear_apertura_curso_profesor(self):

        create_table_query = '''

            CREATE TABLE IF NOT EXISTS apertura_curso_profesor(
                id SERIAL PRIMARY KEY NOT NULL,
                idapertura INTEGER NOT NULL,
                idcurso INTEGER NOT NULL,
                idprofesor INTEGER NOT NULL,
                FOREIGN KEY (idapertura) REFERENCES apertura_escolar(id),
                FOREIGN KEY (idcurso) REFERENCES curso(id),
                FOREIGN KEY (idprofesor) REFERENCES profesor(id)
            );
        '''
        conn.execute_query(create_table_query)
        conn.commit()
    
    def crear_apertura_alumno_grado(self):

        create_table_query = '''

            CREATE TABLE IF NOT EXISTS apertura_alumno_grado(
                id SERIAL PRIMARY KEY NOT NULL,
                idapertura INTEGER NOT NULL,
                idalumno INTEGER NOT NULL,
                FOREIGN KEY (idapertura) REFERENCES apertura_escolar(id),
                FOREIGN KEY (idalumno) REFERENCES alumno(id)
            );
        '''
        conn.execute_query(create_table_query)
        conn.commit()
    
    def crear_registro_alumno_curso(self):

        create_table_query = '''
            CREATE TABLE IF NOT EXISTS registro_alumno_curso(
                id SERIAL PRIMARY KEY NOT NULL,
                idcursoprofesor INTEGER NOT NULL,
                idalumnogrado INTEGER NOT NULL,
                nota INT2 NOT NULL,
                FOREIGN KEY (idcursoprofesor) REFERENCES apertura_curso_profesor(id),
                FOREIGN KEY (idalumnogrado) REFERENCES apertura_alumno_grado(id)
            );
        '''
        conn.execute_query(create_table_query)
        conn.commit()
    
    def crear_registro_nota_periodo_alumno(self):

        create_table_query = '''

            CREATE TABLE IF NOT EXISTS registro_nota_periodo_alumno(
                id SERIAL PRIMARY KEY NOT NULL,
                idalumnocurso INTEGER NOT NULL,
                idperiodoeval INTEGER NOT NULL,
                nota INT2 NOT NULL,
                FOREIGN KEY (idalumnocurso) REFERENCES registro_alumno_curso(id),
                FOREIGN KEY (idperiodoeval) REFERENCES periodo_tipo_evaluacion(id)
            );
        '''
        conn.execute_query(create_table_query)
        conn.commit()
  

conn = Connection()
database= Database(conn)
database.crear_profesor()
database.crear_alumno()
database.crear_salon()
database.crear_nivel_educativo()
database.crear_curso()
database.crear_periodo_tipo_evaluacion()
database.crear_anio_escolar()
database.crear_grado_salon()
database.crear_apertura_escolar()
database.crear_apertura_curso_profesor()
database.crear_apertura_alumno_grado()
database.crear_registro_alumno_curso()
database.crear_registro_nota_periodo_alumno()
conn.close_connection()
