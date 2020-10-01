
# WORK IN PROGRESS

description = ('Country', [
    '2011 ', '2012 ', '2013 ', '2014 ', '2015 ', '2016 ', '2017 ', '2018 ',
    '2019 '
])

raw_data = [
    ('AL', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '84 ', ': ']),
    ('AT', ['75 ', '79 ', '81 ', '81 ', '82 ', '85 ', '89 ', '89 ', '90 ']),
    ('BA', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '69 ', '72 ']),
    ('BE', ['77 ', '78 ', '80 ', '83 ', '82 ', '85 ', '86 ', '87 ', '90 ']),
    ('BG', ['45 ', '51 ', '54 ', '57 ', '59 ', '64 ', '67 ', '72 ', '75 ']),
    ('CH', [': ', ': ', ': ', '91 ', ': ', ': ', '93', ': ', '96 ']),
    ('CY', ['57 ', '62 ', '65 ', '69 ', '71 ', '74 ', '79 ', '86 ', '90 ']),
    ('CZ', ['67 ', '73 ', '73 ', '78 ', '79 ', '82 ', '83 ', '86 ', '87 ']),
    ('DE', ['83 ', '85 ', '88 ', '89 ', '90 ', '92 ', '93 ', '94 ', '95 ']),
    ('DK', ['90 ', '92 ', '93 ', '93 ', '92 ', '94 ', '97 ', '93 ', '95 ']),
    ('EA', ['74 ', '76 ', '79 ', '81 ', '83 ', '85 ', '87 ', '89 ', '90 ']),
    ('EE', ['69 ', '74 ', '79 ', '83 ', '88 ', '86 ', '88 ', '90 ', '90 ']),
    ('EL', ['50 ', '54 ', '56 ', '66 ', '68 ', '69 ', '71 ', '76 ', '79 ']),
    ('ES', ['63 ', '67 ', '70 ', '74 ', '79 ', '82 ', '83 ', '86 ', '91 ']),
    ('FI', ['84 ', '87 ', '89 ', '90 ', '90 ', '92 ', '94 ', '94 ', '94 ']),
    ('FR', ['76 ', '80 ', '82 ', '83 ', '83 ', '86 ', '86 ', '89 ', '90 ']),
    ('HR', ['61 ', '66 ', '65 ', '68 ', '77 ', '77 ', '76 ', '82 ', '81 ']),
    ('HU', ['63 ', '67 ', '70 ', '73 ', '76 ', '79 ', '82 ', '83 ', '86 ']),
    ('IE', ['78 ', '81 ', '82 ', '82 ', '85 ', '87 ', '88 ', '89 ', '91 ']),
    ('IS', ['93 ', '95 ', '96 ', '96 ', ': ', ': ', '98 ', '99 ', '98 ']),
    ('IT', ['62 ', '63 ', '69 ', '73 ', '75 ', '79 ', '81 ', '84 ', '85 ']),
    ('LT', ['60 ', '60 ', '65 ', '66 ', '68 ', '72 ', '75 ', '78 ', '82 ']),
    ('LU', ['91 ', '93 ', '94 ', '96 ', '97 ', '97 ', '97 ', '93', '95 ']),
    ('LV', ['64 ', '69 ', '72 ', '73 ', '76 ', '77 ', '79 ', '82 ', '85 ']),
    ('ME', [': ', '55 ', ': ', ': ', ': ', ': ', '71 ', '72 ', '74 ']),
    ('MK', [': ', '58 ', '65 ', '68 ', '69 ', '75 ', '74 ', '79 ', '82 ']),
    ('MT', ['75 ', '77 ', '78 ', '80 ', '81 ', '81 ', '85 ', '84 ', '86 ']),
    ('NL', ['94 ', '94 ', '95 ', '96 ', '96 ', '97 ', '98 ', '98 ', '98 ']),
    ('NO', ['92 ', '93 ', '94 ', '93 ', '97 ', '97 ', '97 ', '96 ', '98 ']),
    ('PL', ['67 ', '70 ', '72 ', '75 ', '76 ', '80 ', '82 ', '84 ', '87 ']),
    ('PT', ['58 ', '61 ', '62 ', '65 ', '70 ', '74 ', '77 ', '79 ', '81 ']),
    ('RO', ['47 ', '54 ', '58 ', '61', '68 ', '72 ', '76 ', '81 ', '84 ']),
    ('RS', [': ', ': ', ': ', ': ', '64 ', ': ', '68 ', '73 ', '80 ']),
    ('SE', ['91 ', '92 ', '93 ', '90 ', '91 ', '94 ', '95 ', '93 ', '96 ']),
    ('SI', ['73 ', '74 ', '76 ', '77 ', '78 ', '78 ', '82 ', '87 ', '89 ']),
    ('SK', ['71 ', '75 ', '78 ', '78 ', '79 ', '81 ', '81 ', '81 ', '82 ']),
    ('TR', [': ', '47 ', '49 ', '60 ', '70 ', '76 ', '81 ', '84 ', '88 ']),
    ('UK', ['83 ', '87 ', '88 ', '90 ', '91 ', '93 ', '94 ', '95 ', '96 ']),
    ('XK', [': ', ': ', ': ', ': ', ': ', ': ', '89 ', '93 ', '93 ']),
]

# 1 Function that prepares the dataset


def prep_dataset(years, dataset):
    country_dict = {country: [] for country, *_ in dataset}

    length_years = len(years[1])

    for num in range(length_years):
        for country, elements in dataset:
            if elements[num] != ': ':
                country_dict[country].append({'year': years[1][num], 'coverage': int(elements[num].strip())})
            else:
                country_dict[country].append({'year': years[1][num], 'coverage': 0})

    return country_dict


full_dataset = prep_dataset(description, raw_data)
print('This is the revised dataset: ', full_dataset, '\n')


# 2 Function to retrieve data for each year


def year_data(dataset, year):
    year_dict = {year.strip(): []}
    # print(year_dict, '\n')

    for country, element in dataset.items():
        for entry in element:
            if entry['year'].strip() == year:
                year_dict[entry['year'].strip()].append((country, entry['coverage']))

    return year_dict


data_from_year = year_data(full_dataset, '2011')
print('The data for the year is: ', data_from_year, '\n')

data_from_year = year_data(full_dataset, '2013')
print('The data for the year is: ', data_from_year, '\n')


# 3 Function to retrieve data for each country


def country_data(dataset, country):
    country_dict = {country: []}
    # print(country_dict, '\n')

    for countries, elements in dataset.items():
        if countries == country:
            for entry in elements:
                country_dict[country].append((entry['year'].strip(), entry['coverage']))

    return country_dict


data_from_country = country_data(full_dataset, 'AL')
print('The data for the country is: ', data_from_country, '\n')

data_from_country = country_data(full_dataset, 'BG')
print('The data for the country is: ', data_from_country, '\n')

# 4 Function to perform average from an iterable (year or country data)


def average_data(iterable):
    number_elements = len(iterable)
    if number_elements == 0:
        return 'No elements in list. Cannot perform average'
    sum_coverage = 0

    for element in iterable:
        sum_coverage += element[1]

    average = sum_coverage/number_elements
    return average


data_from_country = country_data(full_dataset, 'BE')
data_from_year = year_data(full_dataset, '2013')

print('Average coverage for the country is: ', average_data(data_from_country['BE']), '\n')
print('Average coverage for the year is: ', average_data(data_from_year['2013']), '\n')