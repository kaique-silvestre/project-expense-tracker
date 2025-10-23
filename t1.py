import argparse
import json
import pathlib
import copy
from datetime import datetime


JSON_FILE = pathlib.Path(__file__).parent / "spendings.json"
DATE_FORMATTER = "%d/%m/%Y"

parser = argparse.ArgumentParser()

subparser = parser.add_subparsers(dest="command")

# Add subparser
subparser_add = subparser.add_parser("add", help="")
subparser_add.add_argument("amount", help="", type=float)
subparser_add.add_argument("-d", "--description", help="", type=str, default=None)
subparser_add.add_argument("-c", "--category", help="", type=str, default=None)
subparser_add.add_argument("-D", "-y", "--date", help="", type=str, default=None)

# Delete subparser
subparser_delete = subparser.add_parser("delete", help="")
subparser_delete.add_argument("id", help="", type=int, nargs="+")

# Update subparser 
subparser_update = subparser.add_parser("update", help="")
subparser_update.add_argument("id", help="", type=int)
subparser_update.add_argument("-a", "--amount", help="", type=float)
subparser_update.add_argument("-d", "--description", help="", type=str)
subparser_update.add_argument("-c", "--category", help="", type=str)
subparser_update.add_argument("-D", "--date", type=str)

# List subparser
subparser_list = subparser.add_parser("list", help="")

# Summary subparser
subparser_summary = subparser.add_parser("summary", help="")
subparser_summary.add_argument("-m", "--month", type=int, help="")

args = parser.parse_args()

if not pathlib.Path(JSON_FILE).exists():
    JSON_FILE.touch()
    with open(JSON_FILE, "w") as file:
        json.dump([], file)

elif pathlib.Path(JSON_FILE).exists():
    with open(JSON_FILE, "r+") as file:
        try:
            json.load(file)
        except Exception:
            json.dump([], file)


with open(JSON_FILE, "r+") as file:
    spendings_data = json.load(file)

    if args.date:
        try:
            validation_date = datetime.strptime(args.date, DATE_FORMATTER)
        except Exception:
            raise Exception("ERRO")
if args.command == "add":
    ...

elif args.command == "delete":
    new_list = [item for item in spendings_data if item["id"] not in args.id]
    with open(JSON_FILE, "w+") as file:
        json.dump(new_list, file, indent=4)
    print("# Expense deleted successfully")

elif args.command == "update":
    new_list = copy.copy(spendings_data)

    if args.amount or args.amount == 0: 
        for index, line in enumerate(spendings_data):
            if line["id"] == args.id:
                new_list[index]["amount"] = None if args.amount <= 0 else args.amount
    if args.category:
        for index, line in enumerate(spendings_data):
            if line["id"] == args.id:
                new_list[index]["category"] = args.category
    if args.description:
        for index, line in enumerate(spendings_data):
            if line["id"] == args.id:
                new_list[index]["description"] = args.description

    
    with open(JSON_FILE, "w+") as file:
        json.dump(new_list, file, indent=4)

elif args.command == "list":
    print("ID, AMOUNT, CATEGORY, DESCRIPTION")
    for line in spendings_data:
        print(f"# {line["id"]}, {line["amount"]}, {line["category"]}, {line["description"]}")

elif args.command == "summary":
    total_value = 0
    if args.month:
        for line in spendings_data:
            if line["amount"] != None:
                date = line["date"]
                new_date: datetime = datetime.strptime(date, DATE_FORMATTER)
                if new_date.month == args.month:
                    total_value += line["amount"]
    else:     
        for line in spendings_data:
            total_value += line["amount"] if line["amount"] != None else 0
        print(f"# Total expenses: {total_value:.2f}")
    print(f"# Total expenses for {args.month}: {total_value}")

