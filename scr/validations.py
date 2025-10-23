from datetime import datetime


class Validation:

    def add_validation():
        # less than zero
        ...
    
    def delete_validation():
        # less than zero
        ...
    
    
    
    
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
        