from time import sleep
#Define base form Pokémon types
base_types = {
    "Charizard": ["Fire", "Flying"],
    "Exeggutor": ["Grass", "Psychic"],
    "Dratini": ["Dragon"],
    "Kyogre": ["Water"],
    "Tauros": ["Normal"]
    
}

#Define alternate forms and their types
mega_evolutions = {
    "Mega Charizard X": ["Fire", "Dragon"],
    "Mega Charizard Y": ["Fire", "Flying"]
}

primal_reversion = {
  "Primal Kyogre": ["Water"],
  "Primal Groudon": ["Ground", "Fire"]
}

regional_variants = {
    "Alolan Exeggutor": ["Grass", "Dragon"],
    "Paldean Tauros": {
        "Combat Breed": ["Fighting"],
        "Blaze Breed": ["Fighting", "Fire"],
        "Aqua Breed": ["Fighting", "Water"]
        }
}

alternate_forms = {
    "Urshifu": {
        "Single Strike": ["Fighting", "Dark"],
        "Rapid Strike": ["Fighting", "Water"]
        },
    "Castform": {
        "Normal Form": ["Normal"],
        "Sunny Form": ["Fire"],
        "Rainy Form": ["Water"],
        "Snowy Form": ["Ice"]
        },
    "Wormadam": {
        "Plant Cloak": ["Bug", "Grass"],
        "Sandy Cloak": ["Bug", "Ground"],
        "Trash Cloak": ["Bug", "Steel"]
        },
    "Rotom": {
        "Rotom": ["Electric", "Ghost"],
        "Heat Rotom": ["Electric", "Fire"],
        "Wash Rotom": ["Electric", "Water"],
        "Frost Rotom": ["Electric", "Ice"],
        "Fan Rotom": ["Electric", "Flying"],
        "Mow Rotom": ["Electric", "Flying"]
        },
    "Shaymin": {
        "Land Forme": ["Grass"],
        "Sky Forme": ["Grass", "Flying"]
        },
    "Darmanitan": {
            "Standard Mode": ["Fire"],
            "Zen Mode": ["Fire", "Psychic"],
            "Galarian Standard Mode": ["Ice"],
            "Galarian Zen Mode": ["Ice", "Fire"]
            }
    }
#Merge all forms into a single dictionary
all_forms = {**base_types, **mega_evolutions, **primal_reversion}

for pokemon, variants in regional_variants.items():
    if isinstance(variants, dict):
        all_forms.update({f"{pokemon} ({variant})": types for variant, types in variants.items()})
    else:
        all_forms[pokemon] = variants
for pokemon, variants in alternate_forms.items():
    if isinstance(variants, dict):
        all_forms.update({f"{pokemon} ({variant})": types for variant, types in variants.items()})
    else:
        all_forms[pokemon] = variants
