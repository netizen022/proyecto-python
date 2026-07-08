print("=================================== \n      SISTEMA DE TURNOS HOSPITALARIOS \n ===================================")

ESPECIALIDADES = [
    "Clínica Médica",
    "Pediatría",
    "Traumatología",
    "Cardiología",
    "Odontología"
]

PRIORIDADES = [
    "Normal",
    "Prioritario",
    "Urgente"
]

TURNOS = [
    "08:00",
    "08:30",
    "09:00",
    "09:30",
    "10:00",
    "10:30",
    "11:00",
    "11:30"
]

PACIENTES = []







def validar_dni(dni):
    """Verifica que el DNI tenga 7 u 8 dígitos numéricos."""
    return dni.isdigit() and len(dni) in (7, 8)


def dni_repetido(dni, pacientes):
    """Devuelve True si el DNI ya existe."""
    for paciente in pacientes:
        if paciente["dni"] == dni:
            return True
    return False


def validar_nombre(nombre):
    """controla que el nombre no esté vacío."""
    return nombre.strip() != ""


def validar_edad(edad):
    """Verifica que la edad sea un número entre 0 y 120."""
    if not edad.isdigit():
        return False
    edad = int(edad)
    return 0 <= edad <= 120


def validar_especialidad(opcion):
    """Verifica que la especialidad elegida exista."""
    return opcion.isdigit() and 1 <= int(opcion) <= len(ESPECIALIDADES)


def validar_prioridad(opcion):
    """Verifica que la prioridad elegida exista."""
    return opcion.isdigit() and 1 <= int(opcion) <= len(PRIORIDADES)


def validar_turno(opcion):
    """Verifica que el turno elegido exista."""
    return opcion.isdigit() and 1 <= int(opcion) <= len(TURNOS)




def registrar_paciente():
    print("\n===== REGISTRAR PACIENTE =====")

    while True:
        dni = input("Ingrese DNI: ")
        if not validar_dni(dni):
            print("DNI inválido.")
            continue
        if dni_repetido(dni, PACIENTES):
            print("Ese DNI ya está registrado.")
            continue
        break

    while True:
        nombre = input("Ingrese nombre y apellido: ").strip()
        if validar_nombre(nombre):
            break
        print("Nombre inválido.")

    while True:
        edad = input("Ingrese edad: ")
        if validar_edad(edad):
            edad = int(edad)
            break
        print("Edad inválida.")

    print("\nEspecialidades:")
    i = 1
    for esp in ESPECIALIDADES:
        print(f"{i}. {esp}")
        i += 1

    while True:
        op = input("Seleccione una especialidad: ")
        if validar_especialidad(op):
            especialidad = ESPECIALIDADES[int(op)-1]
            break
        print("Opción inválida.")

    paciente = {
        "dni": dni,
        "nombre": nombre,
        "edad": edad,
        "especialidad": especialidad,
        "turno": None,
        "prioridad": None,
        "atendido": False
    }

    PACIENTES.append(paciente)
    print("\nPaciente registrado correctamente.\n")


def mostrar_pacientes():
    if not PACIENTES:
        print("\nNo hay pacientes registrados.\n")
        return

    print("\n===== LISTA DE PACIENTES =====")
    i = 1
    for paciente in PACIENTES:
        print(f"{i}. {paciente['nombre']} - DNI: {paciente['dni']}")
        i += 1


def mostrar_ficha(indice):
    if indice < 0 or indice >= len(PACIENTES):
        print("Paciente inexistente.")
        return

    p = PACIENTES[indice]

    print("\n==============================")
    print(f"PACIENTE N°{indice+1}")
    print("==============================")
    print("DNI:", p["dni"])
    print("Nombre:", p["nombre"])
    print("Edad:", p["edad"])
    print("Especialidad:", p["especialidad"])
    print("Turno:", p["turno"] if p["turno"] else "Sin asignar")
    print("Prioridad:", p["prioridad"] if p["prioridad"] else "Sin asignar")
    print("Estado:", "Atendido" if p["atendido"] else "Pendiente")
    input("\nPresione ENTER para continuar...")


def consultar_pacientes():
    while True:
        print("\n===== CONSULTAR PACIENTES =====")
        print("1. Mostrar todos los pacientes")
        print("0. Volver")

        op = input("Seleccione una opción: ")

        if op == "0":
            break

        if op == "1":
            if not PACIENTES:
                print("\nNo hay pacientes registrados.")
                continue

            mostrar_pacientes()

            while True:
                eleccion = input("\nSeleccione un paciente (0 para volver): ")

                if eleccion == "0":
                    break

                if eleccion.isdigit():
                    numero = int(eleccion)
                    if 1 <= numero <= len(PACIENTES):
                        mostrar_ficha(numero-1)
                    else:
                        print("Paciente inexistente.")
                else:
                    print("Ingrese un número válido.")
        else:
            print("Opción inválida.")







def turno_ocupado(horario):
    for paciente in PACIENTES:
        if paciente["turno"] == horario:
            return True
    return False


