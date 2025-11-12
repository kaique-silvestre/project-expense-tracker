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
budget_set.add_argument("value", help="")
budget_set.add_argument("month", help="")

# BUDGET SUBPARSER -- REMOVE
budget_remove = subparser_budget.add_parser("delete")
budget_remove.add_argument("month", type=int, nargs="+", help="")

# BUDGET SUBPARSER -- LIST
budget_list = subparser_budget.add_parser("list")
budget_list.add_argument("-m", "--month", type=int, nargs="+", help="")

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

a = Add()

database = JsonOperations.return_json(JsonOperations.DATABASE_FILE)


if args.command == "add":

    # amount
    # - Ser maior que zero
    # - Apenas duas casas decimais

    # category 
    #  - <= 20 Letras de lenght

    # date 

    # description
    # <= 100 letras


    a.add_flow(database, args)

elif args.command == "delete": ##

    # Validar números negativos
    # Validar zero
    Val.delete_validation(args)
    Delete.delete(database, args) # OK / MSG

elif args.command == "update": 

    # id
    # - Validar para que seja maior que zero
    
    # amount
    # - Validar números negativos
    # - Validar zero
    # - Validar que números não sejam maior que 100_000_000_000_000 
    # - Validar para que número tenha apenas duas casas decimais

    # description
    # - Validar que descrição não tenha mais de 100 letras

    # date
    # - Validar data?

    # category
    # Validar que categoria não tenha mais de 20 Letras
    # Validar para que sejam UPPER CASE?

    Update.update(database, args)  # OK / MSG
    
elif args.command == "list": ##

    # year
    # - Ser maior que zero
    # - Ser menor que 10.000?
    
    # month
    # - Estar entre 1 e 12

    # category
    # - Validar que categoria não tenha mais de 20 Letras
    # - Validar para que sejam UPPER CASE?

    # less
    # - Ser maior que zero
    # - ter apenas duas casas decimais

    
    # greater
    # - Ser maior que zero
    # - ter apenas duas casas decimais


    # amount
    # - Ser maior que zero
    # - ter apenas duas casas decimais

    Read.filter(database, args)

elif args.command == "clear": 
    JsonOperations.send_json(JsonOperations.DATABASE_FILE, []) # OK /MSG
    print("# Successfully cleared spends database.")
elif args.command == "export":
    Export.csv_export_flow(database, args)
elif args.command == "budget":
    budget_database = JsonOperations.return_json(JsonOperations.BUDGET_FILE) # Just loads if budget is called
    
    if args.command_budget == "set":
        
        # value 
        # - Ser maior que zero e positivo
        # - Ter duas casas decimais

        # month
        # - Estar entre 1 e 12

        Budget.set_budget(budget_database, args) # OK / MSG

    elif args.command_budget == "list":
        Budget.list_budget(budget_database, args) # OK / MSG
    
    elif args.command_budget == "delete":

        # delete 
        # - Ser maior que zero e positvo
        Budget.delete_budget(budget_database, args) # OK  / # MSG


