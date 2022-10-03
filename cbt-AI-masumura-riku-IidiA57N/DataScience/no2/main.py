import os
import pandas as pd
import csv

def main(input_path, output_path) -> None:
    csv_path = "C:\Users\riku.masumura\cbt-AI-masumura-riku-IidiA57N\DataScience\no2\data\sample1.csv"
    with open (csv_path, 'r') as f: #置換の指定
        s = f.read()
        s = s.replace("　"," ")

    with open (csv_path, 'w') as f: #書き込みの指定
        f.write(s)
    return


if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), 'data/sample1.csv')
    output_path = os.path.join(os.path.dirname(__file__), 'submit.csv')
    main(input_path, output_path)