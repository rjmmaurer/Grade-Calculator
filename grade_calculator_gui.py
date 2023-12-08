import tkinter as tk
from tkinter import messagebox
from typing import List
from grade_calculator_functions import GradeCalculator

class GradeCalculatorGUI:
    """
    GUI for the Grade Calculator application.
    """

    def __init__(self, master: tk.Tk) -> None:
        """
        Initialize the GUI.

        Args:
            master (tk.Tk): The root window.
        """
        self.master = master
        master.title("Grade Calculator")

        master.geometry("400x300")
        master.resizable(False, False)

        self.label_students = tk.Label(master, text="Enter Student's Name:")
        self.label_students.pack()

        self.entry_students = tk.Entry(master)
        self.entry_students.pack()

        self.label_scores = tk.Label(master, text="Enter Score:")
        self.label_scores.pack()

        self.entry_scores = tk.Entry(master)
        self.entry_scores.pack()

        self.button_save = tk.Button(master, text="Save", command=self.save_entry)
        self.button_save.pack()

        self.button_submit = tk.Button(master, text="Submit", command=self.calculate_grades)
        self.button_submit.pack()

        self.result_text = tk.Text(master, height=10, width=50)
        self.result_text.pack()

        self.student_entries = []

    def save_entry(self) -> None:
        """
        Save the current student name and score entry.
        """
        student_name = self.entry_students.get()
        student_score = self.entry_scores.get()
        
        if any(char.isdigit() for char in student_name):
            messagebox.showinfo("Error", "Please enter a name without numbers.")
            return

        if student_name and student_score:
            try:
                score_float = float(student_score)
            except ValueError:
                messagebox.showinfo("Error", "Please enter a valid numeric score.")
                return
            
            entry_str = f"{student_name}: {student_score}"
            self.student_entries.append(entry_str)
            self.entry_students.delete(0, tk.END)
            self.entry_scores.delete(0, tk.END)
        else:
            messagebox.showinfo("Error", "Please enter both student name and score.")

    def calculate_grades(self) -> None:
        """
        Calculate grades based on user input.
        """
        try:
            student_names = [entry.split(":")[0] for entry in self.student_entries]
            scores_str = " ".join([entry.split(":")[1] for entry in self.student_entries])
            
            calculator = GradeCalculator(student_names)
            calculator.input_scores(scores_str)
            result = calculator.calculate_grades()
            self.display_result(result)
            self.student_entries = []
        except ValueError as e:
            self.display_result([f"Error: {e}"])

    def display_result(self, result: List[str]) -> None:
        """
        Display the calculated grades.

        Args:
            result (List[str]): List of strings containing student information and grades.
        """
        self.result_text.delete(1.0, tk.END)
        for line in result:
            self.result_text.insert(tk.END, line + "\n")

def main() -> None:
    root = tk.Tk()
    app = GradeCalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()