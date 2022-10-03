import os
import pandas as pd


def main(input_path, output_path) -> None:
    pass


if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), 'data/sample1.csv')
    output_path = os.path.join(os.path.dirname(__file__), 'submit.csv')
    main(input_path, output_path)