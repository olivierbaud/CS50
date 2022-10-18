import csv
import json
import argparse
import sys
import os
import pprint

class Categories:
    def __init__(self,json_file):
        try:
            with open(json_file) as file:
                self._dict = json.load(file)
            self.jsonfile = json_file
        except FileNotFoundError:
            sys.exit("File not found")

    @property
    def dict(self):
        return self._dict

    def add_category(self, category):
        self._dict.update({category:[]})

    def add_keyword(self, category, keyword):
        self._dict[category].append(keyword)

    def save_file(self):
        with open(self.jsonfile, "w") as outfile:
            json.dump(self.dict, outfile)

    def reset(self):
        empty = {}
        with open(self.jsonfile, "w") as outfile:
            json.dump(empty, outfile)

class Operation:
    def __init__(self, Date, Type, Memo, Amount, Category=None):
        self.date = Date
        self.type = Type
        self.memo = Memo
        self.amount = Amount
        self.category = Category

    def __repr__(self):
        return f"{self.date}, {self.type}, {self.memo}, {self.category}, {self.amount}"

def main():
    args = get_args()
    dict_json = f"util/{args.d}"
    categories = Categories(dict_json)
    check_args(args, categories)
    operations_list = clean_data(csv_to_list(args.f))
    categorised = learn(add_category(operations_list, categories.dict), categories)
    pprint.pprint (get_stats(categorised, categories))

def get_args():
    parser = argparse.ArgumentParser(description="statistics from a bank csv file")
    parser.add_argument("-f", help="csv file from the bank", type=str)
    parser.add_argument("-d", help="Json file for categories", type=str, default="categories.json")
    parser.add_argument("--R",action='store_true')
    return parser.parse_args()

def check_args(args, categories):
    """
    check the arguments from the command line as if there is no csv file specified, if there is the rest command (--R) and the csv extension
    :param args: argparse instance
    :type args: object
    :param categories: Categories instance
    :type categories: object
    """
    if args.f == None:
        sys.exit("PLease specify a valid csv file, type -h for help")
    if args.R:
        categories.reset()
        sys.exit("categories file reset")
    if os.path.splitext(args.f)[1] != ".csv":
        sys.exit("Please specify a CSV file")

def csv_to_list(f):
    """
    data format: [{'date': '', 'Unique Id': '',...},{},{}]
    :param f: json file path
    :type f: string
    :return: list from csv file with each line as dictionnary with keys from header and value from lines
    """
    money = []
    with open(f) as file:
        reader = csv.DictReader(file)
        for row in reader:
            money.append(row)
    return money

def clean_data(l):
    """
    Function to clean the data entry: : some keys removed, key category added etc...
    : param l: list of operations (from csv file)
    : type l: list of dictionnaries
    : return: list operations, each operations passed through the Operation class
    """
    try:
        clean = []
        for row in l:
            row.pop('Unique Id')
            row.pop('Cheque Number')
            row.pop('Payee')
            row["Memo"] = row["Memo"].lower()
            row["Type"] = row.pop('Tran Type') # rename the key Tan Type to Type
            row["Amount"] = float(row["Amount"])
            clean.append(Operation(**row))
        return clean
    except KeyError:
        sys.exit("wrong csv format, consult readme.md")

def add_category(l, categories):
    """
    add category in the row of the operation list (l argument) if it' s in the dictionnary provided (categories argument)
    :param l: operation list from clean_data()
    :type l: list
    :param categories: property dict from instance of Categories class
    :type categories: dictionnary
    :return: list with added key/value if found in categories
    """
    for row in l:
        if row.memo == "":  # set category to unknown if memo field is blank
            row.category = "unknown"
        for key in categories:
            for word in categories[key]:
                if word in row.memo:
                    row.category = key
    return l

def learn(l, c):
    """
    This function takes a list of dictionnaries (operations), a categories dictionnary and a json file to update
    For operations without category, the user is prompt to choose one and add a Keyword associated to the dictionnary (idealy present in the memo of the operation)
    :param l: list of all operations [{},]
    :type l: list
    :param c: instance of Categories class
    :type c: Categories object
    :return: list of operations with categories added
    """
    for row in l:
        keys = (sorted(c.dict.keys())) # keys from categories dictionnary
        add_category(l, c.dict) # check if the new line has a new keyword/category
        if not row.category: # if no category in the operation
            print(f"\n{row}\n") # print the complete operation
            print("Please choose a category:\n",*keys,"\n", sep=" -- ") # prompt the user with existing categories
            manual_category = input(f"categorie? \n")
            if manual_category and manual_category in keys: # if the category does match an axisting category, assign the category to the operation
                row.category = manual_category
                manual_keyword = input("Keyword? ") # prompt the user to add a keyword to the category in the dictionary
                if manual_keyword != "":
                    c.add_keyword(manual_category,manual_keyword)
                    c.save_file() # save json file with new keyword
            else:
                while True:
                    prompt = input("not an existing category, do you want to add one? ").lower() # if the category entered doesn't match to any category in the dictionary, offer to create a new one
                    if prompt == "yes" or prompt == "y":
                        new_cat = input("New category: ")
                        c.add_category(new_cat) # add new category to the category object
                        c.add_keyword(new_cat, input("Keyword?: ")) # add new keyword to the obbject
                        c.save_file()
                        break
                    elif prompt == "no" or prompt == "n":
                        break
                    else:
                        continue
    return l

def get_stats(f, c):
    """
    Get total from each categories
    :param f: list of all operations
    :type f: list
    :param c: Categories instance
    :type c: Categories object
    :return: dictionnary {"category": total,...}
    """
    print(f)
    stats = {}
    for key in c.dict: # create dictionnary with same keys as the categories dictionnary and a list as value
        stats[key] = []
    for row in f: # parse each row and add the amount in the list value of the category
        if row.category:
            stats[row.category].append(row.amount)
    for i in stats:
        stats[i] = "{:.2f}".format(sum(stats[i]))
    return stats

if __name__ == "__main__":
    main()