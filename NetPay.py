import EmployeeClass

import PayrollDeductionClass

def main():

    employee = EmployeeClass.Employee('Jimmy Smith', '58475', 'Information Systems',
                                      'Developer', 6800)

    payroll1 = PayrollDeductionClass.PayrollDeduction('food court', '8/14/22', 22.50, '39119')
    payroll2 = PayrollDeductionClass.PayrollDeduction('gift contribution', '8/12/22', 25.00, '58475')
    payroll3 = PayrollDeductionClass.PayrollDeduction('food court', '8/17/22', 15.25, '21547')
    payroll4 = PayrollDeductionClass.PayrollDeduction('vending machine', '8/22/22', 3.00, '58475')
    payroll5 = PayrollDeductionClass.PayrollDeduction('vending machine', '8/5/22', 2.75, '58475')

    print('*** Employee Pay ***')
    print('Name: ', employee.get_name())
    print('ID Number: ', employee.get_id_number())
    print('Department: ', employee.get_department())
    print('Gross Pay: $', format(employee.get_monthly_salary(), ',.2f'), sep='')
    x = employee.get_monthly_salary() - payroll2.get_charge_amount() - payroll4.get_charge_amount() - payroll5.get_charge_amount()
    print('Net Pay: $', format(x, ',.2f'), sep='')

main()