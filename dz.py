#---------------------------Task 1---------------------------#
def in_dict(dictionary, key):
    return key in dictionary

my_dict = {
    "Name": "Vlad",
    "surname": "Babinsky",
    "age": 21,
    "city": "Bohorodchany"
}
print(in_dict(my_dict, "age"))
print(in_dict(my_dict, "email"))

#---------------------------Task 2---------------------------#

# def get_keys(i, val):
#     keys = []
#     for key in i:
#         if i[key] == val:
#             keys.append(key)
#     return keys

# my_dict = {
#     "Name": "Vlad",
#     "surname": "Babinsky",
#     "age": "15",
#     "city": "Bohorodchany"
# }
# print(get_keys(my_dict, "Bohorodchany"))


#---------------------------Task 3---------------------------#

# student = {
#     'name': 'Ivan', 
#     'surname': 'Ivanovich',
#     'age': 20,
#     'faculty': 'Computer Science'
# }

# print('name : ', student['name'])
# print('faculty:', student['faculty'])

# student['average score'] = 10.5

# print('Оновлений словник:', student)
