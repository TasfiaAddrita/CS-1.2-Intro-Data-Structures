import random
import histogram
import sys


def random_word(source_text):
    words_list = histogram.get_words(source_text)
    return random.choice(words_list)


def get_word_distribution(words_list):
    histo = histogram.histogram_dict(words_list)
    word_distribution = {}
    range_start = 1
    for word in histo:
        word_distribution[word] = list(
            range(range_start, range_start + histo[word]))
        range_start += histo[word]

    return word_distribution


def sample(words_list):
    word_distribution = get_word_distribution(words_list)

    ran_num = random.randint(1, len(words_list))
    for word in word_distribution:
        if ran_num in word_distribution[word]:
            return word


def test(words_list):
    test = []
    histogram_ = histogram.histogram_dict(words_list)
    for _ in range(10000):
        test.append(sample(words_list))
    hist_ran_words = histogram.histogram_dict(test)

    for word in hist_ran_words:
        print(word, 'test', hist_ran_words[word]/10000,
              'distribution', round((histogram_[word]/len(words_list)), 4))

    return


# params = sys.argv[1:]
# words_list = histogram.get_words(params[0])
words_list = histogram.get_words('text/three_wishes.txt')
print(sample(words_list))
# print(get_word_distribution(words_list))
# test(words_list)
