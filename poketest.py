from time import sleep
#Base form Pokémon and typing 
base_types = {
  "Bulbasaur": ["Grass", "Poison"],
  "Ivysaur": ["Grass", "Poison"],
  "Venusaur": ["Grass", "Poison"],
  "Charmander": ["Fire"],
  "Charmeleon": ["Fire"],
  "Charizard": ["Fire", "Flying"],
  "Squirtle": ["Water"],
  "Wartortle": ["Water"],
  "Blastoise": ["Water"],
  "Caterpie": ["Bug"],
  "Metapod": ["Bug"],
  "Butterfree": ["Bug", "Flying"],
  "Weedle": ["Bug", "Poison"],
  "Kakuna": ["Bug", "Poison"],
  "Beedrill": ["Bug", "Poison"],
  "Pidgey": ["Normal", "Flying"],
  "Pidgeotto": ["Normal", "Flying"],
  "Pidgeot": ["Normal", "Flying"],
  "Rattata": ["Normal"],
  "Raticate": ["Normal"],
  "Spearow": ["Normal", "Flying"],
  "Fearow": ["Normal", "Flying"],
  "Ekans": ["Poison"],
  "Arbok": ["Poison"],
  "Pikachu": ["Electric"],
  "Raichu": ["Electric"],
  "Sandshrew": ["Ground"],
  "Sandslash": ["Ground"],
  "Nidoran♀": ["Poison"],
  "Nidorina": ["Poison"],
  "Nidoqueen": ["Poison", "Ground"],
  "Nidoran♂": ["Poison"],
  "Nidorino": ["Poison"],
  "Nidoking": ["Poison", "Ground"],
  "Clefairy": ["Fairy"],
  "Clefable": ["Fairy"],
  "Vulpix": ["Fire"],
  "Ninetales": ["Fire"],
  "Jigglypuff": ["Normal", "Fairy"],
  "Wigglytuff": ["Normal", "Fairy"],
  "Zubat": ["Poison", "Flying"],
  "Golbat": ["Poison", "Flying"],
  "Oddish": ["Grass", "Poison"],
  "Gloom": ["Grass", "Poison"],
  "Vileplume": ["Grass", "Poison"],
  "Paras": ["Bug", "Grass"],
  "Parasect": ["Bug", "Grass"],
  "Venonat": ["Bug", "Poison"],
  "Venomoth": ["Bug", "Poison"],
  "Diglett": ["Ground"],
  "Dugtrio": ["Ground"],
  "Meowth": ["Normal"],
  "Persian": ["Normal"],
  "Psyduck": ["Water"],
  "Golduck": ["Water"],
  "Mankey": ["Fighting"],
  "Primeape": ["Fighting"],
  "Growlithe": ["Fire"],
  "Arcanine": ["Fire"],
  "Poliwag": ["Water"],
  "Poliwhirl": ["Water"],
  "Poliwrath": ["Water", "Fighting"],
  "Abra": ["Psychic"],
  "Kadabra": ["Psychic"],
  "Alakazam": ["Psychic"],
  "Machop": ["Fighting"],
  "Machoke": ["Fighting"],
  "Machamp": ["Fighting"],
  "Bellsprout": ["Grass", "Poison"],
  "Weepinbell": ["Grass", "Poison"],
  "Victreebel": ["Grass", "Poison"],
  "Tentacool": ["Water", "Poison"],
  "Tentacruel": ["Water", "Poison"],
  "Geodude": ["Rock", "Ground"],
  "Graveler": ["Rock", "Ground"],
  "Golem": ["Rock", "Ground"],
  "Ponyta": ["Fire"],
  "Rapidash": ["Fire"],
  "Slowpoke": ["Water", "Psychic"],
  "Slowbro": ["Water", "Psychic"],
  "Magnemite": ["Electric", "Steel"],
  "Magneton": ["Electric", "Steel"],
  "Farfetch'd": ["Normal", "Flying"],
  "Doduo": ["Normal", "Flying"],
  "Dodrio": ["Normal", "Flying"],
  "Seel": ["Water"],
  "Dewgong": ["Water", "Ice"],
  "Grimer": ["Poison"],
  "Muk": ["Poison"],
  "Shellder": ["Water"],
  "Cloyster": ["Water", "Ice"],
  "Gastly": ["Ghost", "Poison"],
  "Haunter": ["Ghost", "Poison"],
  "Gengar": ["Ghost", "Poison"],
  "Onix": ["Rock", "Ground"],
  "Drowzee": ["Psychic"],
  "Hypno": ["Psychic"],
  "Krabby": ["Water"],
  "Kingler": ["Water"],
  "Voltorb": ["Electric"],
  "Electrode": ["Electric"],
  "Exeggcute": ["Grass", "Psychic"],
  "Exeggutor": ["Grass", "Psychic"],
  "Cubone": ["Ground"],
  "Marowak": ["Ground"],
  "Hitmonlee": ["Fighting"],
  "Hitmonchan": ["Fighting"],
  "Lickitung": ["Normal"],
  "Koffing": ["Poison"],
  "Weezing": ["Poison"],
  "Rhyhorn": ["Ground", "Rock"],
  "Rhydon": ["Ground", "Rock"],
  "Chansey": ["Normal"],
  "Tangela": ["Grass"],
  "Kangaskhan": ["Normal"],
  "Horsea": ["Water"],
  "Seadra": ["Water"],
  "Goldeen": ["Water"],
  "Seaking": ["Water"],
  "Staryu": ["Water"],
  "Starmie": ["Water", "Psychic"],
  "Mr. Mime": ["Psychic", "Fairy"],
  "Scyther": ["Bug", "Flying"],
  "Jynx": ["Ice", "Psychic"],
  "Electabuzz": ["Electric"],
  "Magmar": ["Fire"],
  "Pinsir": ["Bug"],
  "Tauros": ["Normal"],
  "Magikarp": ["Water"],
  "Gyarados": ["Water", "Flying"],
  "Lapras": ["Water", "Ice"],
  "Ditto": ["Normal"],
  "Eevee": ["Normal"],
  "Vaporeon": ["Water"],
  "Jolteon": ["Electric"],
  "Flareon": ["Fire"],
  "Porygon": ["Normal"],
  "Omanyte": ["Rock", "Water"],
  "Omastar": ["Rock", "Water"],
  "Kabuto": ["Rock", "Water"],
  "Kabutops": ["Rock", "Water"],
  "Aerodactyl": ["Rock", "Flying"],
  "Snorlax": ["Normal"],
  "Articuno": ["Ice", "Flying"],
  "Zapdos": ["Electric", "Flying"],
  "Moltres": ["Fire", "Flying"],
  "Dratini": ["Dragon"],
  "Dragonair": ["Dragon"],
  "Dragonite": ["Dragon", "Flying"],
  "Mewtwo": ["Psychic"],
  "Mew": ["Psychic"],
  "Chikorita": ["Grass"],
  "Bayleef": ["Grass"],
  "Meganium": ["Grass"],
  "Cyndaquil": ["Fire"],
  "Quilava": ["Fire"],
  "Typhlosion": ["Fire"],
  "Totodile": ["Water"],
  "Croconaw": ["Water"],
  "Feraligatr": ["Water"],
  "Sentret": ["Normal"],
  "Furret": ["Normal"],
  "Hoothoot": ["Normal", "Flying"],
  "Noctowl": ["Normal", "Flying"],
  "Ledyba": ["Bug", "Flying"],
  "Ledian": ["Bug", "Flying"],
  "Spinarak": ["Bug", "Poison"],
  "Ariados": ["Bug", "Poison"],
  "Crobat": ["Poison", "Flying"],
  "Chinchou": ["Water", "Electric"],
  "Lanturn": ["Water", "Electric"],
  "Pichu": ["Electric"],
  "Cleffa": ["Fairy"],
  "Igglybuff": ["Normal", "Fairy"],
  "Togepi": ["Fairy"],
  "Togetic": ["Fairy", "Flying"],
  "Natu": ["Psychic", "Flying"],
  "Xatu": ["Psychic", "Flying"],
  "Mareep": ["Electric"],
  "Flaaffy": ["Electric"],
  "Ampharos": ["Electric"],
  "Bellossom": ["Grass"],
  "Marill": ["Water", "Fairy"],
  "Azumarill": ["Water", "Fairy"],
  "Sudowoodo": ["Rock"],
  "Politoed": ["Water"],
  "Hoppip": ["Grass", "Flying"],
  "Skiploom": ["Grass", "Flying"],
  "Jumpluff": ["Grass", "Flying"],
  "Aipom": ["Normal"],
  "Sunkern": ["Grass"],
  "Sunflora": ["Grass"],
  "Yanma": ["Bug", "Flying"],
  "Wooper": ["Water", "Ground"],
  "Quagsire": ["Water", "Ground"],
  "Espeon": ["Psychic"],
  "Umbreon": ["Dark"],
  "Murkrow": ["Dark", "Flying"],
  "Slowking": ["Water", "Psychic"],
  "Misdreavus": ["Ghost"],
  "Unown": ["Psychic"],
  "Wobbuffet": ["Psychic"],
  "Girafarig": ["Normal", "Psychic"],
  "Pineco": ["Bug"],
  "Forretress": ["Bug", "Steel"],
  "Dunsparce": ["Normal"],
  "Gligar": ["Ground", "Flying"],
  "Steelix": ["Steel", "Ground"],
  "Snubbull": ["Fairy"],
  "Granbull": ["Fairy"],
  "Qwilfish": ["Water", "Poison"],
  "Scizor": ["Bug", "Steel"],
  "Shuckle": ["Bug", "Rock"],
  "Heracross": ["Bug", "Fighting"],
  "Sneasel": ["Dark", "Ice"],
  "Teddiursa": ["Normal"],
  "Ursaring": ["Normal"],
  "Slugma": ["Fire"],
  "Magcargo": ["Fire", "Rock"],
  "Swinub": ["Ice", "Ground"],
  "Piloswine": ["Ice", "Ground"],
  "Corsola": ["Water", "Rock"],
  "Remoraid": ["Water"],
  "Octillery": ["Water"],
  "Delibird": ["Ice", "Flying"],
  "Mantine": ["Water", "Flying"],
  "Skarmory": ["Steel", "Flying"],
  "Houndour": ["Dark", "Fire"],
  "Houndoom": ["Dark", "Fire"],
  "Kingdra": ["Water", "Dragon"],
  "Phanpy": ["Ground"],
  "Donphan": ["Ground"],
  "Porygon2": ["Normal"],
  "Stantler": ["Normal"],
  "Smeargle": ["Normal"],
  "Tyrogue": ["Fighting"],
  "Hitmontop": ["Fighting"],
  "Smoochum": ["Ice", "Psychic"],
  "Elekid": ["Electric"],
  "Magby": ["Fire"],
  "Miltank": ["Normal"],
  "Blissey": ["Normal"],
  "Raikou": ["Electric"],
  "Entei": ["Fire"],
  "Suicune": ["Water"],
  "Larvitar": ["Rock", "Ground"],
  "Pupitar": ["Rock", "Ground"],
  "Tyranitar": ["Rock", "Dark"],
  "Lugia": ["Psychic", "Flying"],
  "Ho-oh": ["Fire", "Flying"],
  "Celebi": ["Psychic", "Grass"],
  "Treecko": ["Grass"],
  "Grovyle": ["Grass"],
  "Sceptile": ["Grass"],
  "Torchic": ["Fire"],
  "Combusken": ["Fire", "Fighting"],
  "Blaziken": ["Fire", "Fighting"],
  "Mudkip": ["Water"],
  "Marshtomp": ["Water", "Ground"],
  "Swampert": ["Water", "Ground"],
  "Poochyena": ["Dark"],
  "Mightyena": ["Dark"],
  "Zigzagoon": ["Normal"],
  "Linoone": ["Normal"],
  "Wurmple": ["Bug"],
  "Silcoon": ["Bug"],
  "Beautifly": ["Bug", "Flying"],
  "Cascoon": ["Bug"],
  "Dustox": ["Bug", "Poison"],
  "Lotad": ["Water", "Grass"],
  "Lombre": ["Water", "Grass"],
  "Ludicolo": ["Water", "Grass"],
  "Seedot": ["Grass"],
  "Nuzleaf": ["Grass", "Dark"],
  "Shiftry": ["Grass", "Dark"],
  "Taillow": ["Normal", "Flying"],
  "Swellow": ["Normal", "Flying"],
  "Wingull": ["Water", "Flying"],
  "Pelipper": ["Water", "Flying"],
  "Ralts": ["Psychic", "Fairy"],
  "Kirlia": ["Psychic", "Fairy"],
  "Gardevoir": ["Psychic", "Fairy"],
  "Surskit": ["Bug", "Water"],
  "Masquerain": ["Bug", "Flying"],
  "Shroomish": ["Grass"],
  "Breloom": ["Grass", "Fighting"],
  "Slakoth": ["Normal"],
  "Vigoroth": ["Normal"],
  "Slaking": ["Normal"],
  "Nincada": ["Bug", "Ground"],
  "Ninjask": ["Bug", "Flying"],
  "Shedinja": ["Bug", "Ghost"],
  "Whismur": ["Normal"],
  "Loudred": ["Normal"],
  "Exploud": ["Normal"],
  "Makuhita": ["Fighting"],
  "Hariyama": ["Fighting"],
  "Azurill": ["Normal", "Fairy"],
  "Nosepass": ["Rock"],
  "Skitty": ["Normal"],
  "Delcatty": ["Normal"],
  "Sableye": ["Dark", "Ghost"],
  "Mawile": ["Steel", "Fairy"],
  "Aron": ["Steel", "Rock"],
  "Lairon": ["Steel", "Rock"],
  "Aggron": ["Steel", "Rock"],
  "Meditite": ["Fighting", "Psychic"],
  "Medicham": ["Fighting", "Psychic"],
  "Electrike": ["Electric"],
  "Manectric": ["Electric"],
  "Plusle": ["Electric"],
  "Minun": ["Electric"],
  "Volbeat": ["Bug"],
  "Illumise": ["Bug"],
  "Roselia": ["Grass", "Poison"],
  "Gulpin": ["Poison"],
  "Swalot": ["Poison"],
  "Carvanha": ["Water", "Dark"],
  "Sharpedo": ["Water", "Dark"],
  "Wailmer": ["Water"],
  "Wailord": ["Water"],
  "Numel": ["Fire", "Ground"],
  "Camerupt": ["Fire", "Ground"],
  "Torkoal": ["Fire"],
  "Spoink": ["Psychic"],
  "Grumpig": ["Psychic"],
  "Spinda": ["Normal"],
  "Trapinch": ["Ground"],
  "Vibrava": ["Ground", "Dragon"],
  "Flygon": ["Ground", "Dragon"],
  "Cacnea": ["Grass"],
  "Cacturne": ["Grass", "Dark"],
  "Swablu": ["Normal", "Flying"],
  "Altaria": ["Dragon", "Flying"],
  "Zangoose": ["Normal"],
  "Seviper": ["Poison"],
  "Lunatone": ["Rock", "Psychic"],
  "Solrock": ["Rock", "Psychic"],
  "Barboach": ["Water", "Ground"],
  "Whiscash": ["Water", "Ground"],
  "Corphish": ["Water"],
  "Crawdaunt": ["Water", "Dark"],
  "Baltoy": ["Ground", "Psychic"],
  "Claydol": ["Ground", "Psychic"],
  "Lileep": ["Rock", "Grass"],
  "Cradily": ["Rock", "Grass"],
  "Anorith": ["Rock", "Bug"],
  "Armaldo": ["Rock", "Bug"],
  "Feebas": ["Water"],
  "Milotic": ["Water"],
  "Kecleon": ["Normal"],
  "Shuppet": ["Ghost"],
  "Banette": ["Ghost"],
  "Duskull": ["Ghost"],
  "Dusclops": ["Ghost"],
  "Tropius": ["Grass", "Flying"],
  "Chimecho": ["Psychic"],
  "Absol": ["Dark"],
  "Wynaut": ["Psychic"],
  "Snorunt": ["Ice"],
  "Glalie": ["Ice"],
  "Spheal": ["Ice", "Water"],
  "Sealeo": ["Ice", "Water"],
  "Walrein": ["Ice", "Water"],
  "Clamperl": ["Water"],
  "Huntail": ["Water"],
  "Gorebyss": ["Water"],
  "Relicanth": ["Water", "Rock"],
  "Luvdisc": ["Water"],
  "Bagon": ["Dragon"],
  "Shelgon": ["Dragon"],
  "Salamence": ["Dragon", "Flying"],
  "Beldum": ["Steel", "Psychic"],
  "Metang": ["Steel", "Psychic"],
  "Metagross": ["Steel", "Psychic"],
  "Regirock": ["Rock"],
  "Regice": ["Ice"],
  "Registeel": ["Steel"],
  "Latias": ["Dragon", "Psychic"],
  "Latios": ["Dragon", "Psychic"],
  "Kyogre": ["Water"],
  "Groudon": ["Ground"],
  "Rayquaza": ["Dragon", "Flying"],
  "Jirachi": ["Steel", "Psychic"],
  "Deoxys": ["Psychic"],
  "Turtwig": ["Grass"],
  "Grotle": ["Grass"],
  "Torterra": ["Grass", "Ground"],
  "Chimchar": ["Fire"],
  "Monferno": ["Fire", "Fighting"],
  "Infernape": ["Fire", "Fighting"],
  "Piplup": ["Water"],
  "Prinplup": ["Water"],
  "Empoleon": ["Water", "Steel"],
  "Starly": ["Normal", "Flying"],
  "Staravia": ["Normal", "Flying"],
  "Staraptor": ["Normal", "Flying"],
  "Bidoof": ["Normal"],
  "Bibarel": ["Normal", "Water"],
  "Kricketot": ["Bug"],
  "Kricketune": ["Bug"],
  "Shinx": ["Electric"],
  "Luxio": ["Electric"],
  "Luxray": ["Electric"],
  "Budew": ["Grass", "Poison"],
  "Roserade": ["Grass", "Poison"],
  "Cranidos": ["Rock"],
  "Rampardos": ["Rock"],
  "Shieldon": ["Rock", "Steel"],
  "Bastiodon": ["Rock", "Steel"],
  "Burmy": ["Bug"],
  "Mothim": ["Bug", "Flying"],
  "Combee": ["Bug", "Flying"],
  "Vespiquen": ["Bug", "Flying"],
  "Pachirisu": ["Electric"],
  "Buizel": ["Water"],
  "Floatzel": ["Water"],
  "Cherubi": ["Grass"],
  "Cherrim": ["Grass"],
  "Shellos": ["Water"],
  "Gastrodon": ["Water", "Ground"],
  "Ambipom": ["Normal"],
  "Drifloon": ["Ghost", "Flying"],
  "Drifblim": ["Ghost", "Flying"],
  "Buneary": ["Normal"],
  "Lopunny": ["Normal"],
  "Mismagius": ["Ghost"],
  "Honchkrow": ["Dark", "Flying"],
  "Glameow": ["Normal"],
  "Purugly": ["Normal"],
  "Chingling": ["Psychic"],
  "Stunky": ["Poison", "Dark"],
  "Skuntank": ["Poison", "Dark"],
  "Bronzor": ["Steel", "Psychic"],
  "Bronzong": ["Steel", "Psychic"],
  "Bonsly": ["Rock"],
  "Mime Jr.": ["Psychic", "Fairy"],
  "Happiny": ["Normal"],
  "Chatot": ["Normal", "Flying"],
  "Spiritomb": ["Ghost", "Dark"],
  "Gible": ["Dragon", "Ground"],
  "Gabite": ["Dragon", "Ground"],
  "Garchomp": ["Dragon", "Ground"],
  "Munchlax": ["Normal"],
  "Riolu": ["Fighting"],
  "Lucario": ["Fighting", "Steel"],
  "Hippopotas": ["Ground"],
  "Hippowdon": ["Ground"],
  "Skorupi": ["Poison", "Bug"],
  "Drapion": ["Poison", "Dark"],
  "Croagunk": ["Poison", "Fighting"],
  "Toxicroak": ["Poison", "Fighting"],
  "Carnivine": ["Grass"],
  "Finneon": ["Water"],
  "Lumineon": ["Water"],
  "Mantyke": ["Water", "Flying"],
  "Snover": ["Grass", "Ice"],
  "Abomasnow": ["Grass", "Ice"],
  "Weavile": ["Dark", "Ice"],
  "Magnezone": ["Electric", "Steel"],
  "Lickilicky": ["Normal"],
  "Rhyperior": ["Ground", "Rock"],
  "Tangrowth": ["Grass"],
  "Electivire": ["Electric"],
  "Magmortar": ["Fire"],
  "Togekiss": ["Fairy", "Flying"],
  "Yanmega": ["Bug", "Flying"],
  "Leafeon": ["Grass"],
  "Glaceon": ["Ice"],
  "Gliscor": ["Ground", "Flying"],
  "Mamoswine": ["Ice", "Ground"],
  "Porygon-Z": ["Normal"],
  "Gallade": ["Psychic", "Fighting"],
  "Probopass": ["Rock", "Steel"],
  "Dusknoir": ["Ghost"],
  "Froslass": ["Ice", "Ghost"],
  "Uxie": ["Psychic"],
  "Mesprit": ["Psychic"],
  "Azelf": ["Psychic"],
  "Dialga": ["Steel", "Dragon"],
  "Palkia": ["Water", "Dragon"],
  "Heatran": ["Fire", "Steel"],
  "Regigigas": ["Normal"],
  "Giratina": ["Ghost", "Dragon"],
  "Cresselia": ["Psychic"],
  "Phione": ["Water"],
  "Manaphy": ["Water"],
  "Darkrai": ["Dark"],
  "Victini": ["Psychic", "Fire"],
  "Snivy": ["Grass"],
  "Servine": ["Grass"],
  "Serperior": ["Grass"],
  "Tepig": ["Fire"],
  "Pignite": ["Fire", "Fighting"],
  "Emboar": ["Fire", "Fighting"],
  "Oshawott": ["Water"],
  "Dewott": ["Water"],
  "Samurott": ["Water"],
  "Patrat": ["Normal"],
  "Watchog": ["Normal"],
  "Lillipup": ["Normal"],
  "Herdier": ["Normal"],
  "Stoutland": ["Normal"],
  "Purrloin": ["Dark"],
  "Liepard": ["Dark"],
  "Pansage": ["Grass"],
  "Simisage": ["Grass"],
  "Pansear": ["Fire"],
  "Simisear": ["Fire"],
  "Panpour": ["Water"],
  "Simipour": ["Water"],
  "Munna": ["Psychic"],
  "Musharna": ["Psychic"],
  "Pidove": ["Normal", "Flying"],
  "Tranquill": ["Normal", "Flying"],
  "Unfezant": ["Normal", "Flying"],
  "Blitzle": ["Electric"],
  "Zebstrika": ["Electric"],
  "Roggenrola": ["Rock"],
  "Boldore": ["Rock"],
  "Gigalith": ["Rock"],
  "Woobat": ["Psychic", "Flying"],
  "Swoobat": ["Psychic", "Flying"],
  "Drilbur": ["Ground"],
  "Excadrill": ["Ground", "Steel"],
  "Audino": ["Normal"],
  "Timburr": ["Fighting"],
  "Gurdurr": ["Fighting"],
  "Conkeldurr": ["Fighting"],
  "Tympole": ["Water"],
  "Palpitoad": ["Water", "Ground"],
  "Seismitoad": ["Water", "Ground"],
  "Throh": ["Fighting"],
  "Sawk": ["Fighting"],
  "Sewaddle": ["Bug", "Grass"],
  "Swadloon": ["Bug", "Grass"],
  "Leavanny": ["Bug", "Grass"],
  "Venipede": ["Bug", "Poison"],
  "Whirlipede": ["Bug", "Poison"],
  "Scolipede": ["Bug", "Poison"],
  "Cottonee": ["Grass", "Fairy"],
  "Whimsicott": ["Grass", "Fairy"],
  "Petilil": ["Grass"],
  "Lilligant": ["Grass"],
  "Basculin": ["Water"],
  "Sandile": ["Ground", "Dark"],
  "Krokorok": ["Ground", "Dark"],
  "Krookodile": ["Ground", "Dark"],
  "Darumaka": ["Fire"],
  "Darmanitan": {
      "Standard Mode": ["Fire"],
      "Zen Mode": ["Fire", "Psychic"]
      },
  "Maractus": ["Grass"],
  "Dwebble": ["Bug", "Rock"],
  "Crustle": ["Bug", "Rock"],
  "Scraggy": ["Dark", "Fighting"],
  "Scrafty": ["Dark", "Fighting"],
  "Sigilyph": ["Psychic", "Flying"],
  "Yamask": ["Ghost"],
  "Cofagrigus": ["Ghost"],
  "Tirtouga": ["Water", "Rock"],
  "Carracosta": ["Water", "Rock"],
  "Archen": ["Rock", "Flying"],
  "Archeops": ["Rock", "Flying"],
  "Trubbish": ["Poison"],
  "Garbodor": ["Poison"],
  "Zorua": ["Dark"],
  "Zoroark": ["Dark"],
  "Minccino": ["Normal"],
  "Cinccino": ["Normal"],
  "Gothita": ["Psychic"],
  "Gothorita": ["Psychic"],
  "Gothitelle": ["Psychic"],
  "Solosis": ["Psychic"],
  "Duosion": ["Psychic"],
  "Reuniclus": ["Psychic"],
  "Ducklett": ["Water", "Flying"],
  "Swanna": ["Water", "Flying"],
  "Vanillite": ["Ice"],
  "Vanillish": ["Ice"],
  "Vanilluxe": ["Ice"],
  "Deerling": ["Normal", "Grass"],
  "Sawsbuck": ["Normal", "Grass"],
  "Emolga": ["Electric", "Flying"],
  "Karrablast": ["Bug"],
  "Escavalier": ["Bug", "Steel"],
  "Foongus": ["Grass", "Poison"],
  "Amoonguss": ["Grass", "Poison"],
  "Frillish": ["Water", "Ghost"],
  "Jellicent": ["Water", "Ghost"],
  "Alomomola": ["Water"],
  "Joltik": ["Bug", "Electric"],
  "Galvantula": ["Bug", "Electric"],
  "Ferroseed": ["Grass", "Steel"],
  "Ferrothorn": ["Grass", "Steel"],
  "Klink": ["Steel"],
  "Klang": ["Steel"],
  "Klinklang": ["Steel"],
  "Tynamo": ["Electric"],
  "Eelektrik": ["Electric"],
  "Eelektross": ["Electric"],
  "Elgyem": ["Psychic"],
  "Beheeyem": ["Psychic"],
  "Litwick": ["Ghost", "Fire"],
  "Lampent": ["Ghost", "Fire"],
  "Chandelure": ["Ghost", "Fire"],
  "Axew": ["Dragon"],
  "Fraxure": ["Dragon"],
  "Haxorus": ["Dragon"],
  "Cubchoo": ["Ice"],
  "Beartic": ["Ice"],
  "Cryogonal": ["Ice"],
  "Shelmet": ["Bug"],
  "Accelgor": ["Bug"],
  "Stunfisk": ["Ground", "Electric"],
  "Mienfoo": ["Fighting"],
  "Mienshao": ["Fighting"],
  "Druddigon": ["Dragon"],
  "Golett": ["Ground", "Ghost"],
  "Golurk": ["Ground", "Ghost"],
  "Pawniard": ["Dark", "Steel"],
  "Bisharp": ["Dark", "Steel"],
  "Bouffalant": ["Normal"],
  "Rufflet": ["Normal", "Flying"],
  "Braviary": ["Normal", "Flying"],
  "Vullaby": ["Dark", "Flying"],
  "Mandibuzz": ["Dark", "Flying"],
  "Heatmor": ["Fire"],
  "Durant": ["Bug", "Steel"],
  "Deino": ["Dark", "Dragon"],
  "Zweilous": ["Dark", "Dragon"],
  "Hydreigon": ["Dark", "Dragon"],
  "Larvesta": ["Bug", "Fire"],
  "Volcarona": ["Bug", "Fire"],
  "Cobalion": ["Steel", "Fighting"],
  "Terrakion": ["Rock", "Fighting"],
  "Virizion": ["Grass", "Fighting"],
  "Tornadus": ["Flying"],
  "Thundurus": ["Electric", "Flying"],
  "Reshiram": ["Dragon", "Fire"],
  "Zekrom": ["Dragon", "Electric"],
  "Landorus": ["Ground", "Flying"],
  "Kyurem": ["Dragon", "Ice"],
  "Keldeo": ["Water", "Fighting"],
  "Genesect": ["Bug", "Steel"],
  "Chespin": ["Grass"],
  "Quilladin": ["Grass"],
  "Chesnaught": ["Grass", "Fighting"],
  "Fennekin": ["Fire"],
  "Braixen": ["Fire"],
  "Delphox": ["Fire", "Psychic"],
  "Froakie": ["Water"],
  "Frogadier": ["Water"],
  "Greninja": ["Water", "Dark"],
  "Bunnelby": ["Normal"],
  "Diggersby": ["Normal", "Ground"],
  "Fletchling": ["Normal", "Flying"],
  "Fletchinder": ["Fire", "Flying"],
  "Talonflame": ["Fire", "Flying"],
  "Scatterbug": ["Bug"],
  "Spewpa": ["Bug"],
  "Vivillon": ["Bug", "Flying"],
  "Litleo": ["Fire", "Normal"],
  "Pyroar": ["Fire", "Normal"],
  "Flabébé": ["Fairy"],
  "Floette": ["Fairy"],
  "Florges": ["Fairy"],
  "Skiddo": ["Grass"],
  "Gogoat": ["Grass"],
  "Pancham": ["Fighting"],
  "Pangoro": ["Fighting", "Dark"],
  "Furfrou": ["Normal"],
  "Espurr": ["Psychic"],
  "Meowstic": ["Psychic"],
  "Honedge": ["Steel", "Ghost"],
  "Doublade": ["Steel", "Ghost"],
  "Aegislash": ["Steel", "Ghost"],
  "Spritzee": ["Fairy"],
  "Aromatisse": ["Fairy"],
  "Swirlix": ["Fairy"],
  "Slurpuff": ["Fairy"],
  "Inkay": ["Dark", "Psychic"],
  "Malamar": ["Dark", "Psychic"],
  "Binacle": ["Rock", "Water"],
  "Barbaracle": ["Rock", "Water"],
  "Skrelp": ["Poison", "Water"],
  "Dragalge": ["Poison", "Dragon"],
  "Clauncher": ["Water"],
  "Clawitzer": ["Water"],
  "Helioptile": ["Electric", "Normal"],
  "Heliolisk": ["Electric", "Normal"],
  "Tyrunt": ["Rock", "Dragon"],
  "Tyrantrum": ["Rock", "Dragon"],
  "Amaura": ["Rock", "Ice"],
  "Aurorus": ["Rock", "Ice"],
  "Sylveon": ["Fairy"],
  "Hawlucha": ["Fighting", "Flying"],
  "Dedenne": ["Electric", "Fairy"],
  "Carbink": ["Rock", "Fairy"],
  "Goomy": ["Dragon"],
  "Sliggoo": ["Dragon"],
  "Goodra": ["Dragon"],
  "Klefki": ["Steel", "Fairy"],
  "Phantump": ["Ghost", "Grass"],
  "Trevenant": ["Ghost", "Grass"],
  "Pumpkaboo": ["Ghost", "Grass"],
  "Gourgeist": ["Ghost", "Grass"],
  "Bergmite": ["Ice"],
  "Avalugg": ["Ice"],
  "Noibat": ["Flying", "Dragon"],
  "Noivern": ["Flying", "Dragon"],
  "Xerneas": ["Fairy"],
  "Yveltal": ["Dark", "Flying"],
  "Zygarde": ["Dragon", "Ground"],
  "Diancie": ["Rock", "Fairy"],
  "Volcanion": ["Fire", "Water"],
  "Rowlet": ["Grass", "Flying"],
  "Dartrix": ["Grass", "Flying"],
  "Decidueye": ["Grass", "Ghost"],
  "Litten": ["Fire"],
  "Torracat": ["Fire"],
  "Incineroar": ["Fire", "Dark"],
  "Popplio": ["Water"],
  "Brionne": ["Water"],
  "Primarina": ["Water", "Fairy"],
  "Pikipek": ["Normal", "Flying"],
  "Trumbeak": ["Normal", "Flying"],
  "Toucannon": ["Normal", "Flying"],
  "Yungoos": ["Normal"],
  "Gumshoos": ["Normal"],
  "Grubbin": ["Bug"],
  "Charjabug": ["Bug", "Electric"],
  "Vikavolt": ["Bug", "Electric"],
  "Crabrawler": ["Fighting"],
  "Crabominable": ["Fighting", "Ice"],
  "Cutiefly": ["Bug", "Fairy"],
  "Ribombee": ["Bug", "Fairy"],
  "Rockruff": ["Rock"],
  "Lycanroc": ["Rock"],
  "Wishiwashi": ["Water"],
  "Mareanie": ["Poison", "Water"],
  "Toxapex": ["Poison", "Water"],
  "Mudbray": ["Ground"],
  "Mudsdale": ["Ground"],
  "Dewpider": ["Water", "Bug"],
  "Araquanid": ["Water", "Bug"],
  "Fomantis": ["Grass"],
  "Lurantis": ["Grass"],
  "Morelull": ["Grass", "Fairy"],
  "Shiinotic": ["Grass", "Fairy"],
  "Salandit": ["Poison", "Fire"],
  "Salazzle": ["Poison", "Fire"],
  "Stufful": ["Normal", "Fighting"],
  "Bewear": ["Normal", "Fighting"],
  "Bounsweet": ["Grass"],
  "Steenee": ["Grass"],
  "Tsareena": ["Grass"],
  "Comfey": ["Fairy"],
  "Oranguru": ["Normal", "Psychic"],
  "Passimian": ["Fighting"],
  "Wimpod": ["Bug", "Water"],
  "Golisopod": ["Bug", "Water"],
  "Sandygast": ["Ghost", "Ground"],
  "Palossand": ["Ghost", "Ground"],
  "Pyukumuku": ["Water"],
  "Type: Null": ["Normal"],
  "Minior": ["Rock", "Flying"],
  "Komala": ["Normal"],
  "Turtonator": ["Fire", "Dragon"],
  "Togedemaru": ["Electric", "Steel"],
  "Mimikyu": ["Ghost", "Fairy"],
  "Bruxish": ["Water", "Psychic"],
  "Drampa": ["Normal", "Dragon"],
  "Dhelmise": ["Ghost", "Grass"],
  "Jangmo-o": ["Dragon"],
  "Hakamo-o": ["Dragon", "Fighting"],
  "Kommo-o": ["Dragon", "Fighting"],
  "Tapu Koko": ["Electric", "Fairy"],
  "Tapu Lele": ["Psychic", "Fairy"],
  "Tapu Bulu": ["Grass", "Fairy"],
  "Tapu Fini": ["Water", "Fairy"],
  "Cosmog": ["Psychic"],
  "Cosmoem": ["Psychic"],
  "Solgaleo": ["Psychic", "Steel"],
  "Lunala": ["Psychic", "Ghost"],
  "Nihilego": ["Rock", "Poison"],
  "Buzzwole": ["Bug", "Fighting"],
  "Pheromosa": ["Bug", "Fighting"],
  "Xurkitree": ["Electric"],
  "Celesteela": ["Steel", "Flying"],
  "Kartana": ["Grass", "Steel"],
  "Guzzlord": ["Dark", "Dragon"],
  "Magearna": ["Steel", "Fairy"],
  "Marshadow": ["Fighting", "Ghost"],
  "Poipole": ["Poison"],
  "Naganadel": ["Poison", "Dragon"],
  "Stakataka": ["Rock", "Steel"],
  "Blacephalon": ["Fire", "Ghost"],
  "Zeraora": ["Electric"],
  "Meltan": ["Steel"],
  "Melmetal": ["Steel"],
  "Grookey": ["Grass"],
  "Thwackey": ["Grass"],
  "Rillaboom": ["Grass"],
  "Scorbunny": ["Fire"],
  "Raboot": ["Fire"],
  "Cinderace": ["Fire"],
  "Sobble": ["Water"],
  "Drizzile": ["Water"],
  "Inteleon": ["Water"],
  "Skwovet": ["Normal"],
  "Greedent": ["Normal"],
  "Rookidee": ["Flying"],
  "Corvisquire": ["Flying"],
  "Corviknight": ["Flying", "Steel"],
  "Blipbug": ["Bug"],
  "Dottler": ["Bug", "Psychic"],
  "Orbeetle": ["Bug", "Psychic"],
  "Nickit": ["Dark"],
  "Thievul": ["Dark"],
  "Gossifleur": ["Grass"],
  "Eldegoss": ["Grass"],
  "Wooloo": ["Normal"],
  "Dubwool": ["Normal"],
  "Chewtle": ["Water"],
  "Drednaw": ["Water", "Rock"],
  "Yamper": ["Electric"],
  "Boltund": ["Electric"],
  "Rolycoly": ["Rock"],
  "Carkol": ["Rock"],
  "Coalossal": ["Rock", "Fire"],
  "Applin": ["Grass", "Dragon"],
  "Flapple": ["Grass", "Dragon"],
  "Appletun": ["Grass", "Dragon"],
  "Silicobra": ["Ground"],
  "Sandaconda": ["Ground"],
  "Cramorant": ["Flying", "Water"],
  "Arrokuda": ["Water"],
  "Barraskewda": ["Water"],
  "Toxel": ["Electric", "Poison"],
  "Toxtricity": ["Electric", "Poison"],
  "Sizzlipede": ["Fire", "Bug"],
  "Centiskorch": ["Fire", "Bug"],
  "Clobbopus": ["Fighting"],
  "Grapploct": ["Fighting"],
  "Sinistea": ["Ghost"],
  "Polteageist": ["Ghost"],
  "Hatenna": ["Psychic"],
  "Hattrem": ["Psychic"],
  "Hatterene": ["Psychic", "Fairy"],
  "Impidimp": ["Dark", "Fairy"],
  "Morgrem": ["Dark", "Fairy"],
  "Grimmsnarl": ["Dark", "Fairy"],
  "Obstagoon": ["Dark", "Normal"],
  "Perrserker": ["Steel"],
  "Cursola": ["Ghost"],
  "Sirfetch'd": ["Fighting"],
  "Mr. Rime": ["Ice", "Psychic"],
  "Runerigus": ["Ground", "Ghost"],
  "Milcery": ["Fairy"],
  "Alcremie": ["Fairy"],
  "Falinks": ["Fighting"],
  "Pincurchin": ["Electric"],
  "Snom": ["Ice", "Bug"],
  "Frosmoth": ["Ice", "Bug"],
  "Stonjourner": ["Rock"],
  "Eiscue": ["Ice"],
  "Indeedee": ["Psychic", "Normal"],
  "Morpeko": ["Electric", "Dark"],
  "Cufant": ["Steel"],
  "Copperajah": ["Steel"],
  "Dracozolt": ["Electric", "Dragon"],
  "Arctozolt": ["Electric", "Ice"],
  "Dracovish": ["Water", "Dragon"],
  "Arctovish": ["Water", "Ice"],
  "Duraludon": ["Steel", "Dragon"],
  "Dreepy": ["Dragon", "Ghost"],
  "Drakloak": ["Dragon", "Ghost"],
  "Dragapult": ["Dragon", "Ghost"],
  "Eternatus": ["Poison", "Dragon"],
  "Kubfu": ["Fighting"],
  "Zarude": ["Dark", "Grass"],
  "Regieleki": ["Electric"],
  "Regidrago": ["Dragon"],
  "Glastrier": ["Ice"],
  "Spectrier": ["Ghost"],
  "Wyrdeer": ["Normal", "Psychic"],
  "Kleavor": ["Bug", "Rock"],
  "Ursaluna": ["Ground", "Normal"],
  "Basculegion": ["Water", "Ghost"],
  "Sneasler": ["Poison", "Fighting"],
  "Overqwil": ["Dark", "Poison"],
  "Enamorus": ["Fairy", "Flying"],
  "Sprigatito": ["Grass"],
  "Floragato": ["Grass"],
  "Meowscarada": ["Grass", "Dark"],
  "Fuecoco": ["Fire"],
  "Crocalor": ["Fire"],
  "Skeledirge": ["Fire", "Ghost"],
  "Quaxly": ["Water"],
  "Quaxwell": ["Water"],
  "Quaquaval": ["Water", "Fighting"],
  "Lechonk": ["Normal"],
  "Oinkologne": ["Normal"],
  "Tarountula": ["Bug"],
  "Spidops": ["Bug"],
  "Nymble": ["Bug"],
  "Lokix": ["Bug", "Dark"],
  "Pawmi": ["Electric"],
  "Pawmo": ["Electric", "Fighting"],
  "Pawmot": ["Electric", "Fighting"],
  "Tandemaus": ["Normal"],
  "Maushold": ["Normal"],
  "Fidough": ["Fairy"],
  "Dachsbun": ["Fairy"],
  "Smoliv": ["Grass", "Normal"],
  "Dolliv": ["Grass", "Normal"],
  "Arboliva": ["Grass", "Normal"],
  "Squawkabilly": ["Normal", "Flying"],
  "Nacli": ["Rock"],
  "Naclstack": ["Rock"],
  "Garganacl": ["Rock"],
  "Charcadet": ["Fire"],
  "Armarouge": ["Fire", "Psychic"],
  "Ceruledge": ["Fire", "Ghost"],
  "Tadbulb": ["Electric"],
  "Bellibolt": ["Electric"],
  "Wattrel": ["Electric", "Flying"],
  "Kilowattrel": ["Electric", "Flying"],
  "Maschiff": ["Dark"],
  "Mabosstiff": ["Dark"],
  "Shroodle": ["Poison", "Normal"],
  "Grafaiai": ["Poison", "Normal"],
  "Bramblin": ["Grass", "Ghost"],
  "Brambleghast": ["Grass", "Ghost"],
  "Toedscool": ["Ground", "Grass"],
  "Toedscruel": ["Ground", "Grass"],
  "Klawf": ["Rock"],
  "Capsakid": ["Grass"],
  "Scovillain": ["Grass", "Fire"],
  "Rellor": ["Bug"],
  "Rabsca": ["Bug", "Psychic"],
  "Flittle": ["Psychic"],
  "Espathra": ["Psychic"],
  "Tinkatink": ["Fairy", "Steel"],
  "Tinkatuff": ["Fairy", "Steel"],
  "Tinkaton": ["Fairy", "Steel"],
  "Wiglett": ["Water"],
  "Wugtrio": ["Water"],
  "Bombirdier": ["Flying", "Dark"],
  "Finizen": ["Water"],
  "Palafin": ["Water"],
  "Varoom": ["Steel", "Poison"],
  "Revavroom": ["Steel", "Poison"],
  "Cyclizar": ["Dragon", "Normal"],
  "Orthworm": ["Steel"],
  "Glimmet": ["Rock", "Poison"],
  "Glimmora": ["Rock", "Poison"],
  "Greavard": ["Ghost"],
  "Houndstone": ["Ghost"],
  "Flamigo": ["Flying", "Fighting"],
  "Cetoddle": ["Ice"],
  "Cetitan": ["Ice"],
  "Veluza": ["Water", "Psychic"],
  "Dondozo": ["Water"],
  "Tatsugiri": ["Dragon", "Water"],
  "Annihilape": ["Fighting", "Ghost"],
  "Clodsire": ["Poison", "Ground"],
  "Farigiraf": ["Normal", "Psychic"],
  "Dudunsparce": ["Normal"],
  "Kingambit": ["Dark", "Steel"],
  "Great Tusk": ["Ground", "Fighting"],
  "Scream Tail": ["Fairy", "Psychic"],
  "Brute Bonnet": ["Grass", "Dark"],
  "Flutter Mane": ["Ghost", "Fairy"],
  "Slither Wing": ["Bug", "Fighting"],
  "Sandy Shocks": ["Electric", "Ground"],
  "Iron Treads": ["Ground", "Steel"],
  "Iron Bundle": ["Ice", "Water"],
  "Iron Hands": ["Fighting", "Electric"],
  "Iron Jugulis": ["Dark", "Flying"],
  "Iron Moth": ["Fire", "Poison"],
  "Iron Thorns": ["Rock", "Electric"],
  "Frigibax": ["Dragon", "Ice"],
  "Arctibax": ["Dragon", "Ice"],
  "Baxcalibur": ["Dragon", "Ice"],
  "Gimmighoul": ["Ghost"],
  "Gholdengo": ["Steel", "Ghost"],
  "Wo-Chien": ["Dark", "Grass"],
  "Chien-Pao": ["Dark", "Ice"],
  "Ting-Lu": ["Dark", "Ground"],
  "Chi-Yu": ["Dark", "Fire"],
  "Roaring Moon": ["Dragon", "Dark"],
  "Iron Valiant": ["Fairy", "Fighting"],
  "Koraidon": ["Fighting", "Dragon"],
  "Miraidon": ["Electric", "Dragon"],
  "Walking Wake": ["Water", "Dragon"],
  "Iron Leaves": ["Grass", "Psychic"],
  "Dipplin": ["Grass", "Dragon"],
  "Poltchageist": ["Grass", "Ghost"],
  "Sinistcha": ["Grass", "Ghost"],
  "Okidogi": ["Poison", "Fighting"],
  "Munkidori": ["Poison", "Psychic"],
  "Fezandipiti": ["Poison", "Fairy"],
  "Archaludon": ["Steel", "Dragon"],
  "Hydrapple": ["Grass", "Dragon"],
  "Gouging Fire": ["Fire", "Dragon"],
  "Raging Bolt": ["Electric", "Dragon"],
  "Iron Boulder": ["Rock", "Psychic"],
  "Iron Crown": ["Steel", "Psychic"],
  "Terapagos": ["Normal"],
  "Pecharunt": ["Poison", "Ghost"]
}

