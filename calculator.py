#!/usr/bin/env python3
import sys

salary_dict = {}

def tax_count(salary):
	social_insur = salary * 0.165
	tax_payable = salary - social_insur - 3500

	if tax_payable <= 0:
		tax = 0
	elif tax_payable <= 1500:
		tax = tax_payable * 0.03
	elif tax_payable>1500 and tax_payable<=4500:
		tax = tax_payable * 0.1 - 105
	elif tax_payable>4500 and tax_payable<=9000:
		tax = tax_payable * 0.2 - 555
	elif tax_payable>9000 and tax_payable<=35000:
		tax = tax_payable * 0.25 - 1005
	elif tax_payable>35000 and tax_payable<=55000:
		tax = tax_payable * 0.3 - 2755
	elif tax_payable>55000 and tax_payable<=80000:
		tax = tax_payable * 0.35 - 5505
	elif tax_payable>80000:
		tax = tax_payable * 0.45 - 13505

	return tax

for arg in sys.argv[1:]:
	input_arg = arg.split(":")
	try:
	    id = input_arg[0]
	    salary = int(input_arg[1])
	except:
		print("Parameter Error")
	tax = tax_count(salary)
	salary_dict[id] = salary - tax - 0.165 * salary

for key,value in salary_dict.items():
	print("{}{}{:.2f}".format(key,":",value))

