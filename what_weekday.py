import calendar as cal

def what_weekday(numeric_str: str) -> str:
    """A simple function that return a weekday base on date string passed"""
    month, day, year = map(int, numeric_str.split())
    weekdays = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
    return weekdays[int(cal.weekday(year, month, day))]


if __name__ == "__main__":
    user_date_input = input()
    print(what_weekday(user_date_input))