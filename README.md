# Companies in Russia After the Invasion
### Exploring the response of different companies following the Russian invasion of Ukraine.

### Initial research question to analyze the dataset to look for correlations between the type of industry and their decisions to leave the country or stay following Russia's invasion of Ukraine.

### Stakeholder interest lies in the development of sanctions regimes to identify which sectors or regions can be targeted to apply political and or economic pressure on Russia.

## Begin with imports

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

import matplotlib

## Import Data

country_data = pd.read_csv('../data/companies.csv')

## Describe Data

country_data.describe()

Count: 1581

Countries: 67

Grade: 5 (A, B, C, D, F)

Industry: 12

Action: "String description of actions taken."

## Exploratory Data Analysis

### Initially explored data based on the number of companies in each sector.  This was not very revealing as industrial companies were the largest in A grade and F grade.  Transitioned to evaluation based on percentage comparisons.

industry_counts = country_data['Industry'].value_counts()
total_companies = len(country_data)

industry_percentages = industry_counts / total_companies * 100

### All 12 industries was visually noisy so I condensed this down to the top 6 industries

top_industries = industry_counts.head(6).index.tolist()

focused_data = country_data[country_data['Industry'].isin(top_industries)]

#Recalculate Data to show percentages of total with only these six categories
top_six_industries = focused_data['Industry'].value_counts()
top_six_percentages = top_six_industries / len(country_data) * 100

#### Industrials: 25.49
#### Consumer Discretionary: 19.80
#### Information Technology: 12.33
#### Consumer Staples: 10.56
#### Financials: 8.22
#### Materials: 6.14
#### In total these industries compose 82.54% of all foreign-owned companies in Russia.

### Next I broke down the percentage by industry for each letter grade to illuminate differences across industries to see if one industry were better than another at divesting of Russian assets: 

## Grade A
grade_A_count = focused_data[focused_data['Grade'] == 'A'].groupby('Industry')['Grade'].count()

industry_percent_A = grade_A_count / len(focused_data) * 100

industry_percent_A_sorted = industry_percent_A.sort_values(ascending=False)

## Grade F

#### Here a "custom_order" line was added to keep the x-axis values in a consistent order across letter grades.  This made for a more "human-readable" presentation.

grade_F_count = focused_data[focused_data['Grade'] == 'F'].groupby('Industry')['Grade'].count()

industry_percent_F = grade_F_count / len(focused_data) * 100

custom_order = ['Industrials', 'Consumer Discretionary', 'Information Technology', 'Consumer Staples', 'Financials', 'Materials']

industry_percent_F_sorted = industry_percent_F.sort_values(key=lambda x: x.index.map(lambda y: custom_order.index(y)), ascending=True)



## Visualizations:

### Top six industries by percentage
top_six_percentages.plot(kind='bar')

plt. title('Percent Share of Foreign Owned Industries in Russia')
plt.xlabel('Type of Industry')
plt.ylabel('Percentage of Total')

### Percentage receiving grade "A"

industry_percent_A_sorted.plot(kind='bar')

plt.title('Grade A Percentage Share')
plt.xlabel(None)
plt.ylabel(None)

plt.xticks(rotation=45)

plt.ylim([0, 12])

### Percentage receiving grade "F"

industry_percent_F_sorted.plot(kind='bar')

plt.title('Grade F Percentage Share')
plt.xlabel(None)
plt.ylabel(None)

plt.xticks(rotation=45)

plt.ylim([0, 12])

### I found that industry comparison delivered inconclusive results.  I then switched to a comparison based upon the country in which companies are headquarted to explore the hypothesis that geopolitics may demonstrate a closer correlation with companies' operations in Russia.

## Country of Origin Analysis

country_counts = country_data['Country'].value_counts()
total_companies = len(country_data)

country_percentages = country_counts / total_companies * 100

### Similar to earlier code except this time filtering by "Country" column instead of "Industry".

country_counts = country_data['Country'].value_counts()

### To ensure the most relevant of the 67 countries with companies in Russia I focused on the top 10 which showed the U.S., several European nations, and China:

#### United States: 457
#### Germany: 147
#### United Kingdom: 128
#### France: 83
#### Japan: 76
#### Switzerland: 58
#### Finland: 55
#### China: 52
#### Netherlands: 50
#### Poland: 41

### I focused the rest of my analysis on these 10 countries.

top_countries = country_counts.head(10).index.tolist()

focused_data = country_data[country_data['Country'].isin(top_countries)]

### Due to the large disparity between the number of businesses I focused on analyzing companies according to the percentage of a country's companies in Russia as a percentage of the total:

