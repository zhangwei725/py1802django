from django.test import TestCase

# Create your tests here.

dic = {'1': 2, '2': 4}
for d in dic:
    print(d)

for key in dic.keys():
    print(key)

for value in dic.values():
    print(value)

for key, value in dic.items():
    print(key)
    print(value)
