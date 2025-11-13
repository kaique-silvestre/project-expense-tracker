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
subparser_add.add_argument("amount", type=float, help="The monetary amount of the transaction. Use negative values for expenses and positive for income.")
subparser_add.add_argument("-c", "--category", type=str, default=None, help="The category of the transaction (e.g., food, transport, salary).")
subparser_add.add_argument("-D", "--date", type=str, default=None, help="The date of the transaction in DD-MM-YYYY format. Defaults to today's date if not provided.")
subparser_add.add_argument("-d", "--description", type=str, default=None, help="A short optional description or note about the transaction.")

# DELETE SUPARSER
subparser_delete = subparser.add_parser("delete", help="")
subparser_delete.add_argument("id", type=int, nargs="+", help="")

# CLEAR SUBPARSER 
subparser_clear = subparser.add_parser("clear", help="")

# LIST SUBPARSER
subparser_list = subparser.add_parser("list")
subparser_list.add_argument("-y","--year", type=int, help="")
subparser_list.add_argument("-m","--month", type=int, help="")
subparser_list.add_argument("-c", "--category", type=str, help="")
subparser_list.add_argument("-l", "--less", type=int, help="")
subparser_list.add_argument("-g", "--greater", type=int, help="")
subparser_list.add_argument("-a", "--amount", type=int, help="")
subparser_list.add_argument("-s", "--summary", action="store_const", const=True, help="")
subparser_list.add_argument("-e", "--export", action="store_const", const=True, help="")

# BUDGET SUBPARSER
budget_parser = subparser.add_parser("budget")

subparser_budget = budget_parser.add_subparsers(dest="command_budget")

# BUDGET SUBPARSER -- SET
budget_set = subparser_budget.add_parser("set")
budget_set.add_argument("value", type=int, help="")
budget_set.add_argument("month", type=int, help="")

# BUDGET SUBPARSER -- DELETE
budget_remove = subparser_budget.add_parser("delete")
budget_remove.add_argument("month", type=int, nargs="+", help="")

# BUDGET SUBPARSER -- LIST
budget_list = subparser_budget.add_parser("list")
budget_list.add_argument("-m", "--month", type=int, nargs="+", help="",)

# UPDATE SUBPARSER  
subparser_update = subparser.add_parser("update")
subparser_update.add_argument("id", type=int, nargs="+", help="")
subparser_update.add_argument("-a", "--amount", type=float, help="")
subparser_update.add_argument("-d", "--description", type=str, help="")
subparser_update.add_argument("-D", "--date", type=str, help="")
subparser_update.add_argument("-c", "--category", type=str, help="")

# Export 
subparser_export = subparser.add_parser("export")
subparser_export.add_argument("file")
subparser_export.add_argument("--folder")
subparser_export.add_argument("-y","--year", type=int, help="")
subparser_export.add_argument("-m","--month", type=int, help="")
subparser_export.add_argument("-c", "--category", type=str, help="")
subparser_export.add_argument("-l", "--less", type=int, help="")
subparser_export.add_argument("-g", "--greater", type=int, help="")
subparser_export.add_argument("-a", "--amount", type=int, help="")



args = parser.parse_args()

JsonOperations.creation()

database = JsonOperations.return_json(JsonOperations.DATABASE_FILE)


if args.command == "add":

    Val.add_validation(args)
    Add.add(database, args)

elif args.command == "delete": 

    Val.delete_validation(args)
    Delete.delete(database, args)

elif args.command == "update": 

    Val.update_validation(args)
    Update.update(database, args)
    
elif args.command == "list":

    Val.list_validation(args)
    Read.filter(database, args)

elif args.command == "clear": 

    JsonOperations.send_json(JsonOperations.DATABASE_FILE, [])
    print("\n# Successfully cleared spends database.\n")

elif args.command == "export":

    Val.list_validation(args)
    Export.csv_export_flow(database, args)

elif args.command == "budget":
    budget_database = JsonOperations.return_json(JsonOperations.BUDGET_FILE) 
    
    if args.command_budget == "set":
        
        Val.budget_set_validation(args)
        Budget.set_budget(budget_database, args) 

    elif args.command_budget == "list":

        Budget.list_budget(budget_database, args)
    
    elif args.command_budget == "delete":

        Val.budget_delete_validation(args)
        Budget.delete_budget(budget_database, args) 


