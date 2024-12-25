import tkinter as tk
from tkinter import ttk, messagebox
import random

class InvalidCategoryError(Exception):
    pass

class QuoteGenerator:
    def __init__(self):
        self.data = {
            "motivation": [
                "always remember that riot had spent 8k attempts on clubstep",
                "отойди от отжиманий и сделай 20 компов",
                "есть у нас, есть! никто из нас суицидом не закончит, ни единый! - Егор Летов"
            ],
            "science": [
                "water boils at 100°C under normal circumstances",
                "pupils are actually just holes in your irises",
                "the speed of light is approximately 299,792 km/s."
            ],
            "music": [
                "i'd like to have fun - Sid Viscious",
                "f minor scale - semi-gayidity - Dimebag Darell",
                "got a mexican homie named Chinese Mike - Danny Brown"
            ]
        }

    def get_quote(self, category):
        if category not in self.data:
            raise InvalidCategoryError(f"category '{category}' is not available")
        return random.choice(self.data[category])


class QuoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("im14andthisisdeep")

        self.generator = QuoteGenerator()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Select a category:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.category_combobox = ttk.Combobox(
            self.root,
            values=list(self.generator.data.keys()),
            state="readonly"
        )
        self.category_combobox.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        self.category_combobox.set("motivation")

        self.generate_button = tk.Button(self.root, text="generate quote", command=self.generate_quote)
        self.generate_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.quote_label = tk.Label(self.root, wraplength=400, justify="center")
        self.quote_label.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

    def generate_quote(self):
        try:
            category = self.category_combobox.get()
            quote = self.generator.get_quote(category)
            self.quote_label.config(text=quote)
        except InvalidCategoryError as e:
            messagebox.showerror("invalid category arghhh >:(", str(e))

root = tk.Tk()
app = QuoteApp(root)
root.mainloop()
