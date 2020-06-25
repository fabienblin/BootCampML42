import pandas as pd
from FileLoader import FileLoader

def YougestFellah(array: pd.DataFrame, year):
    a = {"f":0, "m":0}
    is_year = array["Year"] == year
    year_array = array[is_year]

    is_homme = year_array["Sex"] == "M"
    is_femme = year_array["Sex"] == "F"
    hommes = year_array[is_homme]
    femmes = year_array[is_femme]

    a["f"] = femmes["Age"].min()
    a["m"] = hommes["Age"].min()
    return a

fl = FileLoader()
csv = fl.load("csv.csv")
print(YougestFellah(csv, 2004))