from string import punctuation
from collections import Counter
import argparse


def load_data(filepath):
    with open(filepath, encoding='utf8') as text_file:
        return text_file.read()


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('name')
    return parser


def get_unique_words_count(text):
    clear_text = "".join(ch for ch in text.lower() if ch not in punctuation)
    words_counter = Counter()
    for word in clear_text.split():
        words_counter[word] += 1
    return words_counter


if __name__ == '__main__':
    parser = create_parser()
    params = parser.parse_args()
    data = load_data(params.name)
    words_counter = get_unique_words_count(data)
    print('Most frequent words in text: ')
    for word in words_counter.most_common(10):
        print(word)
