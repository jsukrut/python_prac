

Housing = 20000
food = 5000
Transportation = 2000
Utilities = 4000
Entertainment_And_Miscellaneous = 5000

current_cost_of_living = Housing + food + Transportation + Utilities +\
                            Entertainment_And_Miscellaneous

inflation_rate = float(input("Enter AVG Inflation Rate"))
years_for_calculation = int(input("Enter the no of years for calculation"))
print("Current Cost of Living =",current_cost_of_living)

future_cost_of_living = 0
next_year_cost_of_living = current_cost_of_living
for year in range(1,years_for_calculation+1):
    next_year_cost_of_living = next_year_cost_of_living + (next_year_cost_of_living * inflation_rate/100)
    # print(year)
    # print(next_year_cost_of_living)

print("Future cost of living",next_year_cost_of_living)
