from random import randint
from nltk import word_tokenize


class TweetGenerator:

    def __init__(self):
        self.tokens = self.retrieve_tokens()
        self.word_dict = self.build_word_dict()

    def retrieve_tokens(self):
        file = 'korean_words.txt'
        text = ''
        with open(file, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                text += line

        return word_tokenize(text)

    def build_word_dict(self):
        word_dict = {}
        for i in range(1, len(self.tokens)):
            if self.tokens[i - 1] not in word_dict:
                word_dict[self.tokens[i - 1]] = {}
            if self.tokens[i] not in word_dict[self.tokens[i - 1]]:
                word_dict[self.tokens[i - 1]][self.tokens[i]] = 0
            word_dict[self.tokens[i - 1]][self.tokens[i]] += 1
        return word_dict

    def word_list_sum(self, word_list):
        sum = 0
        for word, value in word_list.items():
            sum += value
        return sum

    def retrieve_random_word(self, word_list):
        rand_idx = randint(1, self.word_list_sum(word_list))
        for word, value in word_list.items():
            rand_idx -= value
            if rand_idx <= 0:
                return word

    def generate_tweet(self):
        start_character = self.tokens[randint(0, len(self.tokens) - 1)]
        chain = [start_character]
        length = randint(3, 25)
        for i in range(0, length):
            new_word = self.retrieve_random_word(self.word_dict[chain[-1]])
            chain.append(new_word)
        return ' '.join(chain)
