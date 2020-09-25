from app.modules.datasets.get_labels import *
from os.path import join
from enum import Enum

dataset_path = "data/datasets"


class DatasetFiles(Enum):
    STOCKS500SYMBOLS = "stocks500symbols.csv"
    STOCKS_TO_DRUGS = "500stocksto100drugcompounds.csv"


DATASET = {
    DatasetFiles.STOCKS500SYMBOLS.value: get_unique_symbols(join(dataset_path, DatasetFiles.STOCKS500SYMBOLS.value)),
    DatasetFiles.STOCKS_TO_DRUGS.value: get_unique_symbols(join(dataset_path, DatasetFiles.STOCKS_TO_DRUGS.value))
}
