from copy import copy
from controller.json_operations import JsonOperations

# Fazer a atualização da data corretamente

class Update:
    @staticmethod
    def update(database, args):

        new_list = copy(database)

        for item in new_list:
            if item['id'] in args.id:
                if args.amount:
                    item['amount'] = args.amount
                if args.description:
                    item['description'] = args.description
                if args.category:
                    item['category'] = args.category
                # DATA 
        JsonOperations.send_json(JsonOperations.DATABASE_FILE, new_list)
