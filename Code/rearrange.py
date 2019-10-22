import sys
import random

def random_params(params_list):
    return random.sample(params_list, k=len(params_list))

def reverse_word(word):
    return word[::-1]

def reverse_sentences(sen_list):
    return

params = sys.argv[1:]
# print(params)

ran_params = random_params(params)
ran_params_string = ""
for param in ran_params:
    ran_params_string += param + " "
print(ran_params_string)

rev_word = reverse_word(random.choice(ran_params))
print(rev_word)