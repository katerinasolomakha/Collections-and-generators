queue = []

while True:
    command = input().strip()
    if command.startswith('push'):
        number = int(command.split()[1])
        queue.insert(0, number)
        print("ok")
    elif command == "pop":
        if len(queue)>0:
            print(queue.pop())
        else:
            print("error")
    elif command == "front":
        if len(queue)>0:
            print(queue[-1])
        else:
            print("error")
    elif command == "size":
        print(len(queue))
    elif command == "clear":
        queue.clear()
        print("ok")
    elif command == "exit":
        print("bye")
        break
    else:
        print("error")