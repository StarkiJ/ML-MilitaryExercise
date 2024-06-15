# import tianshou as ts
# from tianshou.policy import DQNPolicy
# from tianshou.data import VectorReplayBuffer, Collector
# from tianshou.trainer import offpolicy_trainer
# from tianshou.env import DummyVectorEnv
# import torch
# import torch.nn as nn
# import torch.optim as optim
# import numpy as np
# from MEEnv import MilitaryExerciseEnv
#
#
# # 定义Q网络
# class QNet(nn.Module):
#     def __init__(self, state_shape, action_shape):
#         super().__init__()
#         self.model = nn.Sequential(
#             nn.Linear(np.prod(state_shape), 128),
#             nn.ReLU(),
#             nn.Linear(128, 128),
#             nn.ReLU(),
#             nn.Linear(128, np.prod(action_shape))
#         )
#
#     def forward(self, obs, state=None, info={}):
#         obs = torch.flatten(obs, start_dim=1)
#         return self.model(obs), state
#
#
# def machine_learning():
#     # 创建环境
#     file_path = './data2/testcase1.in'  # 替换为你的文件路径
#     env = MilitaryExerciseEnv(file_path)
#     train_envs = DummyVectorEnv([lambda: MilitaryExerciseEnv(file_path) for _ in range(8)])
#     test_envs = DummyVectorEnv([lambda: MilitaryExerciseEnv(file_path) for _ in range(100)])
#
#     # 设置策略
#     state_shape = train_envs.observation_space.shape
#     action_shape = (11 * train_envs.action_space.shape[0],)
#     net = QNet(state_shape, action_shape)
#     optim = optim.Adam(net.parameters(), lr=1e-3)
#     policy = DQNPolicy(net, optim, discount_factor=0.9, estimation_step=3, target_update_freq=320)
#
#     # 创建数据缓冲区
#     buffer = VectorReplayBuffer(20000, buffer_num=len(train_envs))
#     train_collector = Collector(policy, train_envs, buffer, exploration_noise=True)
#     test_collector = Collector(policy, test_envs, exploration_noise=True)
#
#     # 训练
#     result = offpolicy_trainer(
#         policy, train_collector, test_collector,
#         max_epoch=10, step_per_epoch=1000, step_per_collect=10,
#         episode_per_test=100, batch_size=64, update_per_step=0.1,
#         train_fn=lambda epoch, env_step: policy.set_eps(0.1),
#         test_fn=lambda epoch, env_step: policy.set_eps(0.05),
#         stop_fn=lambda mean_rewards: mean_rewards >= env.exercise.max_score,
#         logger=None
#     )
#
#     print(result)
