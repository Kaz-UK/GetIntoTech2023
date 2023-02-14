#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# Add code to print a line of hyphens the same length as the Belgium string

print(len(Belgium) * "-")

# # Alternative version
# for text_string in Belgium:
#     print(text_string.replace(text_string, "-"), end="")

print(Belgium.replace(",", ":"))

# Followed by the population of Belgium plus the population of the capital city

country_list = Belgium.split(",")
print(int(country_list[1]) + int(country_list[3]))

# # Alternative version
# population_Belgium = Belgium[8:16]
# population_capital = Belgium[26:32]
# print(int(population_Belgium) + int(population_capital))
