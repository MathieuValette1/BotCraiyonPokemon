
from .twitter import Bot
from .utils import *
import os
import requests

tw = Bot()


def new_tweet():
    """
    génère et tweet.
    :return:
    """

    #generate images.
    my_tweet_writter = Tweet_writter()
    new_tweet_text, pokemon_name = my_tweet_writter.write_tweet()
    path_image_genere = "data/temp2.jpg"

    if not os.path.exists(f"./img/image_{pokemon_name.lower()}.jpg"):
        # si image non existante, génération image.
        image_url = f"https://img.pokemondb.net/artwork/large/{pokemon_name.lower()}.jpg"
        img_data = requests.get(image_url).content
        with open("data/temp_origine.jpg", 'wb') as handler:
            handler.write(img_data)

    path_image_origine = "data/temp_origine.jpg"

    tw.tweet(new_tweet_text, [path_image_genere, path_image_origine])
    print("Tweet envoyé avec succès")
