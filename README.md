# EXPENSE TRACKER

GitHub: https://github.com/kaique-silvestre/project-expense-tracker

This project was developed using two of my own GitHub accounts.


# ABOUT THE PROJECT

This project is called "expense-tracker," a challenge proposed by: roadmap.sh

CLI tool in Python using argparse for managing expenses and monthly budgets, with JSON storage; it allows adding expenses with category, description, and date, performing all CRUD operations such as update, delete, and read, and it is also possible to apply advanced filters to visualize and export data to CSV.

There are a lot of arguments used representing the data that composes an expense, their explanation are below, we won't be explaning them again.


An expense is a dictionary composed of the following data:
* <code>ID</code>: Integer that uniquely identifies every register.
* <code>AMOUNT</code>: Float representing the value of an expense
* <code>DATE</code>: stored as string in the format DD-MM-YYYY, by default it will be current date on the OS system, it is validated as a datetime class 
* <code>CATEGORY</code>: A string representing a category the user may provide 
* <code>DESCRIPTION</code>: A string representing a description to the expense that the user may provide



## WHAT ARE THE COMMANDS?

### ADD

**Description:**

It saves a new expense in the database.

**Arguments:**

* <code>amount</code> (required)
* <code>-D, --date</code>
* <code>-c, --category</code>
* <code>-d, --description</code>

**Validation Rules:**

* Amount cannot be zero, negative or null and cannot be more than 1,000,000,000.
* Date MUST have the correct format: DD-MM-YYYY, otherwise an exception will be raised.
* Category cannot have a length higher than 20.
* Description cannot have a length higher than 100.

**Syntax:**
```
expense-tracker add [amount] [--date] [--category] [--description]
```

**Examples:**

```
expense-tracker add 1000
expense-tracker add 1000 -c Food -d "A hotdog bought in the store"
expense-tracker add 1000 -c Food -d "A hotdog bought in the store" -D 22/10/2020
```

---

### DELETE

**Description:**

It deletes registers from the database using provided ID(s)

**Arguments:**

* <code>id</code>: (required)

**Validation Rules:**

 The ID must be greater than zero.

**Syntax:**
```
expense-tracker delete [id+]
```
**Example**:
```
expense-tracker delete 1
expense-tracker delete 10 12 13
```
---
### UPDATE

**Description:**

With update, you can make changes in the stored data. You can modify one or more at the same time.

**Arguments:**

* <code>id</code> (required)
* <code>amount</code>: -a, --amount
* <code>date</code>: -D, --date
* <code>category</code>: -c, --category
* <code>description: -d</code>, --description

**Syntax:**
```
expense-tracker update [id+] [--amount] [--date] [--category] [--description]
```
**Example:**
```
expense-tracker update 1 -c Eletronic -d "pc components"

expense-tracker update 1 2 3 6 9 12 15 20 -c House
```

**validation Rules:** ID cannot be zero, negative, or null.
* Amount cannot be zero, negative, or null and cannot be more than 1,000,000,000.
* Date MUST have the correct format: DD-MM-YYYY, otherwise an exception will be raised.
* Category cannot have a length higher than 20.
* Description cannot have a length higher than 100.

---

### LIST
**Description:**

Use this command to view all registered expenses. You can also filter a custom view of the data using the arguments. The arguments will be introduced with the explanation of their use.

**Arguments:**

* <code>--id</code>: Only shows the expense of the given ID(s).
* <code>-y, --year</code>: Only shows the expenses of the given year(s)
* <code>-m, --month</code>: Only shows the expenses of the given month(s)
* <code>-c, --category</code>: Only shows the expenses of the given category(ies)
* <code>-l, --less</code>: Only shows the expenses below the given value
* <code>-g, --greater</code>: Only shows the expenses greater than the given value
* <code>-a, --amount</code>: Only shows the expense correspoding exactly to the given value
* <code>-s, --summary</code>: It show with the view the total amount of the filtered expanses and the quantity of showing registers

**Syntax:**
```
expense tarcker list [--id+] [--year+] [month+] [--category+] [--less] [--greater] [--amount] [--summary]
```
**Example:**
```
expense-tracker list --id 1 2 3
expense-tracker list -y 2025 2024 -m 10 11 12
expense-tracker list -y 2025 2024 -m 10 11 12
expense-tracker list -c House -a 100
expense-tracker list -g 100 -l 1000 --summary
```
---

### CLEAR

**Description:**

Using the clear command will overwrites the current database with an empty one (<code>[]</code>)

**Example:**
```
expense-tracker clear
```

---

### EXPORT

**Description:**

Using "export" command will export a file containing the filtered expenses

By default, the CSV file will be saved in the Desktop folder. Otherwise, you can define a valid folder path in "--folder" and it will be saved there.

**Arguments:**


* <code>file</code>: Required string argument that will be the name of the file.
* <code>--folder</code>: String that should be a valid folder path to store the CSV file.
* <code>--id</code>: It will show only the given id, one or more.
* <code>-y, --year</code>: It will show only the given year, one or more.
* <code>-m, --month</code>: It will show only the given month, one or more.
* <code>-c, --category</code>: It will show only the given category.
* <code>-l, --less</code>: It will show all the values that are less than the given value.
* <code>-g, --greater</code>: It will show all the values that are greater than the given value.
* <code>-a, --amount</code>: It will show all the values that are equal to the given value.

**Syntax:**
```
expense-tracker export [file] [--folder] [--id+] [--year+] [month+] [--category] [--less] [--greater] [--amount] 
```
**Example:**
```
expense-tracker export file
expense-tracker export file --folder "Home/folder/folder1"
expense-tracker export file -y 2025 2024 -m 10 11 12
```
---

### BUDGET

**Description:**


Budget has three subcommands: set, delete, and list.
With budget, you may define a monthly budget for the actual year.

#### SET

**Description:**


It's used for setting an max spending amount for a month.

**Arguments:**
* <code>amount</code> (required)
* <code>month</code> (required): Integer between 1 and 12 representing a month

**syntax:**
```
expense-tracker budget set [amount] [month]
```
**example:**
```
expense-tracker budget set 1000 12
```

#### DELETE

**description:**

It's used to delete a previus budget set for a month, it's possible to delete more than one in the same command

**arguments:**

* <code>id</code>: required
**syntax:**
```
expense-tracker budget delete [id+]
```
**example:**
```
expense-tracker budget delete 1
expense-tracker budget delete 1 2 3 4 5 6 7 8 9
```
#### LIST

**description:**

Used to return a view in the terminal about all months and its budget even if it is not set, it will show as null

**example:**
```
expense-tracker list
```

