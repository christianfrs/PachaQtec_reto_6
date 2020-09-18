import os
import nivel_educativo
from profesor import Profesor
from curso import Cursos
from alumno import Alumno
from anio_escolar import Anio_escolar

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
                        if confirmacion == 'Y' or confirmacion == 'y':
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
                    curso.consultar_curso_todos()

                    print(f"{'código':<10} {'Nombre':<25}")
                    print("--------------------------------")

                    if curso.lista_curso:
                        for p in curso.lista_curso:
                            print(f"{p[0]:<10} {p[1]:<25}")
                    else:
                        print(f"Mensaje -> Sin datos de curso")

                    print()
                    input("Presione cualquier tecla para retornar al módulo >> ")

                elif opcion == '2': #buscar curso por id
                    clear()
                    print("Profesor -> buscar curso por codigo")
                    print("--------------------------------------")
                    print()
                    id = input('Ingresar código de curso >> ')
                    print()

                    curso = Cursos()
                    curso.id = id
                    curso.consultar_curso_id()

                    if curso.id:
                        print(f"Código: {curso.id:>15}")
                        print(f"Nombre: {curso.nombre:>18}")
                        
                    else:
                        print(f"Mensaje -> Curso con código -> {id}, no encontrado")

                    print()
                    input("Presione cualquier tecla para retornar al módulo >> ")

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
                    print("Profesor -> eliminar curso")
                    print("-------------------------------")
                    print()
                    # print("-> Completar los datos de profesor")
                    # print()
                    curso = Cursos()
                    while True:
                        dato = input('Ingresar código de curso >> ')
                        if dato:
                            curso.id = dato
                            break
                        print("Mensaje -> Campo obligatorio")
                        print()
                    
                    curso.consultar_curso_id()
                    if curso.id:
                        confirmacion = input(f'Seguro que desea eliminar el curso -> {curso.nombre} (Y/N) >> ')
                        if confirmacion == 'Y' or confirmacion == 'y':
                            profesor.eliminar_curso_id()
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
                0. Salir del módulo.
                ''')
                opcion = input('Ingresar opción de módulo >> ')
                print()

                if opcion == '0':
                    opcion = ''
                    break
                elif opcion == '1':
                    pass
                elif opcion == '2':
                    pass
                elif opcion == '3':
                    pass
                elif opcion == '4':
                    pass

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
                elif opcion == '1':
                    pass
                elif opcion == '2':
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
                elif opcion == '3':
                    pass
                elif opcion == '4':
                    pass
                elif opcion == '5':
                    pass 
                elif opcion == '6':
                    clear()
                    print("Alumno -> eliminar alumno")
                    print("-------------------------------")
                    print()
                    # print("-> Completar los datos de profesor")
                    # print()
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