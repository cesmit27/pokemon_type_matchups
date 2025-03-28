import json
import tkinter as tk
from tkinter import ttk, messagebox
from collections import OrderedDict

#Open JSON file containing the Pokémon and their type as well as any alternate forms
with open('pokemon_data.json') as f:
    pokemon_data = json.load(f)

#Open JSON file with type matchups
with open('type_effectiveness.json') as f:
    type_effectiveness = json.load(f)

def flatten_forms(node, prefix=""):
    """
    Recursively flatten the forms dictionary while preserving the order.
    If node is a list, return an OrderedDict with {prefix: node}.
    If node is a dict, combine keys (with a space separator) to create a flat mapping.
    """
    forms = OrderedDict()
    if isinstance(node, list):
        key = prefix.strip() if prefix else ""
        forms[key] = node
    elif isinstance(node, dict):
        for key, value in node.items():
            new_prefix = f"{prefix} {key}".strip() if prefix else key
            #Update while preserving order
            forms.update(flatten_forms(value, new_prefix))
    return forms

class PokeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pokémon Type Checker")
        self.geometry("600x700")
        self.resizable(True, True)
        
        #Variables for entry and dropdown selection
        self.pokemon_var = tk.StringVar()
        self.variant_var = tk.StringVar()
        self.flattened_forms = OrderedDict()  #Will hold flattened mapping for current Pokémon
        
        self.create_widgets()

    def create_widgets(self):
        #Top frame for Pokémon search
        self.search_frame = ttk.Frame(self)
        self.search_frame.pack(pady=10, fill='x', padx=10)

        ttk.Label(self.search_frame, text="Enter your Pokémon:").grid(row=0, column=0, padx=5, pady=5)
        self.entry = ttk.Entry(self.search_frame, textvariable=self.pokemon_var, width=30)
        self.entry.grid(row=0, column=1, padx=5, pady=5)

        self.search_button = ttk.Button(self.search_frame, text="Search", command=self.start_search)
        self.search_button.grid(row=0, column=2, padx=5, pady=5)

        #Frame for alternate form dropdown (if needed)
        self.dropdown_frame = ttk.Frame(self)
        self.dropdown_frame.pack(pady=10, fill='x', padx=10)

        #Text widget for results
        self.result_text = tk.Text(self, width=70, height=25, state='disabled')
        self.result_text.pack(pady=10, padx=10, fill='both', expand=True)

    def clear_dropdown(self):
        for widget in self.dropdown_frame.winfo_children():
            widget.destroy()
        self.variant_var.set("")

    def start_search(self):
        #Clear previous dropdowns and results
        self.clear_dropdown()
        self.result_text.config(state='normal')
        self.result_text.delete(1.0, tk.END)
        self.result_text.config(state='disabled')

        name = self.pokemon_var.get().strip().title()
        if not name:
            messagebox.showwarning("Input Error", "Please enter a Pokémon name.")
            return

        if name not in pokemon_data:
            messagebox.showinfo("Not Found", "Pokémon not found. Please be sure you have spelled the name correctly.")
            return

        node = pokemon_data[name]

        #If the node is a list, we have a single (base) form.
        if isinstance(node, list):
            self.display_results(name, node)
        elif isinstance(node, dict):
            #Flatten all forms/subforms into one OrderedDict.
            self.flattened_forms = flatten_forms(node)
            if not self.flattened_forms:
                messagebox.showerror("Data Error", "No valid forms found.")
                return
            #Create a single dropdown listing all forms in the order from the JSON
            ttk.Label(self.dropdown_frame, text="Select a form:").pack(anchor='w', padx=5)
            options = list(self.flattened_forms.keys())
            self.variant_var.set(options[0])
            dropdown = ttk.OptionMenu(self.dropdown_frame, self.variant_var, options[0], *options, command=self.dropdown_callback)
            dropdown.pack(anchor='w', padx=5)
            #Display results for the default option
            self.display_results(f"{name} - {options[0]}", self.flattened_forms[options[0]])
        else:
            messagebox.showerror("Data Error", "Unexpected data format.")

    def dropdown_callback(self, selection):
        #Show alternate form after selection in the dropdown
        name = self.pokemon_var.get().strip().title()
        if selection in self.flattened_forms:
            self.display_results(f"{name} - {selection}", self.flattened_forms[selection])
        else:
            messagebox.showerror("Selection Error", "Selected form not found in data.")

    def display_results(self, display_name, types):
        """
        Calculate type effectiveness and display the result.
        display_name is the combined name to show.
        types is a list of types for that form.
        """
        output = f"Selected Pokémon: {display_name}\n"
        output += f"Type(s): {', '.join(types)}\n\n"

        normally = {}
        weaknesses = {}
        resistances = {}
        immunities = {}
        for move_type in type_effectiveness.keys():
            multiplier = 1.0
            for pokemon_type in types:
                multiplier *= type_effectiveness[pokemon_type][move_type]
            if multiplier == 1.0:
                normally[move_type] = multiplier
            elif multiplier > 1.0:
                weaknesses[move_type] = multiplier
            elif 0 < multiplier < 1.0:
                resistances[move_type] = multiplier
            elif multiplier == 0:
                immunities[move_type] = multiplier

        output += "Damaged normally by:\n"
        if normally:
            for t, mult in normally.items():
                output += f"{t}: {mult}x\n"
        else:
            output += "None\n"

        output += "\nWeaknesses:\n"
        if weaknesses:
            for t, mult in weaknesses.items():
                output += f"{t}: {mult}x\n"
        else:
            output += "None\n"

        output += "\nResistances:\n"
        if resistances:
            for t, mult in resistances.items():
                output += f"{t}: {mult}x\n"
        else:
            output += "None\n"

        output += "\nImmunities:\n"
        if immunities:
            for t in immunities.keys():
                output += f"{t}\n"
        else:
            output += "None\n"

        self.result_text.config(state='normal')
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, output)
        self.result_text.config(state='disabled')

if __name__ == "__main__":
    app = PokeApp()
    app.mainloop()