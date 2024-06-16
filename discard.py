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