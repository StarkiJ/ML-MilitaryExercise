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


def machine_operation(me):
    for fid in range(me.fighters_num):
        fight = me.fighters[fid]
        # 抵达蓝色基地则加油和补充弹药
        if me.map_info[fight.row][fight.col] == "*":
            me.flue(fid, fight.max_fuel)
            me.missile(fid, fight.max_missile)

    while True:
        me.get_targets()
        # 如果战斗机都无法继续行动则结束
        if all(path[0] == -3 for path in me.paths):
            print("Total score: {}/{}".format(me.score, me.max_score))
            break

        # 控制战斗机根据target行动
        for fid in range(me.fighters_num):
            fight = me.fighters[fid]
            # (row, col) = me.targets[fid]
            path = me.paths[fid]
            # 如果无行动则跳过
            if path[0] < 0:
                continue

            dis = len(me.paths[fid]) - 1
            # 未达到所需位置（红色基地隔壁或者蓝色基地）
            if (dis > 1) or (path[0] > 0 and dis > 0):
                dire = me.paths[fid][1]
                me.move(fid, dire)
                me.paths[fid].pop(1)
            # 抵达红色基地隔壁则攻击
            if dis <= 2 and path[0] == 0:
                dire = me.paths[fid][1]
                me.attack(fid, dire, fight.max_missile)
                me.paths[fid] = [-1]
            # 抵达蓝色基地则加油和补充弹药
            elif dis <= 1 and path[0] > 0:
                me.flue(fid, fight.max_fuel)
                me.missile(fid, fight.max_missile)
                me.paths[fid] = [-1]
        # 如果红色基地已全被摧毁则结束
        if not me.red_bases:
            print("Total score: {}/{}".format(me.score, me.max_score))
            break
        print()
        me.next_frame()
