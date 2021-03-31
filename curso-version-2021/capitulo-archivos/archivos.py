archivo = open("archivo_curso.txt", "r")
for linea in archivo:
    print(linea)
archivo.close()
archivo = open("archivo_curso.txt", "r")
print(archivo.readline())