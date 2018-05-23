# coding=utf-8

"""
A simple example for Reinforcement Learning using table lookup Q-learning method.
An agent "o" is on the left of a 1 dimensional world, the treasure is on the rightmost location.
Run this program and to see how the agent will improve its strategy of finding the treasure.

View more on my tutorial page: https://morvanzhou.github.io/tutorials/
"""

'''
https://morvanzhou.github.io/tutorials/machine-learning/reinforcement-learning/2-1-general-rl/
'''

import numpy as np
import pandas as pd
import time

np.random.seed(2)  # reproducible


N_STATES = 6   # the length of the 1 dimensional world--1维世界的宽度
ACTIONS = ['left', 'right']     # available actions--探索者的可用动作
EPSILON = 0.9   # greedy police--贪婪度 Greedy
ALPHA = 0.1     # learning rate--学习率
GAMMA = 0.9    # discount factor--奖励递减值
MAX_EPISODES = 13   # maximum episodes--最大回合数
FRESH_TIME = 0.3    # fresh time for one move--移动间隔时间


'''
Q 表
'''
def build_q_table(n_states, actions):
    table = pd.DataFrame(
        np.zeros((n_states, len(actions))),     # q_table initial values--q_table 全 0 初始
        columns=actions,    # actions's name--对应的是行为名称
    )
    # print(table)    # show table
    return table

'''
定义动作
'''
def choose_action(state, q_table):# 在某个 state 地点, 选择行为
    # This is how to choose an action
    # 选出这个 state 的所有 action 值
    state_actions = q_table.iloc[state, :]
    if (np.random.uniform() > EPSILON) or ((state_actions == 0).all()):  # act non-greedy or state-action have no value--非贪婪 or 或者这个 state 还没有探索过
        action_name = np.random.choice(ACTIONS)
    else:   # act greedy--贪婪模式
        action_name = state_actions.idxmax()    # replace argmax to idxmax as argmax means a different function in newer version of pandas
    return action_name


'''
环境反馈 S_, R
'''
def get_env_feedback(S, A):
    # This is how agent will interact with the environment
    if A == 'right':    # move right
        if S == N_STATES - 2:   # terminate
            S_ = 'terminal'
            R = 1
        else:
            S_ = S + 1
            R = 0
    else:   # move left
        R = 0
        if S == 0:
            S_ = S  # reach the wall
        else:
            S_ = S - 1
    return S_, R


'''
环境更新
'''
def update_env(S, episode, step_counter):
    # This is how environment be updated
    env_list = ['-']*(N_STATES-1) + ['T']   # '---------T' our environment
    if S == 'terminal':
        interaction = 'Episode %s: total_steps = %s' % (episode+1, step_counter)
        print('\r{}'.format(interaction), end='')
        time.sleep(2)
        print('\r                                ', end='')
    else:
        env_list[S] = 'o'
        interaction = ''.join(env_list)
        print('\r{}'.format(interaction), end='')
        time.sleep(FRESH_TIME)


'''
强化学习主循环
'''
def rl():
    # main part of RL loop
    q_table = build_q_table(N_STATES, ACTIONS)# 初始 q tabl
    for episode in range(MAX_EPISODES):# 回合
        step_counter = 0
        S = 0# 回合初始位置
        is_terminated = False# 是否回合结束
        update_env(S, episode, step_counter)# 环境更新
        while not is_terminated:

            A = choose_action(S, q_table)# 选行为
            S_, R = get_env_feedback(S, A)  # take action & get next state and reward--实施行为并得到环境的反馈
            q_predict = q_table.loc[S, A]# 估算的(状态-行为)值
            if S_ != 'terminal':
                q_target = R + GAMMA * q_table.iloc[S_, :].max()   # next state is not terminal--实际的(状态-行为)值 (回合没结束)
            else:
                q_target = R     # next state is terminal--实际的(状态-行为)值 (回合结束)
                is_terminated = True    # terminate this episode

            q_table.loc[S, A] += ALPHA * (q_target - q_predict)  # update--q_table 更新
            S = S_  # move to next state--探索者移动到下一个 state

            update_env(S, episode, step_counter+1)# 环境更新
            step_counter += 1
    return q_table


if __name__ == "__main__":
    q_table = rl()
    print('\r\nQ-table:\n')
    print(q_table)
