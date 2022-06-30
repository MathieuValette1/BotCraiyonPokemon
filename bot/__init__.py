from twitter import Bot
from utils import *

tw = Bot()


def new_tweet():
    """
    génère et tweet.
    :return:
    """

    #generate images.
    path_image_origine = ""
    path_image_genere = ""
    title = "Tortank doing stuff"
    tw.tweet(title,[path_image_genere,path_image_origine])
    """
    mettre le pokemon de base en réponse.
    """