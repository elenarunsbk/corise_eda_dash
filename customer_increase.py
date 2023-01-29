import pandas as pd
from filter_by_year_and_quarter import filter_by_year_and_quarter

# Write a function using the Poisson distribution to model how likely a 10% increase in customers (over the mean) is on any given day
def customer_increase_proba(data: pd.DataFrame, year: int, quarter: int) -> float:
    """
    Calculate how likely a 10% increase in customers (over the mean) is on any given day
    :param data: The dataframe containing the data
    :param year: The year to calculate the probability for
    :param quarter: The quarter to calculate the probability for
    :return: The probability of a 10% increase in customers (over the mean) on any given day
    """
    # Filter the data by the given year and quarter
    data_filtered = filter_by_year_and_quarter(data, year, quarter)

    # Calulate the mean number of customers per day
    daily_customers = pd.DataFrame(data_filtered.groupby(['Year','Month','Day'])['CustomerID'].nunique())
    mean_daily_customers = daily_customers.mean().astype(int)
    
    # Generate the Poisson distribution
    distribution = poisson(mu=mean_daily_customers)
    x = mean_daily_customers*1.1
    x = x.astype(int)

    # Calculate the probability of having 10% more customers on a given day
    return distribution.pmf(x)
