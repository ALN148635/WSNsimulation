# -*- coding: utf-8 -*-
import networkx as nx
from matplotlib import pyplot as plt

from nodes.OrgSISNode import OrgSISNode


def org_sis_model_sim(beta, rou,
                  rd_nodes_pos, nodes_num, sim_time, graph, g_pos,
                  sur_type):
    # 创建用于状态处理的随机节点
    # creat nodes
    # # org_model 节点
    lines = []
    org_nodes = []
    for rd_node in rd_nodes_pos:
        tn = OrgSISNode(rd_node, rd_nodes_pos.index(rd_node), 0,
                     beta=beta, rou=rou)
        org_nodes.append(tn)
    org_nodes_color = ['o_sus'] * nodes_num

    # 更改病毒节点状态
    org_nodes[0].state = 'o_inf'
    org_nodes_color[0] = 'o_inf'

    # 更改补丁包节点状态

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

    for t in range(1, sim_time):
        # tang model
        org_inf_nodes = []
        for org_node in org_nodes:
            if org_node.state == 'o_inf':
                org_inf_nodes.append(org_node)

        for inf_node in org_inf_nodes:
            for nodej in nx.neighbors(graph, inf_node.id):
                org_nodes[nodej].new_inf_state()

        org_states = [0, 0]
        for org_node in org_nodes:
            org_node.new_state()
            org_states[org_node.get_state()] += 1
            org_nodes_color[org_node.id] = org_node.state

        # add count
        org_inf_nums[t] = org_states[1]
        org_sus_nums[t] = org_states[0]

        # # draw graph
        # plt.clf()
        # nx.draw_networkx_nodes(graph, pos=g_pos, node_color=org_nodes_color, node_size=20)
        # # show graph
        # filename = 'WSNsim/WSNsim_org_{}.png'.format(t)
        # plt.savefig(filename, format='png')

    for s_type in sur_type:
        if s_type in 'o_inf':
            lines.append(org_inf_nums)
        elif s_type in 'o_sus':
            lines.append(org_sus_nums)

    return lines
