import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from app.modules.preprocess.stop_words_filtering import StopWords

nltk.download('punkt')

import string
import re


class PreprocessText:
    def __init__(self, important_terms=[], input_text=''):
        self.cleaned_tokens = None
        self.cleaned_text = None
        self.input_text = input_text
        self.important_terms = important_terms
        self.tokenized_sentences = self.tokenize_words(self.input_text)
        self.tokenized_words = [y for x in self.tokenized_sentences for y in x]
        self.STOP_WORDS = StopWords().get_stop_words(self.tokenized_words, self.important_terms)

    def remove_spaces(self, text):
        text = text.strip()
        text = text.split()
        return ' '.join(text)

    def lower(self, text):
        return [i.lower() for i in text]

    def tokenize_words(self, sentences):
        return [word_tokenize(t) for t in sentences]

    def remove_punctuation(self, tokens):
        first_filter = [[word for word in words_lst if word not in string.punctuation] for words_lst in tokens]
        second_filter = [[re.sub(r'[^\w\s]','',word) for word in words_lst if re.sub(r'[^\w\s]','',word)] for words_lst in first_filter]
        return second_filter

    def remove_digits(self, tokens):
        first_filter = [[word for word in words_lst if word not in string.digits] for words_lst in tokens]
        second_filter = [[word for word in words_lst if not word.isdigit()] for words_lst in first_filter]
        return second_filter


    def remove_stop_words(self, tokens):
        return [[word for word in words_lst if word not in self.STOP_WORDS] for words_lst in tokens]

    def get_cleaned_text_tokens(self):
        return self.cleaned_tokens

    def get_cleaned_text(self):
        return self.cleaned_text

    def clean(self, text):
        text = self.lower(text)
        clean_tokens = self.remove_punctuation(self.tokenized_sentences)
        clean_tokens = self.remove_digits(clean_tokens)
        clean_tokens = self.remove_stop_words(clean_tokens)
        self.cleaned_tokens = clean_tokens
        self.cleaned_text = [' '.join(x) for x in clean_tokens if x!=[]]