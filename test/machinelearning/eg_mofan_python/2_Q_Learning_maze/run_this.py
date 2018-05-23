# coding=utf-8

"""
Reinforcement learning maze example.

Red rectangle:          explorer.
Black rectangles:       hells       [reward = -1].
Yellow bin circle:      paradise    [reward = +1].
All other states:       ground      [reward = 0].

This script is the main part which controls the update method of this example.
The RL is in RL_brain.py.

View more on my tutorial page: https://morvanzhou.github.io/tutorials/
"""

'''
https://morvanzhou.github.io/tutorials/machine-learning/reinforcement-learning/2-2-tabular-q1/
'''

from maze_env import Maze
from RL_brain import QLearningTable


def update():
    # 学习 100 回合
    for episode in range(100):
        # initial observation
        # 初始化 state 的观测值
        observation = env.reset()

        while True:
            # fresh env
            # 更新可视化环境
            env.render()

            # RL choose action based on observation
            # RL 大脑根据 state 的观测值挑选 action
            action = RL.choose_action(str(observation))

            # RL take action and get next observation and reward
            # 探索者在环境中实施这个 action, 并得到环境返回的下一个 state 观测值, reward 和 done (是否是掉下地狱或者升上天堂)
            observation_, reward, done = env.step(action)

            # RL learn from this transition
            # RL 从这个序列 (state, action, reward, state_) 中学习
            RL.learn(str(observation), action, reward, str(observation_))

            # swap observation
            # 将下一个 state 的值传到下一次循环
            observation = observation_

            # break while loop when end of this episode
            # 如果掉下地狱或者升上天堂, 这回合就结束了
            if done:
                break

    # end of game
    # 结束游戏并关闭窗口
    print('game over')
    env.destroy()

if __name__ == "__main__":
    # 定义环境 env 和 RL 方式
    env = Maze()
    RL = QLearningTable(actions=list(range(env.n_actions)))
    # 开始可视化环境 env
    env.after(100, update)
    env.mainloop()