#EX3

def insert(tasks,new):
    tasks.append(new)
def remove(tasks, task):
    tasks.remove(task)
def show(tasks):
    tasks = sorted(tasks)
    for task in tasks:
        print(task)

tasks = []

while True:
    print("Insert the number corresponding to the action you want to perform:\n"
      "1. insert a new task;\n"
      "2. remove a task;\n"
      "show all existing tasks, sorted in alphabetic order;\n"
      "4. close the program.\n"
      "Your choice:")

    choice=int(input())

    if choice == 1:
        print("Insert a new task:")
        insert(tasks,input())

    elif choice == 2:
        print("Insert a task to delete:")
        remove(tasks, input())

    elif choice == 3:
        show(tasks)

    elif choice == 4:
        exit()
    else:
        continue