#Type effectiveness multipliers
type_effectiveness = {
    "Normal": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1, "Fighting": 2, "Poison": 1, "Ground": 1, "Flying": 1, "Psychic": 1, "Bug": 1, "Rock": 1, "Ghost": 0, "Dragon": 1, "Dark": 1, "Steel": 1, "Fairy": 1},
    "Fire": {"Normal": 1, "Fire": 0.5, "Water": 2, "Electric": 1, "Grass": 0.5, "Ice": 0.5, "Fighting": 1, "Poison": 1, "Ground": 2, "Flying": 1, "Psychic": 1, "Bug": 0.5, "Rock": 2, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 0.5, "Fairy": 0.5},
    "Water": {"Normal": 1, "Fire": 0.5, "Water": 0.5, "Electric": 2, "Grass": 2, "Ice": 0.5, "Fighting": 1, "Poison": 1, "Ground": 1, "Flying": 1, "Psychic": 1, "Bug": 1, "Rock": 1, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 0.5, "Fairy": 1},
    "Electric": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 0.5, "Grass": 1, "Ice": 1, "Fighting": 1, "Poison": 1, "Ground": 2, "Flying": 0.5, "Psychic": 1, "Bug": 1, "Rock": 1, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 0.5, "Fairy": 1},
    "Grass": {"Normal": 1, "Fire": 2, "Water": 0.5, "Electric": 0.5, "Grass": 0.5, "Ice": 2, "Fighting": 1, "Poison": 2, "Ground": 0.5, "Flying": 2, "Psychic": 1, "Bug": 2, "Rock": 1, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 1, "Fairy": 1},
    "Ice": {"Normal": 1, "Fire": 2, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 0.5, "Fighting": 2, "Poison": 1, "Ground": 1, "Flying": 1, "Psychic": 1, "Bug": 1, "Rock": 2, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 2, "Fairy": 1},
    "Fighting": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1, "Fighting": 1, "Poison": 1, "Ground": 1, "Flying": 2, "Psychic": 2, "Bug": 0.5, "Rock": 0.5, "Ghost": 1, "Dragon": 1, "Dark": 0.5, "Steel": 1, "Fairy": 2},
    "Poison": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 0.5, "Ice": 1, "Fighting": 0.5, "Poison": 0.5, "Ground": 2, "Flying": 1, "Psychic": 2, "Bug": 0.5, "Rock": 1, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 1, "Fairy": 0.5},
    "Ground": {"Normal": 1, "Fire": 1, "Water": 2, "Electric": 0, "Grass": 2, "Ice": 2, "Fighting": 1, "Poison": 0.5, "Ground": 1, "Flying": 1, "Psychic": 1, "Bug": 1, "Rock": 0.5, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 1, "Fairy": 1},
    "Flying": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 2, "Grass": 0.5, "Ice": 2, "Fighting": 0.5, "Poison": 1, "Ground": 0, "Flying": 1, "Psychic": 1, "Bug": 0.5, "Rock": 2, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 1, "Fairy": 1},
    "Psychic": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1, "Fighting": 0.5, "Poison": 1, "Ground": 1, "Flying": 1, "Psychic": 0.5, "Bug": 2, "Rock": 1, "Ghost": 2, "Dragon": 1, "Dark": 2, "Steel": 1, "Fairy": 1},
    "Bug": {"Normal": 1, "Fire": 2, "Water": 1, "Electric": 1, "Grass": 0.5, "Ice": 1, "Fighting": 0.5, "Poison": 1, "Ground": 1, "Flying": 2, "Psychic": 1, "Bug": 1, "Rock": 2, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 1, "Fairy": 1},
    "Rock": {"Normal": 1, "Fire": 0.5, "Water": 2, "Electric": 1, "Grass": 2, "Ice": 1, "Fighting": 2, "Poison": 0.5, "Ground": 2, "Flying": 0.5, "Psychic": 1, "Bug": 1, "Rock": 1, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 2, "Fairy": 1},
    "Ghost": {"Normal": 0, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1, "Fighting": 0, "Poison": 0.5, "Ground": 1, "Flying": 1, "Psychic": 1, "Bug": 0.5, "Rock": 1, "Ghost": 2, "Dragon": 1, "Dark": 2, "Steel": 1, "Fairy": 1},
    "Dragon": {"Normal": 1, "Fire": 0.5, "Water": 0.5, "Electric": 0.5, "Grass": 0.5, "Ice": 2, "Fighting": 1, "Poison": 1, "Ground": 1, "Flying": 1, "Psychic": 1, "Bug": 1, "Rock": 1, "Ghost": 1, "Dragon": 2, "Dark": 1, "Steel": 1, "Fairy": 2},
    "Dark": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1, "Fighting": 2, "Poison": 1, "Ground": 1, "Flying": 1, "Psychic": 0, "Bug": 2, "Rock": 1, "Ghost": 0.5, "Dragon": 1, "Dark": 0.5, "Steel": 1, "Fairy": 2},
    "Steel": {"Normal": 1, "Fire": 2, "Water": 1, "Electric": 1, "Grass": 0.5, "Ice": 0.5, "Fighting": 2, "Poison": 0, "Ground": 2, "Flying": 0.5, "Psychic": 0.5, "Bug": 0.5, "Rock": 0.5, "Ghost": 1, "Dragon": 0.5, "Dark": 1, "Steel": 0.5, "Fairy": 0.5},
    "Fairy": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1, "Fighting": 0.5, "Poison": 2, "Ground": 1, "Flying": 1, "Psychic": 1, "Bug": 0.5, "Rock": 1, "Ghost": 1, "Dragon": 0, "Dark": 0.5, "Steel": 2, "Fairy": 1}
}
while True:
#Get user input
    pokemon = input("Enter your Pokémon: ").title()

