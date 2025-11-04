import argparse

from controller.json_operations import JsonOperations
from controller.add import Add


parser = argparse.ArgumentParser()

subparser = parser.add_subparsers(dest="command")

# ADD SUBPARSER
subparser_add = subparser.add_parser("add", help="")
subparser_add.add_argument("amount", type=float, help="")
subparser_add.add_argument("-c", "--category", type=str, default=None, help="")
subparser_add.add_argument("-D", "--date", type=str, default=None, help="")
subparser_add.add_argument("-d", "--description", type=str, default=None, help="")

# DELETE SUPARSER
subparser_delete = subparser.add_parser("delete", help="")
subparser_delete.add_argument("id", type=int, nargs="+", help="")

# CLEAR SUBPARSER
subparser_clear = subparser.add_parser("clear", help="")

# LIST SUBPARSER
subparser_list = subparser.add_parser("list")

# SUMMARY SUBPARSER
subparser_summary = subparser.add_parser("summary")
summaries = subparser_summary.add_subparsers(dest="mode")

total_subparser = summaries.add_parser("total")
total_subparser.add_argument("-c", "--category")

year_subparser = summaries.add_parser("year")
year_subparser.add_argument("year", type=int)
year_subparser.add_argument("--month", type=int)



# FILTER SUBPARSER
subparser_filter = subparser.add_parser("filter")
subparser_filter.add_argument("-y","--year", type=int)
subparser_filter.add_argument("-m","--month", type=int)
subparser_filter.add_argument("-c", "--category")
subparser_filter.add_argument("-l", "--less", type=int)
subparser_filter.add_argument("-g", "--greater", type=int)
subparser_filter.add_argument("-a", "--amount", type=int)
subparser_filter.add_argument("-e", "--export", action="store_const", const=True )

# BUDGET SUBPARSER
budget_parser = subparser.add_parser("budget")

subparser_budget = budget_parser.add_subparsers(dest="command_budget")

# BUDGET SUBPARSER -- SET
budget_set = subparser_budget.add_parser("set")
budget_set.add_argument("value")
budget_set.add_argument("month")

# BUDGET SUBPARSER -- VIEW
budget_view = subparser_budget.add_parser("view")
budget_view.add_argument("month")

# BUDGET SUBPARSER -- REMOVE
budget_remove = subparser_budget.add_parser("remove")
budget_remove.add_argument("month")

# UPDATE SUBPARSER  
subparser_update = subparser.add_parser("update")
subparser_update.add_argument("id", type=int, nargs="+", help="")
subparser_update.add_argument("-a", "--amount", type=float)
subparser_update.add_argument("-d", "--description", type=str)
subparser_update.add_argument("-D", "--date", type=str)
subparser_update.add_argument("-c", "--category", type=str)

args = parser.parse_args()

json_database = JsonOperations()

Add = Add()

if args.command == "add":
    Add.add(json_database.DATABASE_FILE, args)
