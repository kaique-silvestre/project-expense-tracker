from controller.json_operations import JsonOperations

class Delete:
    @classmethod
    def delete(cls, database, args):
        new_database = [item for item in database if item["id"] not in args.id]
        JsonOperations.send_json(JsonOperations.DATABASE_FILE, new_database)
        print("Successfully deleted.")