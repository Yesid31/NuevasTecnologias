print("--- Calcular nota definitiva ---")
nombre = input("Nombre Estudiante: ")
nota1 = float(input("Ingrese Nota 1: "))
nota2 = float(input("Ingrese Nota 2: "))
nota3 = float(input("Ingrese Nota 3: "))
definitiva = (nota1 + nota2 + nota3)/3
print("Nombre: ", nombre, "Nota 1 -->", nota1, "Nota 2 -->",
      nota2, "Nota 3 -->", nota3, "Definitiva --> ", definitiva)

# if definitiva >= 3.0:
#     print("El Estudiante ", nombre, "tiene una calificacion de ", +
#           definitiva, "por lo tanto no pudo aprobar")

# else:
#     print("El Estudiante ", nombre, "tiene una calificacion de ", +
#           definitiva, "por lo tanto aprobo")
if definitiva >= 0 and definitiva <= 5:
    if definitiva <= 2:
        print("problemas de atención")
    elif definitiva < 3:
        print("puede recuperar")
    elif definitiva < 4:
        print("Muy Bien Gano")
    elif definitiva < 4.6:
        print("Eres Genial")
    elif definitiva > 4.6:
        print("Eres El Mejor")
    print("Error")
