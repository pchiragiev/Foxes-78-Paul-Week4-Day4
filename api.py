class Pokemon:
    def __init__(self):
        self.name = None
        self.types = None
        self.abilities = None
        self.weight = None

    def pokeAPIcall(self, pokemon):
        import requests as r
        req = r.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
        if req.status_code == 200:
            my_data = req.json()
        else:
            return req.status_code
        
        self.name = my_data['name']
        self.types = [x['type']['name'] for x in my_data['types']]
        self.abilities = [x['ability']['name'] for x in my_data['abilities']]
        self.weight = my_data['weight']

class Main:
    def run():
        pokemon_name = ['lugia', 'pikachu', 'spheal', 
        'wailord', 'charmander', 'articuno', 
        'bulbasaur', 'squirtle', 
        'dragonite', 'hitmonlee', 'zubat', 'psyduck', 'growlithe', 'arcanine', 
        'poliwhirl', 'bellsprout', 'golem', 'ponyta', 'slowpoke', 'magnemite']        

        poke = {}
        for name in pokemon_name:
            new = Pokemon()
            new.pokeAPIcall(name)
            poke[name] = new

        print(poke)

Main.run()

#monlist = [pokeAPIcall(name) for name in pokemon]

#types = set()

#for i in monlist:
#    for t in i['types']:
#        types.add(t)

#pokemonbytype = {}

#for t in types:
#    pokemonbytype[t] = {pokemon['name']:pokemon for pokemon in monlist if t in pokemon['types']}

#print(pokemonbytype) 

#pokemonbytype['water'] = {pokemon['name']:pokemon for pokemon in monlist if 'water' in pokemon['types']}
#print(pokemonbytype['water'])