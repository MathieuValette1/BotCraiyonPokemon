from docarray import Document
from settings import SERVER_URL
from prompt_generator import Prompt_generator

class DALLE_img_generator:

    def __init__(self):
        self.my_prompt_generator = Prompt_generator()
        self.server_url = SERVER_URL

    def generate_png(self):
        prompt = self.my_prompt_generator.generate_prompt()

        print(prompt)