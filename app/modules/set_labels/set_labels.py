import pandas as pd 
import json

def set_labels_from_file(dataframe):
	rows=tuple(dataframe.index)
	columns=tuple(dataframe.columns)

	json_str={"rows": rows, "columns": columns}
	header="DATASET = "
	with open("constants.py", 'w') as f:
		f.write(header)
		f.write(json.dumps(json_str, indent=2))



def set_labels_from_file(dataframe, dataframe_filename):
	rows=tuple(dataframe.index)
	columns=tuple(dataframe.columns)

	json_str={dataframe_filename: rows}
	header="DATASET = "
	with open("constants.py", 'w') as f:
		f.write(header)
		f.write(json.dumps(json_str, indent=2))



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

if __name__ == '__main__':
	set_labels(pd.read_csv("test.csv", index_col=0), "test.csv")