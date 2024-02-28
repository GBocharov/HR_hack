import json
from schema import  DodikSet
import csv
from DataToRows import dset_to_dictList



with open('data/train.json', encoding='utf-8') as f:
    data = json.loads(f.read())

d = [DodikSet(**i) for i in data]
data_rows = dset_to_dictList(d)
with open('dataset.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['vacancy', 'resume', 'success']
    writer = csv.DictWriter(csvfile, delimiter=';', quotechar='|', fieldnames=fieldnames,quoting=csv.QUOTE_ALL)

    writer.writeheader()
    for row in data_rows:
        writer.writerow(row)