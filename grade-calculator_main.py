import tkinter as tk
from grade_calculator_gui import GradeCalculatorGUI, main

if __name__ == "__main__":
    root = tk.Tk()
    app = GradeCalculatorGUI(root)
    root.mainloop()
