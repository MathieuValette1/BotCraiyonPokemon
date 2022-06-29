from bot.utils.tweet_writter import Tweet_writter

tweet_writter = Tweet_writter()

tweet_text = tweet_writter.write_tweet()

print(tweet_text)





# from docarray import Document
# import json
# # from settings import SERVER_URL
# from random_pokemon_picker import Random_pokemon_picker
# from prompt_generator import Prompt_generator
#
# prompt_generator = Prompt_generator()
# random_picker = Random_pokemon_picker()
#
# prompt = prompt_generator.generate_prompt()
# SERVER_URL = 'grpc://dalle-flow.jina.ai:51005'
# print(prompt)
# da = Document(text=prompt).post(SERVER_URL, parameters={'num_images':2 }).matches
# print("oy")
# da.plot_image_sprites(output="../data/temp2.jpg", fig_size=(10, 10), show_index=True)

# da.save("../data/temp2.jpg", file_format='jpg')

# fav_id = 0
#
# fav = da[fav_id]
# # fav.display()
# fav.save_image_tensor_to_file(file="../data/temp.jpg", image_format='jpg')
# print('he')

