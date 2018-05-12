# -*- coding: utf-8 -*-
import networkx as nx
from matplotlib import pyplot as plt

from nodes.OrgNode import OrgNode


def org_model_sim(beta, rou, r_t,
                  rd_nodes_pos, nodes_num, sim_time, graph, g_pos,
                  lines):
    # 创建用于状态处理的随机节点
    # creat nodes
    # # org_model 节点
    org_nodes = []
    for rd_node in rd_nodes_pos:
        tn = OrgNode(rd_node, rd_nodes_pos.index(rd_node), 0,
                      beta=beta, rou=rou)
        org_nodes.append(tn)
    org_nodes_color = ['o_sus'] * nodes_num

    # 更改病毒节点状态
    org_nodes[0].state = 'o_inf'
    org_nodes_color[0] = 'o_inf'

    # 更改补丁包节点状态
    org_nodes[1].state = 'o_rco'
    org_nodes_color[0] = 'o_rco'

    # end of creat nodes

    # # draw graph
    # plt.clf()
    # nx.draw_networkx_nodes(graph, pos=g_pos, node_color=org_nodes_color, node_size=20)
    # # show graph
    # filename = 'WSNsim/WSNsim_org_{}.png'.format(0)
    # plt.savefig(filename, format='png')

    # 统计数据
    org_sus_nums = [nodes_num - 1] + [0 for _ in range(1, sim_time)]
    org_inf_nums = [1] + [0 for _ in range(1, sim_time)]
    org_rco_nums = [0] + [0 for _ in range(1, sim_time)]

    for t in range(1, sim_time):
        # tang model
        org_inf_nodes = []
        for org_node in org_nodes:
            if org_node.state == 'o_inf':
                org_inf_nodes.append(org_node)

        for inf_node in org_inf_nodes:
            for nodej in nx.neighbors(graph, inf_node.id):
                org_nodes[nodej].new_inf_state()

        # 判断是否为补丁包投放时刻
        if t == r_t:
            org_nodes[1].state = 'rco'

        org_rco_nodes = []
        for org_node in org_nodes:
            if org_node.state == 'o_rco':
                org_inf_nodes.append(org_node)

        for rco_node in org_rco_nodes:
            for nodej in nx.neighbors(graph, rco_node.id):
                org_nodes[nodej].new_rco_state()

        org_states = [0, 0, 0]
        for org_node in org_nodes:
            org_states[org_node.get_state()] += 1
            org_nodes_color[org_node.id] = org_node.state

        # add count
        org_inf_nums[t] = org_states[1]
        org_sus_nums[t] = org_states[0]
        org_rco_nums[t] = org_states[2]

        # # draw graph
        # plt.clf()
        # nx.draw_networkx_nodes(graph, pos=g_pos, node_color=org_nodes_color, node_size=20)
        # # show graph
        # filename = 'WSNsim/WSNsim_org_{}.png'.format(t)
        # plt.savefig(filename, format='png')

    lines.append(org_inf_nums)
