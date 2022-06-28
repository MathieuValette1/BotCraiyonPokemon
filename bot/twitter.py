import tweepy
from os import environ

class Bot:
    def __init__(self):
        # Authenticate to Twitter
        auth = tweepy.OAuth1UserHandler(environ["API_KEY"], environ["API_SECRET"], environ["ACCESS_TOKEN"],
                                        environ["ACCESS_SECRET"])
        # Create API object
        self.api = tweepy.API(auth)

    def tweet(self, text:str=False, path_image:str=False):
        """
        tweet avec une img si souhaité
        :param text: str
        :param img: str
        :return: status
        """

        return self.api.update_status_with_media(status=text, filename=path_image)


if __name__ == '__main__':
    t = Bot()
    print(t.tweet("Ce bot est trop bien 📌","./img.jpeg"))