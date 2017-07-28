# make a crime thing


import os
import csv
from collections import Counter
from typing import Iterable, List
from itertools import groupby


Crimlist = Iterable[List[list]]


def get_data(path: str) -> str:
    """ get the data file """

    d_data = {i: n for i, n in enumerate(os.listdir(path), start=1)}
    for thi in d_data.items():
        print(thi)
    user_input = int(input('which file you need '))

    return os.path.join(path, d_data[user_input])


def open_file(path: str) -> list:
    """ basic file handler

    open file then pass to csv reader
    """
    with open(path, 'r') as f:
        df = csv.reader(f)
        df = list(df)
    return df


def prosses_data(data: list) -> Crimlist:
    """ val, clean and trans """
    header = data[0]
    body = data[1:]
    # row[1] is 00/00/0000
    # row[3] is type ie larceny

    new_crimes = Counter(cri[3] for cri in body)

    def helper(cr):
        return cr[1][-4:]

    lol_crime = sorted(body, key=helper)

    years = []
    for c, b in groupby(lol_crime, key=helper):
        years.append(Counter(cr[1][-4:] for cr in list(b)))

    return new_crimes, years, header


def calculate_data(cdata: dict, ydata: dict):
    """ get the prossesed data and do math

    find out highest crime year
    mosted commited crime and rareist
    """
    max_type = max(cdata.items(), key=lambda t: t[1])
    min_type = min(cdata.items(), key=lambda t: t[1])
    max_year = max(ydata, key=lambda t: t[1])
    return max_type, min_type, max_year


def show_results():
    """ print/show findings you user """


def lord_func():
    """ the start function """

    the_path = '/home/chris/proj/my_crime/data'
    dirt_file = open_file(get_data(the_path))
    clean_data, years, header = prosses_data(dirt_file)
    mtype, mintype, myear = calculate_data(clean_data, years)


if __name__ == "__main__":
    lord_func()
