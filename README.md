[Previous Project (N/A)]()

# Project #1 - Task Tracker

Task Tracker is a project from [Roadmap.sh](https://roadmap.sh/projects/task-tracker).

> 🌐 [Leer en Español](README.es.md)

As its name suggests, this project is a command-line (CLI) task tracker that allows you to **create**, **list**, **update**, and **delete** tasks. Task data is persisted in a `.json` file.

---

## Prerequisites

- Python **3.10** or higher (`match` statements are used)
- No external dependencies required

---

## Installation and usage

1. Clone the repository.
```bash
git clone https://github.com/fredidiaz17/Task-Traker-CLI.git
```

2. Navigate to the project folder.
```bash
cd Task-Traker-CLI
```

3. Run the program with the desired command. Example:
```bash
python task-cli.py add wash_the_dishes
```

---

## Commands

The program is executed from the terminal. Once inside the project folder, the available commands are:

---

### `add` — Add a task
Creates a new task with the given description.

```bash
python task-cli.py add <description>
```

**Example:**
```bash
python task-cli.py add wash_the_dishes
```

---

### `update` — Update a task
Modifies the description of an existing task by its ID.

```bash
python task-cli.py update <id> <new_description>
```

**Example:**
```bash
python task-cli.py update 1 fix_the_dishes
```

---

### `delete` — Delete a task
Removes a task by its ID.

```bash
python task-cli.py delete <id>
```

**Example:**
```bash
python task-cli.py delete 1
```

---

### `list` — List tasks
Lists all tasks. If a status is provided, filters by it.

```bash
python task-cli.py list [status]
```

**Examples:**
```bash
python task-cli.py list
python task-cli.py list done
```

Available statuses: `done`, `in-progress`, `todo`.

---

### `mark_in_progress` — Mark as in progress
Changes a task's status to *in progress*.

```bash
python task-cli.py mark_in_progress <id>
```

**Example:**
```bash
python task-cli.py mark_in_progress 2
```

---

### `mark_done` — Mark as done
Changes a task's status to *done*.

```bash
python task-cli.py mark_done <id>
```

**Example:**
```bash
python task-cli.py mark_done 2
```

---

## Project structure

```text
Task-Traker-CLI/
├── task-cli.py        # Program entry point
├── tasks.json         # Auto-generated when the first task is added
└── README.md
```

---

## Limitations

- **Non-existent ID**: If the given ID does not match any task, the program prints a message: `Task (ID: 3) does not exist`.
- **Missing `tasks.json`**: If `tasks.json` does not exist and any command other than `add` is run, the program cannot operate as there are no tasks on record. `add` is the command that initializes the file.
- **Descriptions with spaces**: Since the program runs from the CLI, writing a description with regular spaces would cause an error, as the CLI would interpret each word as a separate argument. There are two ways to handle this:
  - Use underscores (`_`) instead of spaces — the program replaces them automatically.
    - Input: `Hello_world` → stored as: `Hello world`
  - Wrap the entire description in quotes: `"Hello world"`

---

## License

This is a **personal project with no defined license**.

---

[Next Project (Project #2 - GitHub User Activity)](https://github.com/fredidiaz17/GitHub-User-Activity)
