# classes/gui.py
import tkinter as tk
from tkinter import ttk
from classes.checks import ResultChecker


class GUIApp:
    def __init__(self, root):
        self.root = root
        self.root.title(" Sisendi Analüsaator")

        self.label = tk.Label(root, text="Sisesta väärtus:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=5)

        self.text = tk.Text(root, height=20, width=60, state='normal')
        self.text.pack(pady=10)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.show_button = tk.Button(self.button_frame, text="Näita", command=self.show_results)
        self.show_button.pack(side=tk.LEFT, padx=5)

        self.clear_button = tk.Button(self.button_frame, text="Puhasta", command=self.clear_text)
        self.clear_button.pack(side=tk.LEFT, padx=5)

    def show_results(self):
        input_val = self.entry.get()
        checker = ResultChecker(input_val)
        results = checker.get_all_results()
        self.text.insert(tk.END, results + "\n\n")
        self.entry.delete(0, tk.END)

    def clear_text(self):
        self.text.delete(1.0, tk.END)
        self.text.delete(1.0, tk.END)