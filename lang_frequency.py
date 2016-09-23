import operator
from string import punctuation


def load_data(filepath):
    with open(filepath, encoding='utf8') as file:
        return file.read()


def get_most_frequent_words(text):
    only_chars = "".join(ch for ch in text if ch not in punctuation)
    words_dict = dict()
    for word in only_chars.split():
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1
    sorted_words = sorted(words_dict.items(), key=operator.itemgetter(1))
    top_ten = sorted_words[-10:][::-1]
    for word in top_ten:
        print(word)
    return top_ten


if __name__ == '__main__':
    data = load_data('lorem.txt')
    get_most_frequent_words(data)
