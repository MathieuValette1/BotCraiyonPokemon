import tweepy
from os import environ

from bot.utils.tweet_writter import Tweet_writter


class Bot:
    def __init__(self):
        # Authenticate to Twitter
        auth = tweepy.OAuth1UserHandler(environ["API_KEY"], environ["API_SECRET"], environ["ACCESS_TOKEN"],
                                        environ["ACCESS_SECRET"])
        # Create API object
        self.api = tweepy.API(auth)

    def tweet(self, text: str = False, path_image: str = False):
        """
        tweet avec une img si souhaité
        :param text: str
        :param img: str
        :return: status
        """

        return self.api.update_status_with_media(status=text, filename=path_image)


if __name__ == '__main__':
    t = Bot()
    tweet_writter = Tweet_writter()

    tweet_text = tweet_writter.write_tweet()
    print(t.tweet(tweet_text, "./data/temp2.jpg"))
