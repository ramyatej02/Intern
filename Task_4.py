import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.expression = ""
        self.text_input = tk.StringVar()

        # Setting a yellow background for the calculator
        self.root.configure(bg='yellow')

        # Creating the display for the calculator
        self.display = tk.Entry(root, font=('arial', 20, 'bold'), textvariable=self.text_input, bd=30, insertwidth=4, width=14, borderwidth=4)
        self.display.grid(row=0, column=0, columnspan=4)

        # Creating buttons
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'clr', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            action = lambda x=button: self.click_event(x)
            tk.Button(self.root, text=button, padx=20, pady=20, bd=8, fg='black', bg='light yellow', font=('arial', 20, 'bold'), command=action).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def click_event(self, key):
        if key == '=':
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Error"
            self.text_input.set(self.expression)
        elif key == 'clr':
            self.expression = ""
            self.text_input.set("")
        else:
            self.expression += str(key)
            self.text_input.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
