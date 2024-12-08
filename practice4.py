my_list = [ 3, 1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Привіт', 'анаконда']

def remove_duplicates(lst):
    result = []
    for element in lst:
        if element not in result:
            result.append(element)
    return result

def sort_list(lst):
    nums = []
    words = []

    for element in lst:
        if type(element) == int or type(element) == float:
            nums.append(element)
        elif type(element) == str:
            words.append(element)

    nums.sort()
    words.sort()

    return nums + words

unique_list = remove_duplicates(my_list)
print("Список без повторень:", unique_list)

sorted_list = sort_list(unique_list)
print("Відсортований список:", sorted_list)