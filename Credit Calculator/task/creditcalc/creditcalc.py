# write your code here
import math


def convert_months_years(months):
    if months >= 12:
        if months % 12 == 0:
            print(f"You need {months // 12} years to repay this credit!")
        else:
            print(f"You need {months // 12} years and {months % 12} months to repay this credit!")
    else:
        print(f"You need {months} months to repay this credit!")



def user_principal():
    print("Enter credit principal:")
    princ = int(input())
    return princ


def user_payment():
    print("Enter monthly payment:")
    pay = float(input())
    return pay


def user_period():
    print("Enter count of periods:")
    periods = int(input())
    return periods


def user_interest():
    print("Enter credit interest:")
    interest = float(input())
    i = interest / (12 * 100)
    return i


def months():
    principal = user_principal()
    payment = user_payment()
    interest = user_interest()
    months = math.log((payment / (payment - interest * principal)), 1 + interest)
    months = math.ceil(months)
    convert_months_years(months)


def payment():
    total_principal = user_principal()
    periods = user_period()
    interest = user_interest()
    ann_pay = total_principal * ((interest * math.pow((1 + interest), periods)) / (math.pow((1 + interest), periods) - 1))
    print(f"Your annuity payment = {math.ceil(ann_pay)}!")


def principal():
    month_pay = user_payment()
    periods = user_period()
    interest = user_interest()
    credit_princ = month_pay / ((interest * pow((1 + interest), periods)) / (pow((1 + interest), periods) - 1))
    print(f"Your credit principal = {int(credit_princ)}!")


print('''What do you want to calculate?
type "n" - for count of months,
type "a" - for annuity monthly payment,
type "p" - for credit principal:''')
user_choice = input()
if user_choice == 'n':
    months()
elif user_choice == 'a':
    payment()
elif user_choice == 'p':
    principal()
