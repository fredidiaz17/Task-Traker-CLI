import json, os, sys
from datetime import datetime

FILEPATH = 'tasks.json'

def write_json(tasks):
    with open(FILEPATH, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=4)


# Crear tarea
def add(task):

    tasks = list(show= False)

    if tasks:
        last_id = tasks[-1]['id']
        t_id = last_id + 1
    else:
        t_id = 1

    now = datetime.now().replace(microsecond=0)

    data = {
        'id': t_id,
        'description': str(task).replace("_"," "),
        'status': 'todo',
        'createdAt': str(now),
        'updatedAt': str(now)
    }
    if tasks:
        tasks.append(data)
    else:
        tasks = [data]

    write_json(tasks)

    print(f"Task added successfully (ID: {t_id})")

# Actualizar tarea
def update(task_id, task_u):
    if task_id:
        done = False
        tasks = list(show= False)

        for task in tasks:
            if task['id'] == task_id:
                task['description'] = str(task_u).replace("_"," ")
                task['updatedAt'] = str(datetime.now().replace(microsecond=0))
                done = True
                break

        if done:
            print(f'Task updated successfully (ID: {task_id})')
        else:
            print(f'Task (ID: {task_id}) does not exist')
        write_json(tasks)

# Eliminar tarea
def delete(task_id):
    if task_id:
        done = False
        tasks = list(show= False)
        for task in tasks:
            if task['id'] == task_id:
                tasks.remove(task)
                done = True
                break

        if done:
            print(f'Task deleted successfully (ID: {task_id})')
        else:
            print(f'Task (ID: {task_id}) does not exist')
        write_json(tasks)

# Actualizar solo estatus - En progreso
def mark_in_progress(task_id):
    if task_id:
        done = False
        tasks = list(show= False)

        for task in tasks:
            if task['id'] == task_id:
                task['status'] = 'in progress'
                task['updatedAt'] = str(datetime.now())
                done = True
                break
        if done:
            print(f'Task {task_id} status changed to "in progress"')
        else:
            print(f'Task {task_id} does not exist')
        write_json(tasks)

# Actualizar solo estatus - Hecho
def mark_done(task_id):
    if task_id:
        done = False
        tasks = list(show= False)
        for task in tasks:
            if task['id'] == task_id:
                task['status'] = 'done'
                task['updatedAt'] = str(datetime.now())
                done = True
                break
        if done:
            print(f'Task {task_id} status changed to "done"')
        else:
            print(f'Task {task_id} does not exist')
        write_json(tasks)

# Listar
def list(only = None, show = True):
    data = None
    if only and only not in("done", "todo", "in_progress"):
        print('Status does not exist, please try with "done", "todo" or "in_progress"')
    elif os.path.isfile(FILEPATH):
        with open(FILEPATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if show:
            only = "in progress" if only == "in_progress" else only
            for task in data:
                if not only or task['status'] == only:
                    print(f"""
                                Task ID: {task["id"]}
                                Description: {task["description"]}
                                Status: {task["status"]} 
                                Created at: {task["createdAt"]}
                                Updated at: {task["updatedAt"]}
                                ----------------------------------------------""")

    return data


def convert_int(arg):
    try:
        return int(arg)
    except ValueError:
        print('Valor invalido')
        return None


if __name__ == "__main__":
    args = len(sys.argv)

    if args >1:
        match sys.argv[1]:

            case "add" if args > 2:
                add(sys.argv[2])

            case "update" if args > 3:
                task_id = convert_int(sys.argv[2])
                update(task_id, sys.argv[3])

            case "delete" if args > 2:
                task_id = convert_int(sys.argv[2])
                delete(task_id)

            case "mark_in_progress" if args > 2:
                task_id = convert_int(sys.argv[2])
                mark_in_progress(task_id)

            case "mark_done" if args > 2:
                task_id = convert_int(sys.argv[2])
                mark_done(task_id)

            case "list":
                if args > 2:
                    list(sys.argv[2])
                else:
                    list()
            case _:
                print("Comando invalido")



