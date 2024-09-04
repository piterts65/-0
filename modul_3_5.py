def get_multiplied_digits(namber):
    str_number = str(namber)
    first = int(str_number[0])
    if int(len(str_number)) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

result = get_multiplied_digits(2022)
print(result)