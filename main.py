a = ('key1', ' key2')
s = 7

men = dict.fromkeys(a, s)
car = {"brand": "Ford", "model": "Mustang", "year": 1964}

car2 = {"brand": "Ford", "model": "Mustang", "year": 1964}

x = car.get("model")
e = car2.items()
g = {'name': 'Madara', 'age': 150, 'eyes': 'rinnegan'}
g.keys()
z = {'Physics': 67, 'Chemistry': 72, 'Math': 89}
z.pop('Math')
person1 = {'name': 'naruta', 'age': 33, 'eyes': 'Kekkei Genkaya'}
person1.popitem()
person = {'name': 'naruta', 'age': 33, 'eyes': 'Kekkei Genkaya'}
person.setdefault('age')
marks = {'Physics': 67, 'Maths': 87}
marks.update({"color": "yellow"})
sales = {'apple': 2, 'orange': 3, 'grapes': 4}
sales["apple"] = 'kiwi'
sales.values()
d = {}

d[float('nan')] = 1
d[float('nan')] = 2
d[1.0] = 'float'
d[1] = 'int'
d[True] = 'bool'

if __name__ == '__main__':
    print(men)
    print(x)
    print(e)
    print(g)
    print(z)
    print(person1)
    print(person)
    print(marks)
    print(sales)
    print(d)