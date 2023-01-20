from tkinter import *
from tkinter import messagebox as mss
from mod_functions import *
import re

# => tareas pendientes al final del archivo

    

# General Function ----------------------------------------------------- 
def press(self, value):

    if value == "+" or value == "-" or value == "×" or value == "÷":
        operators(self, value)

    # press => Total (equal =) ------------------------- 
    elif value == "=":
        total_result(self, value)
 
    # press => C (borrar todo) -------------------------
    elif value == "C":
        delete_C(self, value)

    # press => ← (borrar último caracter) --------------
    elif value == "←":
        delete_last(self, value)

    # press => ( ) (paréntesis) ------------------------
    elif value == "( )":
        parentesis(self, value)

    # press => % (porcentaje) -------------------------- 
    elif value == "%":
        percent(self, value)
    
    # press => números ( 1 al 0) -----------------------
    else:
        number_point(self, value)
