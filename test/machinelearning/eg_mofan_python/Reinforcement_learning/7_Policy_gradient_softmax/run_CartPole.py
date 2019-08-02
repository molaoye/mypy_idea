"""
Policy Gradient, Reinforcement Learning.

The cart pole example

View more on my tutorial page: https://morvanzhou.github.io/tutorials/

Using:
Tensorflow: 1.0
gym: 0.8.0
"""

'''
Policy Gradients 算法更新 (Tensorflow)
'''

import gym
from RL_brain import PolicyGradient
import matplotlib.pyplot as plt
# renders environment if total episode reward is greater then this threshold
# 当 回合总 reward 大于 400 时显示模拟窗口
DISPLAY_REWARD_THRESHOLD = 400
# 在屏幕上显示模拟窗口会拖慢运行速度, 我们等计算机学得差不多了再显示模拟
# rendering wastes time
RENDER = False

env = gym.make('CartPole-v0')# CartPole 这个模拟
# 普通的 Policy gradient 方法, 使得回合的 variance 比较大, 所以我们选了一个好点的随机种子
env.seed(1)     # reproducible, general Policy gradient has high variance
env = env.unwrapped# 取消限制

print(env.action_space)# 显示可用 action
print(env.observation_space)# 显示可用 state 的 observation
print(env.observation_space.high)# 显示 observation 最高值
print(env.observation_space.low)# 显示 observation 最低值

RL = PolicyGradient(# 定义
    n_actions=env.action_space.n,
    n_features=env.observation_space.shape[0],
    learning_rate=0.02,
    reward_decay=0.99,# gamma
    # output_graph=True,# 输出 tensorboard 文件
)

for i_episode in range(3000):

    observation = env.reset()

    while True:
        if RENDER: env.render()

        action = RL.choose_action(observation)

        observation_, reward, done, info = env.step(action)

        RL.store_transition(observation, action, reward)# 存储这一回合的 transition

        if done:
            ep_rs_sum = sum(RL.ep_rs)

            if 'running_reward' not in globals():
                running_reward = ep_rs_sum
            else:
                running_reward = running_reward * 0.99 + ep_rs_sum * 0.01
            # 判断是否显示模拟
            if running_reward > DISPLAY_REWARD_THRESHOLD: RENDER = True     # rendering
            print("episode:", i_episode, "  reward:", int(running_reward))

            vt = RL.learn()# 学习, 输出 vt, 我们下节课讲这个 vt 的作用

            if i_episode == 0:
                plt.plot(vt)    # plot the episode vt# plot 这个回合的 vt
                plt.xlabel('episode steps')
                plt.ylabel('normalized state-action value')
                plt.show()
            break

        observation = observation_