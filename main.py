from MilitaryExercise import MilitaryExercise
from manual_operation import manual_operation
from machine_operation import machine_operation
# from DQNway import machine_learning


def main():
    me = MilitaryExercise('./data2/testcase3.in')
    me.show_info()

    print("Please choose a start mode:")
    print("1. Manual operation")
    print("2. Machine operation")
    print("3. Machine learning")
    print("q. Quit")

    while True:
        # choice = input("Enter choice: ")
        choice = '2'
        if choice == '1':
            manual_operation(me)
            break
        elif choice == '2':
            machine_operation(me)
            break
        elif choice == '3':
            # machine_learning()
            break
        elif choice == 'q':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
