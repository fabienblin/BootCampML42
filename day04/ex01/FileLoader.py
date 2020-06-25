import pandas as pd

class FileLoader:
    def load(self, path):
        try:
            csv = pd.read_csv(path)
            print("Loading dataset of dimensions", csv.shape)
            return csv
        except Exception as e:
            print(e)
            exit(1)

    def display(self, array: pd.DataFrame, n=0):
        if n == 0 :
            print(array)
        elif n > 0 :
            print(array.head(n))
        elif n < 0:
            print(array.tail(-n))
