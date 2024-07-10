import csv
import random

try:
    trabajadores = [
        {
            "Nombre" : "Juan Perez",
            "Sueldo" : 0
        },
        {
            "Nombre" : "Maria Garcia",
            "Sueldo" : 0
        },
        {
            "Nombre" : "Carlos Lopez",
            "Sueldo" : 0
        },
        {
            "Nombre" : "Ana Martinez",
            "Sueldo" : 0
        },
        {
            "Nombre" : "Pedro Rodriguez",
            "Sueldo" : 0
        },
        {
            "Nombre" : "Laura Hernandez",
            "Sueldo" : 0
        },
        {
            "Nombre" : "Miguel Sanchez",
            "Sueldo" : 0
        },
        {
            "Nombre" : "Isabel Gomez",
            "Sueldo" : 0
        },
        {
            "Nombre" : "Francisco Diaz",
            "Sueldo" : 0
        },
        {
            "Nombre" : "Elena Fernandez",
            "Sueldo" : 0
        }
    ]
    start = True

    def sueldos(trabajadores):
        for trabajador in trabajadores:
            sueldo = random.randint(300000, 2500000)
            trabajador["Sueldo"] = sueldo
        return trabajadores

    def clasificar(trabajadores):
        clasificacion = [[], [], []]
        for trabajador in trabajadores:
            if trabajador["Sueldo"] < 800000:
                clasificacion[0].append(trabajador)
            elif trabajador["Sueldo"] >= 800000 and trabajador["Sueldo"] <= 2000000:
                clasificacion[1].append(trabajador)
            else:
                clasificacion[2].append(trabajador)
        return clasificacion

    def mostrar_clasificacion(trabajadores):
        
        print(f"""
Sueldos menores a $800.000 TOTAL: {len(clasificar(trabajadores)[0])}    
\nNombre empleado\t\tSueldo""")
        for trabajador in clasificar(trabajadores)[0]:
            print(f"{trabajador["Nombre"]}\t\t${trabajador["Sueldo"]}")
            
        print(f"""
Sueldos entre $800.000 y $2.000.000 TOTAL: {len(clasificar(trabajadores)[1])}
\nNombre empleado\t\tSueldo""")
        for trabajador in clasificar(trabajadores)[1]:
            print(f"{trabajador["Nombre"]}\t\t${trabajador["Sueldo"]}")
            
        print(f"""
Sueldos superiores a $2.000.000 TOTAL: {len(clasificar(trabajadores)[2])}     
\nNombre empleado\t\tSueldo""")
        for trabajador in clasificar(trabajadores)[2]:
            print(f"{trabajador["Nombre"]}\t\t${trabajador["Sueldo"]}")
        
        total = 0
        for trabajador in trabajadores:
            total += trabajador["Sueldo"]
        print(f"\nTOTAL SUELDOS: ${total}")
    
    def crear_reporte(trabajadores):
        reporte = []
        for i in trabajadores:
            salud = int(i["Sueldo"] * 0.07)
            afp = int(i["Sueldo"] * 0.12)
            liquido = i["Sueldo"] - salud - afp
            reporte.append([i["Nombre"], i["Sueldo"], salud, afp, liquido])
        return reporte
    
    def estadisticas(trabajadores):
        lista_sueldos = [trabajador["Sueldo"] for trabajador in trabajadores]
        promedio = sum(lista_sueldos) / len(lista_sueldos)
        print(f"""
        Sueldo mas alto: ${max(lista_sueldos)}
        Sueldo mas bajo: ${min(lista_sueldos)}
        Promedio de sueldos: ${promedio}""")
            
    while start:
        menu = int(input("""
        ------------ Menu ------------
        1. Asignar sueldos aleatorios
        2. Clasificar sueldos
        3. Ver estadisticas
        4. Reporte de sueldos
        5. Salir del programa
        """))
        
        if menu == 1:
            trabajadores = sueldos(trabajadores)
            print("Sueldos aleatorios asignados.")
        
        elif menu == 2:
            mostrar_clasificacion(trabajadores)
            
        elif menu == 3:
            estadisticas(trabajadores)
                
        elif menu == 4:
            reporte = crear_reporte(trabajadores)
            print("Nombre empleado       Sueldo Base    Descuento Salud    Descuento AFP    Sueldo Liquido")
            for i in reporte:
                print(f"{i[0]}\t\t{i[1]}\t\t{i[2]}\t\t{i[3]}\t\t{i[4]}")
            
            with open("reporte_sueldos.csv", "w", newline="") as reporte_csv:
                escritor_csv = csv.writer(reporte_csv)
                escritor_csv.writerow(["Nombre empleado", "Sueldo base", "Descuento Salud", "Descuento AFP", "Sueldo Liquido"])
                escritor_csv.writerows(reporte)
            
        elif menu == 5:
            start = False
        
    print("""
    Finalizando programa...
    Desarrollado por Natalia Meneses
    RUT 20.235.514-5""")

except Exception:
    print("El valor ingresado no es valido, intente nuevamente")