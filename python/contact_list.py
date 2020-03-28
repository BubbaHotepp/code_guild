import csv
import collections

def main():
    with open('contacts.csv') as csv_file:
        reader = csv.DictReader(csv_file)
        contact_list = [r for r in reader]
        x = 0
        y = 0
        for rows in reader:
            y = rows
        print(y)
        dict_list = []
        while x <= y:
            for i in contact_list:
                dict_list.append(dict(collections.OrderedDict(i)))
            x += 1
        print(dict_list)
        

main()