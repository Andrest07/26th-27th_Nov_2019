import calendar
def formatmonth(year, month):
    print(calendar.month(year, month))
formatmonth(int(input("Year: ")), int(input("Month: ")))