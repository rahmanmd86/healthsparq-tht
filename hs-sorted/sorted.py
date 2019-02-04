import pandas as pd
import numpy as np
from pathlib import Path

# Reads input file and returns a pandas dataframe
def read_input(path):
    file = Path(path)
    try:
        file.resolve(strict=True)
        print("Reading file: {}".format(path.split('/')[1]))
    except FileNotFoundError:
        return 
    else:
        return pd.read_csv(path, header=None) 
    

# Generates output file from the datafram
def generate_output(df, path):
    df.to_csv(path, header=None, index=False)
    print("Generated output at: ", path)
    pass
    

# Sorts dataframe
def sorted_values(df, ascending=True):
    values = df.to_numpy()
    values = np.sort(values)
    if not ascending:
        values = np.flip(values, axis=1)
    
    return pd.DataFrame(values)
    

if __name__ == "__main__":
    df = read_input('data/input.csv')
    if isinstance(df, pd.DataFrame):
        sorted_df = sorted_values(df, ascending=False)
        generate_output(sorted_df, 'data/output.csv')
    pass