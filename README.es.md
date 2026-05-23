[Proyecto Anterior (N/A)]()

# Proyecto #1 - Task Tracker

Task Tracker es un proyecto extraído de [Roadmap.sh](https://roadmap.sh/projects/task-tracker).

> 🌐 [Read this in English](README.md)

Como su nombre indica, este proyecto es un *tracker* de tareas por línea de comandos (CLI),
que permite **crear**, **listar**, **actualizar** y **eliminar** tareas. 
El estado de las tareas se persiste en un archivo `.json`.

---

## Requisitos previos

<!-- [RELLENAR] Versión de Python utilizada. Ejemplo: -->
- Python **3.x** o superior
- No requiere dependencias externas

---

## Instalación y ejecución

1. Clonamos el repositorio.
```bash
git clone https://github.com/fredidiaz17/Task-Traker-CLI.git
```

2. Nos ubicamos en la carpeta del proyecto.
```bash
cd Task-Traker-CLI
```

3. Ejecutamos el programa con el comando deseado. Ejemplo:
```bash
python task-cli.py add lavar_los_platos
```

---

## Uso y comandos

El programa se ejecuta desde la terminal. Una vez ubicados en la carpeta del proyecto,
los comandos disponibles son:

---

### `add` — Agregar tarea
Crea una nueva tarea con la descripción indicada.

```bash
python task-cli.py add <descripción>
```

**Ejemplo:**
```bash
python task-cli.py add lavar_los_platos
```

---

### `update` — Actualizar tarea
Modifica la descripción de una tarea existente según su ID.

```bash
python task-cli.py update <id> <nueva_descripción>
```

**Ejemplo:**
```bash
python task-cli.py update 1 reparar_los_platos
```

---

### `delete` — Eliminar tarea
Elimina una tarea según su ID.

```bash
python task-cli.py delete <id>
```

**Ejemplo:**
```bash
python task-cli.py delete 1
```

---

### `list` — Listar tareas
Lista todas las tareas. Si se indica un estado, filtra por este.

```bash
python task-cli.py list [estado]
```

**Ejemplos:**
```bash
python task-cli.py list
python task-cli.py list done
```

Estados disponibles: `done`, `in-progress`, `todo`.

---

### `mark_in_progress` — Marcar como en progreso
Cambia el estado de una tarea a *in progress*.

```bash
python task-cli.py mark_in_progress <id>
```

**Ejemplo:**
```bash
python task-cli.py mark_in_progress 2
```

---

### `mark_done` — Marcar como completada
Cambia el estado de una tarea a *done*.

```bash
python task-cli.py mark_done <id>
```

**Ejemplo:**
```bash
python task-cli.py mark_done 2
```

---

## Estructura del proyecto

```text
Task-Traker-CLI/
├── task-cli.py        # Punto de entrada del programa
├── tasks.json         # Generado automáticamente al agregar la primera tarea
├── README.es.md      
└── README.md
```

<!-- [RELLENAR] Si hay archivos o carpetas adicionales (src/, módulos, etc.), agrégalos aquí. -->

---

## Limitaciones

<!-- [RELLENAR] Comportamiento ante casos borde que hayas definido tú, por ejemplo:
     - ¿Qué ocurre si se da un ID inexistente?
     - ¿Qué ocurre si tasks.json se elimina manualmente?
     - ¿Las descripciones admiten espacios o solo palabras sueltas? -->

---

## Licencia

Este es un **proyecto personal sin licencia definida**.

---

[Siguiente Proyecto (Proyecto #2 - GitHub User Activity)](https://github.com/fredidiaz17/GitHub-User-Activity)
