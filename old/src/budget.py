from src.json_operations import JsonOperations

class Budget:

    @staticmethod
    def budget_set(path_file, database, args):
        limit = args.value
        month = args.month
        if month in database[0].keys():
            database[0][str(month)]['limit'] = int(limit)
        JsonOperations.send_json(path_file, database) 
        print("set")       

    @staticmethod
    def budget_view():
        ...

    @staticmethod
    def budget_remove(path_file, database, args):
        month = args.month
        if month in database[0].keys():
            database[0][str(month)]['limit'] = None
        JsonOperations.send_json(path_file, database)        

