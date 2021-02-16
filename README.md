Escribir un método "completar_datos_libros", que recibe el nombre de dos archivos "csv_entrada" , "csv_salida" y un diccionario de libros con clave : el código del libro
en la biblioteca y como dato : una tupla (nombre del libro, autor).

El archivo CSV de entrada contiene datos de libros solicitados por los docentes para los cursos, con formato:
  
  "Docente", "Curso", "Codigo Libro"
  
  "Rosita", "Estructura Datos", "10"
  
  "Martin", "Estructura Datos", "20"
 
  "Rosita", "Algoritmos 2", "5"
  
  "Diego", "Algoritmos 1", "2"
  
 
La salida debe contener además los dos primeros campos (docente y curso) más el nombre del libro y el autor del libro (o "Libro desconocido" y "Autor desconocido"
si no se encuentra el libro en el diccionario)


Si el diccionario de libros es: {"20" : ("Mining the Social Web", "M. A. Russell"), "5" : ("Data structures and problem solving using Java", "M. A. Weiss")}
la salida será : 

  "Docente", "Curso", "Nombre Libro", "Autor"
  
  "Rosita", "Estructura Datos", "Libro desconocido", "Autor desconocido"
   
  "Martin", "Estructura Datos", "Mining the Social Web", "M. A. Russell"
  
  "Rosita", "Algoritmos 2", "Data structures and problem solving using Java", "M. A. Weiss"
  
  "Diego", "Algoritmos 1", "Libro desconocido", "Autor desconocido"
  
  - - - - - -
  
  Los archivos csv que se encuentra en el repositorio son solo el emjemplo luego de ejecutar el archivo .py

