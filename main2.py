import os
import nivel_educativo
from profesor import Profesor
from curso import Cursos
from anio_escolar import Anio_escolar
from alumno import Alumno
from nivel_educativo import Nivel_educativo
from grado_salon import Grado_salon

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

try:
    while True:
        clear()
        print('----------SISTEMA DE COLEGIO----------')
        print()
        print('''
        1. Profesor.
        2. Curso.
        3. Año escolar.
        4. Alumno.
        0. Salir del sistema.
        ''')
        opcion = input('Ingresar número de módulo >> ')
        print()

        if opcion == '0':
            opcion = ''
            break
        elif opcion == '1': # Profesor
            while True:
                clear()
                print('----------MODULO PROFESOR----------')
                print()
                print('''
                1. listar profesor.
                2. buscar profesor por codigo.
                3. agregar un profesor.
                4. eliminar profesor.
                5. asignar curso a profesor.
                0. Salir del módulo.
                ''')
                opcion = input('Ingresar opción de módulo >> ')
                print()

                if opcion == '0':
                    opcion = ''
                    break
                elif opcion == '1': # lista profesores.
                    clear()
                    print("Profesor -> lista profesores")
                    print("----------------------------")
                    print()
                    profesor = Profesor()
                    profesor.consultar_profesor_todos()

                    print(f"{'código':<10} {'Nombres':<25} {'Apellido Pat.':<20} {'Apellido Mat.':<20}")
                    print("-------------------------------------------------------------------------------")

                    if profesor.lista_profesor:
                        for p in profesor.lista_profesor:
                            print(f"{p[0]:<10} {p[1]:<25} {p[2]:<20} {p[3]:<20}")
                    else:
                        print(f"Mensaje -> Sin datos de profesor")

                    print()
                    input("Presione cualquier tecla para retornar al módulo >> ")

                elif opcion == '2': # buscar profesor por codigo.
                    clear()
                    print("Profesor -> buscar profesor por codigo")
                    print("--------------------------------------")
                    print()
                    id = input('Ingresar código de profesor >> ')
                    print()

                    profesor = Profesor()
                    profesor.id = id
                    profesor.consultar_profesor_id()

                    if profesor.id:
                        print(f"Código: {profesor.id:>15}")
                        print(f"Nombres: {profesor.nombres:>18}")
                        print(f"Apellido Pat.: {profesor.apellido_pat:>15}")
                        print(f"Apellido Mat.: {profesor.apellido_mat:>15}")
                    else:
                        print(f"Mensaje -> Profesor con código -> {id}, no encontrado")

                    print()
                    input("Presione cualquier tecla para retornar al módulo >> ")

                elif opcion == '3': #agregar un profesor.
                    clear()
                    print("Profesor -> agregar un profesor")
                    print("-------------------------------")
                    print()
                    print("-> Completar los datos de profesor")
                    print()
                    profesor = Profesor()
                    while True:
                        dato = input('Ingresar nombres >> ')
                        if dato:
                            profesor.nombres = dato
                            dato = ''
                            break
                        print("Mensaje -> Campo obligatorio")
                        print()

                    while True:
                        dato = input('Ingresar Apellido Paterno >> ')
                        if dato:
                            profesor.apellido_pat = dato
                            dato = ''
                            break
                        print("Mensaje -> Campo obligatorio")
                        print()

                    while True:
                        dato = input('Ingresar Apellido Materno >> ')
                        if dato:
                            profesor.apellido_mat = dato
                            dato = ''
                            break
                        print("Mensaje -> Campo obligatorio")
                        print()
                    
                    profesor.guardar_profesor()
                    print()
                    input("Presione cualquier tecla para retornar al módulo >> ")


                elif opcion == '4': # eliminar profesor.
                    clear()
                    print("Profesor -> eliminar profesor")
                    print("-------------------------------")
                    print()
                    # print("-> Completar los datos de profesor")
                    # print()
                    profesor = Profesor()
                    while True:
                        dato = input('Ingresar código de profesor >> ')
                        if dato:
                            profesor.id = dato
                            break
                        print("Mensaje -> Campo obligatorio")
                        print()
                    
                    profesor.consultar_profesor_id()
                    if profesor.id:
                        confirmacion = input(f'Seguro que desea eliminar al profesor -> {profesor.nombres} {profesor.apellido_pat} (Y/N) >> ')
                        if confirmacion == 'Y':
                            profesor.eliminar_profesor_id()
                        else:
                            print("Mensaje -> Proceso cancelado por el usuario")
                    else:
                        print(f"Mensaje -> Profesor con código -> {dato}, no encontrado")
                    
                    print()
                    input("Presione cualquier tecla para retornar al módulo >> ")

                elif opcion == '5': # asignar curso a profesor.
                    clear()
                    print("Profesor -> asignar curso a profesor")
                    print("-------------------------------")
                    profesor = Profesor()

                    profesor.consultar_profesor_todos()
                    print(f"{'código':<10} {'Nombres':<25} {'Apellido Pat.':<20} {'Apellido Mat.':<20}")
                    print("Profesores -> lista profesores")
                    print("-------------------------------------------------------------------------------")
                    if profesor.lista_profesor:
                        for p in profesor.lista_profesor:
                            print(f"{p[0]:<10} {p[1]:<25} {p[2]:<20} {p[3]:<20}")
                    else:
                        print(f"Mensaje -> Sin datos de profesor")
                    print()
                    id_profesor=input("Selecciona el código profesor a asignar >> ")

                    apertura_grado=Anio_escolar()
                    apertura_grado.consultar_apertura_esc_todos()
                    print("Apertura Grado -> lista Grados a seleccionar")
                    print(f"{'código':<10} {'Año':<25} {'Nivel':<20} {'Grado':<20}")
                    print("-------------------------------------------------------------------------------")
                    if apertura_grado.lista_apertura_esc:
                        for p in apertura_grado.lista_apertura_esc:
                            print(f"{p[0]:<10} {p[1]:<25} {p[2]:<20} {p[3]:<20}")
                    else:
                        print(f"Mensaje -> Sin datos de apertura")
                    print()
                    id_apertura = input("Selecciona el código del grado aperturado >> ")

                    curso=Cursos()
                    curso.consultar_curso_todos()
                    print("Curso -> lista de cursos")
                    print(f"{'código':<10} {'Curso':<25}")
                    print("-------------------------------------------------------------------------------")
                    if curso.lista_curso:
                        for p in curso.lista_curso:
                            print(f"{p[0]:<10} {p[1]:<25}")
                    else:
                        print(f"Mensaje -> Sin datos de apertura")
                    print()
                    id_curso = input("Selecciona el código del curso >> ")

                    profesor.aperturar_curso_profesor(id_apertura, id_curso, id_profesor)
        
        elif opcion == '2': #Curso
            while True:
                clear()
                print('----------MODULO CURSO----------')
                print()
                print('''
                1. listar curso.
                2. buscar curso por codigo.
                3. agregar un curso.
                4. eliminar curso.
                0. Salir del módulo.
                ''')
                opcion = input('Ingresar opción de módulo >> ')
                print()

                if opcion == '0':
                    opcion = ''
                    break
                elif opcion == '1': # listar curso.
                    clear()
                    print("Curso -> listar curso")
                    print("----------------------------")
                    print()
                    curso = Cursos()
                    curso.fetchall_curso()

                    print(f"{'código':<10} {'Nombre':<25}")
                    print("--------------------------------")

                    if curso.lista_curso:
                        for p in curso.lista_curso:
                            print(f"{p[0]:<10} {p[1]:<25}")
                    else:
                        print(f"Mensaje -> Sin datos de curso")

                    print()
                    input("Presione cualquier tecla para retornar al módulo >> ")

                elif opcion == '2':
                    pass
                elif opcion == '3': # agregar un curso.
                    clear()
                    print("Curso -> agregar un curso")
                    print("-------------------------------")
                    print()
                    print("-> Completar los datos de curso")
                    print()
                    curso = Cursos()
                    while True:
                        dato = input('Ingresar nombre >> ')
                        if dato:
                            curso.nombre = dato
                            dato = ''
                            break
                        print("Mensaje -> Campo obligatorio")
                        print()
                    
                    curso.insert_curso()
                    print()
                    input("Presione cualquier tecla para retornar al módulo >> ")

                elif opcion == '4': # eliminar curso.
                    clear()
                    print("Curso -> eliminar curso")
                    print("-------------------------------")
                    print()

                    curso = Cursos()
                    while True:
                        dato = input('Ingresar código de curso >> ')
                        if dato:
                            curso.id = dato
                            break
                        print("Mensaje -> Campo obligatorio")
                        print()
                    
                    curso.fetchone_curso()
                    if curso.id:
                        confirmacion = input(f'Seguro que desea eliminar el curso -> {curso.nombre} (Y/N) >> ')
                        if confirmacion == 'Y':
                            curso.delete_curso(curso.id)
                        else:
                            print("Mensaje -> Proceso cancelado por el usuario")
                    else:
                        print(f"Mensaje -> Curso con código -> {dato}, no encontrado")
                    
                    print()
                    input("Presione cualquier tecla para retornar al módulo >> ")

        elif opcion == '3': #Año escolar
            while True:
                clear()
                print('----------MODULO AÑO ESCOLAR----------')
                print()
                print('''
                1. apertura de año escolar.                
                2. cerrar año escolar.
                3. listar año escolares abiertos.
                4. modificar año escolar.
                5. Crear año escolar.
                0. Salir del módulo.
                ''')
                opcion = input('Ingresar opción de módulo >> ')
                print()

                if opcion == '0':
                    opcion = ''
                    break
                elif opcion == '1': # apertura de año escolar.
                    clear()
                    print("Año escolar -> Aperturar año escolar")
                    print("-------------------------------")
                    print()

                    anio_escolar = Anio_escolar()
                    anio_escolar.consultar_anio_todos()
                    
                    print(f"{'código':<10} {'Año':<10} {'Descripción.':<20}")
                    print("--------------------------------------------------")

                    if anio_escolar.lista_anio:
                        for p in anio_escolar.lista_anio:
                            print(f"{p[0]:<10} {p[1]:<10} {p[2]:<20}")
                    else:
                        print(f"Mensaje -> Sin datos de año escolar")

                    print()

                    while True:
                        dato = input('Seleccionar código de año escolar a aperturar >> ')
                        anio_escolar.id = dato
                        anio_escolar.consultar_anio_id()
                        if anio_escolar.id:
                            dato = ''
                            break

                    clear()
                    print("Año escolar -> Aperturar año escolar")
                    print("-------------------------------")
                    print()
                    print(f"Año escolar >> {anio_escolar.anio} ")
                    print()

                    nivel_educativo = Nivel_educativo()
                    nivel_educativo.consultar_nivel_todos()

                    print(f"{'código':<10} {'Descripción.':<20}")
                    print("--------------------------------------------------")

                    if nivel_educativo.lista_nivel:
                        for p in nivel_educativo.lista_nivel:
                            print(f"{p[0]:<10} {p[1]:<20}")
                    else:
                        print(f"Mensaje -> Sin datos de nivel educativo")

                    print()

                    while True:
                        dato = input('Seleccionar código de nivel educativo >> ')
                        nivel_educativo.id = dato
                        nivel_educativo.consultar_nivel_id()
                        if nivel_educativo.id:
                            dato = ''
                            break

                    clear()
                    print("Año escolar -> Aperturar año escolar")
                    print("-------------------------------")
                    print()
                    print(f"Año escolar >> {anio_escolar.anio} ")
                    print(f"Nivel educativo >> {nivel_educativo.nombre} ")
                    print()

                    grado_salon = Grado_salon()
                    grado_salon.idnivel = nivel_educativo.id
                    grado_salon.consultar_grado_por_nivel()

                    print(f"{'código':<10} {'Descripción.':<20}")
                    print("--------------------------------------------------")

                    if grado_salon.lista_grado:
                        for p in grado_salon.lista_grado:
                            print(f"{p[0]:<10} {p[2]:<20}")
                    else:
                        print(f"Mensaje -> Sin datos de nivel educativo")

                    print()

                    while True:
                        dato = input(f'¿Activar año escolar {anio_escolar.anio} -> nivel {nivel_educativo.nombre}? (Y/N) >> ')
                        if dato == "Y":
                            for p in grado_salon.lista_grado:
                                anio_escolar.aperturar_anio_escolar(anio_escolar.id, p[0])
                                print(f"{p[2]} -> activado para {nivel_educativo.nombre} - {anio_escolar.anio}")
                            break
                    
                    print()
                    input("Presione cualquier tecla para retornar al módulo >> ")

                elif opcion == '2':
                    pass
                elif opcion == '3': # listar año escolares abiertos.
                    clear()
                    print("Año escolar -> listar año escolares abiertos")
                    print("----------------------------")
                    print()
                    anio_escolar = Anio_escolar()
                    anio_escolar.consultar_anio_todos()

                    print(f"{'código':<10} {'Año':<5} {'Descripción':<20}")
                    print("----------------------------------------------------")

                    if anio_escolar.lista_anio:
                        for p in anio_escolar.lista_anio:
                            print(f"{p[0]:<10} {p[1]:<5} {p[2]:<20}")
                    else:
                        print(f"Mensaje -> Sin datos de año escolar")

                    print()
                    input("Presione cualquier tecla para retornar al módulo >> ")

                elif opcion == '4':
                    pass
                elif opcion == '5': # Crear año escolar
                    clear()
                    print("Año escolar -> Crear año escolar")
                    print("-------------------------------")
                    print()
                    print("-> Completar los datos del año escolar")
                    print()
                    
                    anio_escolar = Anio_escolar()
                    while True:
                        dato = input('Ingresar año >> ')
                        if dato:
                            anio_escolar.anio = dato
                            dato = ''
                            break
                        print("Mensaje -> Campo obligatorio")
                        print()

                    while True:
                        dato = input('Ingresar descripción de año >> ')
                        if dato:
                            anio_escolar.descripcion = dato
                            dato = ''
                            break
                        print("Mensaje -> Campo obligatorio")
                        print()
                    
                    anio_escolar.guardar_anio_escolar()
                    print()
                    input("Presione cualquier tecla para retornar al módulo >> ")

        elif opcion == '4': #Alumno
            while True:
                clear()
                print('----------MODULO ALUMNO----------')
                print()
                print('''
                1. Listar Alumno x grado.
                2. Buscar alumno x nombre.
                3. Registrar alumno grado.
                4. Registro de notas (x bimestre).
                5. Modificar alumno.
                6. Eliminar alumno.
                7. Reporte final (promedio notas x curso y grado).
                8. Promediar alumno.
                0. Salir del módulo.
                ''')
                opcion = input('Ingresar opción de módulo >> ')
                print()

                if opcion == '0':
                    opcion = ''
                    break
                elif opcion == '1': #Listar alumnos por grado
                    clear()
                    print("Alumno -> buscar alumno por grado")
                    print("--------------------------------------")
                    print()
                    apertura_escolar = Anio_escolar()

                    apertura_escolar.consultar_apertura_esc_todos()
                    print(f"{'código':<10} {'Año':<25} {'Nivel':<20} {'Grado':<20}")
                    print("Grados -> Grados por año de apertura")
                    print("-------------------------------------------------------------------------------")
                    if apertura_escolar.lista_apertura_esc:
                        for p in apertura_escolar.lista_apertura_esc:
                            print(f"{p[0]:<10} {p[1]:<25} {p[2]:<20} {p[3]:<20}")
                    else:
                        print(f"Mensaje -> Sin datos de grado")
                    print()
                    id_apertura = input("Selecciona el código del grado aperturado >> ")

                    alumno=Alumno()
                    alumno.consultar_alumno_grado(id_apertura)
                    print(f"{'código':<10} {'Nombres':<25} {'Apellido paterno':<20} {'Apellido materno':<20}")
                    print("Alumnos -> Alumnos encontrados en el grado")
                    print("-------------------------------------------------------------------------------")
                    if alumno.lista_alumno:
                        for p in alumno.lista_alumno:
                            print(f"{p[0]:<10} {p[1]:<25} {p[2]:<20} {p[3]:<20}")
                    else:
                        print(f"Mensaje -> Sin datos de alumno")


                elif opcion == '2': #buscar alumnos por nombre
                    clear()
                    print("Alumno -> buscar alumno por nombre")
                    print("--------------------------------------")
                    print()
                    anio = input('Ingresar el año donde buscará al alumno >> ')
                    nombre = input('Ingresar el nombre del alumno >> ')
                    print()

                    alumno = Alumno()
                    alumno.consultar_alumno_nombre(nombre,anio)

                    if alumno.nombres:
                        print(f"Código: {alumno.id:>15}")
                        print(f"Nombre: {alumno.nombres:>18}")
                        
                    else:
                        print(f"Mensaje -> Alumno con nombre -> {nombre}, no encontrado")
                    print()
                    input("Presione cualquier tecla para retornar al módulo >> ")

                elif opcion == '3': #registrar alumno grado
                    clear()
                    print("Alumno -> registrar alumno grado")
                    print("-------------------------------")
                    alumno = Alumno()
                    idapertura = input('Ingresar el código del año aperturado >> ')
                    idalumno = input('Ingresar el código del alumno >> ')

                    alumno.aperturar_alumno_grado(idapertura,idalumno)

                    print()
                    input("Presione cualquier tecla para retornar al módulo >> ")

                elif opcion == '4':
                    pass
                elif opcion == '5': #modificar alumno
                    clear()
                    print("Alumno -> Modificar alumno")
                    print("-------------------------------")
                    print()
                    
                    alumno = Alumno()
                    while True:
                        dato = input('Ingresar código de alumno >> ')
                        if dato:
                            alumno.id = dato
                            break
                        print("Mensaje -> Campo obligatorio")
                        print()
                    
                    nombre = input('Ingresar los nombres nuevamente >> ')
                    ap_pat = input('Ingresar el apellido paterno nuevamente >> ')
                    ap_mat = input('Ingresar el apellido materno nuevamente >> ')
                    alumno = Alumno(dato,nombre,ap_pat,ap_mat)
                    
                    if alumno.id:
                        confirmacion = input(f'Seguro que desea actualizar el alumno -> {alumno.nombres} {alumno.apellido_pat} por (Y/N) >> ')
                        if confirmacion == 'Y' or confirmacion == 'y':
                            alumno.update_alumno(dato)
                        else:
                            print("Mensaje -> Proceso cancelado por el usuario")
                    else:
                        print(f"Mensaje -> Alumno con código -> {dato}, no encontrado")
                    print()
                    input("Presione cualquier tecla para retornar al módulo >> ")

                elif opcion == '6':
                    clear()
                    print("Alumno -> eliminar alumno")
                    print("-------------------------------")
                    print()
                    
                    alumno = Alumno()
                    while True:
                        dato = input('Ingresar código de alumno >> ')
                        if dato:
                            profesor.id = dato
                            break
                        print("Mensaje -> Campo obligatorio")
                        print()
                    
                    profesor.consultar_alumno_id()
                    if alumno.id:
                        confirmacion = input(f'Seguro que desea eliminar al alumno -> {alumno.nombres} {alumno.apellido_pat} (Y/N) >> ')
                        if confirmacion == 'Y' or confirmacion == 'y':
                            profesor.eliminar_alumno_id()
                        else:
                            print("Mensaje -> Proceso cancelado por el usuario")
                    else:
                        print(f"Mensaje -> Profesor con código -> {dato}, no encontrado")
                    
                    print()
                    input("Presione cualquier tecla para retornar al módulo >> ")
                elif opcion == '7':
                    pass
                elif opcion == '8':
                    pass

except KeyboardInterrupt:
    print("[Error_usuario]: Programa cancelado por el usuario")