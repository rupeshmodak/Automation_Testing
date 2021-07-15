import json

str_courses = '{"name": "rupesh modak", "languages": ["java", "python"]}'
print(type(str_courses))
dict_courses = json.loads(str_courses)
print(type(dict_courses))
print(dict_courses)
print(dict_courses['name'])
languages = dict_courses['languages']
print(languages)
print(languages[0])
print(languages[1])

print("___________________________________________")

with open("C:\\Users\\Aparna\\PycharmProjects\\API\\json.txt") as file:
    data = json.load(file)
    print(data)
    print(type(data))
    print(data['array'][2])
    print(data['object'][0])
    print(data['string'])
    print(type(data['object']))
    for result in data['object']:
        if result['name'] == 'Rupesh':
            print(result['age'])
            assert result['age'] == 30

print("___________________________________________")

with open("C:\\Users\\Aparna\\PycharmProjects\\API\\json1.txt") as file1:
    data1 = json.load(file1)
    print(data == data1)
    assert data == data1


