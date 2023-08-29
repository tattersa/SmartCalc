import tkinter as tk
from src.view_model.check_parse import check_parse


class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Калькулятор")

        # Создаем строку ввода
        self.display_var = tk.StringVar(value="")
        self.display = tk.Label(
            self.master,
            textvariable=self.display_var,
            font='Px\\ IBM\\ EGA8 16',
            justify='left',
            width=37,
            height=3,
            anchor="e",
            bg="white",
            bd=5,
            relief="ridge"
        )
        self.display.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

        self.result_var = tk.StringVar(value="")
        self.result = tk.Label(
            self.master,
            textvariable=self.result_var,
            font='Px\\ IBM\\ EGA8 20',
            width=16,
            height=2,
            anchor="e",
            bg="white",
            bd=5,
            relief="ridge"
        )
        self.result.grid(row=0, column=3, columnspan=3, padx=5, pady=5)

        # Создаем кнопки
        buttons = [
            {"text": "1", "row": 3, "column": 0},
            {"text": "2", "row": 3, "column": 1},
            {"text": "3", "row": 3, "column": 2},
            {"text": "4", "row": 2, "column": 0},
            {"text": "5", "row": 2, "column": 1},
            {"text": "6", "row": 2, "column": 2},
            {"text": "7", "row": 1, "column": 0},
            {"text": "8", "row": 1, "column": 1},
            {"text": "9", "row": 1, "column": 2},
            {"text": "0", "row": 4, "column": 0},
            {"text": "/", "row": 4, "column": 3},
            {"text": "*", "row": 3, "column": 3},
            {"text": "-", "row": 2, "column": 3},
            {"text": "+", "row": 1, "column": 3},
            {"text": ".", "row": 4, "column": 1},
            {"text": "=", "row": 5, "column": 0, "columnspan": 2},
            {"text": "C", "row": 4, "column": 2},
            {"text": "(", "row": 1, "column": 4},
            {"text": ")", "row": 1, "column": 5},
            {"text": "sin", "row": 2, "column": 4},
            {"text": "cos", "row": 2, "column": 5},
            {"text": "tan", "row": 4, "column": 5},
            {"text": "acos", "row": 3, "column": 5},
            {"text": "asin", "row": 3, "column": 4},
            {"text": "atan", "row": 5, "column": 5},
            {"text": "sqrt", "row": 4, "column": 4},
            {"text": "ln", "row": 5, "column": 4},
            {"text": "log", "row": 5, "column": 3},
            {"text": "<-", "row": 5, "column": 2},
            {"text": "Help", "row": 4, "column": 7},
            {"text": "History", "row": 5, "column": 7},
            {"text": "Quit", "row": 6, "column": 7}
        ]
        for button in buttons:
            command = lambda x=button["text"]: self.button_click(x)
            tk.Button(
                self.master,
                text=button["text"],
                font='Px\\ IBM\\ EGA8 16',
                width=5,
                height=2,
                bd=5,
                bg="#F0F0F0",
                command=command
            ).grid(
                row=button["row"],
                column=button["column"],
                padx=10,
                pady=10,
                columnspan=button.get("columnspan", 1),
                sticky="nsew"
            )

    # Обработчик кликов по кнопкам
    def button_click(self, text):
        if text == "C":
            self.display_var.set("")
            self.result_var.set("")
        elif text == "=":
            result = check_parse(self.display_var.get())
            self.result_var.set(result)
        elif text == "(":
            self.display_var.set(self.display_var.get() + "(")
        elif text == ")":
            self.display_var.set(self.display_var.get() + ")")
        elif text == "sin":
            self.display_var.set(self.display_var.get() + "sin")
        elif text == "cos":
            self.display_var.set(self.display_var.get() + "cos")
        elif text == "tan":
            self.display_var.set(self.display_var.get() + "tan")
        elif text == "acos":
            self.display_var.set(self.display_var.get() + "acos")
        elif text == "asin":
            self.display_var.set(self.display_var.get() + "asin")
        elif text == "atan":
            self.display_var.set(self.display_var.get() + "atan")
        elif text == "sqrt":
            self.display_var.set(self.display_var.get() + "sqrt")
        elif text == "ln":
            self.display_var.set(self.display_var.get() + "log1p")
        elif text == "log":
            self.display_var.set(self.display_var.get() + "log")
        elif text == "<-":
            self.display_var.set(self.display_var.get()[:-1])
        else:
            if self.display_var.get() == "0":
                self.display_var.set(text)
            else:
                self.display_var.set(self.display_var.get() + text)


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
