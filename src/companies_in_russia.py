# This document contains all code used to conduct analysis and produce visualizations:

# All imports as follows:

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

# Importing document from csv format

country_data = pd.read_csv('../data/companies.csv')

# Beginning of EDA by describing the data to understand the number of companies represented:

country_data.describe()

# Data parsed according to percentage of companies belonging to one of 12 industries:

industry_counts = country_data['Industry'].value_counts()

total_companies = len(country_data)

industry_percentages = industry_counts / total_companies * 100

# EDA Visualization of industry percentages

industry_percentages.plot(kind='bar')

plt.title('Percent Share of Foreign Companies in Russia')
plt.xlabel('Type of Industry')
plt.ylabel('Percentage of Total')

# Narrowed this data to the six biggest industries:

top_industries = industry_counts.head(6).index.tolist()

focused_data = country_data[country_data['Industry'].isin(top_industries)]

#Recalculate Data to show percentages of total with only these six categories

top_six_industries = focused_data['Industry'].value_counts()

top_six_percentages = top_six_industries / len(country_data) * 100

#Collectively the industries considered represented 82.54% of the total

#Visualized these six industries:

top_six_percentages.plot(kind='bar')

plt. title('Percent Share of Foreign Owned Industries in Russia')
plt.xlabel('Type of Industry')
plt.ylabel('Percentage of Total')

# Next I explored how these industries compare by grouping them according to their 
# letter grades:

industry_grades = country_data.groupby('Industry')['Grade'].value_counts()

# Grade A by percentage of the total in the 6 biggest categories.

grade_A_count = focused_data[focused_data['Grade'] == 'A'].groupby('Industry')['Grade'].count()

industry_percent_A = grade_A_count / len(focused_data) * 100

# This code used throughout industry comparison to lock in this order even if
# values change
custom_order = ['Industrials', 'Consumer Discretionary', 'Information Technology', 'Consumer Staples', 'Financials', 'Materials']

industry_percent_A_sorted = industry_percent_A.sort_values(key=lambda x: x.index.map(lambda y: custom_order.index(y)), ascending=True)

# Visualized Grade A Percentage Share in a bar graph:

industry_percent_A_sorted.plot(kind='bar')

plt.title('Grade A Percentage Share')
plt.xlabel(None)
plt.ylabel(None)

plt.xticks(rotation=45)

plt.ylim([0, 12])

# Grade C by percentage of the total in the 6 biggest categories.

grade_C_count = focused_data[focused_data['Grade'] == 'C'].groupby('Industry')['Grade'].count()

industry_percent_C = grade_C_count / len(focused_data) * 100

custom_order = ['Industrials', 'Consumer Discretionary', 'Information Technology', 'Consumer Staples', 'Financials', 'Materials']

industry_percent_C_sorted = industry_percent_C.sort_values(key=lambda x: x.index.map(lambda y: custom_order.index(y)), ascending=True)

print(round(industry_percent_C_sorted, 2))

# Visualized Grade C Percentage Share in a bar graph:

industry_percent_C_sorted.plot(kind='bar')

plt.title('Grade C Percentage Share')
plt.xlabel(None)
plt.ylabel(None)

plt.xticks(rotation=45)

plt.ylim([0, 12])

# Grade F by percentage of the total in the 6 biggest categories.

grade_F_count = focused_data[focused_data['Grade'] == 'F'].groupby('Industry')['Grade'].count()

industry_percent_F = grade_F_count / len(focused_data) * 100

custom_order = ['Industrials', 'Consumer Discretionary', 'Information Technology', 'Consumer Staples', 'Financials', 'Materials']

industry_percent_F_sorted = industry_percent_F.sort_values(key=lambda x: x.index.map(lambda y: custom_order.index(y)), ascending=True)

print(round(industry_percent_F_sorted, 2))

# Visualized Grade F Percentage Share in a bar graph:

industry_percent_F_sorted.plot(kind='bar')

plt.title('Grade F Percentage Share')
plt.xlabel(None)
plt.ylabel(None)

plt.xticks(rotation=45)

plt.ylim([0, 12])

"""
This concludes this part of my EDA.  I did not find significant disparities across
industries for company decisions.  At both the A and F grades there is not wide variation
and I switched analysis to look at differences by the country of origin
"""

# EDA on Country Comparison

# Imports the same

# Explored first to find out which countries have the most companies in Russia:

# This code counts companies according to the 'Country' column and determines their 
# share as a percentage of the total

country_counts = country_data['Country'].value_counts()

total_companies = len(country_data)

country_percentages = country_counts / total_companies * 100

# This code isolates the 10 biggest according to # and not percentage:

country_counts = country_data['Country'].value_counts()

country_counts.head(10)

# This code limits data frame to the top 10 countries:

