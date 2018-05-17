from Graph import draw_graph
from matplotlib import pyplot as plt

point_1 = draw_graph(density=0.05, side_width=200, side_height=100,
                     sim_time=80, g_r=5,
                     v_x=100, v_y=50,
                     r_x=100, r_y=50, r_t=301)

point_2 = draw_graph(density=0.15, side_width=200, side_height=100,
                     sim_time=50, g_r=5,
                     v_x=100, v_y=50,
                     r_x=100, r_y=50, r_t=301)

point_3 = draw_graph(density=0.25, side_width=200, side_height=100,
                     sim_time=40, g_r=5,
                     v_x=100, v_y=50,
                     r_x=100, r_y=50, r_t=301)

point_4 = draw_graph(density=0.35, side_width=200, side_height=100,
                     sim_time=30, g_r=5,
                     v_x=100, v_y=50,
                     r_x=100, r_y=50, r_t=301)

point_5 = draw_graph(density=0.45, side_width=200, side_height=100,
                     sim_time=20, g_r=5,
                     v_x=100, v_y=50,
                     r_x=100, r_y=50, r_t=301)

point_6 = draw_graph(density=0.55, side_width=200, side_height=100,
                     sim_time=20, g_r=5,
                     v_x=100, v_y=50,
                     r_x=100, r_y=50, r_t=301)

point_7 = draw_graph(density=0.65, side_width=200, side_height=100,
                     sim_time=10, g_r=5,
                     v_x=100, v_y=50,
                     r_x=100, r_y=50, r_t=301)

point_8 = draw_graph(density=0.75, side_width=200, side_height=100,
                     sim_time=10, g_r=5,
                     v_x=100, v_y=50,
                     r_x=100, r_y=50, r_t=301)

point_9 = draw_graph(density=0.85, side_width=200, side_height=100,
                     sim_time=5, g_r=5,
                     v_x=100, v_y=50,
                     r_x=100, r_y=50, r_t=301)

point_10 = draw_graph(density=0.95, side_width=200, side_height=100,
                     sim_time=3, g_r=5,
                     v_x=100, v_y=50,
                     r_x=100, r_y=50, r_t=301)

y_points = [point_1, point_2, point_3, point_4, point_5,
            point_6, point_7, point_8, point_9, point_10]
x_points = [0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75,
            0.85, 0.95]

tang_points = [2.4, 3.25, 3.6, 3.85, 4.0, 4.07, 4.13, 4.18, 4.23, 4.27]
tang_th_points = [1.93, 2.6, 3.03, 3.4, 3.57, 3.79, 3.90, 4.0, 4.06, 4.13]

plt.clf()
plt.ylabel('propagation speed (m/unit of time)')
plt.xlabel(r'$nodes/m^{2}$')
plt.xlim(0, 1)
# print fig
plt.plot(y_points, x_points, 'r--')
plt.plot(y_points, x_points, 'rx')

plt.plot(tang_points, x_points, 'k--')
plt.plot(tang_points, x_points, 'ko')

plt.plot(tang_th_points, x_points, 'r--')
plt.plot(tang_th_points, x_points, 'r^')
# plt.plot(lines_1[3], 'y', label='f')
# plt.legend(loc='lower right')

plt.savefig('test', format='png')

# lines_2 = draw_graph(density=0.15, side_width=200, side_height=100,
#                      sim_time=180, g_r=6,
#                      v_x=100, v_y=50,
#                      r_x=100, r_y=50, r_t=30)
#
# plt.clf()
# plt.ylabel('I(t) & R(t)')
# plt.xlabel('Time/Unit of Time')
# plt.xlim(0, 180)
# # print fig
# plt.plot(lines_2[0], 'r')
# plt.plot(lines_2[1], 'b')
#
# plt.savefig('test_2', format='png')
#
# lines_3 = draw_graph(density=0.15, side_width=200, side_height=100,
#                      sim_time=180, g_r=8,
#                      v_x=100, v_y=50,
#                      r_x=100, r_y=50, r_t=30)
#
# plt.clf()
# plt.ylabel('I(t) & R(t)')
# plt.xlabel('Time/Unit of Time')
# plt.xlim(0, 180)
# # print fig
# plt.plot(lines_3[0], 'r')
# plt.plot(lines_3[1], 'b')
#
# plt.savefig('test_3', format='png')
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
