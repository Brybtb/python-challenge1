import csv

list_months = []
list_pl = []

with open('budget_data.csv', 'r') as csv_file:

    budget = csv.reader(csv_file, delimiter=',')

    next(budget)

    for column in budget:

        Months, Profitlosses = column
        list_pl.append(int(Profitlosses))
        list_months.append(str(Months))

months = (len(list_months))

cash = sum(list_pl)

difference = [y - x for x, y in zip(list_pl[:-1], list_pl[1:])]

def straight_average(num_list):
    total = 0.0
    length = len(num_list)
    for num in num_list:

        total += float(num)

    return (total/length)


sum_cash = sum(list_pl)
months = len(list_months)
max = max(list_pl)
min  = min(list_pl)
min_delta = min(list_pl)
date = min(list_months)


results = (f" Total Months: {months} \n Total Sales: {total})


print("Financial Analysis")
print ("---------------------------------------------")
print(results)