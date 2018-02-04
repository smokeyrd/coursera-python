def future_value(present_value, annual_rate, periods_per_year, years):
    """
    Input: the numbers present_value, annual_rate, periods_per_year, years
    Output: future value based on formula given in question
    """
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years

    # Put your code here.
    print (rate_per_period)
    print(periods)
    return (present_value*(1+rate_per_period)**periods)

print("$1000 at 2% compounded daily for 4 years yields $", future_value(1000, .02, 365, 4))
#print (future_value(500, .04, 10, 10))