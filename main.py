from MilitaryExercise import MilitaryExercise
from manual_operation import manual_operation
from machine_operation import machine_operation


# from DQNway import machine_learning


def main():
    print("Please choose a start mode:")
    print("1. Manual operation")
    print("2. Machine operation")
    print("3. Machine learning")
    print("q. Quit")

    test_num = input("Enter number of testcase: ")
    input_path = './data2/testcase' + test_num + '.in'
    output_path = './data2/testcase' + test_num + '.out'
    me = MilitaryExercise(input_path)
    me.show_info()

    while True:
        # choice = input("Enter choice: ")
        choice = '2'
        if choice == '1':
            manual_operation(me)
            break
        elif choice == '2':
            machine_operation(me, output_path)
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
