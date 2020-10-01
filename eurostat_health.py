'''
Using data from Eurostat, create a list of tuples representing the“Self-perceived health by country and sex, agegroup >16, for people living in cities”for 2017-2018.
Have at least 30 values in your dataset.The dataset will have the following structure:[ (country, year, sex, health_index)]
Example:[(‘France’, 2017, M, 12), . . . ]

Using only comprehensions, create the following dicts:
•  two dicts that group all data by country for each year
health_index_2017 = {‘France’: [sex, health_index]}
health_index_2018 = {‘France’: [sex, health_index]}
•  one dict that groups all data by year for Germany germany = {2017: [sex, health_index]}
•  one dict that grups all data by country and year, by using year in the key together with the country name health_index = {‘France_2017’: [year, sex, health_index]}
•  starting from the previoushealth_indexdict, display only the data where the health_index > 5
•  starting from the previoushealth_indexdict, display only the data where the health_index > 5 and sex is ‘F’
•  starting from the previoushealth_indexdict, create a for loop to print the health_index
'''

# import pandas as pd

# eurostat_file = pd.read_csv(r'/home/eva/python_national/Eurostat Health Index/hlth_silc_01/hlth_silc_01_1_Data.csv')
# print(eurostat_file)
# print(eurostat_file.values.tolist())

# eurostat_data_lists = eurostat_file.values.tolist()
# eurostat_data_tuples = [tuple(row) for row in eurostat_data_lists]
# for item in eurostat_data_tuples:
#     print(item)

from collections import defaultdict

