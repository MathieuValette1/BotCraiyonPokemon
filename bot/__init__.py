from .twitter import Bot
from .utils import *

tw = Bot()


def new_tweet():
    """
    génère et tweet.
    :return:
    """

    #generate images.
    my_tweet_writter = Tweet_writter()
    new_tweet_text, pokemon_name = my_tweet_writter.write_tweet()
    path_image_origine = "data/profil.jpg"
    path_image_genere = "data/temp2.jpg"
    tw.tweet(new_tweet_text, [path_image_genere, path_image_origine])
    print("Tweet envoyé avec succès")
    """
    mettre le pokemon de base en réponse.
    """