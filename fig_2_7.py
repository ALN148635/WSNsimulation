# -*- coding: utf-8 -*-
import math

import matplotlib.pyplot as plt
import networkx as nx

from model.org_model_sim import org_model_sim
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


def draw_graph_2_7(density, side_width, side_height, sim_time, g_r,
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

    # lines[0][1]
    inf_sim = []
    sus_sim = []
    rco_sim = []
    for _ in range(5):
        org_sim = org_model_sim(beta=0.3, rou=0.3, r_t=r_t,
                                rd_nodes_pos=rd_nodes_pos, nodes_num=nodes_num,
                                sim_time=sim_time, graph=g, g_pos=pos,
                                sur_type=['inf', 'sus', 'rco'])
        inf_sim.append(org_sim[0])
        sus_sim.append(org_sim[1])
        rco_sim.append(org_sim[2])
    lines.append(avg_lists(inf_sim, 5))
    lines.append(avg_lists(sus_sim, 5))
    lines.append(avg_lists(rco_sim, 5))

    # plt.clf()
    # plt.ylabel('I(t)')
    # plt.xlabel('Time/Unit of Time')
    # plt.xlim(0, sim_time)
    # # print fig
    # plt.plot(lines[0], 'r', label='a')
    # plt.plot(lines[1], 'com', label='b')
    # plt.plot(lines[2], 'b', label='c')
    # plt.plot(lines[3], 'g', label='d')
    # # plt.plot(lines[4], 'sus', label='e')
    # # plt.plot(lines[5], 'g', label='f')
    # plt.legend(loc='lower right')
    # plt.savefig('test', format='png')
    return lines
