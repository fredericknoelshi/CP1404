# from operator import itemgetter
#
# data = [["Lea",34], ["Sam",24],["Eve", 67]]
#
# data.sort()
# print(data)
#
# data.sort(key=itemgetter(1))
# print(data)
#
# data.sort(key=itemgetter(1), reverse=True)
# print(data)


# words = "This is Python"
# print(words)
#
# words = words.split()
# print(words)
#
# words.append("is")
# print(words)
#
# print([word for word in words])


# numbers = [23, 67, 45, 23]
# new_numbers = []
#
# for number in numbers:
#     total = number * 2
#     new_numbers.append(total)
#
# print(new_numbers)
#
# print([number * 2 for number in numbers])
# # instead of using append
# # formula: Action for X in Xs
#
# print([number * 2 for number in numbers if number > 50])


# words = "This is Python"
# print(words)
# words = words.split()
#
# print([word for word in words if len(word) > 2])
# print([len(word) for word in words])
# print([word.upper() for word in words])


# cars = [["Audi",2006], ["BMW",2016], ["Jaguar",2026]]
# print([tuple(car) for car in cars])
# print([car[0] for car in cars])
# print([year[1] * 2 for year in cars])
# print(min((car[1]) for car in cars))


# x=3
# z=4
# print(x==z)

# numbers = [12, 45, 67]
# new_numbers = numbers
#
# numbers_2 = [12, 45, 67]
#
# print(new_numbers is numbers)
# print(numbers is numbers_2)
# print(new_numbers == numbers)
# print(numbers == numbers_2)
# # "==" is different from "is"

# things = []
#
# for x in range(1, 4):
#     for y in range(1, 4):
#         things.append(x + y)
#
# print(things)
# print([x+y for x in range(1, 4) for y in range(1, 4)])

names = ["Ada", "Alan", "Bill", "John"]
print(", ".join(names))
name_to_remove = input("Who do you want to remove? ")
# if name_to_remove == "" or name_to_remove not in names:
#     print("Invalid input")
while name_to_remove != "":
    try:
        names.remove(name_to_remove)
        print(names)
    except ValueError:
        print("Value not in list")
    name_to_remove = input("Who do you want to remove? ")