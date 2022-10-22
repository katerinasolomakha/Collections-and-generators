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
        if len(dec)>0:
            print(dec.pop(-1))
        else:
            print("error")
    elif command.startswith('pop_back'):
        if len(dec)>0:
            print(dec.pop(0))
        else:
            print("error")
    elif command == "front":
        if len(dec)>0:
            print(dec[0])
        else:
            print("error")
    elif command == "back":
        if len(dec)>0:
            print(dec[-1])
        else:
            print("error")
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
