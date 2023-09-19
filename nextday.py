def next_day(year, month, day):
    # Days in months
    # February has 28 or 29 days based on leap year
    months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Check for leap year
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        months[2] = 29

    # Increment day
    day += 1

    # Check if day exceeds days in month
    if day > months[month]:
        day = 1
        month += 1

        # If month exceeds 12, increment year
        if month > 12:
            month = 1
            year += 1

    return year, month, day

# Example Usage:
year=input("Year: ")
month=input("Month: ")
day=input("Day: ")
nextYear, nextMonth, nextDay = next_day(int(year), int(month), int(day))
print(f"The next day after {year}-{month}-{day} is {nextYear}-{nextMonth}-{nextDay}")
