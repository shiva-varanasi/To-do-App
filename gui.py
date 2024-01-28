import functions
import PySimpleGUI as sg

label = sg.Text("Enter a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My Todo App",
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            todo = values['todo'] + "\n"
            todos = functions.get_todos()
            todos.append(todo)
            functions.write_todos(todos)

        case sg.WINDOW_CLOSED:
            break

window.close()
