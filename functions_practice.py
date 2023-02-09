def hello():
    print("Greetings friend!")

def pack(arg_1, arg_2, arg_3):
    return [arg_1, arg_2, arg_3]

def eat_lunch(list):
    sentence = f"First I eat {list[0]}"
    if list:
        for item in list[1::]:
            sentence += f", Next I eat {item}"
        print (sentence)
    else:
        print("My lunchbox is empty!")

list = ["apple", "pie", "rice", "chicken"]

hello()
print(pack(3, 5, 2))
eat_lunch(list)