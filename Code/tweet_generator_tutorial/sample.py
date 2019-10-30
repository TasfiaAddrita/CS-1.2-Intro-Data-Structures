import random
import histogram

def random_word(source_text):
    words_list = histogram.get_words(source_text)
    return random.choice(words_list)

def sample(words_list):
    histo = histogram.histogram_dict(words_list)
    word_distribution = {}
    range_start = 0
    for word in histo:
        freq_percent = round((histo[word] / len(words_list)) * 100)
        word_distribution[word] = range(range_start, range_start + freq_percent)
        range_start += freq_percent
    
    ran_num = random.randint(0, 100)
    for word in word_distribution:
        if ran_num in word_distribution[word]:
            return word

words_list = histogram.get_words('test.txt')
print(sample(words_list))