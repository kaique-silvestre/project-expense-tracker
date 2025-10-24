from json_operations import JsonOperations
import copy
from validations import Validation

class Update:
    @staticmethod
    def update(file_path, database, args):

        new_list = copy.copy(database)

        for item in new_list:
            if item['id'] in args.id:
                if args.amount:
                    item['amount'] = args.amount
                if args.description:
                    item['description'] = args.description
                if args.category:
                    item['category'] = args.category
                if args.date:
                    date = Validation.correctly_datatype_str(args.date)
                    item['date'] = date
        JsonOperations.send_json(file_path, new_list)
        