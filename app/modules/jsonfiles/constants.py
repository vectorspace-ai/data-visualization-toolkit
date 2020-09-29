from app.modules.datasets.get_labels import *
from os.path import join
from enum import Enum

dataset_path = "data/datasets"


class DatasetFiles(Enum):
    STOCKS500SYMBOLS = "heatmap-realtime-stocks-by-stocks-0x923fcaB5b510C16c656312cFd503B83Fb1A0b2F4-matrix.csv"
    STOCKS_TO_DRUGS = "heatmap-realtime-stocks-by-drugs-0x923fcaB5b510C16c656312cFd503B83Fb1A0b2F4-matrix.csv"


DATASET = {
    DatasetFiles.STOCKS500SYMBOLS.value: get_rows(join(dataset_path, DatasetFiles.STOCKS500SYMBOLS.value)),
    DatasetFiles.STOCKS_TO_DRUGS.value: get_rows(join(dataset_path, DatasetFiles.STOCKS_TO_DRUGS.value))
}
