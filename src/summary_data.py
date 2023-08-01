import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def country_percentages(df):
    """
    Take in data frame, return percentages of each country's 
    number of countries in Russia

    """
    country_counts = df['Country'].value_counts()
    total_companies = len(df)

    country_percentages = country_counts / total_companies * 100
    return round(country_percentages, 2)

def pie_chart_all_countries(country_count_series):
    """
    This function produces a pie chart showing the total percentage
    by country of its companies in Russia.
    """
    y = np.array([country_count_series])

    labels = country_count_series.index
    counts = country_count_series.values
    plt.figure(figsize=(8,8))
    plt.pie(counts, labels=labels, autopct='%1.1f%%')
    plt.title(None)


    plt.show()

if __name__ == '__main__':
    df = pd.read_csv('data/companies.csv')
    # print(df.head())

    c_counts = country_percentages(df)

    pie_chart_all_countries(c_counts)