#Alternate form Pokémon and typing
mega_evolutions = {
  "Mega Venusaur": ["Grass", "Poison"],
  "Mega Charizard": {
      "X": ["Fire", "Dragon"],
      "Y": ["Fire", "Flying"]
      },
  "Mega Blastoise": ["Water"],
  "Mega Beedrill": ["Bug", "Poison"],
  "Mega Pidgeot": ["Normal", "Flying"],
  "Mega Alakazam": ["Psychic"],
  "Mega Slowbro": ["Water", "Psychic"],
  "Mega Gengar": ["Ghost", "Poison"],
  "Mega Kangaskhan": ["Normal"],
  "Mega Pinsir": ["Bug", "Flying"],
  "Mega Gyarados": ["Water", "Dark"],
  "Mega Aerodactyl": ["Rock", "Flying"],
  "Mega Mewtwo": {
      "X": ["Psychic", "Fighting"],
      "Y": ["Psychic"]
      },
  "Mega Ampharos": ["Electric", "Dragon"],
  "Mega Steelix": ["Steel", "Ground"],
  "Mega Scizor": ["Bug", "Steel"],
  "Mega Heracross": ["Bug", "Fighting"],
  "Mega Houndoom": ["Dark", "Fire"],
  "Mega Tyranitar": ["Rock", "Dark"],
  "Mega Sceptile": ["Grass", "Dragon"],
  "Mega Blaziken": ["Fire", "Fighting"],
  "Mega Swampert": ["Water", "Ground"],
  "Mega Gardevoir": ["Psychic", "Fairy"],
  "Mega Sableye": ["Dark", "Ghost"],
  "Mega Mawile": ["Steel", "Fairy"],
  "Mega Aggron": ["Steel"],
  "Mega Medicham": ["Fighting", "Psychic"],
  "Mega Manectric": ["Electric"],
  "Mega Sharpedo": ["Water", "Dark"],
  "Mega Camerupt": ["Fire", "Ground"],
  "Mega Altaria": ["Dragon", "Fairy"],
  "Mega Banette": ["Ghost"],
  "Mega Absol": ["Dark"],
  "Mega Glalie": ["Ice"],
  "Mega Salamence": ["Dragon", "Flying"],
  "Mega Metagross": ["Steel", "Psychic"],
  "Mega Latias": ["Dragon", "Psychic"],
  "Mega Latios": ["Dragon", "Psychic"],
  "Mega Rayquaza": ["Dragon", "Flying"],
  "Mega Lopunny": ["Normal", "Fighting"],
  "Mega Garchomp": ["Dragon", "Ground"],
  "Mega Lucario": ["Fighting", "Steel"],
  "Mega Abomasnow": ["Grass", "Ice"],
  "Mega Gallade": ["Psychic", "Fighting"],
  "Mega Audino": ["Normal", "Fairy"],
  "Mega Diancie": ["Rock", "Fairy"]
}

