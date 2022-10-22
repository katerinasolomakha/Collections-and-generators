queue = []

while True:
    command = input().strip()
    if command.startswith('push'):
        number = int(command.split()[1])
        queue.insert(0, number)
        print("ok")
    elif command == "pop":
        print(queue.pop())
    elif command == "front":
        print(queue[-1])
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