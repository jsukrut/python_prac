from datetime import date

today = date.today()
Str = date.isoformat(today)
print(type(Str))
print(Str)