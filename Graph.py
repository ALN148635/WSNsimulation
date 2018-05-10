# -*- coding: utf-8 -*-
import math
import numpy as np
import random

import matplotlib.pyplot as plt
import networkx as nx

from nodes.RandomNode import RandomNode
from nodes.RandomPosition import get_random_position


# d(node1: RandomNode, node2: RandomNode) -> int
def d(node1, node2):
    pos1_x, pos1_y = node1.get_pos()
    pos2_x, pos2_y = node2.get_pos()
    dis = math.sqrt(pow((pos1_x - pos2_x), 2)
                    + pow((pos1_y - pos2_y), 2))
    return round(dis, 2)


def random_np(low, high, nodes_num):
    m = np.zeros((nodes_num, nodes_num))
    for i in range(nodes_num):
        for j in range(nodes_num):
            m[i, j] = random.uniform(low, high)
    return m


def draw_graph():
    keyFrames = []
    density = 0.15
    side_width = 200
    side_height = 100
    sim_time = 150
    # 病毒位置
    v_x = 100
    v_y = 50
    # 补丁包位置及时间
    r_x = 100
    r_y = 50
    r_t = 10
    # 传播距离
    r = 5
    nodes = []
    # 得到随机节点的坐标
    rd_nodes_pos = get_random_position(density, side_width, side_height)
    pos = {i: (rd_nodes_pos[i][0], rd_nodes_pos[i][1])
           for i in range(len(rd_nodes_pos))}
    nodes_num = len(rd_nodes_pos)
    nodes_color = ['sus'] * nodes_num

    # 创建用于状态处理的随机节点
    for rd_node in rd_nodes_pos:
        rn = RandomNode(rd_node, rd_nodes_pos.index(rd_node), 0, sim_time)
        nodes.append(rn)

    # 指定病毒投放节点
    pos[0] = (v_x, v_y)
    nodes[0].x = v_x
    nodes[0].y = v_y
    nodes[0].set_state(3)
    nodes_color[0] = 'iso'

    # 指定补丁包投放节点
    pos[1] = (r_x, r_y)
    nodes[1].x = r_x
    nodes[1].y = r_y

    # 新建信息传播概率的矩阵
    low = 1
    high = 1
    eta = random_np(low, high, nodes_num)

    # sim
    # 得到点的边
    g = nx.random_geometric_graph(nodes_num, r, pos=pos)

    # draw graph
    nx.draw_networkx_nodes(g, pos=pos, node_color=nodes_color,
                           node_size=20)
    # show graph
    filename = 'WSNsim/WSNsim_{}.png'.format(0)
    plt.savefig(filename, format='png')
    keyFrames.append(filename)

    # 感染概率 和 恢复概率
    v = np.zeros((sim_time, nodes_num))
    r = np.zeros((sim_time, nodes_num))
    # 统计数据
    inf_nums = [1]+[0 for _ in range(1, sim_time)]
    rco_nums = [0]+[0 for _ in range(1, sim_time)]
    sus_nums = [nodes_num-1]+[0 for _ in range(1, sim_time)]
    iso_nums = [1]+[0 for _ in range(1, sim_time)]
    com_nums = [0]+[0 for _ in range(1, sim_time)]
    ins_nums = [0]+[0 for _ in range(1, sim_time)]
    act_nums = [0]+[0 for _ in range(1, sim_time)]
    count_states = [0, 0, 0, 0, 0]
    for t in range(1, sim_time):
        # 更新节点的感染概率和恢复概率
        for nodei in nodes:
            v_pi = 1
            r_pi = 1
            for nodej in nx.neighbors(g, nodei.id):
                if nodes[nodej].is_com():
                    v_pi *= (1 - eta[nodej, nodei.id])
                if nodes[nodej].is_act():
                    r_pi *= (1 - eta[nodej, nodei.id])
            nodei.v = (1 - v_pi) * nodei.get_open(t)
            nodei.r = (1 - r_pi) * nodei.get_open(t)
            v[t, nodei.id] = (1 - v_pi) * nodei.get_open(t)
            r[t, nodei.id] = (1 - r_pi) * nodei.get_open(t)

        # 判断是否为补丁包投放时刻
        if t == r_t:
            nodes[1].set_state(1)
            nodes[1].set_spr(t, sim_time, 'iso')

        # 节点根据概率更新自身状态
        count_states = [0, 0, 0, 0, 0]
        for node in nodes:
            count_states[node.get_state()] += 1
            node.new_state(t, sim_time)
            nodes_color[node.id] = node.state

        # add count
        inf_nums[t] = count_states[3]+count_states[4]
        rco_nums[t] = count_states[1]+count_states[2]
        sus_nums[t] = count_states[0]
        ins_nums[t] = count_states[1]
        act_nums[t] = count_states[2]
        iso_nums[t] = count_states[3]
        com_nums[t] = count_states[4]

        # draw graph
        nx.draw_networkx_nodes(g, pos=pos, node_color=nodes_color,
                               node_size=20)
        # show graph
        filename = 'WSNsim/WSNsim_{}.png'.format(t)
        plt.savefig(filename, format='png')
        keyFrames.append(filename)

    # end of sim

    plt.clf()
    # print fig
    plt.plot(inf_nums, 'r')
    plt.plot(rco_nums, 'b')
    # plt.plot(sus_nums, 'c')
    plt.plot(iso_nums, 'r-.')
    plt.plot(com_nums, 'r--')
    plt.plot(ins_nums, 'b-.')
    plt.plot(act_nums, 'b--')
    plt.savefig('test', format='png')
