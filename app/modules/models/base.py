from abc import ABC, abstractmethod


class BaseModel(ABC):
    def __init__(
        self,
        *,
        domain=None,
        model_type=None,
        path_to_model=None,
        model_filename=None,
        config_filename=None,
        vocab_filename=None,
        keywords=None,
        keywords_vectors=None,
        embeddings_shape = None,
    ):
        self.domain = domain
        self.model_type=model_type,
        self.path_to_model = path_to_model
        self.model_filename = model_filename
        self.config_filename = config_filename
        self.vocab_filename = vocab_filename
        self.keywords = keywords
        self.loaded_model = None
        self.keywords_vectors = keywords_vectors or {}
        self.embeddings_shape = embeddings_shape

    @abstractmethod
    def load_model(self):
        ...

    @abstractmethod
    def get_vector(self, word):
        ...

    def fill_vectors_keywords(self):
        for w in self.keywords:
            vector = self.get_vector(w)
            if vector is not None:
                self.keywords_vectors[w] = vector

    @abstractmethod
    def fine_tune(self, cleaned_corpus):
        ...
