from DALLE_img_generator import DALLE_img_generator
from prompt_generator import Prompt_generator


class Tweet_writter:

    def __init__(self):
        self.my_prompt_generator = Prompt_generator()
        self.img_generator = DALLE_img_generator()

    def write_tweet(self):
        print("Writting tweet")
        prompt, tweet_text = self.my_prompt_generator.generate_prompt()
        self.img_generator.generate_png(prompt)
        print("Tweet written")

        return tweet_text
