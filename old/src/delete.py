from src.json_operations import JsonOperations

class Delete:
    @staticmethod
    def delete(path_file, database, args):
        new_list = [item for item in database if item["id"] not in args.id]
        JsonOperations.send_json(path_file, new_list)
