import read_data
from MilitaryExercise import MilitaryExercise


def manual_operation():
    me = MilitaryExercise('./data/testcase1.in')
    me.show_info()
    fid = 0
    count = 99999

    while True:
        command = input("Please enter your command:")
        if command == 'q':
            me.next_frame()
            break
        elif command == 'n':
            me.next_frame()
        elif command == 'f':
            fid = input("Enter the fighter ID: ")
        # move: command 为 0-3
        elif command in ['0', '1', '2', '3']:
            # fid = input("Enter the fighter ID: ")
            me.move(fid, command)
        elif command in ['4', '5', '6', '7']:
            command = int(command) - 4
            # fid = input("Enter the fighter ID: ")
            # count = input("Enter the number of attack: ")
            me.attack(fid, command, count)
        elif command == '8':
            # fid = input("Enter the fighter ID: ")
            # count = input("Enter the number of flue: ")
            me.flue(fid, count)
        elif command == '9':
            # fid = input("Enter the fighter ID: ")
            # count = input("Enter the number of missile: ")
            me.missile(fid, count)
        else:
            print("Invalid command.")


# def Machine_learning():
#     env = MilitaryExercise('path_to_file')
#     state_size = len(env.get_state())  # 这里需要确定状态向量的长度
#     action_size = 10  # 这里假设有4个基本动作
#     agent = DQNAgent(state_size, action_size)
#     done = False
#     batch_size = 32
#     EPISODES = 1000
#
#     for e in range(EPISODES):
#         state = env.reset()
#         state = np.reshape(state, [1, state_size])
#         for time in range(500):
#             action = agent.act(state)
#             next_state, reward, done, _ = env.step(action)
#             reward = reward if not done else -10
#             next_state = np.reshape(next_state, [1, state_size])
#             agent.remember(state, action, reward, next_state, done)
#             state = next_state
#             if done:
#                 print("episode: {}/{}, score: {}, e: {:.2}".format(e, EPISODES, time, agent.epsilon))
#                 break
#             if len(agent.memory) > batch_size:
#                 agent.replay(batch_size)
#         # 每隔一定的轮数保存一次模型
#         if e % 50 == 0:
#             agent.save(f"military_dqn_{e}.hdf5")

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


def machine_operation():
    me = MilitaryExercise('./data2/testcase2.in')
    me.show_info()

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
            print("Total score: {}/{}".format(me.Score, me.max_score))
            break

        # 控制战斗机根据target行动
        for fid in range(me.fighters_num):
            fight = me.fighters[fid]
            (row, col) = me.targets[fid]
            # 如果已结束行动则跳过
            if row == -1 and col == 0:
                continue

            dis = abs(fight.row - row) + abs(fight.col - col)
            # 未达到所需位置（红色基地隔壁或者蓝色基地）
            if (dis > 1) or (me.map_info[row][col] == "*" and dis > 0):
                dire = get_direction(fight.row, fight.col, row, col)
                me.move(fid, dire)
            # 抵达红色基地隔壁则攻击
            if dis <= 2 and me.map_info[row][col] == "#":
                dire = get_direction(fight.row, fight.col, row, col)
                me.attack(fid, dire, fight.max_missile)
                me.targets[fid] = (-1, -1)
            # 抵达蓝色基地则加油和补充弹药
            elif dis <= 1 and me.map_info[row][col] == "*":
                me.flue(fid, fight.max_fuel)
                me.missile(fid, fight.max_missile)
                me.targets[fid] = (-1, -1)
        # 如果红色基地已全被摧毁则结束
        if not me.red_bases:
            print("Total score: {}/{}".format(me.Score, me.max_score))
            break
        print()
        me.next_frame()


def main():
    print("Please choose a start mode:")
    print("1. Manual operation")
    print("2. Machine operation")
    print("q. Quit")

    while True:
        choice = input("Enter 1 or 2: ")
        if choice == '1':
            manual_operation()
            break
        elif choice == '2':
            machine_operation()
            break
        elif choice == 'q':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
