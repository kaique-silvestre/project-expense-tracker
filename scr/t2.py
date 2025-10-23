import argparse
import pathlib

from json_operations import JsonOperations
from validations import Validation
from add import Add
from delete import Delete
from update import Update
from read import Read

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



if args.command == "add":
    Add.add(JSON_FILE, database, args)
elif args.command == "delete":
    Delete.delete(JSON_FILE, database, args)
elif args.command == "list":
    Read.list(database)
elif args.command == "clear":
    JsonOperations.send_json(JSON_FILE, [])
elif args.command == "update":
    Update.update(JSON_FILE, database, args)