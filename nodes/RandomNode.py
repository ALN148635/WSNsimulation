# -*- coding: utf-8 -*-
import random

# sus:
# ins:
# act:
# iso:
# com:
NODE_STATE = ['sus', 'ins', 'act', 'iso', 'com']


class RandomNode(object):
    def __init__(self, pos, id_no, sta, T):
        self.id = id_no
        self.x = pos[0]
        self.y = pos[1]
        self.state = NODE_STATE[sta]
        self.open = [random.choice([0, 1]) for _ in range(T)]
        self.spr = [random.choice([0, 1]) for _ in range(T)]
        self.v = 0.0
        self.r = 0.0

    def get_pos(self):
        return self.x, self.y

    def get_open(self, t):
        return self.open[t]

    def get_spr(self, t):
        return self.spr[t]

    def is_com(self):
        return self.state == 'com'

    def is_act(self):
        return self.state == 'act'

    def set_state(self, state):
        self.state = NODE_STATE[state]

    def get_state(self):
        return NODE_STATE.index(self.state)

    def is_sus(self):
        return self.state == 'sus'

    def is_rec(self):
        index = NODE_STATE.index(self.state)
        return index < 3 & index > 0

    def is_inf(self):
        index = NODE_STATE.index(self.state)
        return index < 5 & index > 2

    # 节点在时刻 t 发现自己感染病毒, 关闭了自己的传出串口
    def set_spr(self, t, T, state):
        if state == 'com':
            for i in range(t, T):
                self.spr[i] = 0
        elif state == 'iso':
            for i in range(t, T):
                self.spr[i] = random.choice([0, 1])
        else:
            print('Set Spr Error!')
            return

    def new_state(self, t, T):
        # sus
        if self.state == 'sus':
            if self.v == 0 and self.r == 0:
                return
            elif self.v > self.r:
                self.set_state(3)
            else:
                self.set_state(1)
        # iso
        elif self.state == 'iso':
            if self.r > (1 - self.r):
                self.set_spr(t, T, self.state)
                self.set_state(1)
            elif self.get_spr(t):
                self.set_state(4)
            else:
                self.set_state(3)
        # com
        elif self.state == 'com':
            alpha = random.uniform(0.5, 1)
            if self.r > (1 - self.r):
                self.set_state(1)
            elif alpha > (1-alpha):
                self.set_spr(t, T, self.state)
                self.set_state(3)
        # ins
        elif self.state == 'ins':
            if self.get_spr(t):
                self.set_state(2)
        elif self.state == 'act':
            if not self.get_spr(t):
                self.set_state(1)
        else:
            print('Node_state Error!')
            return

    # def get_id(self):
    #     return self.id
