import pandas as pd 
import json

df=pd.read_csv("data/datasets/correlation_matrix_pharm_500.csv")
print(json.dumps(df.columns.tolist(), indent=2))