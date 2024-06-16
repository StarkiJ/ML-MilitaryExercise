import time


# 判断目标方向
def get_direction(frow, fcol, trow, tcol):
    if frow > trow:
        return 0
    elif frow < trow:
        return 1
    elif fcol > tcol:
        return 2
    elif fcol < tcol:
        return 3


def machine_operation(me, output_path):
    start_time = time.time()
    for fid in range(me.fighters_num):
        fight = me.fighters[fid]
        # 抵达蓝色基地则加油和补充弹药
        if me.map_info[fight.row][fight.col] == "*":
            me.flue(fid, fight.max_fuel)
            me.missile(fid, fight.max_missile)

    while True:
        me.get_targets()
        # 如果战斗机都无法继续行动则结束
        if all(target == (-1, 0) for target in me.targets):
            break

        # 控制战斗机根据target行动
        for fid in range(me.fighters_num):
            fight = me.fighters[fid]
            (row, col) = me.targets[fid]

            # 如果已结束行动则跳过
            if row < 0 or col < 0:
                continue

            dis = len(me.paths[fid])
            # 未达到所需位置（红色基地隔壁或者蓝色基地）
            if (dis > 1) or (me.map_info[row][col] == "*" and dis > 0):
                dire = me.paths[fid][0]
                me.move(fid, dire)
                me.paths[fid].pop(0)
            # 抵达红色基地隔壁则攻击
            if dis <= 2 and me.map_info[row][col] == "#":
                dire = me.paths[fid][0]
                me.attack(fid, dire, fight.missile)
                me.targets[fid] = (-1, -1)
            # 抵达蓝色基地则加油和补充弹药
            elif dis <= 1 and me.map_info[row][col] == "*":
                me.flue(fid, fight.max_fuel)
                me.missile(fid, fight.max_missile)
                me.targets[fid] = (-1, -1)
        # 如果红色基地已全被摧毁则结束
        if not me.red_bases:
            break
        print()
        me.next_frame()
    used_time = time.time() - start_time
    print("Total score: {}/{}".format(me.score, me.max_score))
    print("used time: {}".format(used_time))
    print("output path: {}".format(output_path))
    with open(output_path, 'w') as file:
        for command in me.commands:
            file.write(command + '\n')
        file.write("Total score: {}/{}\n".format(me.score, me.max_score))
        file.write("used time: {}\n".format(used_time))
