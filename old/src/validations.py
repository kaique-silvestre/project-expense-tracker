from datetime import datetime

class Validation:

    @staticmethod
    def add_validation(args):
        # Amount Validation
        Validation.is_positive(args.amount)

        # Date Validation
        if args.date is not None:
            Validation.date_validation(args.date)
   
    @staticmethod    
    def delete_validation(args):
        for item in args.id:
            Validation.is_positive(item)

    @staticmethod
    def summary_validation(args):
        if args.month:
            Validation.is_positive(args.month)
            if args.month > 12:
                raise Exception() 
    
    def update_validation(args):
        for item in args.id:
            Validation.is_positive(item)
        if args.amount is not None:
            Validation.is_positive(args.amount)
        if args.date is not None:
            date = datetime.strptime(args.date, '%d/%m/%Y')


#########################################
    
    @staticmethod
    def date_validation(date):
        DATE_FORMATTER = "%d/%m/%Y"
        try:
            val_date = datetime.strptime(date, DATE_FORMATTER)
        except Exception:
            raise Exception("DATE ERROR")
   
   
    @staticmethod
    def is_positive(number):
        if number <= 0:
            raise Exception()
    

    def correctly_datatype_str(args):
        date_type_datetime = datetime.strptime(args, '%d/%m/%Y')
        date_type_str = datetime.strftime(date_type_datetime, '%d/%m/%Y')
        return date_type_str
        