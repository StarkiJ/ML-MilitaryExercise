from collections import deque
import read_data


class MilitaryExercise:
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def __init__(self, input_path):
        max_row, max_col, map_info, blue_bases, red_bases, fighters, max_score = read_data.read_data(input_path)
        self.max_row = max_row
        self.max_col = max_col
        self.map_info = map_info
        self.blue_bases = blue_bases
        self.red_bases = red_bases
        self.fighters = fighters
        self.max_score = max_score
        self.fighters_num = len(fighters)
        self.score = 0
        self.frame = 0
        self.targets = []
        self.paths = []
        self.moved = []
        self.commands = []
        for _ in range(self.fighters_num):
            self.moved.append(False)
            self.targets.append((-1, -1))
            self.paths.append([])

    def show_info(self):
        print("map_info:", self.max_row, self.max_col)
        for row in self.map_info:
            print(row)
        print()
        print("blue_bases:", len(self.blue_bases))
        for blue_base in self.blue_bases.values():
            blue_base.show_info_line()
        print()
        print("red_bases:", len(self.red_bases))
        for red_base in self.red_bases.values():
            red_base.show_info_line()
        print()
        print("fighters:", len(self.fighters))
        for fighter in self.fighters:
            fighter.show_info_line()
        print()
        print("max_score:", self.max_score)
        print()
        print("Score:", self.score, ", Frame:", self.frame)

    def next_frame(self):
        self.frame += 1
        for fid in range(self.fighters_num):
            self.moved[fid] = False
        print("Score:", self.score, ", Frame:", self.frame)
        self.commands.append("Score: {}, Frame: {}".format(self.score, self.frame))

    # 该指令表示战斗机的移动。第一个参数为移动的战斗机编号，第二个参数为移动方向的编号。
    # 0 1 2 3 分别表示 “上、下、左、右”。
    # 若一帧内对同一战斗机输出多条 move 指令，只执行第一条合法的 move 指令，忽略其余指令。
    def move(self, fid, dire):
        fid = int(fid)
        dire = int(dire)
        # 一帧内只能移动一次
        if self.moved[fid]:
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
            # self.move(fid, (dire + 2) % 4)
            # self.targets[fid] = (-1, -1)
            self.targets[fid] = (-1, 0)
            return
        fight.fuel -= 1
        fight.row = tmp_row
        fight.col = tmp_col
        self.moved[fid] = True
        print("[INFO] move <{}> <{}>: ({},{})".format(fid, dire, tmp_row, tmp_col))
        self.commands.append("[INFO] move <{}> <{}>:".format(fid, dire))

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
        red_base = self.red_bases[(tmp_row, tmp_col)]
        # 避免浪费导弹
        if red_base.defense < count:
            count = red_base.defense
        fight.missile -= count
        red_base.defense -= count
        # 敌方基地被摧毁
        if red_base.defense <= 0:
            self.map_info[tmp_row][tmp_col] = "0"
            self.red_bases.pop((tmp_row, tmp_col))
            self.score += red_base.military_value
            print("[INFO] attack <{}> <{}> <{}>: Red base destroyed (Score: {})".format(fid, dire, count,
                                                                                        red_base.military_value))
        else:
            print("[INFO] attack <{}> <{}> <{}>: Red base damaged (defense: {})".format(fid, dire, count,
                                                                                        red_base.defense))
        self.commands.append("INFO] attack <{}> <{}> <{}>: ".format(fid, dire, count))
        return

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
        # 寻找对应的蓝色基地
        blue_base = self.blue_bases[(fight.row, fight.col)]
        if blue_base.fuel_reserve < count:
            print("[WARNING] flue <{}> <{}>: No enough supplies".format(fid, count))
            count = blue_base.fuel_reserve
        # 检查是否超过最大容量
        if fight.fuel + count > fight.max_fuel:
            print("[WARNING] flue <{}> <{}>: No enough capacity".format(fid, count))
            count = fight.max_fuel - fight.fuel
            if count == 0:
                return
        blue_base.fuel_reserve -= count
        fight.fuel += count
        print("[INFO] flue <{}> <{}>: Fuel added ({}/{})".format(fid, count, fight.fuel, fight.max_fuel))
        self.commands.append("[INFO] flue <{}> <{}>: ".format(fid, count))
        return

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
        # 寻找对应的蓝色基地
        blue_base = self.blue_bases[(fight.row, fight.col)]
        if blue_base.missile_reserve < count:
            print("[WARNING] missile <{}> <{}>: No enough supplies".format(fid, count))
            count = blue_base.missile_reserve
        # 检查是否超过最大容量
        if fight.missile + count > fight.max_missile:
            print("[WARNING] missile <{}> <{}>: No enough capacity".format(fid, count))
            count = fight.max_missile - fight.missile
            if count == 0:
                return
        blue_base.missile_reserve -= count
        fight.missile += count
        print("[INFO] missile <{}> <{}>: Missile added ({}/{})".format(fid, count, fight.missile, fight.max_missile))
        self.commands.append("[INFO] missile <{}> <{}>: ".format(fid, count))
        return

    # 检查loc对应位置是否为目标基地，aim为0表示红色基地，1表示燃料库，2表示导弹库
    def is_aim_base(self, loc, aim):
        if aim == 0:
            if self.map_info[loc[0]][loc[1]] == '#':
                red_base = self.red_bases[loc]
                if (red_base.row, red_base.col) not in self.targets:
                    return True
        elif aim == 1:
            if self.map_info[loc[0]][loc[1]] == '*':
                blue_base = self.blue_bases[loc]
                if blue_base.fuel_reserve > 0 and (blue_base.row, blue_base.col) not in self.targets:
                    return True
        elif aim == 2:
            if self.map_info[loc[0]][loc[1]] == '*':
                blue_base = self.blue_bases[loc]
                if blue_base.missile_reserve > 0 and (blue_base.row, blue_base.col) not in self.targets:
                    return True
        return False

    # 检查是否越界或者是障碍物
    def is_valid(self, x, y, aim):
        if 0 <= x < self.max_row and 0 <= y < self.max_col:
            if aim == 0:
                return True
            else:
                return self.map_info[x][y] != '#'
        return False

    def find_base(self, fid, aim):
        start = (self.fighters[fid].row, self.fighters[fid].col)
        # BFS队列
        queue = deque([(start[0], start[1], 0)])  # (x, y, steps)
        visited = {start}  # 记录访问过的节点
        parent = {start: ((-1, -1), None)}  # 记录每个节点的前驱节点和方向
        fuel = self.fighters[fid].fuel

        while queue:
            x, y, steps = queue.popleft()

            # 检查燃料是否充足
            if fuel < steps:
                if aim == 0:
                    if self.fighters[fid].max_fuel < steps:
                        return (-1, 0), []
                    else:
                        return (0, -1), []
                else:
                    return (-1, 0), []

            # 如果到达目标点，构建方向序列
            if self.is_aim_base((x, y), aim):
                dire_path = []
                (tx, ty) = (x, y)
                while parent[(tx, ty)][1] is not None:
                    dire_path.append(parent[(tx, ty)][1])
                    (tx, ty) = parent[(tx, ty)][0]
                dire_path.reverse()
                return (x, y), dire_path
            else:
                # 遍历四个方向
                for i in range(4):
                    nx, ny = x + self.direction[i][0], y + self.direction[i][1]
                    if self.is_valid(nx, ny, aim) and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny, steps + 1))
                        parent[(nx, ny)] = ((x, y), i)
        # 如果没有找到路径
        return (-1, -1), []

    # # 该指令表示战斗机寻找敌方基地。第一个参数为战斗机编号。
    # def find_red_base(self, fid):
    #     fight = self.fighters[fid]
    #     # 寻找最近的敌方基地
    #     target = (-1, -1)
    #     min_dis = self.max_row + self.max_col
    #     min_path = []
    #     for red_base in self.red_bases.values():
    #         if red_base.defense <= 0 or (red_base.row, red_base.col) in self.targets:
    #             continue
    #         tmp_dis, tmp_path = find_path(self.map_info, (fight.row, fight.col), (red_base.row, red_base.col))
    #         if 0 <= tmp_dis < min_dis:
    #             min_dis = tmp_dis
    #             min_path = tmp_path
    #             target = (red_base.row, red_base.col)
    #     # 检查是否可能到达
    #     if fight.max_fuel < min_dis:
    #         print("[WARNING] find_red_base <{}>: No target can get".format(fid))
    #         return -1, 0
    #     # 检查是否有足够的燃料
    #     if fight.fuel <= min_dis:
    #         print("[WARNING] find_red_base <{}>: No enough fuel".format(fid))
    #         return 0, -1
    #     # # 检查是否有足够的导弹
    #     # if fight.missile < self.red_bases[(target[0], target[1])].defense:
    #     #     print("[WARNING] find_red_base <{}>: No enough missile".format(fid))
    #     #     return 0, -2
    #     return target, min_path
    #
    # # 该指令表示战斗机寻找导弹库。第一个参数为战斗机编号。
    # def find_missile(self, fid):
    #     fight = self.fighters[fid]
    #     # 寻找最近的导弹库
    #     target = (-1, -1)
    #     min_dis = self.max_row + self.max_col
    #     min_path = []
    #     for blue_base in self.blue_bases.values():
    #         if blue_base.missile_reserve <= 0 or (blue_base.row, blue_base.col) in self.targets:
    #             continue
    #         tmp_dis, tmp_path = find_path(self.map_info, (fight.row, fight.col), (blue_base.row, blue_base.col))
    #         if 0 <= tmp_dis < min_dis:
    #             min_dis = tmp_dis
    #             min_path = tmp_path
    #             target = (blue_base.row, blue_base.col)
    #     # 检查是否有足够的燃料
    #     if fight.fuel <= min_dis:
    #         print("[WARNING] find_missile <{}>: No enough fuel".format(fid))
    #         return -1, 0
    #     return target, min_path
    #
    # # 该指令表示战斗机寻找燃料库。第一个参数为战斗机编号。
    # def find_fuel(self, fid):
    #     fight = self.fighters[fid]
    #     # 寻找最近的燃料库
    #     target = (-1, -1)
    #     min_dis = self.max_row + self.max_col
    #     min_path = []
    #     for blue_base in self.blue_bases.values():
    #         if blue_base.fuel_reserve <= 0 or (blue_base.row, blue_base.col) in self.targets:
    #             continue
    #         tmp_dis, tmp_path = find_path(self.map_info, (fight.row, fight.col), (blue_base.row, blue_base.col))
    #         if 0 <= tmp_dis < min_dis:
    #             min_dis = tmp_dis
    #             min_path = tmp_path
    #             target = (blue_base.row, blue_base.col)
    #     if fight.fuel <= min_dis:
    #         print("[WARNING] find_fuel <{}>: No enough fuel".format(fid))
    #         return -1, 0
    #     return target, min_path

    # 该指令表示战斗机寻找目标。第一个参数为战斗机编号。
    def find_target(self, fid):
        fight = self.fighters[fid]
        # 路过无预约的蓝色基地则加油和补充弹药
        if self.map_info[fight.row][fight.col] == "*" and (fight.row, fight.col) not in self.targets:
            self.flue(fid, fight.max_fuel)
            self.missile(fid, fight.max_missile)
        # 是否待命
        if not (self.targets[fid] == (-1, -1)):
            return
        # 是否需要补充导弹
        if fight.missile <= 0:
            target, path = self.find_base(fid, 2)
            self.targets[fid] = target
            self.paths[fid] = path
            return
        # 寻找目标敌方基地
        target, path = self.find_base(fid, 0)
        # 是否需要补充燃料
        if target == (0, -1):
            target, path = self.find_base(fid, 1)
        self.targets[fid] = target
        self.paths[fid] = path

    def get_targets(self):
        for fid in range(self.fighters_num):
            # 如果已经无法行动则跳过
            if self.targets[fid] == (-1, 0):
                continue
            self.find_target(fid)
