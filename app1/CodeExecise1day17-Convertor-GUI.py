import PySimpleGUI as sg
import converter as cn

from app1.app1gui import values

feet_label1 = sg.Text("Enter Feet" )
Inches_label2 = sg.Text("Enter Inches")
feet_Input= sg.Input(key= "feet")
inches_Input= sg.Input(key="inches")
choose_button1 = sg.Button("Convert")
output_in_meters = sg.Text(key ="meters")


window = sg.Window("Convertor", layout=[[feet_label1, feet_Input],
                                        [Inches_label2, inches_Input],
                                        [choose_button1, output_in_meters]],
                   font=('Helvetica',20))
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)

    match event:
        case "Convert":
            feet = float(values['feet'])
            inches = float(values['inches'])
            meter = cn.convert(feet, inches)
            window["meters"].update(value=f"{meter} m")

        case sg.WIN_CLOSED:
            break


window.close()
