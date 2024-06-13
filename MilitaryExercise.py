import read_data


class MilitaryExercise:
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    fight_action = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    moved = []

    def __init__(self, file_path):
        max_row, max_col, map_info, blue_bases, red_bases, fighters = read_data.read_data(file_path)
        self.max_row = max_row
        self.max_col = max_col
        self.map_info = map_info
        self.blue_bases = blue_bases
        self.red_bases = red_bases
        self.fighters = fighters
        self.fighters_num = len(fighters)
        self.Score = 0
        self.Frame = 0

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
        print()
        print("Score:", self.Score, ", Frame:", self.Frame)

    def next_frame(self):
        self.Frame += 1
        self.moved = []
        print("Score:", self.Score, ", Frame:", self.Frame)

    # 该指令表示战斗机的移动。第一个参数为移动的战斗机编号，第二个参数为移动方向的编号。
    # 0 1 2 3 分别表示 “上、下、左、右”。
    # 若一帧内对同一战斗机输出多条 move 指令，只执行第一条合法的 move 指令，忽略其余指令。
    def move(self, fid, dire):
        fid = int(fid)
        dire = int(dire)
        # 一帧内只能移动一次
        if fid in self.moved:
            print("[WARNING] move <{}> <{}>: Fighter has already moved".format(fid, dire))
            return
        # 检查参数
        if not (0 <= dire < 4 and 0 <= fid < self.fighters_num):
            print("[WARNING] move <{}> <{}>: Invalid parameter(s)".format(fid, dire))
            return
        # 检查是否还有燃料
        fight = self.fighters[fid]
        if fight.fuel < 1:
            print("[WARNING] move <{}> <{}>: No fuel to fly".format(fid, dire))
            return

        tmp_row = fight.row + self.direction[dire][0]
        tmp_col = fight.col + self.direction[dire][1]
        # 检查是否越界
        if not (0 <= tmp_row < self.max_row and 0 <= tmp_col < self.max_col):
            print("[WARNING] move <{}> <{}>: Fighter will be out of bound".format(fid, dire))
            return
        # 检查是否可以通行
        if self.map_info[tmp_row][tmp_col] == "#":
            print("[WARNING] move <{}> <{}>: Can't pass a non-destroyed red base ({},{})".format(fid, dire, tmp_row,
                                                                                                 tmp_col))
            return
        fight.fuel -= 1
        fight.row = tmp_row
        fight.col = tmp_col
        self.moved.append(fid)
        print("[INFO] move <{}> <{}>: ({},{})".format(fid, dire, tmp_row, tmp_col))

    # 该指令表示战斗机的进攻。第一个参数为进攻的战斗机编号，第二个参数为攻击方向的编号，
    # 0 1 2 3 分别表示 “上、下、左、右”，第三个参数为投放导弹数量。
    def attack(self, fid, dire, count):
        fid = int(fid)
        dire = int(dire)
        count = int(count)
        # 检查参数
        if not (0 <= dire < 4 and 0 <= fid < self.fighters_num and 0 < count):
            print("[WARNING] attack <{}> <{}> <{}>: Invalid parameter(s)".format(fid, dire, count))
            return
        fight = self.fighters[fid]
        # 检查导弹是否足够
        if fight.missile < count:
            print("[WARNING] attack <{}> <{}> <{}>: No enough missile(s)".format(fid, dire, count))
            count = fight.missile

        tmp_row = fight.row + self.direction[dire][0]
        tmp_col = fight.col + self.direction[dire][1]
        # 检查是否越界
        if not (0 <= tmp_row < self.max_row and 0 <= tmp_col < self.max_col):
            print("[WARNING] attack <{}> <{}> <{}>: Invalid target".format(fid, dire, count))
            return
        # 检查是否为敌方基地
        if not self.map_info[tmp_row][tmp_col] == "#":
            print("[WARNING] attack <{}> <{}> <{}>: Invalid target".format(fid, dire, count))
            return
        # 寻找对应的敌方基地
        for red_base in self.red_bases:
            if red_base.row == tmp_row and red_base.col == tmp_col:
                if red_base.defense < count:
                    count = red_base.defense
                fight.missile -= count
                red_base.defense -= count
                if red_base.defense <= 0:
                    self.map_info[red_base.row][red_base.col] = "0"
                    self.Score += red_base.military_value
                    print("[INFO] attack <{}> <{}> <{}>: Red base destroyed (Score: {})".format(fid, dire, count,
                                                                                                self.Score))
                else:
                    print("[INFO] attack <{}> <{}> <{}>: Red base damaged (defense: {})".format(fid, dire, count,
                                                                                                red_base.defense))
                return
        print("[ERROR] attack <{}> <{}> <{}>".format(fid, dire, count))

    # 该指令表示为战斗机添加燃油。第一个参数为添加燃油的战斗机编号，第二个参数为添加燃油的数量。
    def flue(self, fid, count):
        fid = int(fid)
        count = int(count)
        # 检查参数
        if not (0 <= fid < self.fighters_num and 0 < count):
            print("[WARNING] flue <{}> <{}>: Invalid parameter(s)".format(fid, count))
            return

        fight = self.fighters[fid]
        # 检查是否在蓝色基地
        if not self.map_info[fight.row][fight.col] == "*":
            print("[WARNING] flue <{}> <{}>: Not at a blue base".format(fid, count))
            return
        # 检查是否超过最大容量
        if fight.fuel + count > fight.max_fuel:
            print("[WARNING] flue <{}> <{}>: No enough capacity".format(fid, count))
            count = fight.max_fuel - fight.fuel
        # 寻找对应的蓝色基地
        for blue_base in self.blue_bases:
            if blue_base.row == fight.row and blue_base.col == fight.col:
                if blue_base.fuel_reserve < count:
                    print("[WARNING] flue <{}> <{}>: No enough supplies".format(fid, count))
                    count = blue_base.fuel_reserve
                blue_base.fuel_reserve -= count
                fight.fuel += count
                print("[INFO] flue <{}> <{}>: Fuel added ({}/{})".format(fid, count, fight.fuel, fight.max_fuel))
                return
        print("[ERROR] flue <{}> <{}>".format(fid, count))

    # 该指令表示为战斗机添加导弹。第一个参数为添加导弹的战斗机编号，第二个参数为添加导弹的数量。
    def missile(self, fid, count):
        fid = int(fid)
        count = int(count)
        # 检查参数
        if not (0 <= fid < self.fighters_num and 0 < count):
            print("[WARNING] missile <{}> <{}>: Invalid parameter(s)".format(fid, count))
            return

        fight = self.fighters[fid]
        # 检查是否在蓝色基地
        if not self.map_info[fight.row][fight.col] == "*":
            print("[WARNING] missile <{}> <{}>: Not at a blue base".format(fid, count))
            return
        # 检查是否超过最大容量
        if fight.missile + count > fight.max_missile:
            print("[WARNING] missile <{}> <{}>: No enough capacity".format(fid, count))
            count = fight.max_missile - fight.missile
        # 寻找对应的蓝色基地
        for blue_base in self.blue_bases:
            if blue_base.row == fight.row and blue_base.col == fight.col:
                if blue_base.missile_reserve < count:
                    print("[WARNING] missile <{}> <{}>: No enough supplies".format(fid, count))
                    count = blue_base.missile_reserve
                blue_base.missile_reserve -= count
                fight.missile += count
                print("[INFO]missile <{}> <{}>: Missile added ({}/{})".format(fid, count, fight.missile,
                                                                              fight.max_missile))
                return
        print("[ERROR]missile <{}> <{}>".format(fid, count))
