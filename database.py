from connection import Connection

def crear_profesor(conn):
    
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
    conn.close_connection()

def crear_salon(conn):

    create_table_query = '''
        CREATE TABLE IF NOT EXISTS  salon(
            id  SERIAL  PRIMARY KEY NOT NULL,
            nrosalon varchar(4) NOT NULL,
            descripción varchar(100) NOT NULL
        );
    '''
    conn.execute_query(create_table_query)
    conn.commit()
    conn.close_connection()

def crear_nivel_educativo(conn):

    create_table_query = '''
        CREATE TABLE IF NOT EXISTS  nivel_educativo(
            id  SERIAL  PRIMARY KEY NOT NULL,
            nombre varchar(100) NOT NULL
        );
    '''
    conn.execute_query(create_table_query)
    conn.commit()
    conn.close_connection()

def crear_grado_salon(conn):

    create_table_query = '''
        CREATE TABLE IF NOT EXISTS  grado_salon(
            id  SERIAL  PRIMARY KEY NOT NULL,
            idnivel INTEGER,
            nombre varchar(50) NOT NULL,
            idsalon INTEGER,
            FOREIGN KEY (idnivel) REFERENCES nivel_educativo(id)
        );
    '''
    conn.execute_query(create_table_query)
    conn.commit()
    conn.close_connection()

def crear_alumno(conn):

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
    conn.close_connection()

def crear_curso(conn):

    create_table_query = '''

        CREATE TABLE IF NOT EXISTS curso(
            id SERIAL PRIMARY KEY NOT NULL,
            nombre varchar(100) NOT NULL
        );
    '''
    conn.execute_query(create_table_query)
    conn.commit()
    conn.close_connection()

def crear_periodo_tipo_evaluacion(conn):

    create_table_query = '''

        CREATE TABLE IF NOT EXISTS periodo_tipo_evaluacion(
            id SERIAL PRIMARY KEY NOT NULL,
            descripcion varchar(50) NOT NULL
        );
    '''
    conn.execute_query(create_table_query)
    conn.commit()
    conn.close_connection()

def crear_anio_escolar(conn):

    create_table_query = '''

        CREATE TABLE IF NOT EXISTS anio_escolar(
            id SERIAL PRIMARY KEY NOT NULL,
            anio VARCHAR(4) NOT NULL,
            descripcion VARCHAR(4) NOT NULL
        );
    '''
    conn.execute_query(create_table_query)
    conn.commit()
    conn.close_connection()

def crear_apertura_escolar(conn):

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
    conn.close_connection()

def crear_apertura_curso_profesor(conn):

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
    conn.close_connection()

def crear_apertura_alumno_grado(conn):

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
    conn.close_connection()

def crear_registro_alumno_curso(conn):

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
    conn.close_connection()

def crear_registro_nota_periodo_alumno(conn):

    create_table_query = '''

        CREATE TABLE IF NOT EXISTS registro_nota_periodo_alumno(
            id SERIAL PRIMARY KEY NOT NULL,
            idalumnocurso INTEGER NOT NULL,
            idperiodoeval INTEGER NOT NULL,
            nota INT2 NOT NULL
        );
    '''
    conn.execute_query(create_table_query)
    conn.commit()
    conn.close_connection()


conn = Connection()
crear_profesor(conn)
conn = Connection()
crear_salon(conn)
conn = Connection()
crear_nivel_educativo(conn)
conn = Connection()
crear_grado_salon(conn)
conn = Connection()
crear_alumno(conn)
conn = Connection()
crear_curso(conn)
conn = Connection()
crear_periodo_tipo_evaluacion(conn)
conn = Connection()
crear_anio_escolar(conn)
conn = Connection()
crear_apertura_escolar(conn)
conn = Connection()
crear_apertura_curso_profesor(conn)
conn = Connection()
crear_apertura_alumno_grado(conn)
conn = Connection()
crear_registro_alumno_curso(conn)
conn = Connection()
crear_registro_nota_periodo_alumno(conn)