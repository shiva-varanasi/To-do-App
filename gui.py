import functions
import PySimpleGUI as sg

label = sg.Text("Enter a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window("My Todo App", layout=[[label], [input_box, add_button]])
window.read()
window.close()