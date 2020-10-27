'''
In a small town the population is p0 at the beginning of a year. The population regularly increases by x percent per year
and moreover y new inhabitants per year come to live in the town. How many years does the town need to see its population
greater or equal to p inhabitants?
'''


def nb_year(p0, percent, aug, p):
    years_needed = 0
    while p0 < p:
        p0 += p0* (percent/100) + aug
        years_needed += 1
    return years_needed


print('Number of years needed to reach target population: ', nb_year(1500, 4, 10, 3500))
print('Number of years needed to reach target population: ', nb_year(500, 7, 100, 1200))