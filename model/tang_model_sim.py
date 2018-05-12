# -*- coding: utf-8 -*-
import networkx as nx
from matplotlib import pyplot as plt

from nodes.TangNode import TangNode


def tang_model_sim(a, s, beta, rou,
                   rd_nodes_pos, nodes_num, sim_time, graph, g_pos,
                   lines):
    # 创建用于状态处理的随机节点
    # creat nodes
    # # tang_model 节点
    tang_nodes = []
    # # my_model 节点
    for rd_node in rd_nodes_pos:
        tn = TangNode(rd_node, rd_nodes_pos.index(rd_node), 0,
                      beta=beta, rou=rou)
        tang_nodes.append(tn)
    tang_nodes_color = ['t_sus'] * nodes_num

    # 更改病毒节点状态
    tang_nodes[0].state = 't_inf'
    tang_nodes_color[0] = 't_inf'

    # 更改补丁包节点状态

    # end of creat nodes

    # # draw graph
    # plt.clf()
    # nx.draw_networkx_nodes(graph, pos=g_pos, node_color=tang_nodes_color, node_size=20)
    # # show graph
    # filename = 'WSNsim/WSNsim_tang_{}.png'.format(0)
    # plt.savefig(filename, format='png')

    # 统计数据
    tang_sus_nums = [nodes_num - 1] + [0 for _ in range(1, sim_time)]
    tang_inf_nums = [1] + [0 for _ in range(1, sim_time)]
    tang_islp_nums = [0] + [0 for _ in range(1, sim_time)]
    tang_iinf_nums = [1] + [0 for _ in range(1, sim_time)]
    tang_ssus_nums = [nodes_num - 1] + [0 for _ in range(1, sim_time)]
    tang_sslp_nums = [0] + [0 for _ in range(1, sim_time)]

    for t in range(1, sim_time):

        # tang model
        tang_inf_nodes = []
        for tang_node in tang_nodes:
            if tang_node.state == 't_inf':
                tang_inf_nodes.append(tang_node)

        for inf_node in tang_inf_nodes:
            for nodej in nx.neighbors(graph, inf_node.id):
                tang_nodes[nodej].new_inf_state()

        tang_states = [0, 0, 0, 0, 0]
        for tang_node in tang_nodes:
            tang_node.new_state(a, s)
            tang_states[tang_node.get_state()] += 1
            tang_nodes_color[tang_node.id] = tang_node.state

        # add count
        tang_inf_nums[t] = tang_states[2] + tang_states[3]
        tang_sus_nums[t] = tang_states[0] + tang_states[1]
        tang_iinf_nums[t] = tang_states[2]
        tang_islp_nums[t] = tang_states[3]
        tang_ssus_nums[t] = tang_states[0]
        tang_sslp_nums[t] = tang_states[1]

        # # draw graph
        # nx.draw_networkx_nodes(graph, pos=g_pos, node_color=tang_nodes_color,
        #                        node_size=20)
        # # show graph
        # filename = 'WSNsim/WSNsim_tang_{}.png'.format(t)
        # plt.savefig(filename, format='png')

    # end of sim
    lines.append(tang_inf_nums)