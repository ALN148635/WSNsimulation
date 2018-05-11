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


def draw_graph():
    lines = []
    density = 0.15
    side_width = 100
    side_height = 50
    sim_time = 30
    # my model
    my_open = 0.5
    my_spr = 0.5
    my_eta_low = 1
    my_eta_high = 1
    # tang model
    tang_beta = 0.3
    tang_rou = 0
    tang_a = 0.5
    tang_s = 0.5
    # 病毒位置
    v_x = 50
    v_y = 25
    # 补丁包位置及时间
    r_x = 50
    r_y = 25
    r_t = sim_time+1
    # 传播距离
    g_r = 7
    # 得到随机节点的坐标
    rd_nodes_pos = get_random_position(density, side_width, side_height)
    pos = {i: (rd_nodes_pos[i][0], rd_nodes_pos[i][1])
           for i in range(len(rd_nodes_pos))}
    nodes_num = len(rd_nodes_pos)

    # # # 指定病毒投放节点
    pos[0] = (v_x, v_y)
    # # # 指定补丁包投放节点
    pos[1] = (r_x, r_y)

    # sim
    # # 得到点的边
    g = nx.random_geometric_graph(nodes_num, g_r, pos=pos)

    # lines[0]
    my_sim = []
    for _ in range(5):
        my_model_sim(open=my_open, spr=my_spr,
                     eta_low=my_eta_low, eta_high=my_eta_high, r_t=r_t,
                     rd_nodes_pos=rd_nodes_pos, nodes_num=nodes_num,
                     sim_time=sim_time, graph=g, g_pos=pos, lines=my_sim
                     )
    lines.append(avg_lists(my_sim, 5))

    # lines[1]
    # tang_sim = []
    # for _ in range(5):
    #     tang_model_sim(a=tang_a, s=tang_s, beta=tang_beta, rou=tang_rou,
    #                    rd_nodes_pos=rd_nodes_pos, nodes_num=nodes_num,
    #                    sim_time=sim_time, graph=g, g_pos=pos, lines=tang_sim
    #                    )
    # lines.append(avg_lists(tang_sim, 5))
    #
    # # lines[2]
    # org_sim = []
    # for _ in range(5):
    #     org_model_sim(beta=tang_beta, rou=tang_rou, r_t=r_t,
    #                   rd_nodes_pos=rd_nodes_pos, nodes_num=nodes_num,
    #                   sim_time=sim_time, graph=g, g_pos=pos, lines=org_sim
    #                   )
    # lines.append(avg_lists(org_sim, 5))

    plt.clf()
    # print fig
    plt.plot(lines[0], 'r')
    # plt.plot(lines[1], 'b')
    # plt.plot(lines[2], 'c')
    plt.savefig('test', format='png')
