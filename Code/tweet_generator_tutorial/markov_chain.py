import histogram
import dictogram
import sys
import random

class MarkovChain:
    def __init__(self):
        pass

# params = sys.argv[1:]
text = 'text/three_wishes.txt'

words_list = histogram.get_words(text)
text_histo = histogram.histogram_dict(words_list)

markov_histo = {}
for key in text_histo:
    markov_histo[key] = dictogram.Dictogram()

for index in range(len(words_list) - 1):
    markov_histo[words_list[index]].add_count(words_list[index + 1])

# print(markov_histo)

# for _ in markov_histo:
#     print(_, markov_histo[_])

def next_word(word):
    return markov_histo[word].sample()

sentence = []
sentence.append(random.choice(words_list))
prev = sentence[0]
for _ in range(7):
    next_w = next_word(prev)
    sentence.append(next_w)
    prev = next_w

print(' '.join(sentence))