n = print


def dec(func):
    def wrapper(*args, **kwargs):
        user = input("Login >>> ")
        if kwargs.get("Login ") != "bond":
            print("OUT!")
            return False

        result = func(*args, **kwargs)
        return result

    return wrapper

@dec
def foo(par, login):
    return par*2, login

# foo = dec(foo)
print(foo(5, login="bond"))








