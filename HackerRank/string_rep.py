def repeated_string(string, num):
    initial_count = string.count("a")
    str_len = len(string)
    if num > str_len:
        if num % str_len == 0:
            return int(initial_count * (num / str_len))
        else:
            temp = string[0:num % str_len].count("a")
            return int((initial_count * (num - (num % str_len)) / str_len) + temp)
    else:
        return int(string[0:num].count("a"))


line = input()
length = int(input())
print(repeated_string(line, length))
