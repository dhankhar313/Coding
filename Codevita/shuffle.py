y = input()
digits = [i for i in y]
for i in range(len(digits)):
    temp = digits[i]
    for j in range(len(digits) - 1):
        new_list = []
        new_list.insert(j, temp)
        for x in digits:
            if x not in new_list:
                new_list.append(x)
        num = "".join(new_list)
        print(num)
