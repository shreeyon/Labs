'''
Mini Project:
Simple To-Do Manager Using Functional Programming
Objective: Manage a list of to-do tasks using functions, lambda, filter, and map.
Requirements:
● Allow adding tasks using a function add_task(task_list, task_name).
● Each task is a dictionary: { "name": str, "completed": bool }.
● Use lambda and filter() to list only incomplete tasks.
● Use map() to mark all tasks as completed.
● Include a search_tasks(task_list, keyword) function using filter() and lambda.
Sample Workflow:
tasks = []
tasks = add_task(tasks, "Buy groceries")
tasks = add_task(tasks, "Finish assignment")
tasks = add_task(tasks, "Call friend")
# List incomplete tasks
print("Pending Tasks:", list_pending(tasks))
'''
def add_task(task_list, task_name):
    new_task = {"name": task_name, "completed": False}
    return task_list + [new_task]

def list_pending(task_list):
    return list(filter(lambda task: not task["completed"], task_list))

def mark_all_completed(task_list):
    return list(map(lambda task: {**task, "completed": True}, task_list))

def search_tasks(task_list, keyword):
    keyword = keyword.lower()
    return list(filter(lambda task: keyword in task["name"].lower(), task_list))

tasks = []

tasks = add_task(tasks, "Buy groceries")
tasks = add_task(tasks, "Finish assignment")
tasks = add_task(tasks, "Call friend")

print("Pending Tasks before completing:")
for t in list_pending(tasks):
    print("-", t["name"])

tasks = mark_all_completed(tasks)

print("\nPending Tasks after completing:")
pending_after = list_pending(tasks)
if pending_after:
    for t in pending_after:
        print("-", t["name"])
else:
    print("No pending tasks.")

print("\nSearch 'call':")
for t in search_tasks(tasks, "call"):
    print("-", t["name"], "Completed:", t["completed"])
