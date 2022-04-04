


def num1():
    x = [[5, 2, 3], [10, 8, 9]]
    students = [
        {'first_name': 'Michael', 'last_name': 'Jordan'},
        {'first_name': 'John', 'last_name': 'Rosales'}
    ]
    sports_directory = {
        'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
        'soccer': ['Messi', 'Ronaldo', 'Rooney']
    }
    z = [{'x': 10, 'y': 20}]
    # number 1
    z[0].update({'x': 15})
    # number 2
    students[0].update({'last_name': 'Bryant'})
    # number 3
    test = sports_directory.get('soccer')
    test[0] = 'Andres'
    sports_directory.update({'soccer': list(test)})
    # number 4
    z[1].update({'z': 30})

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


def iterateDictionary(some_list):
    for i in students:
        key_names = []
        values = []
        for x in i:
            key_names.append(x)
            values.append(i[x])
        print(str(key_names[0]) + ' - ' + str(values[0]) + ', ' + str(key_names[1]) + ' - ' + str(values[1]))


# iterateDictionary(students)

# number 3
def iterateDictionary2(key_name, some_list):
    for i in some_list:
        for x in i:
            if x == key_name:
                print(i[x])


# iterateDictionary2('last_name', students)

def printinfo(some_dict):
    for i in some_dict:
        test = some_dict[i]
        len_value = len(some_dict[i])
        print(str(len_value) + ' ' + str(i))
        for x in range(len(test)):
            print(test[x])
    pass


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printinfo(dojo)
# output:

