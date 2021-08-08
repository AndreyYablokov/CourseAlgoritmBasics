# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных
# числа) для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и
# вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий,
# чья прибыль ниже среднего

numbers_companies = int(input('Enter numbers of companies: '))
companies = {}
profit_companies = 0
for _ in range(numbers_companies):
    company_name = input('Enter company name: ')
    companies[company_name] = {'profit_for_quarter': [], 'sum_profit': 0}
    for quarter_number in range(4):
        profit = float(input(f'Enter profit for {quarter_number+1} quarter: '))
        companies[company_name]['profit_for_quarter'].append(profit)
        companies[company_name]['sum_profit'] += profit
    profit_companies += companies[company_name]['sum_profit']

avg_profit = profit_companies / numbers_companies
best_companies = set()
for name, profit in companies.items():
    if profit['sum_profit'] >= avg_profit:
        best_companies.add(name)

worse_companies = set(companies) - best_companies
print(f'Average profit of companies: {avg_profit}')
print('Best companies: ', *best_companies)
print('Worst companies: ', *worse_companies)