primal_reversion = {
  "Primal Kyogre": ["Water"],
  "Primal Groudon": ["Ground", "Fire"]
}

regional_variants = {
  "Alolan Rattata": ["Dark", "Normal"],
  "Alolan Raticate": ["Dark", "Normal"],
  "Alolan Raichu": ["Electric", "Psychic"],
  "Alolan Sandshrew": ["Ice", "Steel"],
  "Alolan Sandslash": ["Ice", "Steel"],
  "Alolan Vulpix": ["Ice"],
  "Alolan Ninetales": ["Ice", "Fairy"],
  "Alolan Diglett": ["Ground", "Steel"],
  "Alolan Dugtrio": ["Ground", "Steel"],
  "Alolan Meowth": ["Dark"],
  "Alolan Persian": ["Dark"],
  "Alolan Geodude": ["Rock", "Electric"],
  "Alolan Graveler": ["Rock", "Electric"],
  "Alolan Golem": ["Rock", "Electric"],
  "Alolan Grimer": ["Poison", "Dark"],
  "Alolan Muk": ["Poison", "Dark"],
  "Alolan Exeggutor": ["Grass", "Dragon"],
  "Alolan Marowak": ["Fire", "Ghost"],
  "Galarian Meowth": ["Steel"],
  "Galarian Ponyta": ["Psychic"],
  "Galarian Rapidash": ["Psychic", "Fairy"],
  "Galarian Slowpoke": ["Psychic"],
  "Galarian Slowbro": ["Poison", "Psychic"],
  "Galarian Farfetch'd": ["Fighting"],
  "Galarian Weezing": ["Poison", "Fairy"],
  "Galarian Mr. Mime": ["Ice", "Psychic"],
  "Galarian Articuno": ["Psychic", "Flying"],
  "Galarian Zapdos": ["Fighting", "Flying"],
  "Galarian Moltres": ["Dark", "Flying"],
  "Galarian Slowking": ["Poison", "Psychic"],
  "Galarian Corsola": ["Ghost"],
  "Galarian Zigzagoon": ["Dark", "Normal"],
  "Galarian Linoone": ["Dark", "Normal"],
  "Galarian Darumaka": ["Ice"],
  "Galarian Darmanitan": {
      "Standard Mode": ["Ice"],
      "Zen Mode": ["Ice", "Fire"]
      },
  "Galarian Yamask": ["Ground", "Ghost"],
  "Galarian Stunfisk": ["Ground", "Steel"],
  "Hisuian Growlithe": ["Fire", "Rock"],
  "Hisuian Arcanine": ["Fire", "Rock"],
  "Hisuian Voltorb": ["Electric", "Grass"],
  "Hisuian Electrode": ["Electric", "Grass"],
  "Hisuian Typhlosion": ["Fire", "Ghost"],
  "Hisuian Qwilfish": ["Water", "Dark"],
  "Hisuian Sneasel": ["Fighting", "Poison"],
  "Hisuian Samurott": ["Water", "Dark"],
  "Hisuian Lilligant": ["Grass", "Fighting"],
  "Hisuian Zorua": ["Normal", "Ghost"],
  "Hisuian Zoroark": ["Normal", "Ghost"],
  "Hisuian Braviary": ["Psychic", "Flying"],
  "Hisuian Sliggoo": ["Steel", "Dragon"],
  "Hisuian Goodra": ["Steel", "Dragon"],
  "Hisuian Avalugg": ["Ice", "Rock"],
  "Hisuian Decidueye": ["Grass", "Fighting"],
  "Paldean Wooper": ["Poison", "Ground"],
  "Paldean Tauros": {
        "Combat Breed": ["Fighting"],
        "Blaze Breed": ["Fighting", "Fire"],
        "Aqua Breed": ["Fighting", "Water"]
        }
  }

