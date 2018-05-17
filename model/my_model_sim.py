# -*- coding: utf-8 -*-
import numpy as np
import random

import networkx as nx
from matplotlib import pyplot as plt

from nodes.RandomNode import RandomNode


def my_model_sim(open, spr, eta_low, eta_high, alpha, r_t, beta, rho,
                 rd_nodes_pos, nodes_num, sim_time, graph, g_pos,
                 sur_type):
    lines = []
    # 创建用于状态处理的随机节点
    # my_model 节点
    my_nodes = []
    for rd_node in rd_nodes_pos:
        rn = RandomNode(rd_node, rd_nodes_pos.index(rd_node), 0, sim_time)
        my_nodes.append(rn)
    my_nodes_color = ['sus'] * nodes_num

    # 更改病毒投放节点属性
    my_nodes[0].set_state(3)
    my_nodes_color[0] = 'iso'

    # # # 指定补丁包投放节点

    # # # 新建信息传播概率的矩阵
    eta = random_np(eta_low, eta_high, nodes_num)

    # plt.clf()
    # nx.draw_networkx_nodes(graph, pos=g_pos, node_color=my_nodes_color, node_size=20)
    # # show graph
    # filename = 'WSNsim/WSNsim_{}.png'.format(0)
    # plt.savefig(filename, format='png')

    # 感染概率 和 恢复概率
    v = np.zeros((sim_time, nodes_num))
    r = np.zeros((sim_time, nodes_num))

    # 统计数据
    inf_nums = [1] + [0 for _ in range(1, sim_time)]
    rco_nums = [0] + [0 for _ in range(1, sim_time)]
    sus_nums = [nodes_num - 1] + [0 for _ in range(1, sim_time)]
    iso_nums = [1] + [0 for _ in range(1, sim_time)]
    com_nums = [0] + [0 for _ in range(1, sim_time)]
    ins_nums = [0] + [0 for _ in range(1, sim_time)]
    act_nums = [0] + [0 for _ in range(1, sim_time)]

    for t in range(1, sim_time):
        # R_t = g_r*t
        # 更新节点的感染概率和恢复概率
        for nodei in my_nodes:
            v_pi = 1
            r_pi = 1
            for nodej in nx.neighbors(graph, nodei.id):
                if my_nodes[nodej].is_com():
                    v_pi *= (1 - eta[nodej, nodei.id])
                if my_nodes[nodej].is_act():
                    r_pi *= (1 - eta[nodej, nodei.id])
            nodei.v = (1 - v_pi) * nodei.get_open(t, open)
            nodei.r = (1 - r_pi) * nodei.get_open(t, open)
            v[t, nodei.id] = (1 - v_pi) * nodei.get_open(t, open) * beta
            r[t, nodei.id] = (1 - r_pi) * nodei.get_open(t, open) * rho

        # 判断是否为补丁包投放时刻
        if t == r_t:
            my_nodes[1].set_state(1)
            my_nodes[1].set_spr(t, sim_time, 'iso')

        # 节点根据概率更新自身状态
        count_states = [0, 0, 0, 0, 0]
        for node in my_nodes:
            node.new_state(t, sim_time, spr, alpha)
            count_states[node.get_state()] += 1
            my_nodes_color[node.id] = node.state

        # add count
        inf_nums[t] = count_states[3] + count_states[4]
        rco_nums[t] = count_states[1] + count_states[2]
        sus_nums[t] = count_states[0]
        ins_nums[t] = count_states[1]
        act_nums[t] = count_states[2]
        iso_nums[t] = count_states[3]
        com_nums[t] = count_states[4]

        # # draw graph
        # plt.clf()
        # nx.draw_networkx_nodes(graph, pos=g_pos, node_color=my_nodes_color,
        #                        node_size=20)
        # # show graph
        # filename = 'WSNsim/WSNsim_{}.png'.format(t)
        # plt.savefig(filename, format='png')

    # end of sim
    for type in sur_type:
        if type == 'inf':
            lines.append(inf_nums)
        elif type == 'rco':
            lines.append(rco_nums)

    return lines


def random_np(low, high, nodes_num):
    m = np.zeros((nodes_num, nodes_num))
    for i in range(nodes_num):
        for j in range(nodes_num):
            m[i, j] = random.uniform(low, high)
    return m