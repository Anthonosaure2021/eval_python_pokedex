### Pokédex MORIN Anthonin et GOBBE Aurélien



import requests
from tkinter import Tk, Label, Button, Entry, Text, END

class PokemonApp:
    def __init__(self, master):
        self.master = master
        master.title("Pokémon App")

        self.label = Label(master, text="Nom du Pokémon:")
        self.label.pack()

        self.entry = Entry(master)
        self.entry.pack()

        self.button = Button(master, text="Rechercher", command=self.search_pokemon)
        self.button.pack()

        self.text_display = Text(master, height=10, width=40)
        self.text_display.pack()

    def search_pokemon(self):
        pokemon_name = self.entry.get().lower()
        if pokemon_name:
            pokemon_info = self.get_pokemon_info(pokemon_name)
            if pokemon_info:
                self.display_pokemon_info(pokemon_info)
            else:
                self.text_display.delete(1.0, END)
                self.text_display.insert(END, "Pokémon non trouvé.")

    def get_pokemon_info(self, pokemon_name):
        api_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/"
        response = requests.get(api_url)

        if response.status_code == 200:
            return response.json()
        else:
            return None

    def display_pokemon_info(self, pokemon_info):
        self.text_display.delete(1.0, END)

        name = pokemon_info['name'].capitalize()
        self.text_display.insert(END, f"Nom: {name}\n")

        types = ', '.join([t['type']['name'].capitalize() for t in pokemon_info['types']])
        self.text_display.insert(END, f"Types: {types}\n")

        abilities = ', '.join([a['ability']['name'].capitalize() for a in pokemon_info['abilities']])
        self.text_display.insert(END, f"Capacités: {abilities}\n")

        height = pokemon_info['height'] / 10  # Convert to meters
        weight = pokemon_info['weight'] / 10  # Convert to kilograms
        self.text_display.insert(END, f"Taille: {height} m\n")
        self.text_display.insert(END, f"Poids: {weight} kg\n")

# Créer et démarrer l'application
root = Tk()
app = PokemonApp(root)
root.mainloop()