alternate_forms = {
    "Magnemite (Before Gen 2)": ["Electric"], 
    "Magneton (Before Gen 2)": ["Electric"],
    "Azumarill (Before Gen 6)": ["Water"],
    "Azurill (Before Gen 6)": ["Normal"], 
    "Clefable (Before Gen 6)": ["Normal"],
    "Clefairy (Before Gen 6)": ["Normal"],
    "Cleffa (Before Gen 6)": ["Normal"], 
    "Cottonee (Before Gen 6)": ["Grass"],
    "Gardevoir (Before Gen 6)": ["Psychic"],
    "Granbull (Before Gen 6)": ["Normal"], 
    "Igglybuff (Before Gen 6)": ["Normal"],
    "Jigglypuff (Before Gen 6)": ["Normal"], 
    "Kirlia (Before Gen 6)": ["Psychic"], 
    "Marill (Before Gen 6)": ["Water"], 
    "Mawile (Before Gen 6)": ["Steel"], 
    "Mime Jr. (Before Gen 6)": ["Psychic"],
    "Mr. Mime (Before Gen 6)": ["Psychic"],
    "Ralts (Before Gen 6)": ["Psychic"], 
    "Snubbull (Before Gen 6)": ["Normal"],
    "Togekiss (Before Gen 6)": ["Normal", "Flying"], 
    "Togepi (Before Gen 6)": ["Normal"], 
    "Togetic (Before Gen 6)": ["Normal", "Flying"],
    "Whimsicott (Before Gen 6)": ["Grass"],
    "Wigglytuff (Before Gen 6)": ["Normal"],
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
        "Mow Rotom": ["Electric", "Flying"],
        "Heat Rotom":  ["Electric", "Ghost"],
        "Wash Rotom (Before Gen 5)": ["Electric", "Ghost"],
        "Frost Rotom (Before Gen 5)": ["Electric", "Ghost"],
        "Fan Rotom (Before Gen 5)": ["Electric", "Ghost"],
        "Mow Rotom (Before Gen 5)": ["Electric", "Ghost"]
        },
    "Shaymin": {
        "Land Forme": ["Grass"],
        "Sky Forme": ["Grass", "Flying"]
        },
    "Arceus": {
        "No Plate": ["Normal"],
        "Fist Plate": ["Fighting"],
        "Sky Plate": ["Flying"],
        "Toxic Plate": ["Poison"],
        "Earth Plate": ["Ground"],
        "Stone Plate": ["Rock"],
        "Insect Plate": ["Bug"],
        "Spooky Plate": ["Ghost"],
        "Iron Plate": ["Steel"],
        "Flame Plate": ["Fire"],
        "Splash Plate": ["Water"],
        "Meadow Plate": ["Grass"],
        "Zap Plate": ["Electric"],
        "Mind Plate": ["Psychic"],
        "Icicle Plae": ["Ice"],
        "Draco Plate": ["Dragon"],
        "Dread Plate": ["Dark"],
        "Pixie Plate": ["Fairy"]
        },
    "Meloetta": {
        "Aria Forme": ["Normal", "Psychic"],
        "Pirouette Forme": ["Normal", "Fighting"]
        },
    "Hoopa": {
        "Confined": ["Psychic", "Ghost"],
        "Unbound": ["Psychic", "Dark"]
        },
    "Oricorio": {
        "Baile Style": ["Fire", "Flying"],
        "Pom-Pom Style": ["Electric", "Flying"],
        "Pa'u Style": ["Psychic", "Flying"],
        "Sensu Style": ["Ghost", "Flying"]
        },
    "Silvally": {
        "Type: Normal": ["Normal"],
        "Type: Fighting": ["Fighting"],
        "Type: Flying": ["Flying"],
        "Type: Poison": ["Poison"],
        "Type: Ground": ["Ground"],
        "Type: Rock": ["Rock"],
        "Type: Bug": ["Bug"],
        "Type: Ghost": ["Ghost"],
        "Type: Steel": ["Steel"],
        "Type: Fire": ["Fire"],
        "Type: Water": ["Water"],
        "Type: Grass": ["Grass"],
        "Type: Electric": ["Electric"],
        "Type: Psychic": ["Psychic"],
        "Type: Ice": ["Ice"],
        "Type: Dragon": ["Dragon"],
        "Type: Dark": ["Dark"],
        "Type: Fairy": ["Fairy"]
        },
    "Necrozma": {
        "Necrozma": ["Psychic"],
        "Dusk Mane Necrozma": ["Psychic", "Steel"],
        "Dawn Wings Necrozma": ["Psychic", "Ghost"],
        "Ultra Necrozma": ["Psychic", "Dragon"]
        },
    "Zacian": {
        "Hero of Many Battles": ["Fairy"],
        "Crowned Sword": ["Fairy", "Steel"]
        },
    "Zamazenta": {
        "Hero of Many Battles": ["Fighting"],
        "Crowned Shield": ["Fighting", "Steel"]
        },
    "Urshifu": {
        "Single Strike": ["Fighting", "Dark"],
        "Rapid Strike": ["Fighting", "Water"]
        },
    "Calyrex": {
        "Calyrex": ["Psychic", "Grass"],
        "Ice Rider": ["Psychic", "Ice"],
        "Shadow Rider": ["Psychic", "Ghost"]
        },
    "Ogerpon": {
        "Teal Mask": ["Grass"],
        "Wellspring Mask": ["Grass", "Water"],
        "Hearthflame Mask": ["Grass", "Fire"],
        "Cornerstone Mask": ["Grass", "Rock"]
        }
    }

