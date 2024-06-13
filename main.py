import read_data
from MilitaryExercise import MilitaryExercise


def manual_operation():
    me = MilitaryExercise('./data/testcase1.in')
    me.show_info()
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
            # count = input("Enter the number of flue: ")
            me.flue(fid, count)
        elif command == '9':
            # fid = input("Enter the fighter ID: ")
            # count = input("Enter the number of missile: ")
            me.missile(fid, count)
        else:
            print("Invalid command.")


def main():
    print("Please choose a start mode:")
    print("1. Manual operation")
    print("2. Machine learning")
    print("3. Exit")

    while True:
        choice = input("Enter 1 or 2: ")
        if choice == '1':
            manual_operation()
            break
        elif choice == '2':
            # start_mode_2()
            break
        elif choice == 'q':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