def asignar_turno():
    if not PACIENTES:
        print("\nNo hay pacientes registrados.\n")
        return

    mostrar_pacientes()

    while True:
        opcion = input("\nSeleccione un paciente (0 para volver): ")

        if opcion == "0":
            return

        if opcion.isdigit() and 1 <= int(opcion) <= len(PACIENTES):
            indice = int(opcion) - 1
            break

        print("Opción inválida.")

    paciente = PACIENTES[indice]

    print("\n===== HORARIOS DISPONIBLES =====")

    i = 1
    for horario in TURNOS:
        estado = "Ocupado" if turno_ocupado(horario) else "Disponible"
        print(f"{i}. {horario} - {estado}")
        i += 1

    while True:
        opcion = input("Seleccione un horario: ")

        if not validar_turno(opcion):
            print("Opción inválida.")
            continue

        horario = TURNOS[int(opcion)-1]

        if turno_ocupado(horario):
            print("Ese horario ya está ocupado.")
            continue

        break

    print("\n===== PRIORIDADES =====")
    i = 1
    for prioridad in PRIORIDADES:
        print(f"{i}. {prioridad}")
        i += 1

    while True:
        opcion = input("Seleccione una prioridad: ")

        if validar_prioridad(opcion):
            prioridad = PRIORIDADES[int(opcion)-1]
            break

        print("Opción inválida.")

    paciente["turno"] = horario
    paciente["prioridad"] = prioridad

    print("\nTurno asignado correctamente.\n")







def registrar_atencion():
    if not PACIENTES:
        print("\nNo hay pacientes registrados.\n")
        return

    mostrar_pacientes()

    while True:
        opcion = input("\nSeleccione un paciente (0 para volver): ")

        if opcion == "0":
            return

        if opcion.isdigit() and 1 <= int(opcion) <= len(PACIENTES):
            indice = int(opcion) - 1
            break

        print("Opción inválida.")

    paciente = PACIENTES[indice]

    if paciente["turno"] is None:
        print("\nEl paciente todavía no tiene un turno asignado.\n")
        return

    if paciente["atendido"]:
        print("\nEl paciente ya fue atendido.\n")
        return

    print("\nPaciente seleccionado")
    print("----------------------")
    print("Nombre:", paciente["nombre"])
    print("DNI:", paciente["dni"])
    print("Turno:", paciente["turno"])
    print("Prioridad:", paciente["prioridad"])

    confirmar = input("\n¿Registrar atención? (S/N): ").upper()

    if confirmar == "S":
        paciente["atendido"] = True
        print("\nAtención registrada correctamente.\n")
    else:
        print("\nOperación cancelada.\n")







def mostrar_estadisticas():
    while True:
        print("\n===== ESTADÍSTICAS =====")
        print("1. Total de pacientes")
        print("2. Pacientes atendidos")
        print("3. Pacientes pendientes")
        print("4. Pacientes por especialidad")
        print("5. Pacientes por prioridad")
        print("0. Volver")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "0":
            break

        elif opcion == "1":
            print(f"\nTotal de pacientes registrados: {len(PACIENTES)}")

        elif opcion == "2":
            atendidos = 0
            for paciente in PACIENTES:
                if paciente["atendido"]:
                    atendidos += 1
            print(f"\nPacientes atendidos: {atendidos}")

        elif opcion == "3":
            pendientes = 0
            for paciente in PACIENTES:
                if not paciente["atendido"]:
                    pendientes += 1
            print(f"\nPacientes pendientes: {pendientes}")

        elif opcion == "4":
            print()
            for especialidad in ESPECIALIDADES:
                contador = 0
                for paciente in PACIENTES:
                    if paciente["especialidad"] == especialidad:
                        contador += 1
                print(f"{especialidad}: {contador}")

        elif opcion == "5":
            print()
            for prioridad in PRIORIDADES:
                contador = 0
                for paciente in PACIENTES:
                    if paciente["prioridad"] == prioridad:
                        contador += 1
                print(f"{prioridad}: {contador}")

        else:
            print("\nOpción inválida.")

        input("\nPresione ENTER para continuar...")







def mostrar_menu():
    print("\n=========================================")
    print(" SISTEMA DE TURNOS HOSPITALARIOS")
    print("=========================================")
    print("1. Registrar paciente")
    print("2. Asignar turno")
    print("3. Registrar atención")
    print("4. Consultar pacientes")
    print("5. Estadísticas")
    print("0. Salir")


def main():
    print("\nBienvenido al Sistema de Turnos Hospitalarios")
    input("Presione ENTER para mostrar el menú principal...")
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            registrar_paciente()

        elif opcion == "2":
            asignar_turno()

        elif opcion == "3":
            registrar_atencion()

        elif opcion == "4":
            consultar_pacientes()

        elif opcion == "5":
            mostrar_estadisticas()

        elif opcion == "0":
            print("\nGracias por utilizar el sistema.")
            break

        else:
            print("\nOpción inválida.")


if __name__ == "__main__":
    main()
