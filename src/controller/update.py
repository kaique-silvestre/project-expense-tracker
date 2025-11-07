from copy import deepcopy
from controller.json_operations import JsonOperations
from controller.validation import Validation

class Update:

    @classmethod
    def update(cls, database, args):
        new_list = deepcopy(database)
        for item in new_list:
            if item['id'] in args.id:
                if args.amount:
                    item['amount'] = args.amount
                if args.description:
                    item['description'] = args.description
                if args.category:
                    item['category'] = args.category
                if args.date:
                    date = Validation.str_to_date(args.date)
                    date_str = Validation.date_to_str(date) 
                    item['date'] = date_str
        JsonOperations.send_json(JsonOperations.DATABASE_FILE, new_list)
        print("Successfully updated.")
