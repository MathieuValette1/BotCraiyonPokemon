from docarray import Document

server_url = 'grpc://dalle-flow.jina.ai:51005'

prompt = "a painting of a pikachu"



da = Document(text=prompt).post(server_url, parameters={'num_images': 2}).matches

da.plot_image_sprites(fig_size=(10,10), show_index=True)
