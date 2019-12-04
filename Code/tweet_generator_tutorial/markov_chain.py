import histogram
from data_structures.histogram_implementation.dictogram import Dictogram
import sys
import random

'''
STRETCH CHALLENGES

- Implement MarkovChain class to store states of word frequency histograms
    - Add methods for constructing state histograms and sampling words
- Handle beginning and end of sentences with special start and stop tokens
'''

class MarkovChain(Dictogram):
    def __init__(self, words_list, start=None, stop=None):
        super(MarkovChain, self).__init__()  
        self.words_list = words_list
        self.start = start
        self.stop = stop
        for key in self.build_text_histogram():
            self[key] = Dictogram()
        
    def build_text_histogram(self):
        return histogram.histogram_dict(self.words_list)
        
    def build_state_histogram(self):
        for index in range(len(self.words_list)-1):
            self[words_list[index]].add_count(words_list[index + 1])

    def get_next_word(self, word):
        return self[word].sample()

    def build_sentence(self, num_words):
        sentence = []
        if self.start is not None:
            sentence.append(self.start)
        else:
            sentence.append(random.choice(words_list))
        prev = sentence[0]
        for _ in range(num_words):
            next_word = self.get_next_word(prev)
            sentence.append(next_word)
            prev = next_word
        return ' '.join(sentence)

if __name__ == '__main__':
    text = 'text/test.txt'
    words_list = histogram.get_words(text)
    sentence = MarkovChain(words_list, 'deep')
    sentence.build_state_histogram()
    print(sentence.build_sentence(5))
    print(sentence)
