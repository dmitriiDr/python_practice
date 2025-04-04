import argparse
import pandas as pd
from pathlib import Path

def get_stats(data, col):
    print(f'Statistic for {col}\nMean: {data[col].mean()}\nMin: {data[col].min()}\nMax: {data[col].max()}')

def main(input, col):
    data = pd.read_csv(input)
    get_stats(data, col)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('csv_file', type=str, help='path to the csv file')
    parser.add_argument('--column', type=str, required=True, help='select a column')

    args = parser.parse_args()

    input = Path(args.csv_file)
    col = args.column

    main(input, col)