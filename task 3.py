import random
import string
import tkinter as tk
from tkinter import ttk

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Password Generator")

        self.length_label = ttk.Label(master, text="Length:")
        self.length_label.grid(row=0, column=0, sticky="w")

        self.length_entry = ttk.Entry(master)
        self.length_entry.grid(row=0, column=1)

        self.complexity_label = ttk.Label(master, text="Complexity:")
        self.complexity_label.grid(row=1, column=0, sticky="w")

        self.complexity_combo = ttk.Combobox(master, values=["Low", "Medium", "High"])
        self.complexity_combo.grid(row=1, column=1)
        self.complexity_combo.current(1)

        self.generate_button = ttk.Button(master, text="Generate", command=self.generate_password)
        self.generate_button.grid(row=2, columnspan=2)

        self.password_label = ttk.Label(master, text="")
        self.password_label.grid(row=3, columnspan=2)

    def generate_password(self):
        length = int(self.length_entry.get())
        complexity = self.complexity_combo.get()

        if complexity == "Low":
            characters = string.ascii_letters + string.digits
        elif complexity == "Medium":
            characters = string.ascii_letters + string.digits + string.punctuation
        else:
            characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase

        password = ''.join(random.choice(characters) for i in range(length))
        self.password_label.config(text=password)

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()