from constants import TEMPLATES
from random_pokemon_picker import Random_pokemon_picker
import random


class Prompt_generator:

    def __init__(self):
        self.templates = TEMPLATES
        self.random_picker = Random_pokemon_picker()

    def generate_prompt(self):
        pokemon = self.random_picker.pick_random_pokemon_as_dict()

        pokemon_id = pokemon['id']
        pokemon_name_english = pokemon['name']['english']
        pokemon_name_french = pokemon['name']['french']
        pokemon_name_japanese = pokemon['name']['japanese']

        template = random.choice(self.templates)

        on_a_bicycle = ' on a bicycle'

        prompt = template.format(pokemon_name_english) + on_a_bicycle


        return prompt