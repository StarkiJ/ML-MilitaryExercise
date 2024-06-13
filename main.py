import read_data
from MilitaryExercise import MilitaryExercise


def output_commands(commands):
    for command in commands:
        print(command)
    print("OK")


def main():
    military_exercise = MilitaryExercise('./data/testcase1.in')
    military_exercise.show_info()
    for i in range(len(military_exercise.fighters)):
        military_exercise.move(i, 1)
    military_exercise.show_info()

    commands = []


if __name__ == "__main__":
    main()
