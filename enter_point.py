from Graph import draw_graph
from matplotlib import pyplot as plt

# from fig_2_3 import draw_graph_2_3

# line = draw_graph_2_3(density=0.15, side_width=200, side_height=100,
#                       sim_time=50, g_r=5,
#                       v_x=100, v_y=50,
#                       r_x=100, r_y=50, r_t=51)
#
# plt.clf()
# plt.ylabel('I(t) & S(t)')
# plt.xlabel('Time/Unit of Time')
# plt.xlim(0, 50)
# # print fig
# plt.plot(line[0], 'r', label='I(t)')
# plt.plot(line[1], 'b', label='S(t)')
# plt.legend(loc='lower right')
#
# plt.savefig('fig_2_3', format='png')


# from fig_2_5 import draw_graph_2_5
#
# lines_2 = draw_graph_2_5(density=0.15, side_width=200, side_height=100,
#                          sim_time=100, g_r=5,
#                          v_x=100, v_y=50,
#                          r_x=100, r_y=50, r_t=101)
#
# plt.clf()
# plt.ylabel('I(t) & S(t)')
# plt.xlabel('Time/Unit of Time')
# plt.xlim(0, 100)
# # print fig
# plt.plot(lines_2[0], 'r', label='I(t)')
# plt.plot(lines_2[1], 'b', label='S(t)')
# plt.legend(loc='lower right')
#
# plt.savefig('fig_2_5', format='png')
from fig_2_7 import draw_graph_2_7

lines_3 = draw_graph_2_7(density=0.15, side_width=200, side_height=100,
                         sim_time=100, g_r=5,
                         v_x=100, v_y=50,
                         r_x=100, r_y=50, r_t=10)

plt.clf()
plt.ylabel('I(t) & S(t) & R(t)')
plt.xlabel('Time/Unit of Time')
plt.xlim(0, 100)
# print fig
plt.plot(lines_3[0], 'r', label='I(t)')
plt.plot(lines_3[1], 'b', label='S(t)')
plt.plot(lines_3[2], 'y', label='R(t)')
plt.legend(loc='lower right')

plt.savefig('fig_2_7', format='png')
#
# lines_4 = draw_graph(density=0.15, side_width=200, side_height=100,
#                      sim_time=180, g_r=10,
#                      v_x=100, v_y=50,
#                      r_x=100, r_y=50, r_t=30)
#
# plt.clf()
# plt.ylabel('I(t) & R(t)')
# plt.xlabel('Time/Unit of Time')
# plt.xlim(0, 180)
# # print fig
# plt.plot(lines_4[0], 'r')
# plt.plot(lines_4[1], 'b')
#
# plt.savefig('test_4', format='png')


# lines_5 = draw_graph(density=0.15, side_width=200, side_height=100,
#                      sim_time=180, g_r=5,
#                      v_x=100, v_y=50,
#                      r_x=100, r_y=50, r_t=30)
#
# plt.clf()
# plt.ylabel('I(t) & R(t)')
# plt.xlabel('Time/Unit of Time')
# plt.xlim(0, 180)
# # print fig
# plt.plot(lines_5[0], 'r')
# plt.plot(lines_5[1], 'b')
#
# plt.savefig('test_5', format='png')
# #
# lines_6 = draw_graph(density=0.15, side_width=200, side_height=100,
#                      sim_time=180, g_r=5,
#                      v_x=100, v_y=50,
#                      r_x=100, r_y=50, r_t=30)
#
# plt.clf()
# plt.ylabel('I(t) & R(t)')
# plt.xlabel('Time/Unit of Time')
# plt.xlim(0, 180)
# # print fig
# plt.plot(lines_6[0], 'r')
# plt.plot(lines_6[1], 'b')
#
# plt.savefig('test_6', format='png')
