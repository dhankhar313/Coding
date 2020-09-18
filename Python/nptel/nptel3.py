import random

dict_age = {}
dict_age["Arun"] = 2
dict_age["Bhima"] = 1
dict_age["Chirag"] = 4000
dict_age["Deepak"] = 30

l = list(dict_age.values())
dict1 = {}
l_name = dict_age.keys()
i = 0
prev = 0
for each in dict_age:
    dict1[each] = prev + l[i]
    prev = dict1[each]
    i += 1
print(dict1)

r = random.randint(0, sum(dict_age.values()))
print(r)
for each in dict1:
    if r < dict1[each]:
        print("Give all my money to", each)
        break