top_countries = country_counts.head(10).index.tolist()

focused_data = country_data[country_data['Country'].isin(top_countries)]

# Later analysis requires a variable to present this data by percentage:

top_10_countries = focused_data['Country'].value_counts()

top_countries_percentage = top_10_countries / len(country_data) * 100

# Visually expressed as a percentage:

top_countries_percentage.plot(kind='bar')

plt. title('Percent Share of Foreign Owned Companies in Russia')
plt.xlabel('Country of Origin')
plt.ylabel('Percentage of Total')

# This variable allows an analysis of data by country by grade.  Combining the data
# in this way helps to clarify whether there are significant disparities in how
# countries perform as a percentage of their total.

country_grades = country_data.groupby('Country')['Grade'].value_counts()

# This shows as a percentage of that country's companies that receive an A.  
# This configuration also sets the "custom_order" line of code.
# I use this order of countries in my presentation to make findings most readily
# "human readable" to ease the story embedded in the data.

grade_A_count = focused_data[focused_data['Grade'] == 'A'].groupby('Country')['Grade'].count()
country_counts = focused_data['Country'].value_counts()

custom_order = ['Finland', 'United Kingdom', 'Poland', 'Switzerland', 'United States', 'Netherlands', 'Germany', 'France', 'Japan', 'China']

country_percent_A = grade_A_count / country_counts * 100
country_percent_A_sorted = country_percent_A.sort_values(key=lambda x: x.index.map(lambda y: custom_order.index(y)), ascending=True)

print(round(country_percent_A_sorted, 2))

# Visualized as Grade A Percentage Share

country_percent_A_sorted.plot(kind='bar')

plt.title('Grade A Percentage Share')
plt.xlabel(None)
plt.ylabel(None)

plt.xticks(rotation=45)

plt.ylim([0, 80])

"""Embedded in the "country_comparison.ipynb is additional code
in which I conducted an analysis of "A & B" and "D & F".  My findings were consistent
and did not help create a clearer picture so I have dismissed these findings
from the final presentation.  There are also charts and data considering only "C" 
grades as well but they have not been included in the final presentation."""

#This shows as a percentage of that country's companies that receive an F.

grade_F_count = focused_data[focused_data['Grade'] == 'F'].groupby('Country')['Grade'].count()
country_counts = focused_data['Country'].value_counts()

custom_order = ['Finland', 'United Kingdom', 'Poland', 'Switzerland', 'United States', 'Netherlands', 'Germany', 'France', 'Japan', 'China']

country_percent_F = grade_F_count / country_counts * 100
country_percent_F_sorted = country_percent_F.sort_values(key=lambda x: x.index.map(lambda y: custom_order.index(y)), ascending=True)

print(round(country_percent_F_sorted, 2))

# Visualized as Grade F Percentage Share

country_percent_F_sorted.plot(kind='bar')

plt.title('Grade F Percentage Share')
plt.xlabel(None)
plt.ylabel(None)

plt.xticks(rotation=45)

plt.ylim([0, 80])

""" At this point I have reached an MVP.  This analysis demonstrates an easily
presentable story from the data and the visualizations demonstrate my analysis
in an easily presentable format."""

# Here I will detail my stretch goals work.  I wanted to developed a stacked bar
# chart which would demonstrate some of my findings as a comparison of the total
# number of foreign companies in Russia.  I felt this was a necessary step given 
# the relatively small number of companies captured when they are narrowed down
# to a single letter grade.

# First I verified that I was working with the correct dataset of the largest 10 
# countries grouped by their industry.

top_countries = country_counts.head(10).index.tolist()

focused_data = country_data[country_data['Country'].isin(top_countries)]

country_industries = focused_data.groupby('Country')['Industry'].value_counts()

# Visualized as a stacked bar chart by country and by industry
# I maintained my custom_order to keep consistency accross visualizations.

custom_order = ['Finland', 'United Kingdom', 'Poland', 'Switzerland', 'United States', 'Netherlands', 'Germany', 'France', 'Japan', 'China']

reordered_data = country_industries.reindex(custom_order, level='Country')

stacked_data = reordered_data.unstack()

plt.figure(figsize=(12, 6))
sns.set_palette("crest")
stacked_data.plot(kind='bar', stacked=True)
plt.title('Count of Companies by Country and Industry')
plt.xlabel(None)
plt.ylabel('Count of Companies')
plt.xticks(rotation=45)
plt.legend(title='Industry', prop={'size': 8})

plt.show()

# It is worth acknowledging that this is the wrong tool if one wants to see how 
# countries vary by industry.  This was more of a proof of concept for myself.  
# However, seeing the number of companies by country clarifies earlier findings
# to communicate significance.
# Color scheme is likely not color-blind friendly but it does match (somewhat)
# with the schema of my Powerpoint Presentation.