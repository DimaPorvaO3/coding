info = {
    "name": "Dima",
    "age": 17,
    "contact": {
        "email": "dimaporva2007@gmail.com",
        "country": "Ukraine",
        "city": "Lutsk",
        "street": "Defenders of Ukraine ",
        "house_number": 1},
    "student": True}

type_info = {}
for key, value in info.items():
    if type(value) == dict:
        for nested_key, nested_value in value.items():
            type_info[nested_key] = type(nested_value)
    else:
        type_info[key] = type(value)

print(type_info)