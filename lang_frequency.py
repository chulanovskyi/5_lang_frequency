from string import punctuation
from collections import Counter
import operator
import argparse
import sys


def load_data(filepath):
    with open(filepath, encoding='utf8') as text_file:
        return text_file.read()


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('name')
    return parser


def get_most_frequent_words(text):
    clear_text = "".join(ch for ch in text if ch not in punctuation)
    words_counter = Counter()
    for word in clear_text.split():
        words_counter[word] += 1
    top_ten = words_counter.most_common(10)
    return top_ten


if __name__ == '__main__':
    parser = create_parser()
    params = parser.parse_args()
    data = load_data(params.name)
    print('Most frequent words in text: ')
    for word in get_most_frequent_words(data):
        print(word)        
