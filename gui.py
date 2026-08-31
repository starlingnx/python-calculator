import tkinter as tk
from tkinter import messagebox
from calculator import Calculator

class CalculatorApp:
    """Simple Tkinter GUI for the Calculator class."""

    def __init__(self, master=None):
        self.calc = Calculator()
        self.root = master or tk.Tk()
        self.root.title("Python Calculator")
        self._build_ui()

    def _build_ui(self):
        frm = tk.Frame(self.root, padx=10, pady=10)
        frm.pack(fill=tk.BOTH, expand=True)

        self.expr_var = tk.StringVar()
        self.result_var = tk.StringVar()

        tk.Label(frm, text="Expression:").grid(row=0, column=0, sticky=tk.W)
        self.expr_entry = tk.Entry(frm, textvariable=self.expr_var, width=40)
        self.expr_entry.grid(row=0, column=1, columnspan=3, sticky=tk.W)

        tk.Button(frm, text="Evaluate", command=self.on_evaluate).grid(row=1, column=1)
        tk.Button(frm, text="Clear", command=self.on_clear).grid(row=1, column=2)
        tk.Button(frm, text="History", command=self.on_history).grid(row=1, column=3)

        tk.Label(frm, text="Result:").grid(row=2, column=0, sticky=tk.W)
        tk.Label(frm, textvariable=self.result_var, width=40, anchor=tk.W, relief=tk.SUNKEN).grid(row=2, column=1, columnspan=3, sticky=tk.W)

        # make Enter evaluate
        self.expr_entry.bind("<Return>", lambda e: self.on_evaluate())

    def on_evaluate(self):
        expr = self.expr_var.get().strip()
        if not expr:
            return
        try:
            result = self.calc.evaluate(expr)
            self.result_var.set(str(result))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def on_clear(self):
        self.expr_var.set("")
        self.result_var.set("")

    def on_history(self):
        hist = self.calc.get_history()
        win = tk.Toplevel(self.root)
        win.title("Calculation History")
        lb = tk.Listbox(win, width=80)
        lb.pack(padx=8, pady=8, fill=tk.BOTH, expand=True)
        for item in hist:
            lb.insert(tk.END, item)

    def run(self):
        self.root.mainloop()
