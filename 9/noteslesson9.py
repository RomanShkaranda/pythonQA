

def maleware_sms():
    pass



def string_cutter(string, max_alloswed_length=70):
    """
    Function cuts the given string
    :param string (str):
    :param max_alloswed_length (int):
    :return: (str)
    """
    if len(string) <= max_alloswed_length:
        return string
    else:
        result = string[:max_alloswed_length - 3] + "..."
        return result


print(len(string_cutter("*" * 200, 80)))
print(string_cutter("*" * 200, 10))


assert type(string_cutter("")) == str
assert type(string_cutter("*" * 200))
assert len(string_cutter("*" * 200, 80)) == 80
assert len(string_cutter("*" * 50, 80)) <= 80
assert string_cutter("*" * 100, 80)[-3:] == "..."
# assert string_cutter("*" * 50, 80)[-3:] == "***"









