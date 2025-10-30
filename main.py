import argparse
import pathlib

from src.json_operations import JsonOperations
from src.validations import Validation
from src.add import Add
from src.delete import Delete
from src.update import Update
from src.read import Read
from src.budget import Budget


JSON_FILE = pathlib.Path(__file__).parent / "spendings.json"


parser = argparse.ArgumentParser()

subparser = parser.add_subparsers(dest="command")

# add subparser
subparser_add = subparser.add_parser("add", help="")
subparser_add.add_argument("amount", type=float, help="")
subparser_add.add_argument("-c", "--category", type=str, default=None, help="")
subparser_add.add_argument("-D", "--date", type=str, default=None, help="")
subparser_add.add_argument("-d", "--description", type=str, default=None, help="")

# delete subparser
subparser_delete = subparser.add_parser("delete", help="")
subparser_delete.add_argument("id", type=int, nargs="+", help="")

# clear
subparser_clear = subparser.add_parser("clear", help="")

# list subparser
subparser_list = subparser.add_parser("list")

# summary
subparser_summary = subparser.add_parser("summary")
summaries = subparser_summary.add_subparsers(dest="mode")

total_subparser = summaries.add_parser("total")
total_subparser.add_argument("-c", "--category")

year_subparser = summaries.add_parser("year")
year_subparser.add_argument("year", type=int)
year_subparser.add_argument("--month", type=int)



# Filter teste
subparser_filter = subparser.add_parser("filter")
subparser_filter.add_argument("-y","--year", type=int)
subparser_filter.add_argument("-m","--month", type=int)
subparser_filter.add_argument("-c", "--category")
subparser_filter.add_argument("-l", "--less", type=int)
subparser_filter.add_argument("-g", "--greater", type=int)
subparser_filter.add_argument("-a", "--amount", type=int)
subparser_filter.add_argument("-e", "--export", action="store_const", const=True )

# Budget
budget_parser = subparser.add_parser("budget")

subparser_budget = budget_parser.add_subparsers(dest="command_budget")

budget_set = subparser_budget.add_parser("set")
budget_set.add_argument("value")
budget_set.add_argument("month")

budget_view = subparser_budget.add_parser("view")
budget_view.add_argument("month")

budget_remove = subparser_budget.add_parser("remove")
budget_remove.add_argument("month")






# update subparser 
subparser_update = subparser.add_parser("update")
subparser_update.add_argument("id", type=int, nargs="+", help="")
subparser_update.add_argument("-a", "--amount", type=float)
subparser_update.add_argument("-d", "--description", type=str)
subparser_update.add_argument("-D", "--date", type=str)
subparser_update.add_argument("-c", "--category", type=str)

args = parser.parse_args()

JsonOperations.create(JSON_FILE)
database = JsonOperations.return_json(JSON_FILE)

print(args)


if args.command == "add":
    Validation.add_validation(args)
    Add.add(JSON_FILE, database, args)
elif args.command == "delete":
    Validation.delete_validation(args)
    Delete.delete(JSON_FILE, database, args)
elif args.command == "list":
    Read.list(database)
elif args.command == "clear":
    JsonOperations.send_json(JSON_FILE, [])
elif args.command == "update":
    Validation.update_validation(args)
    Update.update(JSON_FILE, database, args)
elif args.command == "summary":
    if args.mode == "total" or args.mode is None:
        Read.total_summary(database, args)
elif args.command == "filter":
    Read.filter(database, args)
elif args.command == "budget":
    if args.command_budget == "set":
        print("set")
        Budget.budget_set(JSON_FILE, database, args)
    elif args.command_budget == "view":
        print("view")
    elif args.command_budget == "remove":
        print("remove")