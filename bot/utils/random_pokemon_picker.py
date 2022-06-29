import json
import random


class Random_pokemon_picker:
    """
    This class loads the json containing the list of Pokemons.

    The function pick_random_pokemon_as_dict() select a random pokemon il the list of Pokemons and return it as a dict.
    """

    def __init__(self):
        with open("../data/pokedex_until_4g.json", 'r', encoding="utf8") as f:
            self.pokedex = json.load(f)

    def pick_random_pokemon_as_dict(self):
        """
        The function pick_random_pokemon_as_dict() select a random pokemon il the list of Pokemons.

        Exemple of dict returned: {'id': 70, 'name': {'english': 'Weepinbell', 'japanese': 'ウツドン', 'chinese': '口呆花',
        'french': 'Boustiflor'}, 'type': ['Grass', 'Poison'], 'base': {'HP': 65, 'Attack': 90, 'Defense': 50,
        'Sp. Attack': 85, 'Sp. Defense': 45, 'Speed': 55}}

        :return: a dict containing the information about a random Pokemon.
        """
        return random.choice(self.pokedex)
