<div align="center">

```
████████╗ ██████╗       ██████╗  ██████╗      ██╗     ██╗███████╗████████╗
╚══██╔══╝██╔═══██╗      ██╔══██╗██╔═══██╗     ██║     ██║██╔════╝╚══██╔══╝
   ██║   ██║   ██║█████╗██║  ██║██║   ██║     ██║     ██║███████╗   ██║   
   ██║   ██║   ██║╚════╝██║  ██║██║   ██║     ██║     ██║╚════██║   ██║   
   ██║   ╚██████╔╝      ██████╔╝╚██████╔╝     ███████╗██║███████║   ██║   
   ╚═╝    ╚═════╝       ╚═════╝  ╚═════╝      ╚══════╝╚═╝╚══════╝   ╚═╝   
```

### 🐍 Python Internship Project 1 — Industrial Training Kit

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![Internship](https://img.shields.io/badge/DecodeLabs-Internship%202026-orange?style=for-the-badge)
![GTU](https://img.shields.io/badge/GTU-Computer%20Engineering-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

<br>

> *"This isn't just a list. It is the primitive structure of every database you will ever build."*
> — DecodeLabs Industrial Training Kit

</div>

---

## 🧠 What Is This Project?

This is **Project 1** from the DecodeLabs Python Industrial Training Kit (Batch 2026), built as part of my 7th semester internship for **B.E. Computer Engineering under GTU**.

The goal was simple on the surface — build a To-Do List — but the real lesson was deeper:

| Surface Level | What It Actually Teaches |
|---|---|
| A list of tasks | How RAM stores ordered data |
| `append()` | INSERT operation in any database |
| `for` loop | Iterator Protocol used by every backend |
| `.txt` file | Data Persistence — keeping data alive after process death |
| `enumerate()` | Pythonic indexing, the professional way |

This is not a beginner's toy project. **It is the DNA of backend engineering.**

---

## ✨ Features

```
 ┌─────────────────────────────────────────────┐
 │                                             │
 │   📋  View all tasks                        │
 │   ➕  Add a new task                        │
 │   🗑️  Remove a completed task               │
 │   💾  Auto-save to tasks.txt on disk        │
 │   🔁  Persistent across sessions            │
 │                                             │
 └─────────────────────────────────────────────┘
```

---

## 🏗️ The Logic Skeleton (IPO Model)

```
┌────────────┐       ┌─────────────────┐       ┌──────────────┐
│            │       │                 │       │              │
│   INPUT    │──────▶│    PROCESS      │──────▶│   OUTPUT     │
│            │       │                 │       │              │
│ User types │       │ append/remove   │       │ Print tasks  │
│ a task     │       │ list operations │       │ to terminal  │
│            │       │                 │       │              │
└────────────┘       └─────────────────┘       └──────────────┘
                              │
                              ▼
                     ┌─────────────────┐
                     │   PERSISTENCE   │
                     │   tasks.txt     │
                     │   (Disk/Storage)│
                     └─────────────────┘
```

---

## 🗂️ Project Structure

```
📁 todo-list-python/
│
├── 📄 todo_list_simple.py     ← Main script
├── 📄 tasks.json              ← Auto-generated; stores your tasks
└── 📄 README.md               ← You are here
```

---

## 🚀 How to Run

**Step 1 — Make sure Python is installed:**
```bash
python --version
```

**Step 2 — Clone or download this repo:**
```bash
git clone https://github.com/YOUR_USERNAME/todo-list-python.git
cd todo-list-python
```

**Step 3 — Run the script:**
```bash
python todo_list_simple.py
```

**Step 4 — Use it:**
```
1. Show tasks  2. Add task  3. Remove task  4. Quit
Choose: 2
Task: Finish GTU assignment
Added!
```

> No pip install needed. No libraries. Pure Python. 🐍

---

## 🖥️ Sample Output

```
1. Show tasks  2. Add task  3. Remove task  4. Quit
Choose: 2
Task: Buy groceries
Added!

Choose: 2
Task: Complete Python project
Added!

Choose: 1
1. Buy groceries
2. Complete Python project

Choose: 3
Remove which number? 1
Removed: Buy groceries

Choose: 1
1. Complete Python project

Choose: 4
Bye! Tasks saved in tasks.txt
```

---

## 🔬 Under The Hood — What Python Is Actually Doing

```python
# Your variable is just a POINTER on the Stack...
my_tasks = []                        # Stack holds reference

# ...the actual LIST object lives in the Heap
my_tasks.append("Buy groceries")     # O(1) amortized — Heap expands

# Iteration uses the Iterator Protocol
for task in my_tasks:                # Creates temporary view
    print(task)

# enumerate() — the professional way (not range+len)
for i, task in enumerate(my_tasks, start=1):
    print(f"{i}. {task}")            # Clean, Pythonic, industry-standard

# Persistence — data moves from volatile RAM to permanent disk
with open("tasks.txt", "w") as f:   # Serialization to storage
    f.write(task + "\n")
```

---

## 📈 Key Python Concepts Practised

- ✅ **Lists** — Dynamic arrays, the foundation of every database
- ✅ **File I/O** — Reading and writing to disk (persistence)
- ✅ **`enumerate()`** — Professional iteration with index
- ✅ **`while` loop** — Menu-driven programs
- ✅ **`try/except`** — Graceful error handling
- ✅ **Functions** — Decoupled logic (load, save, show, add, remove)
- ✅ **String methods** — `.strip()`, `.isdigit()`

---

## 🛣️ Roadmap — What Comes Next

```
Project 1  ✅  To-Do List (Lists + File I/O)
    │
    ▼
Project 2  📌  Add due dates + mark done (Dictionaries + JSON)
    │
    ▼
Project 3  📌  Student Marks Calculator (Functions + OOP)
    │
    ▼
Project 4  📌  Database version (SQLite + Python)
    │
    ▼
  🚀         Full Backend with Flask REST API
```

---

## 👨‍💻 About Me

<div align="center">

```
 ██████╗ ██╗  ██╗ █████╗ ██╗   ██╗██╗   ██╗
 ██╔══██╗██║  ██║██╔══██╗██║   ██║╚██╗ ██╔╝
 ██████╔╝███████║███████║██║   ██║ ╚████╔╝ 
 ██╔══██╗██╔══██║██╔══██║╚██╗ ██╔╝  ╚██╔╝  
 ██████╔╝██║  ██║██║  ██║ ╚████╔╝    ██║   
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝     ╚═╝  
```

</div>

| | |
|---|---|
| 👤 **Name** | PATEL BHAVY |
| 🎓 **Degree** | B.E. Computer Engineering (4th Year) |
| 🏫 **University** | Gujarat Technological University (GTU) |
| 🏢 **Internship** | DecodeLabs — Python Programming Track |
| 📅 **Batch** | 2026 |
| 🌐 **LinkedIn** | [linkedin.com/in/bhavykumar-patel-3ba52530a](https://www.linkedin.com/in/bhavykumar-patel-3ba52530a) |

<br>

> *"The journey to becoming a professional developer begins right here, right now,*
> *with the very first line of code you write today."*
> — DecodeLabs

---

<div align="center">

Made with ❤️ and 🐍 by **PATEL BHAVY**

⭐ If this helped you, give it a star on GitHub!

</div>
