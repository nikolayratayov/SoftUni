class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f'Caught {pokemon.pokemon_details()}'
        else:
            return f"This pokemon is already caught"

    def release_pokemon(self, pok_name):
        for i in self.pokemons:
            if i.name == pok_name:
                self.pokemons.remove(i)
                return f"You have released {pok_name}"
        return 'Pokemon is not caught'

    def trainer_data(self):
        res = f'Pokemon Trainer {self.name}\n'
        res += f'Pokemon count {len(self.pokemons)}\n'
        for i in self.pokemons:
            res += f'- {i.pokemon_details()}\n'
        return res[0:len(res) - 1]
