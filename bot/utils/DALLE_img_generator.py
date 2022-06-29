from docarray import Document
from settings import SERVER_URL


class DALLE_img_generator:

    def __init__(self):
        self.server_url = SERVER_URL

    def generate_png(self, prompt):
        print("Generating jpg...")
        print(prompt)
        da = Document(text=prompt).post(self.server_url, parameters={'num_images': 2}).matches
        da.plot_image_sprites(output="../data/temp2.jpg", fig_size=(10, 10), show_index=True)
        print("jpg generated")
