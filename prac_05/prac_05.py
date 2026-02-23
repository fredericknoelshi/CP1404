from operator import itemgetter

data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]

# name_width = max(len(str(item[0])) for item in data)
# number_width = max(len(str(item[1])) for item in data)

data.sort(key=itemgetter(1), reverse=True)

for name, number in data:
    print(f"{name:<15   } = {number:>5}")
    # this is fine but can be better (avoid hard coding)

    # print(f"{name:<{name_width}} = {number:>{number_width}}")
