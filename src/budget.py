from src.json_operations import JsonOperations

class Budget:

    @staticmethod
    def budget_set(path_file, database, args):
        limit = args.value
        month = args.month
        if month in database[0].keys():
            database[0][str(month)]['Limite'] = limit
        JsonOperations.send_json(path_file, database)        

    @staticmethod
    def budget_view():
        ...

    @staticmethod
    def budget_remove():
        ...
