import sys
from random import randint

# shuffles list
def fisher_yates(list_):
    last_index = len(list_) - 1
    while last_index > 0:
        random_index = randint(0, last_index)
        temp = list_[random_index]
        list_[random_index] = list_[last_index]
        list_[last_index] = temp
        
        last_index -= 1
    
    return list_

def reverse_word(word):
    # return word[::-1] # high level attempt
    reverse = ""
    for letter in range(len(word)-1, -1, -1):
        reverse += word[letter]
    return reverse

def reverse_sentences(sen_list):
    reverse = []
    for word in range(len(sen_list), 0, -1):
        reverse.append(sen_list[word-1])
    return reverse

# help from https://stackoverflow.com/questions/11989502/producing-all-the-anagrams-from-a-string-python
def simple_anagram(elements):
    if len(elements) <= 1:
        return elements
    else:
        ans = []
        for perm in simple_anagram(elements[1:]):
            for index in range(len(elements)):
                ans.append(perm[:index] + elements[0:1] + perm[index:])
        return ans

# print(simple_anagram('abc'))