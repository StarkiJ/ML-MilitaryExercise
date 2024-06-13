import read_data


class MilitaryExercise():
    def __init__(self, file_path):
        max_row, max_col, map_info, blue_bases, red_bases, fighters = read_data.read_data(file_path)
        self.max_row = max_row
        self.max_col = max_col
        self.map_info = map_info
        self.blue_bases = blue_bases
        self.red_bases = red_bases
        self.fighters = fighters

    def show_info(self):
        print("map_info:", self.max_row, self.max_col)
        for row in self.map_info:
            print(row)
        print()
        print("blue_bases:", len(self.blue_bases))
        for blue_base in self.blue_bases:
            blue_base.show_info()
        print()
        print("red_bases:", len(self.red_bases))
        for red_base in self.red_bases:
            red_base.show_info()
        print()
        print("fighters:", len(self.fighters))
        for fighter in self.fighters:
            fighter.show_info()