#Check for base Pokémon and forms
    forms = []
    if pokemon in base_types:
        forms.append(pokemon)
        if f"Mega {pokemon} X" in mega_evolutions:
            forms.append(f"Mega {pokemon} X")
        if f"Mega {pokemon} Y" in mega_evolutions:
            forms.append(f"Mega {pokemon} Y")
        if f"Mega {pokemon}" in mega_evolutions:
            forms.append(f"Mega {pokemon}")
        if f"Primal {pokemon}" in primal_reversion:
            forms.append(f"Primal {pokemon}")
        if f"Alolan {pokemon}" in regional_variants:
            forms.append(f"Alolan {pokemon}")
        if f"Galarian {pokemon}" in regional_variants:
            forms.append(f"Galarian {pokemon}")
        if f"Hisuian {pokemon}" in regional_variants:
            forms.append(f"Hisuian {pokemon}")
        if f"Paldean {pokemon}" in regional_variants:
            forms.append(f"Paldean {pokemon}")
        if f"{pokemon}" in alternate_forms:
            forms.append(f"{pokemon}")
    elif pokemon in mega_evolutions or pokemon in primal_reversion or pokemon in regional_variants or pokemon in alternate_forms:
        forms.append(pokemon)

#Handle case where Pokémon is not found
    if not forms:
        print("Pokémon not found.")
    else:
    # Prompt the user to select the form if there are multiple
        if len(forms) > 1:
            print(pokemon ,"has multiple forms.")
            for i, form in enumerate(forms):
                print(f"{i + 1}. {form}")
            choice = int(input("Select the form of " + pokemon + " you wanted by entering the number: "))
            selected_pokemon = forms[choice - 1]
        else:
            selected_pokemon = forms[0]
        if selected_pokemon == ("Darmanitan") and isinstance(alternate_forms[selected_pokemon], dict):
            breeds = list(alternate_forms[selected_pokemon].keys())
            print(f"{selected_pokemon} has multiple forms:")
            for i, breed in enumerate(breeds):
                print(f"{i + 1}. {breed}")
            breed_choice = int(input(f"Select the form of {pokemon} you want by entering the number: "))
            selected_pokemon = f"{selected_pokemon} ({breeds[breed_choice - 1]})"
        if selected_pokemon == "Paldean Tauros" and isinstance(regional_variants[selected_pokemon], dict):
            breeds = list(regional_variants[selected_pokemon].keys())
            print(f"{selected_pokemon} has multiple breeds:")
            for i, breed in enumerate(breeds):
                print(f"{i + 1}. {breed}")
            breed_choice = int(input("Select the breed of Paldean Tauros you want by entering the number: "))
            selected_pokemon = f"{selected_pokemon} ({breeds[breed_choice - 1]})"
        if selected_pokemon == "Urshifu" and isinstance(alternate_forms[selected_pokemon], dict):
            breeds = list(alternate_forms[selected_pokemon].keys())
            print(f"{selected_pokemon} has multiple forms:")
            for i, breed in enumerate(breeds):
                print(f"{i + 1}. {breed}")
            breed_choice = int(input(f"Select the form of {pokemon} you want by entering the number: "))
            selected_pokemon = f"{selected_pokemon} ({breeds[breed_choice - 1]})"   

    #Determine the Pokémon's types
        types = all_forms.get(selected_pokemon, [])

    #Determine weaknesses and resistances
        weaknesses = {}
        resistances = {}
        immunities = {}
        for move_type in type_effectiveness.keys():
            multiplier = 1.0
            for pokemon_type in types:
                multiplier *= type_effectiveness[pokemon_type][move_type]
        
            if multiplier > 1.0:
                weaknesses[move_type] = multiplier
            elif 0.1 < multiplier < 1.0:
                resistances[move_type] = multiplier
            elif multiplier == 0:
                immunities[move_type] = multiplier
        print ("")
    #Display results
        if types:
            type_string = f"{types[0]} type"
            if len(types) > 1:
                type_string = f"{types[0]} and {types[1]} type"
            print(f"{selected_pokemon} is a {type_string}.")
            sleep(1.5)
            if weaknesses:
                weak_to = [f"{move} (x{multiplier})" for move, multiplier in weaknesses.items()]
                print(f"{selected_pokemon}" , f"is weak to: {', '.join(weak_to)}")
            else:
                print(f"{selected_pokemon} has no weaknesses.")
            sleep(1.5)
            if resistances:
                resists = [f"{move} (x{multiplier})" for move, multiplier in resistances.items()]
                print(f"{selected_pokemon}" , f"resists: {', '.join(resists)}")
            else:
                print(f"{selected_pokemon} has no resistances.")
            sleep(1.5)
            if immunities:
                immune = [f"{move} (x{multiplier})" for move, multiplier in immunities.items()]
                print(f"{selected_pokemon}" , f"is immune to: {', '.join(immune)}")
            else:
                print(f"{selected_pokemon} has no immunities.")
    sleep(3)
    choice = input("Would you like to do another Pokémon? (y/n): ").lower()
    if choice != 'y':
        break
