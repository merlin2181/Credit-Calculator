# write your code here
import math
import sys
import argparse


def convert_months_years(months):
    if months >= 12:
        if months % 12 == 0:
            print(f"You need {months // 12} years to repay this credit!")
        else:
            print(f"You need {months // 12} years and {months % 12} months to repay this credit!")
    else:
        print(f"You need {months} months to repay this credit!")


def months(prin, pay, inte):
    principal = prin
    payment = pay
    interest = inte
    months = math.log((payment / (payment - interest * principal)), 1 + interest)
    months = math.ceil(months)
    convert_months_years(months)
    print(f"Overpayment = {(payment * months) - principal}")


def payment(prin, per, inte):
    total_principal = prin
    periods = per
    interest = inte
    ann_pay = total_principal * ((interest * math.pow((1 + interest), periods)) / (math.pow((1 + interest), periods) - 1))
    ann_pay = math.ceil(ann_pay)
    print(f"Your annuity payment = {ann_pay}!")
    print(f"Overpayment = {(ann_pay * periods) - total_principal}")


def principal(pay, per, inte):
    month_pay = pay
    periods = per
    interest = inte
    credit_princ = month_pay / ((interest * pow((1 + interest), periods)) / (pow((1 + interest), periods) - 1))
    print(f"Your credit principal = {int(credit_princ)}!")
    print(f"Overpayment = {math.ceil((month_pay * periods) - credit_princ)}")


credit_calc = argparse.ArgumentParser(description="A calculator to annuity or differentiated payments")
credit_calc.add_argument("--type", help="Indicate what type of payment to calculate")
credit_calc.add_argument("--payment", type=int, help="The monthly payment")
credit_calc.add_argument("--principal", type=int, help="The principal of the loan")
credit_calc.add_argument("--periods", type=int, help="The number of months to repay loan")
credit_calc.add_argument("--interest", type=float, help="The interest rate, if 5.6% enter 5.6")
args = credit_calc.parse_args()

if len(sys.argv) != 5:
    print("Incorrect parameters")
else:
    if args.type != "diff" and args.type != "annuity":
        print("Incorrect parameters")
    elif args.type == "diff" and args.payment:
        print("Incorrect parameters")
    else:
        interest = args.interest / (12 * 100)
        if args.type == "diff":
            total = 0
            for m in range(1, args.periods + 1):
                answer = math.ceil((args.principal / args.periods) + interest *
                                   (args.principal - ((args.principal * (m - 1)) / args.periods)))
                print(f"Month {m}: paid out {answer}")
                total += answer
            over_pay = total - args.principal
            print("")
            print(f"Overpayment = {over_pay}")
        elif args.type == "annuity":
            if args.principal and args.payment:
                months(args.principal, args.payment, interest)
            elif args.principal and args.periods:
                payment(args.principal, args.periods, interest)
            elif args.payment and args.periods:
                principal(args.payment, args.periods, interest)
