
def combiner(list):
    new_list = []
    sum = 0

    for item in list:
        if isinstance(item, str):
            new_list.append(item)
        elif isinstance(item, (int, float)):
            sum += item
    new_list.append(sum)
    return ''.join(map(str, new_list))

my_list = ["apple", 5.2, "dog", 8]
print(combiner(my_list))

