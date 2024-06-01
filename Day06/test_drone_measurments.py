import extracrt_drone_measurments as dr
import pandas as pd
import pytest


def test_csv_to_df():
    file = '2023-08-26 05-46-33.csv'
    df = dr.csv_to_df(file, index_col='timestamp')
    assert df.shape == (4260, 17)


def test_drop_high_var_idxs():
    file = '2023-08-26 05-46-33.csv'
    df_clean = dr.drop_high_var_idxs(file, index_col='timestamp', window_size=10, ths=20, col='hum_pressure')
    assert df_clean.shape == (3863,1)


if __name__ == "__main__":
    pytest.main()