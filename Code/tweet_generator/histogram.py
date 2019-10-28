import re
import string

def histogram(source_text):

    text = open(source_text)
    story = text.read()
    text.close()

    # regex help
    # https://stackoverflow.com/a/13184791/12049271
    delimiters = ' ', '\n'
    regexPattern = '|'.join(map(re.escape, delimiters))
    words = re.split(regexPattern, story)
    words = list(filter(None, [word.strip(string.punctuation).lower() for word in words]))
    # print(words)

    histogram = {}

    for word in words:
        if word not in histogram:
            histogram[word] = 1
        else:
            histogram[word] += 1
    
    return histogram

def unique_words(histogram):
    # easy
    return len(histogram.keys())

    # low-level attempt
    # count = 0
    # for word in histogram:
    #     count += 1
    
    # return count

def frequency(word, histogram):
    return histogram[word]

if __name__ == "__main__":
    hist = histogram('test.txt')
    print(unique_words(hist))
    print(frequency('hi', hist))