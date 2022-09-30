class PayrollDeduction:

    def __init__(self, descr, date, charge_amt, emp_id):
        self.__description = descr
        self.__date = date
        self.__charge_amount = charge_amt
        self.__employee_id = emp_id

    def set_description(self, descr):
        self.__description = descr

    def set_date(self, date):
        self.__date = date

    def set_charge_amount(self, charge_amt):
        self.__charge_amount = charge_amt

    def set_employee_id(self, emp_id):
        self.__employee_id = emp_id
        
    def get_description(self):
        return self.__description

    def get_date(self):
        return self.__date
    
    def get_charge_amount(self):
        return self.__charge_amount

    def get_employee_id(self):
        return self.__employee_id