import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")

        self.result_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Entry widget to display the result
        entry_frame = ttk.Frame(self.root, padding="10")
        entry_frame.grid(row=0, column=0, columnspan=4)
        entry = ttk.Entry(entry_frame, textvariable=self.result_var, font=('Helvetica', 18), justify="right")
        entry.grid(row=0, column=0, sticky="nsew")
        entry_frame.columnconfigure(0, weight=1)

        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, col) in buttons:
            btn = ttk.Button(self.root, text=text, command=lambda t=text: self.button_click(t), style='TButton')
            btn.grid(row=row, column=col, sticky="nsew", ipadx=10, ipady=10)
            self.root.grid_columnconfigure(col, weight=1)
            self.root.grid_rowconfigure(row, weight=1)

    def button_click(self, button_text):
        current_text = self.result_var.get()

        if button_text == '=':
            try:
                result = eval(current_text)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif button_text == 'C':
            self.result_var.set('')
        else:
            self.result_var.set(current_text + button_text)


if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    style.configure('TButton', font=('Helvetica', 14), foreground='black', background='#a6a6a6')
    calculator = Calculator(root)
    root.mainloop()
