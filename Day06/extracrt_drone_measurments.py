import csv
import pandas as pd
import statistics
import sys

def csv_to_df(filename, index_col):
    df = pd.read_csv(filename, index_col=index_col, parse_dates=True)
    return df

def drop_high_var_idxs(filename, index_col, window_size, ths, col):
    df = csv_to_df(filename, index_col=index_col)
    df_interest = df[col]
    if window_size > len(df_interest):
        raise ValueError("Window size must be less than or equal to the length of the list.")
    
    rows_to_drop = []

    for i in range(len(df_interest) - window_size + 1):
        window = df_interest.iloc[i:i + window_size]
        window_var = statistics.variance(window)
        if window_var > ths:
            rows_to_drop.append(df_interest.index[i])
    
    df_clean = pd.DataFrame(df_interest.drop(rows_to_drop))
    return df_clean

def main():
    if len(sys.argv) != 6:
        exit(f"Usage: {sys.argv[0]} FileName index_col window_size ths col")
    
    file_name = sys.argv[1]
    index_col = sys.argv[2]
    window_size = int(sys.argv[3])
    ths = float(sys.argv[4])
    col = sys.argv[5]
    
    result = drop_high_var_idxs(file_name, index_col, window_size, ths, col)
    print(result)

if __name__ == "__main__":
    main()