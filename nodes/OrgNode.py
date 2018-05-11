import random

NODE_STATE = ['o_sus', 'o_inf', 'o_rco']


class OrgNode(object):
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
        if self.state == 'o_sus':
            if self.beta > st:
                self.state = 'o_inf'

    def new_rco_state(self):
        st = random.random()
        if self.state == 'o_sus' or self.state == 'o_inf':
            if self.rou > st:
                self.state = 'o_rco'
