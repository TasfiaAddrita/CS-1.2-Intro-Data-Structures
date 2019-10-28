def histogram(source_text):
    text = open(source_text)
    text = text.split()
    text.close()

    histogram = {}

    for word in text:
        if word not in histogram:
            histogram[word] = 1
        else:
            histogram[word] += 1
    
    return histogram

def unique_words(histogram):
    pass

def frequency(word, histogram):
    pass