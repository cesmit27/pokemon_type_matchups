pokemon_input = """
Totodile (Pokémon)
Croconaw (Pokémon)
Feraligatr (Pokémon)
"""

pokemon_list = pokemon_input.strip().split('\n')


cleaned_pokemon_list = ['"' + pokemon.replace(" (Pokémon)", "") + '"' for pokemon in pokemon_list]

print(", ".join(cleaned_pokemon_list))

#in this case, the output would be: "Totodile", "Croconaw", "Feraligatr"
