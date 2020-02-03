from tkinter import *
from functools import partial  # To prevent unvanted windows

import random


class Convertor:
    def __init__(self, parent):

        # Formatting variables..
        background_color = "light blue"

        # Converter Main Screen GUI...
        self.converter_frame = Frame(width=300, height=300, bg=background_color)
        self.converter_frame.grid()

        #Temporature Conversion Heading (row 0)
        self.temp_converter_lebel = Label(self.converter_frame, text="Temperature Converter",
                                          font=("Arial","16","bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_lebel.grid(row=0)

        # Help Button (row 1)
        self.help_button = Button(self.converter_frame, text="help",
                                  padx=10, pady=10)
        self.help_button.grid(row=1)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Convertor(root)
    root.mainloop()
