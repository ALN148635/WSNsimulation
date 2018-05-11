import random

NODE_STATE = ['t_sus', 't_sslp', 't_inf', 't_islp']


class TangNode(object):
    def __init__(self, pos, id_no, sta, beta, rou):
        self.id = id_no
        self.x = pos[0]
        self.y = pos[1]
        self.state = NODE_STATE[sta]
        self.beta = beta
        self.rou = rou

    def get_state(self):
        return NODE_STATE.index(self.state)

    def new_inf_state(self):
        st = random.random()
        if self.state == 't_sus':
            if self.beta > st:
                self.state = 't_inf'

    def new_state(self, a, s):
        st = random.random()
        if self.state == 't_sus':
            if a > st:
                self.state = 't_sslp'
        elif self.state == 't_sslp':
            if s > st:
                self.state = 't_sus'
        elif self.state == 't_inf':
            if a > st:
                self.state = 't_islp'
        elif self.state == 't_islp':
            if self.rou > st:
                self.state = 't_sus'
            elif (self.beta + (1-self.beta)*s) > st:
                self.state = 't_inf'
        else:
            print("Tang State Error!")
            return
