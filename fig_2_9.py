# -*- coding: utf-8 -*-
import math

import matplotlib.pyplot as plt
import networkx as nx

from model.my_model_sim import my_model_sim
from model.org_model_sim import org_model_sim
from model.tang_model_sim import tang_model_sim
from nodes.RandomPosition import get_random_position


# d(node1: RandomNode, node2: RandomNode) -> int
def d(node1, node2):
    pos1_x, pos1_y = node1.get_pos()
    pos2_x, pos2_y = node2.get_pos()
    dis = math.sqrt(pow((pos1_x - pos2_x), 2)
                    + pow((pos1_y - pos2_y), 2))
    return round(dis, 2)


def avg_lists(lists, l_num):
    avg = []
    for i in range(len(lists[0])):
        sum = 0
        for j in range(l_num):
            sum += lists[j][i]
        avg.append(int(sum/l_num))
    return avg


def draw_graph_2_9(density, side_width, side_height, sim_time, g_r,
               v_x, v_y, r_x, r_y, r_t):
    lines = []
    # 得到随机节点的坐标
    rd_nodes_pos = get_random_position(density, side_width, side_height)
    pos = {i: (rd_nodes_pos[i][0], rd_nodes_pos[i][1])
           for i in range(len(rd_nodes_pos))}
    nodes_num = len(rd_nodes_pos)

    # # # 指定病毒投放节点
    pos[0] = (v_x, v_y)
    rd_nodes_pos[0] = (v_x, v_y)
    # # # 指定补丁包投放节点
    pos[1] = (r_x, r_y)
    rd_nodes_pos[1] = (r_x, r_y)

    # sim
    # # 得到点的边
    g = nx.random_geometric_graph(nodes_num, g_r, pos=pos)

    # lines[1]
    inf_sim = []
    sus_sim = []
    for _ in range(5):
        tang_sim = tang_model_sim(a=0.5, s=0.5, beta=0.3, rou=0.3,
                                  rd_nodes_pos=rd_nodes_pos, nodes_num=nodes_num,
                                  sim_time=sim_time, graph=g, g_pos=pos,
                                  sur_type=['inf', 'sus']
                                  )
        inf_sim.append(tang_sim[0])
        sus_sim.append(tang_sim[1])
    lines.append(avg_lists(inf_sim, 5))
    lines.append(avg_lists(sus_sim, 5))

    return lines
