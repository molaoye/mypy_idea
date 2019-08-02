"""
This part of code is the reinforcement learning brain, which is a brain of the agent.
All decisions are made in here.

Policy Gradient, Reinforcement Learning.

View more on my tutorial page: https://morvanzhou.github.io/tutorials/

Using:
Tensorflow: 1.0
gym: 0.8.0
"""

'''
Policy Gradients 思维决策 (Tensorflow)
'''

import numpy as np
import tensorflow as tf

# reproducible
np.random.seed(1)
tf.set_random_seed(1)


class PolicyGradient:
    # 初始化 (有改变)
    def __init__(
            self,
            n_actions,
            n_features,
            learning_rate=0.01,
            reward_decay=0.95,
            output_graph=False,
    ):
        self.n_actions = n_actions
        self.n_features = n_features
        self.lr = learning_rate# 学习率
        self.gamma = reward_decay# reward 递减率

        self.ep_obs, self.ep_as, self.ep_rs = [], [], []# 这是我们存储 回合信息的 list

        self._build_net()# 建立 policy 神经网络

        self.sess = tf.Session()

        if output_graph:# 是否输出 tensorboard 文件
            # $ tensorboard --logdir=logs
            # http://0.0.0.0:6006/
            # tf.train.SummaryWriter soon be deprecated, use following
            tf.summary.FileWriter("logs/", self.sess.graph)

        self.sess.run(tf.global_variables_initializer())

    # 建立 policy gradient 神经网络 (有改变)
    def _build_net(self):
        with tf.name_scope('inputs'):
            self.tf_obs = tf.placeholder(tf.float32, [None, self.n_features], name="observations")# 接收 observation
            self.tf_acts = tf.placeholder(tf.int32, [None, ], name="actions_num")# 接收我们在这个回合中选过的 actions
            self.tf_vt = tf.placeholder(tf.float32, [None, ], name="actions_value")# 接收每个 state-action 所对应的 value (通过 reward 计算)
        # fc1
        layer = tf.layers.dense(
            inputs=self.tf_obs,
            units=10,# 输出个数
            activation=tf.nn.tanh,  # tanh activation# 激励函数
            kernel_initializer=tf.random_normal_initializer(mean=0, stddev=0.3),
            bias_initializer=tf.constant_initializer(0.1),
            name='fc1'
        )
        # fc2
        all_act = tf.layers.dense(
            inputs=layer,
            units=self.n_actions,# 输出个数
            activation=None,# 之后再加 Softmax
            kernel_initializer=tf.random_normal_initializer(mean=0, stddev=0.3),
            bias_initializer=tf.constant_initializer(0.1),
            name='fc2'
        )

        self.all_act_prob = tf.nn.softmax(all_act, name='act_prob')  # use softmax to convert to probability# 激励函数 softmax 出概率

        with tf.name_scope('loss'):
            # to maximize total reward (log_p * R) is to minimize -(log_p * R), and the tf only have minimize(loss)
            # 最大化 总体 reward (log_p * R) 就是在最小化 -(log_p * R), 而 tf 的功能里只有最小化 loss
            neg_log_prob = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=all_act, labels=self.tf_acts)   # this is negative log of chosen action# 所选 action 的概率 -log 值
            # or in this way:
            # neg_log_prob = tf.reduce_sum(-tf.log(self.all_act_prob)*tf.one_hot(self.tf_acts, self.n_actions), axis=1)
            loss = tf.reduce_mean(neg_log_prob * self.tf_vt)  # reward guided loss# (vt = 本reward + 衰减的未来reward) 引导参数的梯度下降

        with tf.name_scope('train'):
            self.train_op = tf.train.AdamOptimizer(self.lr).minimize(loss)

    # 选行为 (有改变)
    # 这个行为不再是用 Q value 来选定的, 而是用概率来选定. 即使不用 epsilon-greedy, 也具有一定的随机性.
    def choose_action(self, observation):
        prob_weights = self.sess.run(self.all_act_prob, feed_dict={self.tf_obs: observation[np.newaxis, :]})# 所有 action 的概率
        action = np.random.choice(range(prob_weights.shape[1]), p=prob_weights.ravel())  # select action w.r.t the actions prob# 根据概率来选 action
        return action

    # 存储回合 transition (有改变)
    # 就是将这一步的 observation, action, reward 加到列表中去. 因为本回合完毕之后要清空列表, 然后存储下一回合的数据, 所以我们会在 learn() 当中进行清空列表的动作.
    def store_transition(self, s, a, r):
        self.ep_obs.append(s)
        self.ep_as.append(a)
        self.ep_rs.append(r)

    # 学习更新参数 (有改变)
    # 首先我们要对这回合的所有 reward 动动手脚, 使他变得更适合被学习. 第一就是随着时间推进, 用 gamma 衰减未来的 reward, 然后为了一定程度上减小 policy gradient 回合 variance
    def learn(self):
        # discount and normalize episode reward
        # 衰减, 并标准化这回合的 reward
        discounted_ep_rs_norm = self._discount_and_norm_rewards()

        # train on episode
        self.sess.run(self.train_op, feed_dict={
             self.tf_obs: np.vstack(self.ep_obs),  # shape=[None, n_obs]
             self.tf_acts: np.array(self.ep_as),  # shape=[None, ]
             self.tf_vt: discounted_ep_rs_norm,  # shape=[None, ]
        })

        self.ep_obs, self.ep_as, self.ep_rs = [], [], []    # empty episode data# 清空回合 data
        return discounted_ep_rs_norm# 返回这一回合的 state-action value

    # 衰减回合的 reward (新内容)
    def _discount_and_norm_rewards(self):
        # discount episode rewards
        discounted_ep_rs = np.zeros_like(self.ep_rs)
        running_add = 0
        for t in reversed(range(0, len(self.ep_rs))):
            running_add = running_add * self.gamma + self.ep_rs[t]
            discounted_ep_rs[t] = running_add

        # normalize episode rewards
        discounted_ep_rs -= np.mean(discounted_ep_rs)
        discounted_ep_rs /= np.std(discounted_ep_rs)
        return discounted_ep_rs



