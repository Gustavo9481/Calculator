from tkinter import *
from tkinter import messagebox as mss
from mod_buttons import *
from mod_functions import *
from mod_press import *
import re



# Interface Colors -----------------------------------------------------

FOREGROUND = "#EAF4F4"    # font color, screens and buttons
BACKGROUND = "#000814"    # window color
BUTTONS = "#001D3D"       # Buttons color

root = Tk()


# Interface Generator -------------------------------------------------- 
class Calculadora:

    def __init__(self, window):
        self.window = window
        self.window.title("GUScode Calculator.")
        self.window.config(bg=BACKGROUND)
    
        
        # Display equation
        self.equation = Entry(window)
        self.equation.config(bd=0, width=26, font=("JetBrains", 15), fg=FOREGROUND, bg=BACKGROUND, justify="right")
        self.equation.grid(row=0, column=0, columnspan=4, padx=3, pady=1)

        # Display result
        self.result = Entry(window)
        self.result.config(bd=0, width=16, font=("JetBrains", 24), fg=FOREGROUND, bg=BACKGROUND, justify="right")
        self.result.grid(row=1, column=0, columnspan=4, padx=3, pady=1)

        # Color interface
        colors(self, FOREGROUND, BACKGROUND, BUTTONS)

        # Buttons
        btn_Delete = mk_button(self, "C")
        btn_Par = mk_button(self, "( )")
        btn_Percent = mk_button(self, "%")
        btn_Division = mk_button(self, "÷")
        btn_7 = mk_button(self, "7")
        btn_8 = mk_button(self, "8")
        btn_9 = mk_button(self, "9")
        btn_Multiply = mk_button(self, "×")
        btn_4 = mk_button(self, "4")
        btn_5 = mk_button(self, "5")
        btn_6 = mk_button(self, "6")
        btn_Sustract = mk_button(self, "-")
        btn_1 = mk_button(self, "1")
        btn_2 = mk_button(self, "2")
        btn_3 = mk_button(self, "3")
        btn_Sum = mk_button(self, "+")
        btn_0 = mk_button(self, "0")
        btn_Point = mk_button(self, ".")
        btn_DeleteLast = mk_button(self, "←")
        btn_Total = mk_button(self, "=")

        # function mk_button from modulo_botones

        buttons = [btn_Delete, btn_Par, btn_Percent, btn_Division, 
                btn_7, btn_8, btn_9, btn_Multiply, 
                btn_4, btn_5, btn_6, btn_Sustract, 
                btn_1, btn_2, btn_3, btn_Sum, 
                btn_0, btn_Point, btn_DeleteLast, btn_Total]

        mk_grid_buttons(self, buttons, 5) 
        # function mk_grid_buttons from modulo_botones



# Instance
The_Calculator = Calculadora(root)

if __name__ == "__main__":
    root.mainloop()