top_10_countries = focused_data['Country'].value_counts()
top_countries_percentage = top_10_countries / len(country_data) * 100

### Next I focused on comparing how each country performed and grouped by letter grade.

country_grades = country_data.groupby('Country')['Grade'].value_counts()

### Grade A
### The "custom_order" code again allowed for a cleaner human-readable comparison by letter grade.

grade_A_count = focused_data[focused_data['Grade'] == 'A'].groupby('Country')['Grade'].count()
country_counts = focused_data['Country'].value_counts()

custom_order = ['Finland', 'United Kingdom', 'Poland', 'Switzerland', 'United States', 'Netherlands', 'Germany', 'France', 'Japan', 'China']

country_percent_A = grade_A_count / country_counts * 100
country_percent_A_sorted = country_percent_A.sort_values(key=lambda x: x.index.map(lambda y: custom_order.index(y)), ascending=True)

### Grade F

grade_F_count = focused_data[focused_data['Grade'] == 'F'].groupby('Country')['Grade'].count()
country_counts = focused_data['Country'].value_counts()

custom_order = ['Finland', 'United Kingdom', 'Poland', 'Switzerland', 'United States', 'Netherlands', 'Germany', 'France', 'Japan', 'China']

country_percent_F = grade_F_count / country_counts * 100
country_percent_F_sorted = country_percent_F.sort_values(key=lambda x: x.index.map(lambda y: custom_order.index(y)), ascending=True)

## Visualizations:

### Percentage of Foreign Owned Companies in Russia:

top_countries_percentage.plot(kind='bar')

plt. title('Percent Share of Foreign Owned Companies in Russia')
plt.xlabel('Country of Origin')
plt.ylabel('Percentage of Total')

### Grade A Country Comparison

country_percent_A_sorted.plot(kind='bar')

plt.title('Grade A Percentage Share')
plt.xlabel(None)
plt.ylabel(None)

plt.xticks(rotation=45)

plt.ylim([0, 80])

### Grade F Country Comparison

country_percent_F_sorted.plot(kind='bar')

plt.title('Grade F Percentage Share')
plt.xlabel(None)
plt.ylabel(None)

plt.xticks(rotation=45)

plt.ylim([0, 80])

## Findings

### Comparing companies by country of origin shows inverted results when juxtaposing "A" and "F" grades with 60% of Finnish companies receiving "A" and less than 5% of Chinese companies receiving "A" whereas 0% of Finnish companies received an "F" and nearly 80% of Chinese companies received an "F". 

## Additional Visualization

### To further elucidate some of the findings I wanted to create a chart which showed which the number of companies that each country has in Russia.  I've decided to break this apart by industry in a stack chart as a proof of concept for my own capabilities.  

### I wanted to keep the order of countries consistent with the previous two charts for readability.  Together I believe that this helps "tell the story" of my findings and presents the honest caveat that, while we are talking about a relatively small number of companies which receive an "F", that this number is still revealing given the countries which similar numbers of companies and their received grades.

top_countries = country_counts.head(10).index.tolist()

focused_data = country_data[country_data['Country'].isin(top_countries)]

### This code groups countries and produces a count of how many companies there are in each industry.

country_industries = focused_data.groupby('Country')['Industry'].value_counts()

### Count of Industries by Country

plt.figure(figsize=(12, 6))
sns.set_palette("crest")
stacked_data.plot(kind='bar', stacked=True)
plt.title('Count of Industries by Country')
plt.xlabel('Country')
plt.ylabel('Count of Industries')
plt.xticks(rotation=45)
plt.legend(title='Industry', prop={'size': 8})

plt.show()

### My chosen colorscheme "crest" looks good with my chosen powerpoint presentation but is probably not very colorblind-friendly.  I am at peace with this because it is a proof of concept for my own ability and not essential to the meaning of my presentation.

## Conclusions

### This analysis suggests that geopolitics correlate closer to a company's decisions about its Russian market following the invasion of Ukraine than does the type of industry.  

### Current geopolitical signals reflect my findings in the data.  China received the most F grades for its companies which is supported by President Xi's claims of a "no limits" partnership with Russia.  Additionally, the second nation with the highest percentage of F grades, France, recently met with President Xi and spoke about the importance of not getting caught up in crises that are not [France's].  

### China has a similar number of companies as Finland and the Netherlands, but both have 0 companies which received an F grade.

### Caveat: It would take additional evaluation of the data itself to see how well the researchers have accounted for all nations and all companies in Russia.  Perhaps there was deliberate or accidental under/over counting of companies which distort the numbers, and this would be easy to do given the relatively small sample size.  

