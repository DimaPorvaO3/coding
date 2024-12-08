a = "Hello World"
name = "Dima"
surname = "Porva"
age = 17
growth = 191
weight = 93.8
values_list = [a, name, surname, age, growth, weight]

types_list = []
for i in values_list:  
    types_list.append(type(i))  

types_count = {}
for t in types_list: 
    if t not in types_count:  
        types_count[t] = 1  
    else:
        types_count[t] += 1 

def find_most_frequent_type(count_dict):
    max_type = None
    max_count = 0
    for key in count_dict:  
        if count_dict[key] > max_count:  
            max_count = count_dict[key]
            max_type = key
    return max_type

most_frequent_type = find_most_frequent_type(types_count)

print("Список значень:", values_list)
print("Список типів:", types_list)
print("Найпоширеніший тип даних:", most_frequent_type)