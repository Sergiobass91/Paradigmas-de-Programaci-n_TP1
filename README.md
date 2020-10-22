# Paradigmas de Programación TP1
#### Primer TP - Paradigmas IFTS18

Cada año se desarrolla el campeonato nacional de tiro con arco y flecha. Se desea reemplazar el sistema de seguimiento y control de los participantes por un programa escrito en Python.
Que es lo que sabemos del concurso:

•	Pueden participar hombres y mujeres de todas las edades.
•	Cada participante deberá realizar 3 disparos (obligatorio).
•	Se dispara a un blanco cuyo centro coincide con el origen de coordenadas de un eje 	  cartesiano (x, y). La mejor puntuación la obtiene el disparo más cercano al origen.
•	Cada participante tiene un número único que lo identifica del resto.
•	El radio del tablero es de 80 cm.

El programa debe realizar por cada participante, el ingreso de los siguientes datos:
a)	Número único del participante.
b)	Nombre y Apellido del participante.
c)	Edad del participante.
d)	Sexo del participante.
e)	Ubicación de los disparos en pares X e Y. Solo almacenar la distancia al origen de cada disparo.
•	El fin de ingreso de participantes se determina ingresando con número de participante igual a 999.
  -	El campo MejorDisp deberá almacenar el mejor disparo de cada participante.
  -	El campo PromDisp deberá almacenar el promedio de los 3 disparos de cada participante.
  
Se pide:
a)	Mostrar el podio de los ganadores (los 3 primeros) en función del Mejor Disparo (Nro Participante, Nombre, Apellido y Mejor disparo). Se pide informar por pantalla y en un archivo de texto.
b)	Informar quien fue el último (Nro Participante, Nombre, Apellido y Mejor disparo).
c)	Informar cuantos participantes formaron parte del concurso.
d)	Informar cuantos hombres formaron parte del concurso.
e)	Informar edad promedio de las mujeres.
f)	Mostrar el listado de todos los participantes ordenados por edad.
g)	Informar el promedio de todos los disparos.
h)	Mostrar los participantes cuyo promedio de disparo sea mayor al promedio general.
i)	Opcional: Mejorar el punto a) asumiendo que se puede dar el caso en que dos participantes tengan el mismo Mejor Disparo, ordenar también por mejor promedio.
