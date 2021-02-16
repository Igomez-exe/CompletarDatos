import csv
class Datos():

    def completar_datos_libros(self,csv_entrada, csv_salida, diccionario_de_libros):
        f = open(csv_entrada,"r")
        self.reader_f = csv.reader(f)

        with open(csv_salida, "w") as archivo_salida:
            
            fieldnames = ["Docente", "Curso", "Nombre Libro", "Autor"]
            writer = csv.DictWriter(archivo_salida, fieldnames=fieldnames)
            writer.writeheader()

            for linea in self.reader_f:
                if linea[0]!="Docente":
                    if linea[2] in diccionario_de_libros:
                        writer.writerow({"Docente":linea[0],"Curso":linea[1],"Nombre Libro":diccionario_de_libros[linea[2]][0],
                        "Autor":diccionario_de_libros[linea[2]][1]})
                    else:
                        writer.writerow({"Docente":linea[0],"Curso":linea[1],"Nombre Libro":"Libro desconocido",
                        "Autor":"Autor desconocido"})

        f.close()              

              
if __name__ == "__main__":
    prueba = Datos()
    diccionario = {"20":("Mining the Social Web", "M. A. Russell"), "5": ("Data structures and problem solving using Java", "M. A. Weiss")}
    prueba.completar_datos_libros("csv_entrada.csv","csv_salida.csv",diccionario)