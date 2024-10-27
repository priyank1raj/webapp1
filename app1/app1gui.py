import PySimpleGUI as sg
import function
import time

sg.theme('Dark Blue 3')
clock = sg.Text("", key= "clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add", size= 10)
list_box = sg.Listbox(values=function.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button('Edit')
complete_button = sg.Button("Complete")
exit_button = sg.Button('Exit')

window=sg.Window('My To-Do App',
                 layout=[[clock],
                         [label],
                         [input_box, add_button],
                         [list_box, edit_button, complete_button],
                         [exit_button]],
                 font=('Helvetica',20))
while True:
    event, values = window.read(timeout=500)
    window["clock"].update(value=time.strftime("%b %d %Y %H:%M:%S"))
    print(1, event)
    print(2, values)
    print (3, values['todos'])
    match event:
        case "Add":
            todos = function.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            function.write_todos(todos)
            window['todos'].update(values=todos)
        case "todos":
            try:
                window['todo'].update(value=values['todos'][0])
            except TypeError:
                break
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"
                todos = function.get_todos()
                index =todos.index(todo_to_edit)
                todos[index] = new_todo
                function.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica',10))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = function.get_todos()
                todos.remove(todo_to_complete)
                function.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value = "")
            except IndexError:
                sg.popup("Please Select a Item first", font=('Helvetica',10))
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
window.close()