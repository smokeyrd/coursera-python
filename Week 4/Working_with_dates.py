"""Final exam time! Let's test dates and see if I can figure it out."""
import datetime
def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    month2=month+1
    year2=year

    if month>=12:
        month2=1
        year2=year+1
    else:
        month2=month+1
    date0= datetime.date(year,month, 1)
    date1=datetime.date(year2, month2, 1)
    days= date1-date0
    return days.days


def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    if (year >=datetime.MINYEAR and year<=datetime.MAXYEAR):
        if (month>=1 and month <=12):
            if (day >=1 and day <=days_in_month(year,month)):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    #check if date is valid before calculating days between two dates
    if is_valid_date(year1,month1,day1)==True and is_valid_date(year2,month2,day2) ==True:
        date1 = datetime.date(year1, month1, day1)
        date2 = datetime.date(year2, month2, day2)
        difference = (date2 - date1)
        if (difference.days >= 0):
            return (difference.days)
        else:
            return 0
    else:
        return 0



def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid of if the input
      date is in the future.
    """
    #check if date is valid before calculating days between then and now
    if is_valid_date(year, month, day) == True:
        todays_date = datetime.date.today()
        birthdate = datetime.date(year, month, day)
        if birthdate > todays_date:
            return 0
        else:
            age = (todays_date - birthdate).days
            return age
    else:
        return 0


days_between(20000, 1, 1, 2047, 8, 2)