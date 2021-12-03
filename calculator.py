#tax calculator project
import sys

while True:
    try:
        income = int(sys.argv[1])
    except ValueError:
        print("Parameter Error")
        continue
    else:
        break

if (income-3500) < 1500:
    tax = (income-3500) * .03 - 0
elif (income-3500) <= 4500:
    tax = (income-3500) * .10 - 105
elif (income-3500) <= 9000:
    tax = (income-3500) * .20 - 555
elif (income-3500) <= 35000:
    tax = (income-3500) * .25 - 1005
elif (income-3500) <= 55000:
    tax = (income-3500) * .30 - 2755
elif (income-3500) <= 80000:
    tax = (income-3500) * .35 - 5505
else:
    tax = (income-3500) * .45 - 13505

print (f'{tax:.2f}')

