import pandas as pd
import json
import os


def set_labels_from_file():
    dataset_path = "data/datasets/"

    file_list = [i for i in os.listdir(dataset_path) if ".csv" in i]
    json_str = {}
    for i in file_list:
        dataframe = pd.read_csv(os.path.join(dataset_path, i), index_col=0)
        rows = tuple(dataframe.index)
        columns = tuple(dataframe.columns)
        json_str[i]={}
        json_str[i]["columns"] = columns
        json_str[i]["rows"] = rows



    return json.dumps(json_str, indent=2)


"""
1. take dataframe
2. get row labels from dataframe(and column labels too eventually). Set them as a list
3. get filename of dataframe
4. make json object with filename and labels in a list
5. overwrite constants.py with "DATASET ="  and append the JSON

FUTURE
-get column labels too
-ignore filename and make the keys "ROWS" or "COLUMNS" as the matrix will be loaded either way
-make it handle REAL JSON instead of saving to a constants.py file"""

"""if __name__ == '__main__':
	set_labels(pd.read_csv("test.csv", index_col=0), "test.csv")"""
