import functions
import PySimpleGUI as sg

label = sg.Text("Enter a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events= True, size = [45,10])
edit_button = sg.Button("Edit")

window = sg.Window("My Todo App",
                   layout=[[label], [input_box, add_button],
                           [list_box, edit_button]],
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
            window['todos'].update(values=todos)

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = functions.get_todos()
            position = todos.index(todo_to_edit)
            todos[position] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "todos":
            window['todo'].update(value=values['todos'][0])

        case sg.WINDOW_CLOSED:
            break

window.close()
