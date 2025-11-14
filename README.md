github: https://github.com/kaique-silvestre/project-expense-tracker
# Expanse Tracker 

## About the Project

This project is called "expense-tracker" a challenge proposed by: [roadmap.sh](https://roadmap.sh/projects/expense-tracker)

This application allows the user to track their spends. It is a classic CRUD with the data being stored in a JSON file. You can: Add, delete, update, set monthly budgets, list and export (both with filters)

you can also define a monthly budget to each month of the actual year, if you spend more than expected you will be notified

An expense is composed of the following data: 
ID -- It's an integer that identifies every single expense, It will never be Null or less than zero and cannot be modified by the user by CLI
AMOUNT -- Float number that represents the spend value, It will never be Null or less than zero
DATE -- A datetime class, represents when the spends were made by default is the actual date of the system
CATEGORY -- A string represiting a category for the spend, you can write anything (Ex: Food, Car, House, grocery), It can be null and it's case sensitive and the max lentgh is 20
DESCRIPTION -- A string represiting a description for the spend, you can write anything (Ex: Fast food, party with friends), It can be null and it's case sensitive and the max lentgh is 100

## What are the Commands?

### add

it saves an expense in the database

The arguments are:
<ul>
<li>amount: required<br/>
<li>-D, --date<br>
<li>-c, --category<br/>
<li> -d, --description
</ul>



What you cannot do: 
- Amount cannot be zero, negative or null and cannot be more than 1_000_000_000
- Date MUST have the correct format: DD-MM-YYYY otherwise an exception will be raised
- category cannot have a len higher than 20
- description cannot have a len higher than 100


- add 1000 <br/>
<code>{ id": 1, "amount": 1000.0, "category": null, "date": "13/11/2025", "description": null }<code/>

- add 1000 -c Food -d "A hotdog bought in the store"
>>> { id": 2, "amount": 1000.0, "category": "Food", "date": "13/11/2025", "description": "A hotdog bought in the store" }

- add 1000 -c Food -d "A hotdog bought in the store" -D 22/10/2020
>>> { id": 2, "amount": 1000.0, "category": "Food", "date": "22/10/2020", "description": "A hotdog bought in the store" }

### delete

The command will uses the ID to delete the data from the datase
You can type as much IDs as you want 

What you cannot do:
- The id cannot be negative, zero or null

The argumnets are:
id: required, one or more values

- delete 1

- delete 10 12 13

### update 

with update you can make changes in the stored data
you can modify one or more at the same time 

id: required
amount: -a, --amount 
date: -D, --date
category: -c, --category
description: -d, --description

Example:

- add 5000 
>>> {"id": 1, "amount": 5000.0, "category": null, "date": "13/11/2025", "description": null}

Opsss we forgot to add category and description... look who update works:

- update 1 -c Eletronic -d "pc components"

>>> {"id": 1, "amount": 5000.0, "category": "Eletronic", "date": "13/11/2025", "description": "pc components"}

It's possible to change all arguments or just one, and also possible to apply the same changes for more than one ID

- update 1 2 3 6 9 12 15 20 -c House 

What you cannot do: 
- ID  cannot be zero, negative or null
- Amount cannot be zero, negative or null and cannot be more than 1_000_000_000
- Date MUST have the correct format: DD-MM-YYYY otherwise an exception will be raised
- category cannot have a len higher than 20
- description cannot have a len higher than 100

### list

Use this command to view all registered expenses. But you can also filter a custom view of the data. the arguments will be introduced with the explanation of its use

--id
    - it will show only the given id, one or more
-y, --year
    - It will show only the given year, one or more 
-m, --month
    - It will show only the given month, one or more 
-c, --category
    - It will show only the given category, (for now it is only possible one argument, but i think it is possible to improve the program to it understand different cattegories divided by comma; Ex: "Food, Eletronic")
-l, --less
    - It will show all the values that are less than the given value
-g, --greater
        - It will show all the values that are greater than the given value
-a, --amount
            - It will show all the values that are equal to the given value
-s, summary
    - It shows bellow the spend view the summary: How much spends were registered and the sum of all spends in the view

### clear

This comamnd will clear the database -- JSON file

- clear

### export 

Using this command you can export a CSV file with the spending, it's possible also to export using filters

By default the CSV file will be saved in the Desktop folder, otherwise you can define a valid folder path in "--folder" and it will be save in 


file 
    - Required string argument that will be the name of the file 
--folder 
    - String that should be a valid folder path to stores the CSV file
--id
    - it will show only the given id, one or more
-y, --year
    - It will show only the given year, one or more 
-m, --month
    - It will show only the given month, one or more 
-c, --category
    - It will show only the given category, (for now it is only possible one argument, but i think it is possible to improve the program to it understand different cattegories divided by comma; Ex: "Food, Eletronic")
-l, --less
    - It will show all the values that are less than the given value
-g, --greater
        - It will show all the values that are greater than the given value
-a, --amount
            - It will show all the values that are equal to the given value

### budget

Budget has three subcommands: set, delete and list

With budget you may define a monthly budget for th actual year

### set

It's used for setting an amount for a month 

If your spends for the month get

The arguments are:

amount: required 

month: required 

