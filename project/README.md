# Bankify
    #### Video Demo:  https://youtu.be/fTnxsnlw-Pc
    #### Description: program to categorise operations from a csv file from a bank account

## Description
welcome to Bankify!

This program aim to analyse datas from a csv file from a bank account and categorize operations so we can have some stats

The csv file to analyse has to be in a very specific format (you can find a sample in util folder):
header:
Date,Unique Id,Tran Type,Cheque Number,Payee,Memo,Amount

And then each row represent an operation:
2022/08/18,2022081802,DEBIT,,"DEBIT","CARD 7152 COUNTDOWN FE RRYMEAD CHRISTCHURCH",-36.45

The program also works with a dictionnary (json format); if none provided, the default one will be used (util/categories.json)
At first the dictionnary is empty but as we'll see later, the program allows the user to add categories and keywords associated to the dictionnary.
The repetitive operations will be categorised automatically in the future:

For example, if you have an operation like this one:

2022/08/18,2022081802,DEBIT,,"DEBIT","CARD 7152 COUNTDOWN FE RRYMEAD CHRISTCHURCH",-36.45

if no keyword is found in the "memo" field, the user will be prompt to add a categoy; if yes he will be asked a new category (in this case "groceries") ans a keyword (in this case "countdown")which is the name of the supermarket)
The operation will be added a category "groceries" and all other operations in the csv file with the keyword "countdown" will be automatically marked as groceries.

When all lines are categorised, the program wiil print the total of every categories.

## Usage:
python project.py -f file.csv -d file.json
optionnal: --R to reset the json file (empty)

Enter the informations when prompted

The stats will be printed when all the operations are "categorised"

## How it works

- first we need to get arguments from the command line with the function get_args() where we parse the arguments and return them

- then we do a class instance of "Categories" with the json file we got from the argument; this cals has an error catch in the init fonction, has a dict property and several functions: add_category(), add_keyword(), save_file() and reset()

- once the instance of Categories is created and stored in the variable categories, we can check the arguments from the command line as if there is no csv file specified, if there is the rest command (--R) and the csv extension. The format of the csv file will be checked after in the clean_data() function.

- with the csv_to_list() function, we open the csv file and parse it with the DictReader method from csv lib. The function return a list with a dictionnary for every row with the header as keys:
[{'date': '...', 'Unique Id': '...', 'Tran Type':'...', 'Cheque Number':'...', 'Payee':'...', 'Memo':'...', 'Amount':'...'},{...},{...}]

- the function clean_data() is to remove some useless keys as 'Unique Id', 'Cheque number' etc..., lower the 'Memo' value, float the 'Amount' value and use the class Operation to return a list of Operation instances. The result is stored in 'opearions_list' variable in main()

- then we add all known categories according to the jsons file used with function add_categorie(). A new key/value is added ('categorie' : ''). If the 'memo' field is blank, the default 'unknown' categorie is added.

- the learn() function will prompt the user for each line where no keyword from any categories is found. The user has the possibility to add a new category, and then add the most relevant keyword found in the memo field so if the keyword is found in another operation, the operation will be added the category automatically. This is done using the class methods add_category(), add_keyword() and the json dictionnary file is updated with the save_file() method.

Finally the get_stats() function prints out the sum of each category.



