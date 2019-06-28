import os
import glob

import csv

def read_csv(filepath):
    if not filepath:
        return
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        #headers = list(row.keys())
        res = {}
        for row in reader:
            headers = list(row.keys())
            for h in headers:
                if row[h]:
                    if h in res:
                        res[h].append(row[h])
                    else:
                        res[h] = [row[h]]
        return res


if __name__ == "__main__":
    d = read_csv('color.csv')
    for key,value in d.items():
        print(key, tuple(value))
    print(d)