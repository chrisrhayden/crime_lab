# make a crime thing


import os
import csv
import string
from collections import Counter
from typing import Iterable, List, Tuple
from itertools import groupby


Crimlist = Iterable[List[list]]


def get_data(path: str) -> str:
    """ get the data file """

    d_data = {i: n for i, n in enumerate(os.listdir(path), start=1)}
    for thi in d_data.items():
        print(thi)
    user_input = input('which file you need ')
    if user_input == 'a':
        return 'a'
    else:
        user_input = int(user_input)

    return os.path.join(path, d_data[user_input])


def all_files(apath: list):
        files = []
        for i in os.listdir(apath):
            if i.endswith('.csv'):
                files.append(os.path.join(apath, i))
        return files


def open_file(path: str) -> list:
    """ basic file handler

    open file then pass to csv reader
    """
    with open(path, 'r') as f:
        df = csv.reader(f)
        df = list(df)
    return df


def prosses_data(data: list) -> Tuple:
    """ val, clean and trans

    sepirate header and body
    count all instences of crimes
    count crimes in years
    """
    header = data[0]
    body = data[1:]
    # row[1] is 00/00/0000
    # row[3] is type ie larceny

    new_crimes = Counter(cri[3] for cri in body)    # get dict, key by count

    def helper(cr):                                 # helper func, by year
        return cr[1][-4:]

    lol_crime = sorted(body, key=helper)

    years = []
    # group by year, then count crimes[row] by year
    # adding total to years list
    for c, b in groupby(lol_crime, key=helper):
        years.append(list(Counter(cr[1][-4:] for cr in list(b)).items())[0])

    return new_crimes, years, header


def calculate_data(cdata: dict, ydata: list):
    """ get the prossesed data and do math

    find out highest crime year
    mosted commited crime and rareist
    """
    # list of dict, key instances count
    max_type = max(cdata.items(), key=lambda t: t[1])
    min_type = min(cdata.items(), key=lambda t: t[1])
    # dict by year, value by all crime instances's of year
    max_year = max(ydata, key=lambda t: t[1])
    return max_type, min_type, max_year


def calculate_all_data(maxtyp: list, mintyp: list, myear: list):
    """ get the prossesed data and do oon all

    """
    print(maxtyp, 'ma', mintyp, 'min', myear, 'my')
    max_type = max(maxtyp, key=lambda t: t[1])
    min_type = min(mintyp, key=lambda t: t[1])
    max_year = max(myear, key=lambda t: t[1])
    return max_type, min_type, max_year


def show_results(max_t: tuple, min_t: tuple, max_y: dict):
    """ print/show findings you user """
    print()
    print()
    print()
    print(f'the most commited crime is {max_t[0]} with {max_t[1]} instances')
    print()
    print(f'the least commited crime is {min_t[0]} with {min_t[1]} instances')
    print()
    print(f'{max_y[0]} was had the higest instences with {max_y[1]}')


def lord_func():
    """ the start function """

    the_path = '/home/chris/proj/my_crime/data'
    dat_path = get_data(the_path)

    if dat_path == 'a':
        alist = all_files(the_path)
        all_mtype = []
        all_mintype = []
        all_myear = []
        for a_file in alist:
            dirt_file = open_file(a_file)
            clean_data, years, header = prosses_data(dirt_file)
            mtype, mintype, myear = calculate_data(clean_data, years)
            all_mtype.append(mtype)
            all_mintype.append(mintype)
            all_myear.append(myear)
        all_mtype, all_mintype, all_myear = calculate_all_data(all_mtype,
                                                               all_mintype,
                                                               all_myear)
        show_results(all_mtype, all_mintype, all_myear)
    else:
        dirt_file = open_file(dat_path)
        clean_data, years, header = prosses_data(dirt_file)
        mtype, mintype, myear = calculate_data(clean_data, years)
        show_results(mtype, mintype, myear)


if __name__ == "__main__":
    lord_func()
