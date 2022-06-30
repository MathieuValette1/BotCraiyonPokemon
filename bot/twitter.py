import tweepy
import os
from dotenv import load_dotenv

# if not os.path.isfile(".env"):
#     print("No config found.")
#     exit("Please read README.md.")

load_dotenv()

CONSUMER_KEY = os.getenv("API_KEY")
CONSUMER_SECRET = os.getenv("API_SECRET")
ACCESS_KEY = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")


class Bot:
    def __init__(self):
        # Authenticate to Twitter
        auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
        # Create API object
        self.api = tweepy.API(auth)

    def tweet(self, text: str = False, images: str or list = False):
        """
        tweet avec une img si souhaité
        :param text: str
        :param img: str
        :return: status
        """
        media_id = []
        if images:
            if type(images) == str:
                images = [images]
            for image in images:
                media_id.append(self.api.media_upload(image).media_id)
        return self.api.update_status(text, media_ids=media_id)


if __name__ == '__main__':
    t = Bot()


    #tweet_writter = Tweet_writter()

    #tweet_text = tweet_writter.write_tweet()
    #print(t.tweet(tweet_text, "./data/temp2.jpg"))
