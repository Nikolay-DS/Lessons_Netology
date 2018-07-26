import pandas as pd
import numpy as np

FILE_PATH = '/Users/nicolas13/Lessons_Netology/Lesson4_1/names/'

years = [1985]
def count_top3(year, FILE_PATH):
    path = FILE_PATH + 'yob' + str(year) +'.txt'
    names = pd.read_csv(
    path,
    names=['Names', 'Gender', 'Count'])
    return names

for year in years:
    count_top3(year, FILE_PATH).head(10)

