import pandas as pd
import json
import os

DATASET_PATH= "data/datasets/"
def set_labels_from_file():


    file_list = [i for i in os.listdir(DATASET_PATH) if ".csv" in i]
    json_str = {}
    for i in file_list:
        dataframe = pd.read_csv(os.path.join(DATASET_PATH, i), index_col=0)
        rows = tuple(dataframe.index)
        columns = tuple(dataframe.columns)
        json_str[i]={}
        json_str[i]["columns"] = columns
        json_str[i]["rows"] = rows



    return json.dumps(json_str, indent=2)


def set_dataset():
    file_list = [i for i in os.listdir(DATASET_PATH) if ".csv" in i]
    json_str = {}
    for i in file_list:
        json_str[i]=""

    return json.dumps(json_str, indent=2)