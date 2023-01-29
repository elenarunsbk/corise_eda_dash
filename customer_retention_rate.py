import pandas as pd
from filter_by_year_and_quarter import filter_by_year_and_quarter

def customer_retention_rate(data: pd.DataFrame, year: int, quarter: int) -> float:
    """
    Calculate the customer retention rate for a given year and quarter
    :param data: The dataframe containing the data
    :param year: The year to calculate the customer retention rate for
    :param quarter: The quarter to calculate the customer retention rate for
    :return: The customer retention rate for the given year and quarter
    """
    # Filter the data by the given year and quarter
    data_filtered = filter_by_year_and_quarter(data, year, quarter)

    # Calculate the number of unique customers
    num_customers = data_filtered['CustomerID'].nunique()

    # Calculate the number of repeat customers
    customer_order_count = data_filtered.groupby('CustomerID')['InvoiceNo'].nunique().reset_index()
    
    num_repeat_customers = customer_order_count[customer_order_count['InvoiceNo']>=2]['CustomerID'].count()

    # Calculate the customer retention rate
    return 100*num_repeat_customers/num_customers
