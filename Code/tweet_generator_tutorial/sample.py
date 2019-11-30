import random
import histogram
import sys


def random_word(source_text):
    words_list = histogram.get_words(source_text)
    return random.choice(words_list)


def get_freq_percent(word_occurance):
    return round((word_occurance / len(words_list)) * 100)


def get_word_distribution(words_list):
    histo = histogram.histogram_dict(words_list)
    word_distribution = {}
    range_start = 0
    for word in histo:
        freq_percent = get_freq_percent(histo[word])
        word_distribution[word] = (freq_percent, list(
            range(range_start, range_start + freq_percent + 1)))
        range_start += freq_percent

    return word_distribution


def sample(words_list):
    word_distribution = get_word_distribution(words_list)

    ran_num = random.randint(0, 100)
    for word in word_distribution:
        if ran_num in word_distribution[word][1]:
            return word
        # else:
        #     return (None, ran_num) # ask Alan why expression doesn't think ran_num is in word_distribution


def test(words_list):
    test = []
    word_distribution = get_word_distribution(words_list)
    for _ in range(1000):
        test.append(sample(words_list))
    hist_ran_words = histogram.histogram_dict(test)

    for word in hist_ran_words:
        print(word, 'test', hist_ran_words[word]/1000,
              'dist', word_distribution[word][0]/100)
        # print('dist', word, word_distribution[word][0]/100)

    return

# words_list = histogram.get_words('test.txt')
# test(words_list)


# params = sys.argv[1:]
# words_list = histogram.get_words(params[0])
words_list = histogram.get_words('text/three_wishes.txt')
print(sample(words_list))
