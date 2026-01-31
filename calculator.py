import tkinter as tk
import math
import ast
import operator

# ---------------- SAFE EVALUATOR ----------------
class SafeEvaluator:
    operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow
    }

    functions = {
        'sin': math.sin,
        'cos': math.cos,
        'log': math.log,
        'sqrt': math.sqrt
    }

    def evaluate(self, expr):
        return self._eval(ast.parse(expr, mode='eval').body)

    def _eval(self, node):
        if isinstance(node, ast.BinOp):
            return self.operators[type(node.op)](
                self._eval(node.left),
                self._eval(node.right)
            )
        elif isinstance(node, ast.Call):
            func = node.func.id
            return self.functions[func](self._eval(node.args[0]))
        elif isinstance(node, ast.Num):
            return node.n
        else:
            raise ValueError("Invalid Expression")

# ---------------- CALCULATOR APP ----------------
class CalculatorApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Scientific Calculator")
        self.root.geometry("500x450")
        self.root.configure(bg="#1e1e1e")

        self.expression = ""
        self.history = []
        self.evaluator = SafeEvaluator()

        self.create_ui()
        self.bind_keys()

    # ---------- UI ----------
    def create_ui(self):
        self.display_var = tk.StringVar()

        entry = tk.Entry(
            self.root, textvariable=self.display_var,
            font=("Arial", 20), bg="black", fg="white",
            justify="right", bd=10
        )
        entry.pack(fill="x", padx=10, pady=10)

        main = tk.Frame(self.root, bg="#1e1e1e")
        main.pack()

        buttons = [
            '7','8','9','/','sin',
            '4','5','6','*','cos',
            '1','2','3','-','log',
            '0','.','=','+','sqrt'
        ]

        r = c = 0
        for btn in buttons:
            tk.Button(
                main, text=btn, width=6, height=2,
                font=("Arial", 12),
                bg="#2d2d2d", fg="white",
                command=lambda x=btn: self.on_click(x)
            ).grid(row=r, column=c, padx=4, pady=4)

            c += 1
            if c == 5:
                c = 0
                r += 1

        # ---------- HISTORY ----------
        history_frame = tk.Frame(self.root, bg="#1e1e1e")
        history_frame.pack(fill="both", expand=True)

        tk.Label(history_frame, text="History",
                 fg="white", bg="#1e1e1e").pack()

        self.history_box = tk.Listbox(
            history_frame, bg="black", fg="white"
        )
        self.history_box.pack(fill="both", expand=True, padx=10, pady=5)

    # ---------- BUTTON LOGIC ----------
    def on_click(self, value):
        if value == '=':
            self.calculate()
        elif value in ['sin', 'cos', 'log', 'sqrt']:
            self.expression += f"{value}("
            self.update()
        else:
            self.expression += value
            self.update()

    def calculate(self):
        try:
            result = self.evaluator.evaluate(self.expression)
            self.history.append(f"{self.expression} = {result}")
            self.history_box.insert(tk.END, self.history[-1])
            self.expression = str(result)
            self.update()
        except:
            self.display_var.set("Error")
            self.expression = ""

    def update(self):
        self.display_var.set(self.expression)

    # ---------- KEYBOARD ----------
    def bind_keys(self):
        self.root.bind("<Return>", lambda e: self.calculate())
        self.root.bind("<BackSpace>", lambda e: self.backspace())
        self.root.bind("<Escape>", lambda e: self.clear())

    def backspace(self):
        self.expression = self.expression[:-1]
        self.update()

    def clear(self):
        self.expression = ""
        self.update()

# ---------------- RUN APP ----------------
root = tk.Tk()
app = CalculatorApp(root)
root.mainloop()
