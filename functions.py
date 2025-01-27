# Argument: det vi skickar till funktionen
# Parameter: variablerna som skapas inuti funktionen

def hello(username):
    if username == "":
        print("Hello guest!")
    else:
        print(f"Hello {username}!")
    print("Nice to meet you.")

#hello("David")
#hello("Krister")
#hello("Pia")
#hello("")

def add(x, y):
    print("add 1")
    print("add 2")
    return x + y

result = add(5, 10)
print(result)

def fun(a, b):
    print(f"a är: {a}")
    print(f"b är: {b}")

fun(b="aaaa", a="bbbb")


def get_user_input():
    return input("Please enter a value: ")