#Merge all forms into a single dictionary
all_forms = {**base_types, **mega_evolutions, **primal_reversion}

#Needed due to items such as Paldean Tauros and Urshifu having nested dictionaries
for pokemon, variants in base_types.items():
    if isinstance(variants, dict):
        all_forms.update({f"{pokemon} ({variant})": types for variant, types in variants.items()})
    else:
        all_forms[pokemon] = variants
for pokemon, variants in mega_evolutions.items():
    if isinstance(variants, dict):
        all_forms.update({f"{pokemon} ({variant})": types for variant, types in variants.items()})
    else:
        all_forms[pokemon] = variants
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
        if f"{pokemon} (Before Gen 6)" in alternate_forms:
            forms.append(f"{pokemon} (Before Gen 6)")
        if f"{pokemon} (Before Gen 2)" in alternate_forms:
            forms.append(f"{pokemon} (Before Gen 2)")
    elif pokemon in mega_evolutions or pokemon in primal_reversion or pokemon in regional_variants or pokemon in alternate_forms:
        forms.append(pokemon)

#Handle case where Pokémon is not found due to mispelling or not existing
    if not forms:
        print("Pokémon not found. Please be sure you have spelled the name correctly.")
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
            
        if selected_pokemon == ("Mega Charizard") and isinstance(mega_evolutions[selected_pokemon], dict):
            breeds = list(mega_evolutions[selected_pokemon].keys())
            print(f"{selected_pokemon} has multiple breeds:")
            for i, breed in enumerate(breeds):
                print(f"{i + 1}. {breed}")
            breed_choice = int(input(f"Select the breed of {pokemon} you want by entering the number: "))
            selected_pokemon = f"{selected_pokemon} ({breeds[breed_choice - 1]})"
        if selected_pokemon == ("Mega Mewtwo") and isinstance(mega_evolutions[selected_pokemon], dict):
            breeds = list(mega_evolutions[selected_pokemon].keys())
            print(f"{selected_pokemon} has multiple breeds:")
            for i, breed in enumerate(breeds):
                print(f"{i + 1}. {breed}")
            breed_choice = int(input(f"Select the breed of {pokemon} you want by entering the number: "))
            selected_pokemon = f"{selected_pokemon} ({breeds[breed_choice - 1]})"
        if selected_pokemon == ("Paldean Tauros") and isinstance(regional_variants[selected_pokemon], dict):
            breeds = list(regional_variants[selected_pokemon].keys())
            print(f"{selected_pokemon} has multiple breeds:")
            for i, breed in enumerate(breeds):
                print(f"{i + 1}. {breed}")
            breed_choice = int(input(f"Select the breed of {pokemon} you want by entering the number: "))
            selected_pokemon = f"{selected_pokemon} ({breeds[breed_choice - 1]})"
        if selected_pokemon == "Darmanitan" and isinstance(base_types[selected_pokemon], dict):
            breeds = list(base_types[selected_pokemon].keys())
            print(f"{selected_pokemon} has multiple forms:")
            for i, breed in enumerate(breeds):
                print(f"{i + 1}. {breed}")
            breed_choice = int(input(f"Select the form of {pokemon} you want by entering the number: "))
            selected_pokemon = f"{selected_pokemon} ({breeds[breed_choice - 1]})"
        if selected_pokemon == "Galarian Darmanitan" and isinstance(regional_variants[selected_pokemon], dict):
            breeds = list(regional_variants[selected_pokemon].keys())
            print(f"{selected_pokemon} has multiple forms:")
            for i, breed in enumerate(breeds):
                print(f"{i + 1}. {breed}")
            breed_choice = int(input(f"Select the form of {pokemon} you want by entering the number: "))
            selected_pokemon = f"{selected_pokemon} ({breeds[breed_choice - 1]})"

    #I tried to use an or statement for this alternate_forms dictionary but I coulnd't get it to work so each alt form gets its own if statement. Whoopee. Thanks ctrl-c and ctrl-v
        if selected_pokemon == "Castform" and isinstance(alternate_forms[selected_pokemon], dict):
            breeds = list(alternate_forms[selected_pokemon].keys())
            print(f"{selected_pokemon} has multiple forms:")
            for i, breed in enumerate(breeds):
                print(f"{i + 1}. {breed}")
            breed_choice = int(input(f"Select the form of {pokemon} you want by entering the number: "))
            selected_pokemon = f"{selected_pokemon} ({breeds[breed_choice - 1]})"
        if selected_pokemon == "Wormadam" and isinstance(alternate_forms[selected_pokemon], dict):
            breeds = list(alternate_forms[selected_pokemon].keys())
            print(f"{selected_pokemon} has multiple forms:")
            for i, breed in enumerate(breeds):
                print(f"{i + 1}. {breed}")
            breed_choice = int(input(f"Select the form of {pokemon} you want by entering the number: "))
            selected_pokemon = f"{selected_pokemon} ({breeds[breed_choice - 1]})"
        if selected_pokemon == "Rotom" and isinstance(alternate_forms[selected_pokemon], dict):
            breeds = list(alternate_forms[selected_pokemon].keys())
            print(f"{selected_pokemon} has multiple forms:")
            for i, breed in enumerate(breeds):
                print(f"{i + 1}. {breed}")
            breed_choice = int(input(f"Select the form of {pokemon} you want by entering the number: "))
            selected_pokemon = f"{selected_pokemon} ({breeds[breed_choice - 1]})"
        if selected_pokemon == "Shaymin" and isinstance(alternate_forms[selected_pokemon], dict):
            breeds = list(alternate_forms[selected_pokemon].keys())
            print(f"{selected_pokemon} has multiple forms:")
            for i, breed in enumerate(breeds):
                print(f"{i + 1}. {breed}")
            breed_choice = int(input(f"Select the form of {pokemon} you want by entering the number: "))
            selected_pokemon = f"{selected_pokemon} ({breeds[breed_choice - 1]})"
        if selected_pokemon == "Arceus" and isinstance(alternate_forms[selected_pokemon], dict):
            breeds = list(alternate_forms[selected_pokemon].keys())
            print(f"{selected_pokemon} has multiple forms:")
            for i, breed in enumerate(breeds):
                print(f"{i + 1}. {breed}")
            breed_choice = int(input(f"Select the form of {pokemon} you want by entering the number: "))
            selected_pokemon = f"{selected_pokemon} ({breeds[breed_choice - 1]})"
        if selected_pokemon == "Meloetta" and isinstance(alternate_forms[selected_pokemon], dict):
            breeds = list(alternate_forms[selected_pokemon].keys())
            print(f"{selected_pokemon} has multiple forms:")
            for i, breed in enumerate(breeds):
                print(f"{i + 1}. {breed}")
            breed_choice = int(input(f"Select the form of {pokemon} you want by entering the number: "))
            selected_pokemon = f"{selected_pokemon} ({breeds[breed_choice - 1]})"
        if selected_pokemon == "Hoopa" and isinstance(alternate_forms[selected_pokemon], dict):
            breeds = list(alternate_forms[selected_pokemon].keys())
            print(f"{selected_pokemon} has multiple forms:")
            for i, breed in enumerate(breeds):
                print(f"{i + 1}. {breed}")
            breed_choice = int(input(f"Select the form of {pokemon} you want by entering the number: "))
            selected_pokemon = f"{selected_pokemon} ({breeds[breed_choice - 1]})"
        if selected_pokemon == "Oricorio" and isinstance(alternate_forms[selected_pokemon], dict):
            breeds = list(alternate_forms[selected_pokemon].keys())
            print(f"{selected_pokemon} has multiple forms:")
            for i, breed in enumerate(breeds):
                print(f"{i + 1}. {breed}")
            breed_choice = int(input(f"Select the form of {pokemon} you want by entering the number: "))
            selected_pokemon = f"{selected_pokemon} ({breeds[breed_choice - 1]})"
        if selected_pokemon == "Silvally" and isinstance(alternate_forms[selected_pokemon], dict):
            breeds = list(alternate_forms[selected_pokemon].keys())
            print(f"{selected_pokemon} has multiple forms:")
            for i, breed in enumerate(breeds):
                print(f"{i + 1}. {breed}")
            breed_choice = int(input(f"Select the form of {pokemon} you want by entering the number: "))
            selected_pokemon = f"{selected_pokemon} ({breeds[breed_choice - 1]})"
        if selected_pokemon == "Necrozma" and isinstance(alternate_forms[selected_pokemon], dict):
            breeds = list(alternate_forms[selected_pokemon].keys())
            print(f"{selected_pokemon} has multiple forms:")
            for i, breed in enumerate(breeds):
                print(f"{i + 1}. {breed}")
            breed_choice = int(input(f"Select the form of {pokemon} you want by entering the number: "))
            selected_pokemon = f"{selected_pokemon} ({breeds[breed_choice - 1]})"
        if selected_pokemon == "Zacian" and isinstance(alternate_forms[selected_pokemon], dict):
            breeds = list(alternate_forms[selected_pokemon].keys())
            print(f"{selected_pokemon} has multiple forms:")
            for i, breed in enumerate(breeds):
                print(f"{i + 1}. {breed}")
            breed_choice = int(input(f"Select the form of {pokemon} you want by entering the number: "))
            selected_pokemon = f"{selected_pokemon} ({breeds[breed_choice - 1]})"
        if selected_pokemon == "Zamazenta" and isinstance(alternate_forms[selected_pokemon], dict):
            breeds = list(alternate_forms[selected_pokemon].keys())
            print(f"{selected_pokemon} has multiple forms:")
            for i, breed in enumerate(breeds):
                print(f"{i + 1}. {breed}")
            breed_choice = int(input(f"Select the form of {pokemon} you want by entering the number: "))
            selected_pokemon = f"{selected_pokemon} ({breeds[breed_choice - 1]})"
        if selected_pokemon == "Urshifu" and isinstance(alternate_forms[selected_pokemon], dict):
            breeds = list(alternate_forms[selected_pokemon].keys())
            print(f"{selected_pokemon} has multiple forms:")
            for i, breed in enumerate(breeds):
                print(f"{i + 1}. {breed}")
            breed_choice = int(input(f"Select the form of {pokemon} you want by entering the number: "))
            selected_pokemon = f"{selected_pokemon} ({breeds[breed_choice - 1]})"
        if selected_pokemon == "Calyrex" and isinstance(alternate_forms[selected_pokemon], dict):
            breeds = list(alternate_forms[selected_pokemon].keys())
            print(f"{selected_pokemon} has multiple forms:")
            for i, breed in enumerate(breeds):
                print(f"{i + 1}. {breed}")
            breed_choice = int(input(f"Select the form of {pokemon} you want by entering the number: "))
            selected_pokemon = f"{selected_pokemon} ({breeds[breed_choice - 1]})"
        if selected_pokemon == "Ogerpon" and isinstance(alternate_forms[selected_pokemon], dict):
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
            print(f"{selected_pokemon} is {type_string}.")
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
