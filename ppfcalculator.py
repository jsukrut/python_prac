from datetime import date
# roi = float(input("Rate of interest"))
# investment_amount= float(input("monthly investment amount"))
# investment_years =float(input("Investment for years"))
# monthly_roi = float(roi/12)

roi = 6.0
investment_amount= 5000
investment_years = 15
monthly_roi = float(roi/12)



today = date.today()
print(today)
current_year = today.year
maturity_date = date(today.year + 15, today.month, today.day)
print(maturity_date)
no_of_months = 12 * investment_years

principle = 0
default_principle = 0
only_interest =0

for month in range(0,no_of_months):
    default_principle += investment_amount
    interest =  round(principle * monthly_roi/100,3)
    only_interest += interest
    only_interest= round(only_interest,3)
    principle += interest
    principle += investment_amount
    principle= round(principle,3)

print("Invested Amount",default_principle)
print("Total Interest",only_interest)
print("Maturity Amount",principle)



