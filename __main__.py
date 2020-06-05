import tkinter
from tkinter import ttk
import abc

from Include.enums.Sex_enum import Sex
from Include.generateService import *


def generate_person() -> str:
    result = ""
    result += generate_name(Sex.MALE)
    result += generate_surname()
    result += str(generate_age())
    return result


class Window(ttk.Frame):
    """Abstract base class for a popup window"""
    __metaclass__ = abc.ABCMeta

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.resizable(width=False, height=False)
        self.validate_notempty = (self.register(self.notEmpty), '%P')
        self.init_gui()

    @abc.abstractmethod
    def init_gui(self):
        '''Initiates GUI of any popup window'''
        pass

    @abc.abstractmethod
    def action_button(self):
        '''Does something that all popup windows need to do'''
        pass

    def notEmpty(self, P):
        '''Validates Entry fields to ensure they aren't empty'''
        if P.strip():
            valid = True
        else:
            print("Error: Field must not be empty.")  # Prints to console
            valid = False
        return valid

    def close_win(self):
        '''Closes window'''
        self.parent.destroy()


class GeneratePersonWindow(Window):

    def init_gui(self):
        self.parent.title("Generate person")
        self.parent.columnconfigure(0, weight=1)
        self.parent.rowconfigure(3, weight=1)

        ##Validator
        def validate_float(inp):
            try:
                float(inp)
            except ValueError:
                return False
            return True

        vcmd = root.register(validate_float)

        def limit_size(*args):
            value = inputValue.get()
            if len(value) > 4: inputValue.set(value[:4])

        inputValue = tkinter.StringVar()
        inputValue.trace('w', limit_size)

        # Create Widgets
        self.label_title = ttk.Label(self.parent, text="Choose column in table!")
        self.frame_table_name = ttk.Frame(self.parent, relief="groove")
        self.contentframe = ttk.Frame(self.parent, relief="sunken")
        self.data_ammount_frame = ttk.Frame(self.parent, relief="groove")

        # Table Name
        self.label_table_name = ttk.Label(self.frame_table_name, text='Table name:')
        self.input_table_name = ttk.Entry(self.frame_table_name, state='normal')

        # Labels
        self.label_column_name = ttk.Label(self.contentframe, text='Column name:')
        self.label_to_generate = ttk.Label(self.contentframe, text='To generate:')
        self.label_in_queue = ttk.Label(self.contentframe, text='In queue:')

        # Name
        self.label_name = ttk.Label(self.contentframe, text='Name:')
        self.checkboxName = ttk.Checkbutton(self.contentframe)
        self.input_name = ttk.Entry(self.contentframe, validate='key', validatecommand=(vcmd, '%P'))

        # Surname
        self.label_surname = ttk.Label(self.contentframe, text='Surname:')
        self.checkbox_surname = ttk.Checkbutton(self.contentframe)
        self.input_surname = ttk.Entry(self.contentframe, validate='key', validatecommand=(vcmd, '%P'))

        # Sex
        self.label_sex = ttk.Label(self.contentframe, text='Sex:')
        self.checkbox_sex = ttk.Checkbutton(self.contentframe)
        self.input_sex = ttk.Entry(self.contentframe, validate='key', validatecommand=(vcmd, '%P'))

        # Age
        self.label_age = ttk.Label(self.contentframe, text='Age:')
        self.checkbox_age = ttk.Checkbutton(self.contentframe)
        self.input_age = ttk.Entry(self.contentframe, validate='key', validatecommand=(vcmd, '%P'))

        # Amount of data to generate
        self.label_data_amount = ttk.Label(self.data_ammount_frame, text='Data amount:')
        self.input_data_amount = ttk.Entry(self.data_ammount_frame, validate='key', validatecommand=(vcmd, '%P'),
                                           textvariable=inputValue)

        self.btn_do = ttk.Button(self.parent, text='Action', command=self.action_button)
        self.btn_cancel = ttk.Button(self.parent, text='Cancel', command=self.close_win)

        # Layout
        self.label_title.grid(row=0, column=0, columnspan=2, sticky='nsew')
        self.frame_table_name.grid(row=1, column=0, columnspan=2, sticky='nsew')
        self.contentframe.grid(row=3, column=0, columnspan=2, sticky='nsew')
        self.data_ammount_frame.grid(row=6, column=0, columnspan=3, sticky='nsew')

        # Labels
        row_value = 0
        self.label_column_name.grid(row=row_value, column=0)
        self.label_to_generate.grid(row=row_value, column=1)
        self.label_in_queue.grid(row=row_value, column=2)

        # Name
        row_value = 1
        self.label_name.grid(row=row_value, column=0)
        self.checkboxName.grid(row=row_value, column=1)
        self.input_name.grid(row=row_value, column=2)

        # Surname
        row_value = 2
        self.label_surname.grid(row=row_value, column=0)
        self.checkbox_surname.grid(row=row_value, column=1)
        self.input_surname.grid(row=row_value, column=2)

        # Sex
        row_value = 3
        self.label_sex.grid(row=row_value, column=0)
        self.checkbox_sex.grid(row=row_value, column=1)
        self.input_sex.grid(row=row_value, column=2)

        # Age
        row_value = 4
        self.label_age.grid(row=row_value, column=0)
        self.checkbox_age.grid(row=row_value, column=1)
        self.input_age.grid(row=row_value, column=2)

        # Data Amount
        self.label_data_amount.grid(row=0, column=0)
        self.input_data_amount.grid(row=0, column=1)

        # Button
        self.btn_do.grid(row=7, column=0, sticky='e')
        self.btn_cancel.grid(row=7, column=1, sticky='e')

        # Padding
        for child in self.parent.winfo_children():
            child.grid_configure(padx=10, pady=5)
        for child in self.contentframe.winfo_children():
            child.grid_configure(padx=5, pady=2)
        for child in self.frame_table_name.winfo_children():
            child.grid_configure(padx=5, pady=2)
        for child in self.data_ammount_frame.winfo_children():
            child.grid_configure(padx=2, pady=1)


    def action_button(self):  # text = self.input_name.get().strip()
        print(generate_person())


class GUI(ttk.Frame):
    """Main GUI class"""

    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()

    def generatePerson(self):
        self.new_win = tkinter.Toplevel(self.root)  # Set parent
        GeneratePersonWindow(self.new_win)

    def generateLocation(self):
        self.new_win = tkinter.Toplevel(self.root)  # Set parent
        ##GenerateLocationWindow(self.new_win)

    def init_gui(self):
        self.root.title('sqlGenerator')
        self.root.geometry("300x200")
        self.grid(column=0, row=0, sticky='nsew')
        self.grid_columnconfigure(0, weight=1)  # Allows column to stretch upon resizing
        self.grid_rowconfigure(0, weight=1)  # Same with row
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        # Create Widgets
        self.btn_generatePerson = ttk.Button(self, text='Generate person', command=self.generatePerson)
        self.btn_generate = ttk.Button(self, text='Generate location', command=self.generateLocation)

        # Layout using grid
        self.btn_generatePerson.grid(row=0, column=0, sticky='ew')
        self.btn_generate.grid(row=1, column=0, sticky='ew')

        # Padding
        for child in self.winfo_children():
            child.grid_configure(padx=10, pady=5)


if __name__ == '__main__':
    root = tkinter.Tk()
    GUI(root)
    root.mainloop()
