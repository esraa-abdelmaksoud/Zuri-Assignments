# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from collections import Counter
import re

def read_file_content(filename):
    # [assignment] Add your code here 
    with open (filename) as f:
        lines = f.readlines()

    # Join text lines and convert to lowercase
    text = "".join(lines).lower()

    return text


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here

    # Cleaning text to remove symbols, question marks, etc
    clean_text = re.sub('[^a-z ]', '', text)
    words = clean_text.split()

    # Consider any of the two solutions
    # Solution 1
    # word_dict = Counter(words)

    # Solution 2
    word_dict = {}
    for w in words:
        if w in word_dict.keys():
            word_dict[w] += 1
        else:
            word_dict[w] = 1

    return word_dict
