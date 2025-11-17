# EXPENSE TRACKER

GitHub: https://github.com/kaique-silvestre/project-expense-tracker

---

# ABOUT THE PROJECT

This project is called "expense-tracker," a challenge proposed by: roadmap.sh <!--Adicionar link-->

CLI tool in Python using argparse for managing expenses and monthly budgets, with JSON storage; it allows adding expenses with category, description, and date, performing all CRUD operations such as update, delete, and read, and it is also possible to apply advanced filters to visualize and export data to CSV.

An expense is a dictionary composed of the following data:
* ID: It's an integer that identifies every single expense. It will never be Null or less than zero and cannot be modified by the user by CLI.
* AMOUNT: Float number that represents the spend value. It will never be Null or less than zero.
* DATE: A datetime class, represents when the spends were made. By default is the actual date of the system.
* CATEGORY: A string representing a category for the spend. You can write anything (Ex: Food, Car, House, grocery). It can be null, it's case sensitive, and the max length is 20.
* DESCRIPTION: A string representing a description for the spend. You can write anything (Ex: Fast food, party with friends). It can be null, it's case sensitive, and the max length is 100.



## WHAT ARE THE COMMANDS?

### ADD

It saves an expense in the database.

The arguments are:
* amount: required
* -D, --date
* -c, --category
* -d, --description

What you cannot do:
* Amount cannot be zero, negative or null and cannot be more than 1,000,000,000.
* Date MUST have the correct format: DD-MM-YYYY, otherwise an exception will be raised.
* Category cannot have a length higher than 20.
* Description cannot have a length higher than 100.

**Examples:**<br>

```
add 1000
add 1000 -c Food -d "A hotdog bought in the store"
add 1000 -c Food -d "A hotdog bought in the store" -D 22/10/2020
```

{ "id": 1, "amount": 1000.0, "category": null, "date": "13/11/2025", "description": null }



{ "id": 2, "amount": 1000.0, "category": "Food", "date": "13/11/2025", "description": "A hotdog bought in the store" }


{ "id": 2, "amount": 1000.0, "category": "Food", "date": "22/10/2020", "description": "A hotdog bought in the store" }

---

### DELETE

The command will use the ID to delete the data from the database. You can type as many IDs as you want.

The arguments are:
* id: required, one or more values

What you cannot do:
* The ID cannot be negative, zero, or null.

Examples:
```
delete 1
delete 10 12 13
```
---
### UPDATE

With update, you can make changes in the stored data. You can modify one or more at the same time.

* id: required
* amount: -a, --amount
* date: -D, --date
* category: -c, --category
* description: -d, --description

Example:
```
add 5000

# Opsss, we forgot to add category and description... look how update works:

update 1 -c Eletronic -d "pc components"

# It's possible to change all arguments or just one, and also possible to apply the same changes for more than one ID.

update 1 2 3 6 9 12 15 20 -c House


```
{"id": 1, "amount": 5000.0, "category": null, "date": "13/11/2025", "description": null}
{"id": 1, "amount": 5000.0, "category": "Eletronic", "date": "13/11/2025", "description": "pc components"}

What you cannot do:
* ID cannot be zero, negative, or null.
* Amount cannot be zero, negative, or null and cannot be more than 1,000,000,000.
* Date MUST have the correct format: DD-MM-YYYY, otherwise an exception will be raised.
* Category cannot have a length higher than 20.
* Description cannot have a length higher than 100.

---

### LIST

Use this command to view all registered expenses. But you can also filter a custom view of the data. The arguments will be introduced with the explanation of their use.
* --id: It will show only the given id, one or more.
* -y, --year: It will show only the given year, one or more.
* -m, --month: It will show only the given month, one or more.
* -c, --category: It will show only the given category (for now, it is only possible one argument, but I think it is possible to improve the program so it understands different categories divided by comma; Ex: "Food, Eletronic").
* -l, --less: It will show all the values that are less than the given value.
* -g, --greater: It will show all the values that are greater than the given value.
* -a, --amount: It will show all the values that are equal to the given value.
* -s, --summary: It shows below the spend view the summary: How much spends were registered and the sum of all spends in the view.

---

### CLEAR

This command will clear (It overwrites the old file with a new empty list <code>[]</code>)

```
clear
```

---

### EXPORT

Using this command, you can export a CSV file with the spending. It's possible also to export using filters.

By default, the CSV file will be saved in the Desktop folder. Otherwise, you can define a valid folder path in "--folder" and it will be saved there.

* file: Required string argument that will be the name of the file.
* --folder: String that should be a valid folder path to store the CSV file.
* --id: It will show only the given id, one or more.
* -y, --year: It will show only the given year, one or more.
* -m, --month: It will show only the given month, one or more.
* -c, --category: It will show only the given category (for now, it is only possible one argument, but I think it is possible to improve the program so it understands different categories divided by comma; Ex: "Food, Eletronic").
* -l, --less: It will show all the values that are less than the given value.
* -g, --greater: It will show all the values that are greater than the given value.
* -a, --amount: It will show all the values that are equal to the given value.

---

BUDGET

Budget has three subcommands: set, delete, and list.
With budget, you may define a monthly budget for the actual year.

SET

It's used for setting an amount for a month.
If your spends for the month get (The sentence is incomplete in the original text)

The arguments are:
* amount: required
* month: required
