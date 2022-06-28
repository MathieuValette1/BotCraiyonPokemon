from docarray import Document
import json
from settings import SERVER_URL
from random_pokemon_picker import Random_pokemon_picker
from prompt_generator import Prompt_generator

prompt_generator = Prompt_generator()
random_picker = Random_pokemon_picker()

prompt = prompt_generator.generate_prompt()

print(prompt)
da = Document(text=prompt).post(SERVER_URL, parameters={'num_images': 4}).matches
print("oy")
# da.plot_image_sprites(fig_size=(10, 10), show_index=True)
fav_id = 3

fav = da[fav_id]

fav.display()
print('he')

