import pandas as pd


def get_df(path):
    df = pd.read_csv(path)
    return df


def get_rows(path):
    # Return rows name from df
    df = get_df(path)
    return df.columns.tolist()[1:]


def get_columns(path):
    # Return columns name from df
    df = get_df(path)
    return df['SYMBOL'].values.tolist()


def get_unique_symbols(path):
    # Return unique symbols from rows and columns name
    return list(set(get_columns(path)).union(set(get_rows(path))))
