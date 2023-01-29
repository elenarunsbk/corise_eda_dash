import pandas as pd
from filter_by_year_and_quarter import filter_by_year_and_quarter

# Write a function to find the most popular product for a given year and quarter
def most_popular_product(data: pd.DataFrame, year: int, quarter: int) -> str:
    """
    Find the most popular product for a given year and quarter
    :param data: The dataframe containing the data
    :param year: The year to find the most popular product for
    :param quarter: The quarter to find the most popular product for
    :return: The most popular product for the given year and quarter
    """
    # Filter the data by the given year and quarter
    data_filtered = filter_by_year_and_quarter(data, year, quarter)
    data_filtered['Product'] = data_filtered['StockCode'].astype(str) + " - " + data_filtered['Description'].astype(str)
    # Find the most popular product
    return data_filtered['Product'].mode()