written_eurostat_data = [('Belgium', 2017, 'Males', '1.8'), ('Belgium', 2017, 'Females', '2.3'), ('Bulgaria', 2017, 'Males', '1.8'),
('Bulgaria', 2017, 'Females', '1.8'), ('Czechia', 2017, 'Males', '2.1'), ('Czechia', 2017, 'Females', '2.7'), ('Denmark', 2017, 'Males', '3.3'),
('Denmark', 2017, 'Females', '2.7'), ('Germany', 2017, 'Males', '2.6'), ('Germany', 2017, 'Females', '2.9'), ('Estonia', 2017, 'Males', '3.6'),
('Estonia', 2017, 'Females', '4.3'), ('Ireland', 2017, 'Males', '0.5'), ('Ireland', 2017, 'Females', '0.8'), ('Greece', 2017, 'Males', '1.7'),
('Greece', 2017, 'Females', '2'), ('Spain', 2017, 'Males', '1.2'), ('Spain', 2017, 'Females', '1.3'), ('France', 2017, 'Males', '3.2'),
('France', 2017, 'Females', '4.3'), ('Croatia', 2017, 'Males', '3.6'), ('Croatia', 2017, 'Females', '3.9'), ('Italy', 2017, 'Males', '0.8'),
('Italy', 2017, 'Females', '1.3'), ('Cyprus', 2017, 'Males', '1.7'), ('Cyprus', 2017, 'Females', '0.7'), ('Latvia', 2017, 'Males', '5'),
('Latvia', 2017, 'Females', '6.3'), ('Lithuania', 2017, 'Males', '2.4'), ('Lithuania', 2017, 'Females', '3.3'), ('Luxembourg', 2017, 'Males', '4.2'),
('Luxembourg', 2017, 'Females', '4.1'), ('Hungary', 2017, 'Males', '2.8'), ('Hungary', 2017, 'Females', '3.7'), ('Malta', 2017, 'Males', '0.9'),
('Malta', 2017, 'Females', '0.4'), ('Netherlands', 2017, 'Males', '1.2'), ('Netherlands', 2017, 'Females', '1.6'), ('Austria', 2017, 'Males', '1.8'),
('Austria', 2017, 'Females', '2.4'), ('Poland', 2017, 'Males', '3.7'), ('Poland', 2017, 'Females', '3.7'), ('Portugal', 2017, 'Males', '3.8'),
('Portugal', 2017, 'Females', '4.8'), ('Romania', 2017, 'Males', '0.4'), ('Romania', 2017, 'Females', '0.5'), ('Slovenia', 2017, 'Males', '3.7'),
('Slovenia', 2017, 'Females', '3.3'), ('Slovakia', 2017, 'Males', '2.7'), ('Slovakia', 2017, 'Females', '2.7'), ('Finland', 2017, 'Males', '1.4'),
('Finland', 2017, 'Females', '1.8'), ('Sweden', 2017, 'Males', '1.3'), ('Sweden', 2017, 'Females', '2.5'), ('United Kingdom', 2017, 'Males', '1.7'),
('United Kingdom', 2017, 'Females', '2.6'), ('Belgium', 2018, 'Males', '2'), ('Belgium', 2018, 'Females', '2.5'), ('Bulgaria', 2018, 'Males', '1.5'),
('Bulgaria', 2018, 'Females', '1.5'), ('Czechia', 2018, 'Males', '2.3'), ('Czechia', 2018, 'Females', '2.8'), ('Denmark', 2018, 'Males', '2.5'),
('Denmark', 2018, 'Females', '3'), ('Germany', 2018, 'Males', '2.5'), ('Germany', 2018, 'Females', '2.5'), ('Estonia', 2018, 'Males', '4.7'),
('Estonia', 2018, 'Females', '4.4'), ('Ireland', 2018, 'Males', '0.7'), ('Ireland', 2018, 'Females', '0.6'), ('Greece', 2018, 'Males', '1'),
('Greece', 2018, 'Females', '1'), ('Spain', 2018, 'Males', '1.2'), ('Spain', 2018, 'Females', '2'), ('France', 2018, 'Males', '2.8'),
('France', 2018, 'Females', '4.3'), ('Croatia', 2018, 'Males', '3.3'), ('Croatia', 2018, 'Females', '3.8'), ('Italy', 2018, 'Males', '0.8'),
('Italy', 2018, 'Females', '1.3'), ('Cyprus', 2018, 'Males', '0.9'), ('Cyprus', 2018, 'Females', '0.9'), ('Latvia', 2018, 'Males', '3.1'),
('Latvia', 2018, 'Females', '4.3'), ('Lithuania', 2018, 'Males', '3.2'), ('Lithuania', 2018, 'Females', '2.9'), ('Luxembourg', 2018, 'Males', '5.1'),
('Luxembourg', 2018, 'Females', '5.3'), ('Hungary', 2018, 'Males', '2.7'), ('Hungary', 2018, 'Females', '3'), ('Malta', 2018, 'Males', '0.9'),
('Malta', 2018, 'Females', '1'), ('Netherlands', 2018, 'Males', '1.7'), ('Netherlands', 2018, 'Females', '1.2'), ('Austria', 2018, 'Males', '2.1'),
('Austria', 2018, 'Females', '2.2'), ('Poland', 2018, 'Males', '3.4'), ('Poland', 2018, 'Females', '2.9'), ('Portugal', 2018, 'Males', '3'),
('Portugal', 2018, 'Females', '5.3'), ('Romania', 2018, 'Males', '0.5'), ('Romania', 2018, 'Females', '0.4'), ('Slovenia', 2018, 'Males', '3.4'),
('Slovenia', 2018, 'Females', '3.5'), ('Slovakia', 2018, 'Males', '3.2'), ('Slovakia', 2018, 'Females', '3.5'), ('Finland', 2018, 'Males', '1.4'),
('Finland', 2018, 'Females', '1.9'), ('Sweden', 2018, 'Males', '1.6'), ('Sweden', 2018, 'Females', '3.1'), ('United Kingdom', 2018, 'Males', '2'),
('United Kingdom', 2018, 'Females', '2.8')]


# 1st Assignment - two dicts that group all data by country for each year
health_index_2017_males = {country: [sex, health_index] for country, year, sex, health_index in written_eurostat_data if year == 2017 and sex == 'Males'}
health_index_2017_females = {country: [sex, health_index] for country, year, sex, health_index in written_eurostat_data if year == 2017 and sex == 'Females'}
# print('Health Index for 2017, males: ', health_index_2017_males)
# print('Health Index for 2017, females: ', health_index_2017_females)

health_index_2017 = defaultdict(list)
for elems in (health_index_2017_males, health_index_2017_females):
    for key, values in elems.items():
        health_index_2017[key].append(values)
print('Health Index 2017: ', health_index_2017)

health_index_2018_males = {country: [sex, health_index] for country, year, sex, health_index in written_eurostat_data if year == 2018 and sex == 'Males'}
health_index_2018_females = {country: [sex, health_index] for country, year, sex, health_index in written_eurostat_data if year == 2018 and sex == 'Females'}
# print('Health Index for 2018, males: ', health_index_2018_males)
# print('Health Index for 2018, females: ', health_index_2018_females)

health_index_2018 = defaultdict(list)
for elems in (health_index_2018_males, health_index_2018_females):
    for key, values in elems.items():
        health_index_2018[key].append(values)
