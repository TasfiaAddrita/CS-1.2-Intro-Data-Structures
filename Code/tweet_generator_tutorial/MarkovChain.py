import histogram
import sys

class MarkovChain:
    def __init__(self):
        pass

# params = sys.argv[1:]
text = 'text/test.txt'

words_list = histogram.get_words(text)
histo = histogram.histogram_dict(words_list)

print(histo)