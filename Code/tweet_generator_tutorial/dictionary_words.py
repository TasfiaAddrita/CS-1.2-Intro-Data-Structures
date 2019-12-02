import sys
from random import randint, choice, randrange
import time
import math
from rearrange import simple_anagram

def time_it(func):
    # Made wth love by Ben :heart: - DS2.3
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + ' took ' + str((end - start) * 10000) + ' ms\n')
        return result
    return wrapper

def get_dict_words():
    f = open('/usr/share/dict/words')
    word_list = f.readlines()
    word_list = [word.strip() for word in word_list]
    f.close()
    return word_list

# @time_it
def random_words(num_words):
    word_list = get_dict_words()
    
    ran_words = []
    dict_words = 0
    while dict_words < int(num_words):
        # ran_words.append(word_list[randint(0, len(word_list)-1)])
        ran_words.append(word_list[randrange(len(word_list))])
        dict_words += 1

    # return ' '.join(ran_words)
    return ran_words

def real_anagram(elements):
    dict_words = get_dict_words()
    sim_ana = simple_anagram(elements)
    real_ana = []
    for word in sim_ana:
        if word in dict_words:
            real_ana.append(word)
    return real_ana

# print(real_anagram('abc'))

cow = '''
________________________________________
/ You have Egyptian flu: you're going to \
|                                        |
\ be a mummy.                            /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

MAX_CHAR = 41
def cowsay(word_list):
    # begin = '________________________________________\n'

    cow = ''
    cow_max_char = MAX_CHAR - 2
    for _ in range(cow_max_char):
        cow += '_'
    cow += '\n'

    total_len = 0
    for word in word_list:
        total_len += len(word)
    if total_len < cow_max_char:
        num_lines = 1
    else: 
        num_lines = int(math.ceil(total_len / cow_max_char))
    
    index = 0
    for line in range(1, num_lines+1):
        char_count = 0
        if line == 1:
            cow += '/ '
        else:
            cow += '| '
        char_count += 2

        while (char_count < cow_max_char) and (index < len(word_list)):
            add_word = word_list[index] + " "
            char_count_2 = char_count + len(add_word)

            if char_count_2 < cow_max_char:
                cow += add_word
                char_count += len(add_word)
                index += 1
            else:
                break

        if line == 1:
            cow += '\\\n'
        else:
            cow += '|\n'

    return cow

# params = sys.argv[1:]
# print(random_words(params[0]))
print(cowsay(random_words(4)))