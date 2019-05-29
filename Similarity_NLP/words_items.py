import numpy as np
from scipy.stats import itemfreq


def boc_term_vectors(word_list):
    word_list = [word.lower() for word in word_list]
    unique_chars = np.unique(np.hstack([list(word) for word in word_list]))
    print(unique_chars)
    word_list_term_counts = [{char: count for char, count in itemfreq(list(word))} for word in word_list]
    print(word_list_term_counts)
    boc_vectors = [np.array([int(word_term_counts.get(char, 0)) for char in unique_chars]) for word_term_counts in word_list_term_counts]
    return list(unique_chars), boc_vectors

term1 = 'this'
term2 = 'that'
term3 = 'these'
word_lists = [term1, term2, term3]
# word_lists = ['one two three', 'am is are ours', 'the this that these those']
features, (term1, term2, term3) = boc_term_vectors(word_lists)
print(features)
print(term1)
print(term2)
print(term3)