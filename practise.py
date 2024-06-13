import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam
from rl.agents.dqn import DQNAgent
from rl.policy import EpsGreedyQPolicy
from rl.memory import SequentialMemory

def build_model(state_shape, action_shape):
    model = Sequential()
    model.add(Flatten(input_shape=(1,) + state_shape))
    model.add(Dense(24, activation='relu'))
    model.add(Dense(24, activation='relu'))
    model.add(Dense(action_shape, activation='linear'))
    return model

def build_agent(model, action_shape):
    policy = EpsGreedyQPolicy()
    memory = SequentialMemory(limit=50000, window_length=1)
    dqn = DQNAgent(model=model, memory=memory, policy=policy,
                   nb_actions=action_shape, nb_steps_warmup=10, target_model_update=1e-2)
    return dqn

# 定义环境
env = FighterEnv(n, m, map_matrix, blue_bases, red_bases, fighters)

# 构建模型
model = build_model(env.observation_space.shape, env.action_space.n)

# 构建智能体
dqn = build_agent(model, env.action_space.n)
dqn.compile(Adam(lr=1e-3), metrics=['mae'])

# 训练模型
dqn.fit(env, nb_steps=50000, visualize=False, verbose=1)

# 测试模型
dqn.test(env, nb_episodes=10, visualize=True)
