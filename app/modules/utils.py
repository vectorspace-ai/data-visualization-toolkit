
def read_file_to_lst(filepath):
    "File where symbols separeted with \n. Return list of the symbols "
    with open(filepath, 'r') as f:
        symbols = f.readlines()
    return [x.replace('\n', '').lower() for x in symbols]