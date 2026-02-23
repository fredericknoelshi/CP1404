# from operator import itemgetter
#
# data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]
#
# # name_width = max(len(str(item[0])) for item in data)
# # number_width = max(len(str(item[1])) for item in data)
#
# data.sort(key=itemgetter(1), reverse=True)
#
# for name, number in data:
#     print(f"{name:<15   } = {number:>5}")
#     # this is fine but can be better (avoid hard coding)
#
#     # print(f"{name:<{name_width}} = {number:>{number_width}}")

"""get method"""
# for word in words:
#       word_to_count[word] = word_to_count.get(word, 0) + 1
#       print(word, word_to_count[word])

# module_to_number = {"CP1401": 45, "CP1404": 78, "CP5639": 34}
# modules = ["CP1401", "CP1404", "CP5639"]
#
# for module in modules:
#     module_to_number[module] = module_to_number.get(module, 0) + 1
#     print(module, module_to_number[module])
#
# my_subjects = {"CP1401", "CP5639", "CP1404"}
# your_subjects = {"CP1401", "CP5966", "CP1404"}
#
# print(f"Union = {my_subjects | your_subjects}")
# print(f"Intersection = {my_subjects & your_subjects}")
# print(f"Difference = {my_subjects - your_subjects}")
# print(f"Symmetric difference = {my_subjects ^ your_subjects} ")

# flowers = ("cala lily", "rose", "rose", "tulip")
# numbers = {34, 56, 12, 90}

# print(dict(zip(flowers, numbers)))
# print(list(zip(flowers, numbers)))
# print(tuple(zip(flowers, numbers)))
# print(set(zip(flowers, numbers)))

import json
name_to_age = {}

from operator import itemgetter
data_dictionary = {'Derek': 7, 'Xavier': 80, 'Bob': 612, 'Chantanelle': 9}

name_width = max(len(str(name)) for name in data_dictionary.keys())
number_width = max(len(str(number)) for number in data_dictionary.values())

for name, number in sorted(data_dictionary.items(), key=itemgetter(1), reverse=True):
    print(f"{name:{name_width}} = {number:{number_width}}")