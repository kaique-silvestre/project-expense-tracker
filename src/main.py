import argparse

from controller.json_operations import JsonOperations
from controller.add import Add
from controller.delete import Delete
from controller.update import Update
from controller.read import Read
from controller.budget import Budget
from controller.export import Export
from controller.validation import Validation

Val = Validation()
parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest="command")

# ADD SUBPARSER
subparser_add = subparser.add_parser("add", help="Add a new transaction with a specified amount, category, date, and description.")
subparser_add.add_argument("amount", type=float, help="The monetary float amount of the transaction.")
subparser_add.add_argument("-c", "--category", type=str, default=None, help="The category of the transaction (food, transport, salary).")
subparser_add.add_argument("-D", "--date", type=str, default=None, help="The date of the transaction in DD-MM-YYYY format. Defaults to today's date if not provided.")
subparser_add.add_argument("-d", "--description", type=str, default=None, help="A short optional description or note about the transaction.")

# DELETE SUPARSER
subparser_delete = subparser.add_parser("delete", help="It deletes registers from the database using provided ID(s)")
subparser_delete.add_argument("id", type=int, nargs="+", help="Integer that uniquely identifies every register")

# CLEAR SUBPARSER 
subparser_clear = subparser.add_parser("clear", help="Using the clear command will overwrites the current database with an empty one")

# LIST SUBPARSER
subparser_list = subparser.add_parser("list", help="Use this command to view all registered expenses. You can also filter a custom view of the data using the arguments. The arguments will be introduced with the explanation of their use.")
subparser_list.add_argument("--id", type=int, nargs="+", help="Use this command to view all registered expenses. You can also filter a custom view of the data using the arguments.")
subparser_list.add_argument("-y","--year", type=int, nargs="+", help="Only shows the expenses of the given year(s)")
subparser_list.add_argument("-m","--month", type=int, nargs="+", help="Only shows the expenses of the given month(s)")
subparser_list.add_argument("-c", "--category", type=str, help="Only shows the expenses of the given category(ies)")
subparser_list.add_argument("-l", "--less", type=int, help=" Only shows the expenses below the given value")
subparser_list.add_argument("-g", "--greater", type=int, help="Only shows the expenses greater than the given value")
subparser_list.add_argument("-a", "--amount", type=int, help="Only shows the expense correspoding exactly to the given value")
subparser_list.add_argument("-s", "--summary", action="store_const", const=True, help="It show with the view the total amount of the filtered expanses and the quantity of showing registers")

# BUDGET SUBPARSER
budget_parser = subparser.add_parser("budget", help="Budget has three subcommands: set, delete, and list. With budget, you may define a monthly budget for the actual year")

subparser_budget = budget_parser.add_subparsers(dest="command_budget")

# BUDGET SUBPARSER -- SET
budget_set = subparser_budget.add_parser("set", help="It is used for setting an max spending amount for a month.")
budget_set.add_argument("value", type=int, help="Float representing the value of an expense")
budget_set.add_argument("month", type=int, help="Integer between 1 and 12 representing a month")

# BUDGET SUBPARSER -- DELETE
budget_remove = subparser_budget.add_parser("delete")
budget_remove.add_argument("month", type=int, nargs="+", help="It\'s used to delete a previus budget set for a month, it's possible to delete more than one in the same command")

# BUDGET SUBPARSER -- LIST
budget_list = subparser_budget.add_parser("list")
budget_list.add_argument("-m", "--month", type=int, nargs="+", help="Used to return a view in the terminal about all months and its budget even if it is not set, it will show as null")

# UPDATE SUBPARSER  
subparser_update = subparser.add_parser("update")
subparser_update.add_argument("id", type=int, nargs="+", help="Integer that uniquely identifies every register.")
subparser_update.add_argument("-a", "--amount", type=float, help="Float representing the value of an expense")
subparser_update.add_argument("-d", "--description", type=str, help="stored as string in the format DD-MM-YYYY, by default it will be current date on the OS system, it is validated as a datetime class ")
subparser_update.add_argument("-D", "--date", type=str, help="A string representing a category the user may provide ")
subparser_update.add_argument("-c", "--category", type=str, help="A string representing a description to the expense that the user may provide")

# Export 
subparser_export = subparser.add_parser("export", help="export a file containing the filtered expenses. By default, the CSV file will be saved in the Desktop folder. Otherwise, you can define a valid folder path in '--folder' and it will be saved there.")
subparser_export.add_argument("file", type=str, help="Required string argument that will be the name of the file.")
subparser_export.add_argument("--folder", type=str, help="string that should be a valid folder path to store the CSV file.")
subparser_export.add_argument("--id", nargs="+", type=int, help="It will show only the given id, one or more.")
subparser_export.add_argument("-y","--year", nargs="+", type=int, help="It will show only the given year, one or more.")
subparser_export.add_argument("-m","--month", nargs="+", type=int, help="It will show only the given month, one or more.")
subparser_export.add_argument("-c", "--category", type=str, help="It will show only the given category.")
subparser_export.add_argument("-l", "--less", type=int, help="It will show all the values that are less than the given value.")
subparser_export.add_argument("-g", "--greater", type=int, help="It will show all the values that are greater than the given value.")
subparser_export.add_argument("-a", "--amount", type=int, help="It will show all the values that are equal to the given value.")



args = parser.parse_args()

JsonOperations.creation()

database = JsonOperations.return_json(JsonOperations.DATABASE_FILE)


match args.command:
    case "add":
        Val.add_validation(args)
        Add.add(database, args)
    case "update":
        Val.update_validation(args)
        Update.update(database, args)
    case "delete":  
        Val.delete_validation(args)
        Delete.delete(database, args)
    case "list":
        Read.list_flow(database, args)
    case "clear":
        JsonOperations.send_json(JsonOperations.DATABASE_FILE, [])
        print("\n# Successfully cleared spends database.\n")
    case "export":
        Val.list_validation(args)
        Export.csv_export_flow(database, args)

if 'command_budget' in args:
    budget_database = JsonOperations.return_json(JsonOperations.BUDGET_FILE) 
    match args.command_budget:
        case "set":
            Val.budget_set_validation(args)
            Budget.set_budget(budget_database, args)
        case "list":
            Budget.list_budget(budget_database, args)
        case "delete":
            Val.budget_delete_validation(args)
            Budget.delete_budget(budget_database, args) 
