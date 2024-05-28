import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from calculator.calculator import Calculator
from calculator.calc_operations import *

class InputField:
    def __init__(self, master):
        self.current_expression = tk.StringVar()
        self.input_field = ttk.Entry(master, textvariable=self.current_expression, font=('Arial', 14))
        self.input_field.grid(row=0, column=0, columnspan=5, sticky="nsew")

    def get_expression(self):
        return self.current_expression.get()

    def set_expression(self, expression):
        self.current_expression.set(expression)

    def clear(self):
        self.set_expression("")

    def delete_last_character(self):
        self.set_expression(self.get_expression()[:-1])


class HistoryPanel:
    def __init__(self, master):
        self.history_frame = ttk.Frame(master)
        self.history_frame.grid(row=1, column=0, columnspan=5, sticky="nsew")
        self.history_frame.grid_remove()  # Ukryj historię na początku

        self.history_text = tk.Text(self.history_frame, height=5, width=50, state='disabled')
        self.history_text.grid(row=0, column=0, sticky="nsew")

        self.toggle_button = ttk.Button(master, text="Pokaż historię", command=self.toggle_history)
        self.toggle_button.grid(row=2, column=0, columnspan=5, sticky="nsew")

        self.master = master

    def update_history(self, history):
        self.history_text.config(state='normal')
        self.history_text.delete('1.0', tk.END)
        for item in history[-5:]:
            self.history_text.insert(tk.END, item + "\n")
        self.history_text.config(state='disabled')

    def toggle_history(self):
        if self.history_frame.winfo_ismapped():
            self.history_frame.grid_remove()
            self.master.grid_rowconfigure(1, weight=0)
        else:
            self.history_frame.grid()
            self.master.grid_rowconfigure(1, weight=1)


class ButtonPanel:
    def __init__(self, master, on_button_click):
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 14), padding=10)

        self.buttons_frame = ttk.Frame(master)
        self.buttons_frame.grid(row=3, column=0, columnspan=5, sticky="nsew")

        buttons = [
            '7', '8', '9', '/', sqrt.__name__,
            '4', '5', '6', '*', pow.__name__,
            '1', '2', '3', '-', sin.__name__,
            '.', '0', '=', '+', cos.__name__,
            ',', '←', '(', ')', tan.__name__,
            'C', fac.__name__, ln.__name__, log_base.__name__, cot.__name__,
            circ.__name__, rect.__name__, lin.__name__, quad.__name__, absolute.__name__,
            mod.__name__, log10.__name__, dec_to_bin.__name__, dec_to_oct.__name__, dec_to_hex.__name__
        ]

        row = 0
        col = 0
        for button in buttons:
            button_widget = ttk.Button(self.buttons_frame, text=button, style='TButton', command=lambda b=button: on_button_click(b))
            button_widget.grid(row=row, column=col, sticky="nsew")
            col += 1
            if col > 4:
                col = 0
                row += 1

        # Ustawienie wagi kolumn dla buttons_frame
        for i in range(5):
            self.buttons_frame.grid_columnconfigure(i, weight=1)
        # Ustawienie wagi wierszy dla buttons_frame
        for i in range(row + 1):
            self.buttons_frame.grid_rowconfigure(i, weight=1)


class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Kalkulator - s26110")

        self.model = Calculator()

        self.input_field = InputField(master)
        self.history_panel = HistoryPanel(master)
        self.button_panel = ButtonPanel(master, self.on_button_click)

        self.update_history()

        master.bind('<Return>', lambda event: self.on_button_click('='))
        master.bind('<BackSpace>', lambda event: self.on_button_click('←'))

        # Elastyczne zarządzanie rozmiarem wierszy i kolumn
        for i in range(4):
            master.grid_rowconfigure(i, weight=1)
            master.grid_columnconfigure(i, weight=1)

    def on_button_click(self, button):
        match button:
            case '=':
                try:
                    result = eval(self.input_field.get_expression())
                    self.model.history.add_to_history(self.input_field.get_expression() + " = " + str(result))
                    self.input_field.set_expression(str(result))
                    self.update_history()
                except Exception as e:
                    messagebox.showerror("Błąd", str(e))
            case '←':
                self.input_field.delete_last_character()
            case 'C':
                self.input_field.clear()
            case 'sqrt':
                self.input_field.set_expression(self.input_field.get_expression() + "sqrt(")
            case 'pow':
                self.input_field.set_expression(self.input_field.get_expression() + "**")
            case 'sin':
                self.input_field.set_expression(self.input_field.get_expression() + "sin(")
            case 'cos':
                self.input_field.set_expression(self.input_field.get_expression() + "cos(")
            case 'tan':
                self.input_field.set_expression(self.input_field.get_expression() + "tan(")
            case 'cot':
                self.input_field.set_expression(self.input_field.get_expression() + "cot(")
            case 'fac':
                self.input_field.set_expression(self.input_field.get_expression() + "fac(")
            case 'ln':
                self.input_field.set_expression(self.input_field.get_expression() + "ln(")
            case 'log_base':
                self.input_field.set_expression(self.input_field.get_expression() + "log_base(")
            case 'circ':
                self.input_field.set_expression(self.input_field.get_expression() + "circ(")
            case 'rect':
                self.input_field.set_expression(self.input_field.get_expression() + "rect(")
            case 'lin':
                self.input_field.set_expression(self.input_field.get_expression() + "lin(")
            case 'quad':
                self.input_field.set_expression(self.input_field.get_expression() + "quad(")
            case 'absolute':
                self.input_field.set_expression(self.input_field.get_expression() + "abs(")
            case 'mod':
                self.input_field.set_expression(self.input_field.get_expression() + "%")
            case 'log10':
                self.input_field.set_expression(self.input_field.get_expression() + "log10(")
            case 'dec_to_bin':
                self.input_field.set_expression(self.input_field.get_expression() + "dec_to_bin(")
            case 'dec_to_oct':
                self.input_field.set_expression(self.input_field.get_expression() + "dec_to_oct(")
            case 'dec_to_hex':
                self.input_field.set_expression(self.input_field.get_expression() + "dec_to_hex(")
            case _:
                self.input_field.set_expression(self.input_field.get_expression() + button)

    def update_history(self):
        history = self.model.history.get_history()
        self.history_panel.update_history(history)