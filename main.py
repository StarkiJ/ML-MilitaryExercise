from MilitaryExercise import MilitaryExercise
from manual_operation import manual_operation
from machine_operation import machine_operation


# from DQNway import machine_learning


def main():
    test_num = input("Enter number of testcase: ")
    input_path = './data2/testcase' + test_num + '.in'
    output_path = './data2/testcase' + test_num + '.out'

    me = MilitaryExercise(input_path)
    me.show_info()

    machine_operation(me, output_path)


if __name__ == "__main__":
    main()
