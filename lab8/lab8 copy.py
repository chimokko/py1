import tkinter as tk
from tkinter import ttk, messagebox
import random
from abc import ABC, abstractmethod

class InvalidCategoryError(Exception):
    pass

class QuoteGenerator(ABC):
    def __init__(self):
        self.motivation = [
                "always remember that riot had spent 8k attempts on clubstep",
                "отойди от отжиманий и сделай 20 компов",
                "есть у нас, есть! никто из нас суицидом не закончит, ни единый! - Егор Летов"
            ]
        self.science = [
                "water boils at 100°C under normal circumstances",
                "pupils are actually just holes in your irises",
                "the speed of light is approximately 299,792 km/s."
            ]
        self.music = [
                "i'd like to have fun - Sid Viscious",
                "f minor scale - semi-gayidity - Dimebag Darell",
                "got a mexican homie named Chinese Mike - Danny Brown"
            ]

    @abstractmethod
    def generate_quote(self, category):
        pass

class Motivation(QuoteGenerator):
    def generate_quote(self):
        return random.choice(self.motivation)
class Science(QuoteGenerator):
    def generate_quote(self):
        return random.choice(self.science)
class Music(QuoteGenerator):
    def generate_quote(self):
        return random.choice(self.music)



class QuoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("im14andthisisdeep")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Select a category:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.category_input = tk.Text(self.root,height=3,width=30)
        self.category_input.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        self.generate_button = tk.Button(self.root, text="generate quote", command=self.get_quote)
        self.generate_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.quote_label = tk.Label(self.root, wraplength=400, justify="center")
        self.quote_label.grid(row=2, column=0, columnspan=2, pady=10, padx=10)
            

    def get_quote(self):
        try:
            category = self.category_input.get("1.0","end-1c").lower()
            self.quote = ""
            if category=="motivation":
                self.generator = Motivation()
                self.quote = self.generator.generate_quote()
            elif category=="science":
                self.generator = Science()
                self.quote = self.generator.generate_quote()
            elif category=="music":
                self.generator = Music()
                self.quote = self.generator.generate_quote()
            else:
                raise InvalidCategoryError
            self.quote_label.config(text=self.quote)
        except InvalidCategoryError as e:
            messagebox.showerror("invalid category arghhh >:(", f"no {category} category")

root = tk.Tk()
app = QuoteApp(root)
root.mainloop()
