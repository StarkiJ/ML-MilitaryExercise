def manual_operation(me):
    fid = 0
    count = 99999

    while True:
        command = input("Please enter your command:")
        if command == 'q':
            me.next_frame()
            break
        elif command == 'n':
            me.next_frame()
        elif command == 'f':
            fid = input("Enter the fighter ID: ")
        # move: command 为 0-3
        elif command in ['0', '1', '2', '3']:
            # fid = input("Enter the fighter ID: ")
            me.move(fid, command)
        elif command in ['4', '5', '6', '7']:
            command = int(command) - 4
            # fid = input("Enter the fighter ID: ")
            # count = input("Enter the number of attack: ")
            me.attack(fid, command, count)
        elif command == '8':
            # fid = input("Enter the fighter ID: ")
            # count = input("Enter the number of fuel: ")
            me.fuel(fid, count)
        elif command == '9':
            # fid = input("Enter the fighter ID: ")
            # count = input("Enter the number of missile: ")
            me.missile(fid, count)
        else:
            print("Invalid command.")
