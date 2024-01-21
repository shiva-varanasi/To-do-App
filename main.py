import functions
import time

now = time.strftime("%b %d - %Y")
print("It is", now)

while True:
    user_action = input("Enter add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{(index + 1)}-{item}")

    elif user_action.startswith("edit"):
        try:
            pos = int(user_action[5:])
            new_todo = input("Enter the new todo: ") + '\n'
            todos = functions.get_todos()

            todos[pos-1] = new_todo

            functions.write_todos(todos)
        except ValueError:
            print("Your command is invalid. Enter the number of the todo you want to edit")
            continue

    elif user_action.startswith("complete"):
        try:
            pos = int(user_action[9:])
            todos = functions.get_todos()

            completed_todo = todos.pop(pos - 1)
            completed_todo = completed_todo.strip('\n')

            functions.write_todos(todos)

            print(f"Todo {completed_todo} is marked as complete and removed from the todos")
        except IndexError:
            print("There is no todo with that number")
            continue
        except ValueError:
            print("Your command is invalid. Enter the number of the todo you want to complete")

    elif user_action.startswith("exit"):
        break

    else:
        print("Hey, you entered an unknown command")

print("you are exited")