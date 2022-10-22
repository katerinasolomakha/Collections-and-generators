dec = []

while True:
    command = input().strip()
    if command.startswith('push_front'):
        number = int(command.split()[1])
        dec.append(number)
        print("ok")
    elif command.startswith('push_back'):
        number = int(command.split()[1])
        dec.insert(-1, number)
        print("ok")
    elif command.startswith('pop_front'):
        print(dec.pop(-1))
    elif command.startswith('pop_back'):
        print(dec.pop(0))
    elif command == "front":
        print(dec[0])
    elif command == "back":
        print(dec[-1])
    elif command == "size":
        print(len(dec))
    elif command == "clear":
        dec.clear()
        print("ok")
    elif command == "exit":
        print("bye")
        break
    else:
        print("error")
