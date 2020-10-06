from app.modules.preprocess.preprocess import PreprocessText
from app.modules.models.word2vec import Word2Vec
import pandas as pd

MOCK_PATH = 'data/models/word2vec_pubmed/'
MOCK_MODEL_NAME = 'general_pubmed.model'
MOCK_EMBEDDINGS_SIZE = 300


def get_important_symbols(filepath):
    # Read file with important symbols (rows, columns)
    with open(filepath, 'r') as f:
        symbols = f.readlines()
    return [x.replace('\n', '').lower() for x in symbols]


def read_datasource(filepath):
    # Read file with datasource
    abstracts = pd.read_csv(filepath)['text'].values.tolist()
    abstracts = [x.replace('\n', '') for x in abstracts]
    return abstracts


def fine_tuning_preprocess(filepath):
    # Model fine-tuning script. filepath to the .csv datasource file
    columns = []
    datasource = []
    abstracts = read_datasource(filepath)
    rows = get_important_symbols('data/rows/stocks.txt')
    terms = columns + rows
    preprocess = PreprocessText(important_terms=terms, input_text=abstracts)
    preprocess.clean(abstracts)
    datasource += preprocess.cleaned_tokens
    Word2Vec(path_to_model=MOCK_PATH, model_filename=MOCK_MODEL_NAME).fine_tune(datasource)