print('Health Index 2018: ', health_index_2018, '\n')


# 2nd Assignment - one dict that groups all data by year for Germany
germany_males = {year: [sex, health_index] for country, year, sex, health_index in written_eurostat_data if country == 'Germany' and sex == 'Males'}
germany_females = {year: [sex, health_index] for country, year, sex, health_index in written_eurostat_data if country == 'Germany' and sex == 'Females'}

germany = defaultdict(list)
for elems in (germany_males, germany_females):
    for key, values in elems.items():
        germany[key].append(values)
print('Health Index for Germany: ', germany, '\n')


# 3rd Assignment - one dict that groups all data by country and year, by using year in the key together with the country name
all_data_2017_males = {country: [year, sex, health_index] for country, year, sex, health_index in written_eurostat_data if year == 2017 and sex == 'Males'}
all_data_2017_females = {country: [year, sex, health_index] for country, year, sex, health_index in written_eurostat_data if year == 2017 and sex == 'Females'}
all_data_2018_males = {country: [year, sex, health_index] for country, year, sex, health_index in written_eurostat_data if year == 2018 and sex == 'Males'}
all_data_2018_females = {country: [year, sex, health_index] for country, year, sex, health_index in written_eurostat_data if year == 2018 and sex == 'Females'}

health_index_full_2017 = defaultdict(list)
for elems in (all_data_2017_females, all_data_2017_males):
    for key, values in elems.items():
        health_index_full_2017[key+'_'+str(2017)].append(values)

health_index_full_2018 = defaultdict(list)
for elems in ( all_data_2018_females, all_data_2018_males ):
    for key, values in elems.items():
        health_index_full_2018[key+'_'+str(2018)].append(values)

# print('All data in Health Index 2017: ', health_index_full_2017)
# print('All data in Health Index 2018: ', health_index_full_2018)

health_index_full = {**health_index_full_2017, **health_index_full_2018}
print('All data in Health Index 2017-2018', health_index_full, '\n')


# 4th Assignment - starting from the previous health_index dict, display only the data where the health_index > 5
health_index_greater_five = {key: [val for val in values if float(val[2]) > 5] for key, values in health_index_full.items()}
health_index_greater_five_optimised = {key: value for key, value in health_index_greater_five.items() if value}
print('Health index 2017-2018 greater than 5: ', health_index_greater_five_optimised, '\n')


# 5th Assignment - starting from the previous health_index dict, display only the data where the health_index > 5 and sex is ‘F’
health_index_five_female = {key: [val for val in values if val[1] == 'Females'] for key, values in health_index_greater_five_optimised.items()}
print('Health index 2017-2018 greater than 5 for women: ', health_index_five_female, '\n')


# 6th Assignment - starting from the previous health_index dict, create a for loop to print the health_index
for key, values in health_index_full.items():
    print(key, values)



# Alternative solution

health_2017 = defaultdict(list)
# for country, *_ in written_eurostat_data:
#     health_2017[country] = []
# print(health_2017)

# for country, year, sex, health_index in written_eurostat_data:
#     if year == 2017:
#         health_2017[country].append((sex, health_index))
# print('New version 2017 health overview: ',health_2017)

health_2017 = {country: [] for country, *_ in written_eurostat_data}
dummy_health = [health_2017[country].append((sex, health_index)) for country, year, sex, health_index in written_eurostat_data if year == 2017]
print('New version 2017 health overview: ', health_2017)

health_2018 = defaultdict(list)
health_2018 = {country: [] for country, *_ in written_eurostat_data}
dummy_health = [health_2018[country].append((sex, health_index)) for country, year, sex, health_index in written_eurostat_data if year == 2018]
print('New version 2018 health overview: ', health_2018)

germany_new = defaultdict(list)
dummy_health = [germany_new[country].append((sex, health_index)) for country, year, sex, health_index in written_eurostat_data if country == 'Germany']
print('New Germany 2017-2018 health overview: ', germany_new)

all_health = defaultdict(list)
all_health = {country: [] for country, *_ in written_eurostat_data}
dummy_health = [all_health[country].append((year, sex, health_index)) for country, year, sex, health_index in written_eurostat_data]
print('All health data 2017-2018: ', all_health)

# greater_than_five = defaultdict(list)
# greater_than_five = {country: [] for country, *_ in all_health}
# dummy_health = [greater_than_five[country].append(year, sex, health_index) for country, year, sex, health_index in all_health if float(health_index) > 5]
# print('Greater than five index new: ', greater_than_five)