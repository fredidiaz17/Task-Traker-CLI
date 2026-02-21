# Proyecto #1 - Task Traker
task-tracker-cli es un proyecto extraido de [Roadma.sh](https://roadmap.sh/projects/task-tracker)

Como su nombre indica, este proyecto es un *tracker* de tareas por medio de línea de comandos  
(CLI), permitiendo hacer acciones como *crear*, *listar*, *actualizar* y *eliminar* tareas.
Se vale del manejo de un archivo .JSON para esta labor.

## Modo de uso + Ejemplos
El proyecto está pensando para ser ejecutado con comandos desde terminal (o similar), 
razón por la que el programa no posee una GUI.
Una vez ubicados en la ruta del archivo (en terminal), ya podemos empezar a usar el programa.
Entre las funciones disponibles tenemos:
- **add**: Agregar tarea. Solo es necesario suministrar la descripción de esta. 
</br>     Ejemplo: `py task-cli.py add lavar_los_platos`
- **update**: Actualiza la tarea seleccionada. Es necesario dar el ID de la tarea y la descripción a cambiar.
</br>    Ejemplo: `py task-cli.py update 1 reparar_los_platos`
- **delete**: Elimina la tarea. Solo hay que dar la ID de la tarea.
</br>    Ejemplo: `py task-cli.py delete 1`
- **list**: Lista todas las tareas según el status. Si no se da status, simplemente las lista todas.
</br>    Ejemplo 1: `py task-cli.py list`
</br>    Ejemplo 2: `py task-cli.py list done`
- **mark_in_progress**: Marca (el estado) la tarea como "in progress" (En progreso). Se suministra el ID de la tarea.
</br>    Ejemplo: `py task-cli.py mark_in_progress 2`
- **mark_done**: Marca la tarea como "done" (Hecho). Se suministra el ID de la tarea
</br>    Ejemplo: `py task-cli.py mark_done 2`

Estas funciones van de acuerdo a los ejemplos dados en la pagina del proyecto, razón por la que mark_in_progress y mark_done son 2 funciones diferentes y no una sola. </br>
El proyecto tiene ciertos detalles que no se especificaron como manejarlos, dejandome la libertad de decidir como tratarlos, </br>
razón por la que puede parecer que este proyecto pequeño está mas completo de lo normal en algunos aspectos, pero flaqueando en otros. </br>
Igualmente, al tratarse de un proyecto sencillo y siendo el primero de varios, considero que no es necesario darle mas complejidad de lo necesario. </br>

Aunque es un proyecto muy basico (considerando lo que he hecho y estoy haciendo), </br> he decidido hacerlo con tal de
mantener el orden de proyectos establecido en la página anteriormente mencionada

[Siguiente proyecto]() 