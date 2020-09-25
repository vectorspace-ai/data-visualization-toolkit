from app.modules.models.base import BaseModel
from gensim.models import KeyedVectors
from gensim.models import Word2Vec as Word2Vec_gensim
from os.path import join
import numpy as np


class Word2Vec(BaseModel):

    ''' Word2Vec model class '''
    def __init__(
            self, *, path_to_model=None, model_filename=None, embeddings_shape=None, **kwargs,
    ):

        if path_to_model is None:
            raise AttributeError("path_to_model cannot be None")
        if model_filename is None:
            raise AttributeError("model_filename cannot be None")
        super().__init__(path_to_model=path_to_model, model_filename=model_filename,
                         embeddings_shape=embeddings_shape, **kwargs)

    def load_model(self):
        self.loaded_model = Word2Vec_gensim.load(join(self.path_to_model, self.model_filename))

    def get_vector(self, word):
        try:
            return self.loaded_model[word]
        except:
            return np.zeros(self.embeddings_shape)

    def fine_tune(self, cleaned_corpus):
        ''' Fine-tuning the model on corpus and save to the mocked directory'''

        model = Word2Vec_gensim.load(join(self.path_to_model, self.model_filename))
        model.build_vocab(cleaned_corpus, update=True)
        model.train(cleaned_corpus, total_examples=len(cleaned_corpus), epochs=30, report_delay=1)
        model.save('data/models/fine_tuned.model')