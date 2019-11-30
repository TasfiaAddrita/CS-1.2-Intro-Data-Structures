import re
import string


def get_words(source_text):
    text = open(source_text)
    story = text.read()
    text.close()

    # regex help https://stackoverflow.com/a/13184791/12049271
    delimiters = ' ', '\n'
    regexPattern = '|'.join(map(re.escape, delimiters))
    words = re.split(regexPattern, story)
    words = list(
        filter(None, [word.strip(string.punctuation).lower() for word in words]))
    return words


def histogram_dict(words):
    histogram = {}
    for word in words:
        if word not in histogram:
            histogram[word] = 1
        else:
            histogram[word] += 1
    return histogram


def histogram_list(words):
    histogram = []

    for word in words:
        in_list = False
        for w in histogram:
            if word == w[0]:
                in_list = True
                w[1] += 1
                break
        if in_list == False:
            histogram.append([word, 1])

    return histogram


def histogram_tuple(words):
    histogram = []
    in_tuple = False

    for word in words:
        in_tuple = False
        for w in histogram:
            if word == w[0]:
                in_tuple = True
                histogram.append((word, w[1]+1))
                histogram.remove(w)
                break
        if in_tuple == False:
            histogram.append((word, 1))

    return histogram


def histogram_counts(words):
    histogram = [(1, [])]
    in_count = False

    for word in words:
        in_count = False
        for histo in histogram:
            if word in histo[1]:
                in_count = True
                histo[1].remove(word)
                if histo[0] == len(histogram):
                    histogram.append((histo[0] + 1, [word]))
                else:
                    histogram[histo[0]][1].append(word)
                break
        if in_count == False:
            histogram[0][1].append(word)

    return list(filter(lambda histo: histo[1] != [], histogram))


# assumes histogram is a hist_dict object
def write_histogram_file(file_name, histogram):
    f = open(file_name, 'w')
    for key in histogram:
        f.write(f'{key} {histogram[key]}\n')
    f.close()


def unique_words(histogram):
    return len(histogram.keys())

    # low-level attempt
    # count = 0
    # for word in histogram:
    #     count += 1

    # return count


def frequency(word, histogram):
    return histogram[word]


if __name__ == "__main__":
    words = get_words('text/three_wishes.txt')
    # words = get_words('text/fish.txt')
    # print(words)
    # print(histogram_counts(words))

    hist_dict = histogram_dict(words)
    print(hist_dict)
    # write_histogram_file('histogram_file', hist_dict)

    # hist_list = histogram_list(words)
    # print(hist_list)

    # hist_count = histogram_count(words)
    # print(hist_count)
