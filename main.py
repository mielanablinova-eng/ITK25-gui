# main.py
import tkinter as tk
from classes.gui import GUIApp

if __name__ == "__main__":
    root = tk.Tk()
    app = GUIApp(root)
    root.mainloop()