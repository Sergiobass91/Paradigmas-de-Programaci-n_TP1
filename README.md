# Paradigmas de Programación TP1
#### Primer TP - Paradigmas IFTS18

Cada año se desarrolla el campeonato nacional de tiro con arco y flecha. Se desea reemplazar el sistema de seguimiento y control de los participantes por un programa escrito en Python.
Que es lo que sabemos del concurso:

- Pueden participar hombres y mujeres de todas las edades.
- Cada participante deberá realizar 3 disparos (obligatorio).
- Se dispara a un blanco cuyo centro coincide con el origen de coordenadas de un eje 	  	cartesiano (x, y). La mejor puntuación la obtiene el disparo más cercano al origen.
- Cada participante tiene un número único que lo identifica del resto.
- El radio del tablero es de 80 cm.

El programa debe realizar por cada participante, el ingreso de los siguientes datos:
a)	Número único del participante.
b)	Nombre y Apellido del participante.
c)	Edad del participante.
d)	Sexo del participante.
e)	Ubicación de los disparos en pares X e Y. Solo almacenar la distancia al origen de cada disparo.
- El fin de ingreso de participantes se determina ingresando con número de participante igual a 999.
-   El campo MejorDisp deberá almacenar el mejor disparo de cada participante.
-   El campo PromDisp deberá almacenar el promedio de los 3 disparos de cada participante.

Se pide:
1. Mostrar el podio de los ganadores (los 3 primeros) en función del Mejor Disparo (Nro Participante, Nombre, Apellido y Mejor disparo). Se pide informar por pantalla y en un archivo de texto.
2. Informar quien fue el último (Nro Participante, Nombre, Apellido y Mejor disparo).
3. Informar cuantos participantes formaron parte del concurso.
4. Informar cuantos hombres formaron parte del concurso.
5. Informar edad promedio de las mujeres.
6. Mostrar el listado de todos los participantes ordenados por edad.
7. Informar el promedio de todos los disparos.
8. Mostrar los participantes cuyo promedio de disparo sea mayor al promedio general.
9. Opcional: Mejorar el punto a) asumiendo que se puede dar el caso en que dos participantes tengan el mismo Mejor Disparo, ordenar también por mejor promedio.
