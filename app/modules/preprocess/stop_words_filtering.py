from nltk.corpus import stopwords as stopwords_nltk
import nltk
nltk.download('stopwords')



class StopWords:
    def __init__(self):
        ...

    def get_tuatara_stop_words(self):
        with open('data/stop_words/tuatara.txt', 'r') as f:
            list_words = f.readlines()
        return [x.replace('\n', '') for x in list_words]

    def get_freq_dist(self, tokens):
        fdist = nltk.FreqDist(tokens)
        most_common_words = fdist.most_common()
        return most_common_words

    def get_most_frequent_stop_words(self, freq_words, k=50):
        return [k[0] for k in freq_words[0:k]]

    def get_low_frequent_words(self, freq_words, k=50):
        return [k[0] for k in freq_words[-k:]]

    def get_stops_by_freq(self, tokens):
        freq_words = self.get_freq_dist(tokens)
        return self.get_most_frequent_stop_words(freq_words) + self.get_low_frequent_words(freq_words)

    def filter_stop_words(self, stop_lst, important_terms):
        return [x for x in stop_lst if x not in important_terms]

    def get_stop_words(self, tokens=[], important_terms=[]):
        stop_words = []
        nltk_stop_words = stopwords_nltk.words('english')
        stop_words.extend(['n'])
        stop_words.extend(self.get_tuatara_stop_words())
        stop_words.extend(nltk_stop_words)
        stop_words.extend(self.get_stops_by_freq(tokens))
        lower_stops = [x.lower() for x in stop_words]
        return self.filter_stop_words(lower_stops, important_terms)

