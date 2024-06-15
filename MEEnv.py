# import gymnasium as gym
# from gymnasium import spaces
# import numpy as np
# from MilitaryExercise import MilitaryExercise
#
#
# class MilitaryExerciseEnv(gym.Env):
#     def __init__(self, file_path):
#         super(MilitaryExerciseEnv, self).__init__()
#         self.file_path = file_path
#         self.exercise = MilitaryExercise(file_path)
#
#         # 动作空间: 每个战斗机有11个动作
#         self.action_space = spaces.MultiDiscrete([11] * self.exercise.fighters_num)
#
#         # 观测空间: 包括地图的状态，所有战斗机的位置及状态
#         self.observation_space = spaces.Box(low=0, high=1, shape=(self.exercise.max_row, self.exercise.max_col, 3),
#                                             dtype=np.float32)
#         self.reset()
#
#     def reset(self):
#         self.exercise = MilitaryExercise(self.file_path)
#         return self._get_obs()
#
#     def step(self, actions):
#         for fid, action in enumerate(actions):
#             fight = self.exercise.fighters[fid]
#             if action == 0:
#                 self.exercise.move(fid, 0)  # 上
#             elif action == 1:
#                 self.exercise.move(fid, 1)  # 下
#             elif action == 2:
#                 self.exercise.move(fid, 2)  # 左
#             elif action == 3:
#                 self.exercise.move(fid, 3)  # 右
#             elif action == 4:
#                 self.exercise.attack(fid, 0, fight.missile)  # 向上攻击
#             elif action == 5:
#                 self.exercise.attack(fid, 1, fight.missile)  # 向下攻击
#             elif action == 6:
#                 self.exercise.attack(fid, 2, fight.missile)  # 向左攻击
#             elif action == 7:
#                 self.exercise.attack(fid, 3, fight.missile)  # 向右攻击
#             elif action == 8:
#                 self.exercise.flue(fid, fight.max_fuel)  # 补给燃油
#             elif action == 9:
#                 self.exercise.missile(fid, fight.max_missile)  # 补给弹药
#             elif action == 10:
#                 pass  # 无动作
#
#         self.exercise.next_frame()
#
#         obs = self._get_obs()
#         reward = self.exercise.Score
#         done = self.exercise.Frame >= 100  # 可以根据需求修改结束条件
#         info = {}
#         return obs, reward, done, info
#
#     def render(self, mode='human'):
#         self.exercise.show_info()
#
#     def close(self):
#         pass
#
#     def _get_obs(self):
#         # 将map_info转换为数值数组
#         obs = np.zeros((self.exercise.max_row, self.exercise.max_col, 3), dtype=np.float32)
#         for i in range(self.exercise.max_row):
#             for j in range(self.exercise.max_col):
#                 if self.exercise.map_info[i][j] == '#':
#                     obs[i][j][0] = 1.0
#                 elif self.exercise.map_info[i][j] == '*':
#                     obs[i][j][1] = 1.0
#                 elif self.exercise.map_info[i][j] == '.':
#                     obs[i][j][2] = 1.0
#         return obs