import random
from histogram import get_words

def random_word(source_text):
    words_list = get_words(source_text)
    return random.choice(words_list)

print(random_word('test.txt'))