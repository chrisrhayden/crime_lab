# make a crime thing


import os
import csv
from itertools import groupby


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


def prosses_data(data: list) -> list:
    """ val, clean and trans """
    header = data[0]
    body = data[1:]
    # row[1] is 00/00/0000
    crime_date = []
    # row[3] is type ie larceny
    crime_type = []

    crimes = [(cri[1], cri[3]) for cri in body]
    print(crimes)

    crimes.sort()
    new_crime = groupby(crimes, key=lambda t: t[1])
    print(list(new_crime))


    return crimes


def lord_func():
    """ the start function """

    the_path = '/home/chris/proj/my_crime/data'
    dirt_file = open_file(get_data(the_path))
    clean_data = prosses_data(dirt_file)
    #print(clean_data)


if __name__ == "__main__":
    lord_func()
