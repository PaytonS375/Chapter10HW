class Employee:

    def __init__(self, name, id_num, dept, j_title, m_salary):
        self.__name = name
        self.__id_number = id_num
        self.__department = dept
        self.__job_title = j_title
        self.__monthly_salary = m_salary

    def set_name(self, name):
        self.__name = name

    def set_id_number(self, id_num):
        self.__id_number = id_num

    def set_department(self, dept):
        self.__department = dept

    def set_job_title(self, j_title):
        self.__job_title = j_title

    def set_monthly_salary(self, m_salary):
        self.__monthly_salary = m_salary

    def get_name(self):
        return self.__name

    def get_id_number(self):
        return self.__id_number

    def get_department(self):
        return self.__department
    
    def get_job_title(self):
        return self.__job_title

    def get_monthly_salary(self):
        return self.__monthly_salary