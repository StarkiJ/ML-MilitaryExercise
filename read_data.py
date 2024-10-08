from MilitaryClasses import MilitaryBase, Fighter


def read_data(file_path):
    file = open(file_path, 'r')
    data = file.read().split()

    index = 0
    max_score = 0
    total_fuel = 0
    total_missile = 0
    total_defense = 0

    # 读取地图信息
    max_row = int(data[index])
    max_col = int(data[index + 1])
    index += 2

    map_info = []
    for i in range(max_row):
        row = []
        for j in range(max_col):
            row.append(data[index][j])
        map_info.append(row)
        index += 1

    # 读取蓝方基地信息
    blue_base_count = int(data[index])
    index += 1

    blue_bases = {}
    for i in range(blue_base_count):
        row = int(data[index])
        col = int(data[index + 1])
        index += 2
        fuel_reserve = int(data[index])
        missile_reserve = int(data[index + 1])
        defense = int(data[index + 2])
        military_value = int(data[index + 3])
        index += 4
        total_fuel += fuel_reserve
        total_missile += missile_reserve
        blue_base = MilitaryBase(i, row, col, fuel_reserve, missile_reserve, defense, military_value)
        blue_bases[(row, col)] = blue_base

    # 读取红方基地信息
    red_base_count = int(data[index])
    index += 1

    red_bases = {}
    for i in range(red_base_count):
        row = int(data[index])
        col = int(data[index + 1])
        index += 2
        fuel_reserve = int(data[index])
        missile_reserve = int(data[index + 1])
        defense = int(data[index + 2])
        military_value = int(data[index + 3])
        index += 4
        # if defense == 0:
        #     map_info[row][col] = "0"
        #     continue
        max_score += military_value
        total_defense += defense
        red_base = MilitaryBase(i, row, col, fuel_reserve, missile_reserve, defense, military_value)
        red_bases[(row, col)] = red_base

    # 读取战斗机信息
    fighter_count = int(data[index])
    index += 1

    fighters = []
    for i in range(fighter_count):
        row = int(data[index])
        col = int(data[index + 1])
        max_fuel = int(data[index + 2])
        max_missile = int(data[index + 3])
        index += 4
        fighter = Fighter(i, row, col, max_fuel, max_missile)
        fighters.append(fighter)

    print("max score:{}".format(max_score))
    print("total fuel:{}".format(total_fuel))
    print("total missile:{}".format(total_missile))
    print("total defense:{}".format(total_defense))

    return max_row, max_col, map_info, blue_bases, red_bases, fighters, max_score
