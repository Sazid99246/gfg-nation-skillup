# insert into dictionary
def insert_dict(query, dict):
    command, key, value = query
    dict[key] = value


# deleting from dictionary
def del_dict(query, dict):
    command, key = query
    if key in dict:
        del dict[key]


# print marks of required name
def print_dict(key, dict):
    if key in dict:
        print(f"Marks of {key} is {dict[key]}")
    else:
        print(-1)
