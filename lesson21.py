tasks = []
def show_tasks():
    if not tasks:
        print("No tasks yet!")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
while True:
    choice = input("(a)dd, (s)how, (q)uit: ").lower()
    if choice == "a":
        tasks.append(input("New task: "))
    elif choice == "s":
        show_tasks()
    elif choice == "q":
        print("Bye!")
        break
    else:
        print("Unknown choice")