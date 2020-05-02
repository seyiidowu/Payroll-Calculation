#This Program is to prepare a Pay Slip to be included in a cheque envelope for the employees of a small business
#
#
#Name: Idowu Oluwaseyi
#      28/01/2020
#
#
#Data input section from the user and calculating regular, overtime hours, and deductions if the user answer yes
# defining function for float data input

def v(prompt):
    value = float(input(prompt))
    while value < 0:
        print("please enter the value of zero or positive number")
        value = float(input(prompt))
    return value

try:
    employee_name = input("please enter your employee name: ")
    hourly_rate = v("please enter your hourly rate of pay: ")
    
    work_hours = v("please enter the number of hours worked over the week: ")
    if (work_hours <= 40):
        regular_hours = work_hours   #number of regular hours of work in a day
        overtime_hours = 0           # number of overtime hours outside of regular hours
    else :
        regular_hours = 40
        overtime_hours = work_hours - regular_hours 
    
    deduction = input("Do you want deductions removed from your gross pay [Y/N]: ")
    deduction = deduction.lower()
    if (deduction == "y") or (deduction == "yes") :
        percentage_deduction = int(input("what percentage deduction (# only) do you want to remove from your gross pay: "))
    elif (deduction == "n") or (deduction == "no"):
        percentage_deduction = 0
    
# Calculation section; regular pay, overtime pay, gross_pay, deduction amount, net pay and display the payslip content

    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * 1.5 * hourly_rate         # amount from overtime hours spent
    gross_pay = regular_pay + overtime_pay                    # total amount of pay from both regular hours and overtime hours
    deduction_amount = (percentage_deduction/100) * gross_pay  # amount of money to be deducted from the gross pay
    net_pay = gross_pay - deduction_amount                     # total amount of money that is payable to the employee

    print("                                  Employee Pay Slip Record for {:s}".format(employee_name))
    print("Total Hours Worked: {:.2f}hrs                Overtime hours: {:.2f}hrs              hourly pay rate: ${:,.2f}".format(work_hours,overtime_hours,hourly_rate))
    print("         Gross Pay: ${:,.2f}                 Deduction Amount: ${:,.2f}              Net Pay: ${:,.2f}".format(gross_pay,deduction_amount,net_pay))

except NameError :
    print ("you entered the wrong value: please enter only Y/N for deduction removed from your gross pay")
except ValueError :
    print("please enter a number and not strings for percentage deduction since you answered yes")
