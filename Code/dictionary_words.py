import sys
from random import randint

def random_words(num_words):
    f = open('/usr/share/dict/words')
    word_list = f.readlines()
    f.close()
    
    ran_words = []
    dict_words = 0
    while dict_words < int(num_words):
        ran_words.append(word_list[randint(0, len(word_list)-1)])
        dict_words += 1

    return ''.join(ran_words)

params = sys.argv[1:]
print(random_words(params[0]))