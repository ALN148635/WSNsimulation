from Graph import draw_graph
from matplotlib import pyplot as plt

# from fig_2_3 import draw_graph_2_3
#
# line = draw_graph_2_3(density=0.15, side_width=200, side_height=100,
#                       sim_time=50, g_r=5,
#                       v_x=100, v_y=50,
#                       r_x=100, r_y=50, r_t=51)
#
# plt.clf()
# plt.ylabel('I(t) & S(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time', fontsize=20)
# plt.xlim(0, 50)
# # print fig
# plt.plot(line[0], 'r', label='I(t)')
# plt.plot(line[1], 'b', label='S(t)')
# plt.legend(loc='lower right')
#
# plt.savefig('fig_2_3.png', format='png')
#
#
# from fig_2_5 import draw_graph_2_5
#
# lines_2 = draw_graph_2_5(density=0.15, side_width=200, side_height=100,
#                          sim_time=100, g_r=5,
#                          v_x=100, v_y=50,
#                          r_x=100, r_y=50, r_t=101)
#
# plt.clf()
# plt.ylabel('I(t) & S(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time', fontsize=20)
# plt.xlim(0, 100)
# # print fig
# plt.plot(lines_2[0], 'r', label='I(t)')
# plt.plot(lines_2[1], 'b', label='S(t)')
# plt.legend(loc='lower right')
#
# plt.savefig('fig_2_5.png', format='png')
#
#
# from fig_2_7 import draw_graph_2_7
#
# lines_3 = draw_graph_2_7(density=0.15, side_width=200, side_height=100,
#                          sim_time=60, g_r=5,
#                          v_x=100, v_y=50,
#                          r_x=100, r_y=50, r_t=20)
#
# plt.clf()
# plt.ylabel('I(t) & S(t) & R(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time', fontsize=20)
# plt.xlim(0, 60)
# # print fig
# plt.plot(lines_3[0], 'r', label='I(t)')
# plt.plot(lines_3[1], 'b', label='S(t)')
# plt.plot(lines_3[2], 'y', label='R(t)')
# plt.legend(loc='lower right')
#
# plt.savefig('fig_2_7.png', format='png')


# from fig_2_9 import draw_graph_2_9
#
# lines_4 = draw_graph_2_9(density=0.15, side_width=200, side_height=100,
#                          sim_time=100, g_r=10,
#                          v_x=100, v_y=50,
#                          r_x=100, r_y=50, r_t=30)
#
# plt.clf()
# plt.ylabel('I(t) & S(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time', fontsize=20)
# plt.xlim(0, 100)
# # print fig
# plt.plot(lines_4[0], 'r', label='I(t)')
# plt.plot(lines_4[1], 'b', label='S(t)')
# plt.legend(loc='lower right')
#
# plt.savefig('fig_2_9.png', format='png')


# from fig_2_10 import draw_graph_2_10
#
# lines_5 = draw_graph_2_10(density=0.15, side_width=200, side_height=100,
#                      sim_time=150, g_r=5,
#                      v_x=100, v_y=50,
#                      r_x=100, r_y=50, r_t=30)
#
# plt.clf()
# plt.ylabel('I(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time', fontsize=20)
# plt.xlim(0, 150)
# # print fig
# plt.plot(lines_5[0], 'b', label=r'SIS: $\beta$=0.6 $\delta$=0.3')
# plt.plot(lines_5[1], 'r', label=r'tang-SIS: $\beta$=0.6 $\rho$=0.3')
# plt.plot(lines_5[2], 'm', label=r'tang-SIS: $\beta$=0.6 $\rho$=0.7')
# plt.legend(loc='lower right')
#
# plt.savefig('fig_2_10.png', format='png')


# from fig_3_3 import draw_graph_3_3
#
# lines = draw_graph_3_3(density=0.15, side_width=200, side_height=100,
#                        sim_time=180, g_r=5,
#                        v_x=100, v_y=50,
#                        r_x=100, r_y=50, r_t=181)
#
# plt.clf()
# plt.ylabel('I(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time', fontsize=20)
# plt.xlim(0, 180)
# # print fig
# plt.plot(lines[0], 'b', label='P(open)=P(spr)=0.2')
# plt.plot(lines[1], 'g', label='P(open)=P(spr)=0.3')
# plt.plot(lines[2], 'r', label='P(open)=P(spr)=0.4')
# plt.plot(lines[3], 'c', label='P(open)=P(spr)=0.5')
# plt.plot(lines[4], 'm', label='P(open)=P(spr)=0.6')
# plt.plot(lines[5], 'y', label='P(open)=P(spr)=0.7')
# plt.legend(loc='lower right')
#
# plt.savefig('fig_3_3.png', format='png')
#
#
# from fig_3_4 import draw_graph_3_4
#
# lines = draw_graph_3_4(density=0.15, side_width=200, side_height=100,
#                        sim_time=180, g_r=5,
#                        v_x=100, v_y=50,
#                        r_x=100, r_y=50, r_t=181)
#
# plt.clf()
# plt.ylabel('I(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time', fontsize=20)
# plt.xlim(0, 180)
# # print fig
# plt.plot(lines[0], 'b', label='P(spr)=0.2')
# plt.plot(lines[1], 'g', label='P(spr)=0.3')
# plt.plot(lines[2], 'r', label='P(spr)=0.4')
# plt.plot(lines[3], 'c', label='P(spr)=0.5')
# plt.plot(lines[4], 'm', label='P(spr)=0.6')
# plt.plot(lines[5], 'y', label='P(spr)=0.7')
# plt.legend(loc='lower right')
#
# plt.savefig('fig_3_4.png', format='png')
#
#
# from fig_3_5 import draw_graph_3_5
#
# lines = draw_graph_3_5(density=0.15, side_width=200, side_height=100,
#                        sim_time=180, g_r=5,
#                        v_x=100, v_y=50,
#                        r_x=100, r_y=50, r_t=181)
#
# plt.clf()
# plt.ylabel('I(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time', fontsize=20)
# plt.xlim(0, 180)
# # print fig
# plt.plot(lines[0], 'b', label='P(open)=0.2')
# plt.plot(lines[1], 'g', label='P(open)=0.3')
# plt.plot(lines[2], 'r', label='P(open)=0.4')
# plt.plot(lines[3], 'c', label='P(open)=0.5')
# plt.plot(lines[4], 'm', label='P(open)=0.6')
# plt.plot(lines[5], 'y', label='P(open)=0.7')
# plt.legend(loc='lower right')
#
# plt.savefig('fig_3_5.png', format='png')


# from fig_3_6 import draw_graph_3_6
#
# lines = draw_graph_3_6(density=0.15, side_width=200, side_height=100,
#                        sim_time=180, g_r=5,
#                        v_x=100, v_y=50,
#                        r_x=100, r_y=50, r_t=181)
#
# plt.clf()
# plt.ylabel('I(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time\n(a)', fontsize=20)
# plt.xlim(0, 180)
# # print fig
# plt.plot(lines[0], 'b', label='40%~100%')
# plt.plot(lines[1], 'g', label='50%~100%')
# plt.plot(lines[2], 'r', label='60%~100%')
# plt.plot(lines[3], 'c', label='70%~100%')
# plt.plot(lines[4], 'm', label='80%~100%')
# plt.plot(lines[5], 'y', label='90%~100%')
# plt.legend(loc='lower right')
# plt.savefig('fig_3_6_1.png', format='png')
#
# plt.clf()
# plt.ylabel('I(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time\n(b)', fontsize=20)
# plt.xlim(0, 180)
# # print fig
# plt.plot(lines[6], 'b', label='40%~50%')
# plt.plot(lines[7], 'g', label='50%~60%')
# plt.plot(lines[8], 'r', label='60%~70%')
# plt.plot(lines[9], 'c', label='70%~80%')
# plt.plot(lines[10], 'm', label='80%~90%')
# plt.plot(lines[11], 'y', label='90%~100%')
# plt.legend(loc='lower right')
# plt.savefig('fig_3_6_2.png', format='png')

#
# from fig_3_7 import draw_graph_3_7
#
# lines = draw_graph_3_7(density=0.15, side_width=200, side_height=100,
#                        sim_time=100, g_r=5,
#                        v_x=100, v_y=50,
#                        r_x=100, r_y=50, r_t=181)
#
# plt.clf()
# plt.ylabel('I(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time', fontsize=20)
# plt.xlim(0, 100)
# # print fig
# plt.plot(lines[0], 'b', label='without')
# plt.plot(lines[1], 'r', label='with')
# plt.legend(loc='lower right')
#
# plt.savefig('fig_3_7.png', format='png')
#
#
# from fig_3_9 import draw_graph_3_9
#
# lines_1 = draw_graph_3_9(density=0.05, side_width=200, side_height=100,
#                          sim_time=100, g_r=5,
#                          v_x=100, v_y=50,
#                          r_x=100, r_y=50, r_t=181)
#
# lines_2 = draw_graph_3_9(density=0.15, side_width=200, side_height=100,
#                          sim_time=100, g_r=5,
#                          v_x=100, v_y=50,
#                          r_x=100, r_y=50, r_t=181)
#
# lines_3 = draw_graph_3_9(density=0.15, side_width=200, side_height=100,
#                          sim_time=100, g_r=3,
#                          v_x=100, v_y=50,
#                          r_x=100, r_y=50, r_t=181)
#
# plt.clf()
# plt.ylabel('I(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time', fontsize=20)
# plt.xlim(0, 100)
# # print fig
# plt.plot(lines_1[0], 'b', label='without')
# plt.plot(lines_1[1], 'r', label='with')
# plt.legend(loc='lower right')
# plt.savefig('fig_3_9_1.png', format='png')
#
# plt.clf()
# plt.ylabel('I(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time\n()', fontsize=20)
# plt.xlim(0, 100)
# # print fig
# plt.plot(lines_2[0], 'b', label='without')
# plt.plot(lines_2[1], 'r', label='with')
# plt.legend(loc='lower right')
# plt.savefig('fig_3_9_2.png', format='png')
#
# plt.clf()
# plt.ylabel('I(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time', fontsize=20)
# plt.xlim(0, 100)
# # print fig
# plt.plot(lines_3[0], 'b', label='without')
# plt.plot(lines_3[1], 'r', label='with')
# plt.legend(loc='lower right')
# plt.savefig('fig_3_9_3.png', format='png')
#
#
# from fig_4_1 import draw_graph_4_1
#
# lines_1 = draw_graph_4_1(density=0.15, side_width=200, side_height=100,
#                          sim_time=150, g_r=4,
#                          v_x=100, v_y=50,
#                          r_x=100, r_y=50, r_t=20, pic=True, picName='_gr4_')
#
# lines_2 = draw_graph_4_1(density=0.15, side_width=200, side_height=100,
#                          sim_time=150, g_r=6,
#                          v_x=100, v_y=50,
#                          r_x=100, r_y=50, r_t=20)
#
# lines_3 = draw_graph_4_1(density=0.15, side_width=200, side_height=100,
#                          sim_time=150, g_r=8,
#                          v_x=100, v_y=50,
#                          r_x=100, r_y=50, r_t=20)
#
# lines_4 = draw_graph_4_1(density=0.15, side_width=200, side_height=100,
#                          sim_time=150, g_r=10,
#                          v_x=100, v_y=50,
#                          r_x=100, r_y=50, r_t=20)
#
# plt.clf()
# plt.ylabel('I(t) & R(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time\n(a)', fontsize=20)
# plt.xlim(0, 150)
# # print fig
# plt.plot(lines_1[0], 'r', label='I(t)')
# plt.plot(lines_1[1], 'b', label='R(t)')
# plt.legend(loc='lower right')
# plt.savefig('fig_4_1_1.png', format='png')
#
# plt.clf()
# plt.ylabel('I(t) & R(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time\n(b)', fontsize=20)
# plt.xlim(0, 150)
# # print fig
# plt.plot(lines_2[0], 'r', label='I(t)')
# plt.plot(lines_2[1], 'b', label='R(t)')
# plt.legend(loc='lower right')
# plt.savefig('fig_4_1_2.png', format='png')
#
# plt.clf()
# plt.ylabel('I(t) & R(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time\n(c)', fontsize=20)
# plt.xlim(0, 150)
# # print fig
# plt.plot(lines_3[0], 'r', label='I(t)')
# plt.plot(lines_3[1], 'b', label='R(t)')
# plt.legend(loc='lower right')
# plt.savefig('fig_4_1_3.png', format='png')
#
# plt.clf()
# plt.ylabel('I(t) & R(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time\n(d)', fontsize=20)
# plt.xlim(0, 150)
# # print fig
# plt.plot(lines_4[0], 'r', label='I(t)')
# plt.plot(lines_4[1], 'b', label='R(t)')
# plt.legend(loc='lower right')
# plt.savefig('fig_4_1_4.png', format='png')
#

# from fig_4_2 import draw_graph_4_2
#
# lines_1 = draw_graph_4_2(density=0.15, side_width=200, side_height=100,
#                          sim_time=180, g_r=5,
#                          v_x=100, v_y=50,
#                          r_x=100, r_y=50, r_t=20, pic=False, picName='_rt20_')
#
# lines_2 = draw_graph_4_2(density=0.15, side_width=200, side_height=100,
#                          sim_time=180, g_r=5,
#                          v_x=100, v_y=50,
#                          r_x=100, r_y=50, r_t=40)
#
# lines_3 = draw_graph_4_2(density=0.15, side_width=200, side_height=100,
#                          sim_time=180, g_r=5,
#                          v_x=100, v_y=50,
#                          r_x=100, r_y=50, r_t=60)
#
# lines_4 = draw_graph_4_2(density=0.15, side_width=200, side_height=100,
#                          sim_time=180, g_r=5,
#                          v_x=100, v_y=50,
#                          r_x=100, r_y=50, r_t=80)
#
# lines_5 = draw_graph_4_2(density=0.15, side_width=200, side_height=100,
#                          sim_time=180, g_r=5,
#                          v_x=100, v_y=50,
#                          r_x=100, r_y=50, r_t=100)
#
# plt.clf()
# plt.ylabel('I(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time', fontsize=20)
# plt.xlim(0, 180)
# # print fig
# plt.plot(lines_1[0], 'r', label='I(t)')
# plt.plot(lines_1[1], 'b', label='R(t)')
# plt.legend(loc='lower right')
# plt.savefig('fig_4_2_1.png', format='png')
#
# plt.clf()
# plt.ylabel('I(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time\n()', fontsize=20)
# plt.xlim(0, 180)
# # print fig
# plt.plot(lines_2[0], 'r', label='I(t)')
# plt.plot(lines_2[1], 'b', label='R(t)')
# plt.legend(loc='lower right')
# plt.savefig('fig_4_2_2.png', format='png')
#
# plt.clf()
# plt.ylabel('I(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time', fontsize=20)
# plt.xlim(0, 180)
# # print fig
# plt.plot(lines_3[0], 'r', label='I(t)')
# plt.plot(lines_3[1], 'b', label='R(t)')
# plt.legend(loc='lower right')
# plt.savefig('fig_4_2_3.png', format='png')
#
# plt.clf()
# plt.ylabel('I(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time', fontsize=20)
# plt.xlim(0, 180)
# # print fig
# plt.plot(lines_4[0], 'r', label='I(t)')
# plt.plot(lines_4[1], 'b', label='R(t)')
# plt.legend(loc='lower right')
# plt.savefig('fig_4_2_4.png', format='png')
#
# plt.clf()
# plt.ylabel('I(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time', fontsize=20)
# plt.xlim(0, 180)
# # print fig
# plt.plot(lines_5[0], 'r', label='I(t)')
# plt.plot(lines_5[1], 'b', label='R(t)')
# plt.legend(loc='lower right')
# plt.savefig('fig_4_2_5.png', format='png')
#
#
# from fig_4_3 import draw_graph_4_3
#
# lines_1 = draw_graph_4_3(density=0.15, side_width=200, side_height=100,
#                          sim_time=150, g_r=5,
#                          v_x=10, v_y=10,
#                          r_x=60, r_y=30, r_t=20, pic=False, picName='_4_3_')
#
# lines_2 = draw_graph_4_3(density=0.15, side_width=200, side_height=100,
#                          sim_time=150, g_r=5,
#                          v_x=60, v_y=30,
#                          r_x=60, r_y=30, r_t=20, pic=False, picName='_4_3_')
#
# lines_3 = draw_graph_4_3(density=0.15, side_width=200, side_height=100,
#                          sim_time=150, g_r=5,
#                          v_x=100, v_y=50,
#                          r_x=60, r_y=30, r_t=20, pic=False, picName='_4_3_')
#
# plt.clf()
# plt.ylabel('I(t) & R(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time', fontsize=20)
# plt.xlim(0, 150)
# # print fig
# plt.plot(lines_1[0], 'r', label='I(t)')
# plt.plot(lines_1[1], 'b', label='R(t)')
# plt.legend(loc='lower right')
# plt.savefig('fig_4_3_1.png', format='png')
#
# plt.clf()
# plt.ylabel('I(t) & R(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time', fontsize=20)
# plt.xlim(0, 150)
# # print fig
# plt.plot(lines_2[0], 'r', label='I(t)')
# plt.plot(lines_2[1], 'b', label='R(t)')
# plt.legend(loc='lower right')
# plt.savefig('fig_4_3_2.png', format='png')
#
# plt.clf()
# plt.ylabel('I(t) & R(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time', fontsize=20)
# plt.xlim(0, 150)
# # print fig
# plt.plot(lines_3[0], 'r', label='I(t)')
# plt.plot(lines_3[1], 'b', label='R(t)')
# plt.legend(loc='lower right')
# plt.savefig('fig_4_3_3.png', format='png')
#
# lines_1 = draw_graph_4_3(density=0.15, side_width=200, side_height=100,
#                          sim_time=150, g_r=7,
#                          v_x=10, v_y=10,
#                          r_x=60, r_y=30, r_t=20)
#
# lines_2 = draw_graph_4_3(density=0.15, side_width=200, side_height=100,
#                          sim_time=150, g_r=7,
#                          v_x=60, v_y=30,
#                          r_x=60, r_y=30, r_t=20)
#
# lines_3 = draw_graph_4_3(density=0.15, side_width=200, side_height=100,
#                          sim_time=150, g_r=7,
#                          v_x=100, v_y=50,
#                          r_x=60, r_y=30, r_t=20)
#
# plt.clf()
# plt.ylabel('I(t) & R(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time', fontsize=20)
# plt.xlim(0, 150)
# # print fig
# plt.plot(lines_1[0], 'r', label='I(t)')
# plt.plot(lines_1[1], 'b', label='R(t)')
# plt.legend(loc='lower right')
# plt.savefig('fig_4_3_4.png', format='png')
#
# plt.clf()
# plt.ylabel('I(t) & R(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time', fontsize=20)
# plt.xlim(0, 150)
# # print fig
# plt.plot(lines_2[0], 'r', label='I(t)')
# plt.plot(lines_2[1], 'b', label='R(t)')
# plt.legend(loc='lower right')
# plt.savefig('fig_4_3_5.png', format='png')
#
# plt.clf()
# plt.ylabel('I(t) & R(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time', fontsize=20)
# plt.xlim(0, 150)
# # print fig
# plt.plot(lines_3[0], 'r', label='I(t)')
# plt.plot(lines_3[1], 'b', label='R(t)')
# plt.legend(loc='lower right')
# plt.savefig('fig_4_3_6.png', format='png')
#
#
# lines_1 = draw_graph_4_3(density=0.15, side_width=200, side_height=100,
#                          sim_time=150, g_r=9,
#                          v_x=10, v_y=10,
#                          r_x=60, r_y=30, r_t=20)
#
# lines_2 = draw_graph_4_3(density=0.15, side_width=200, side_height=100,
#                          sim_time=150, g_r=9,
#                          v_x=60, v_y=30,
#                          r_x=60, r_y=30, r_t=20)
#
# lines_3 = draw_graph_4_3(density=0.15, side_width=200, side_height=100,
#                          sim_time=150, g_r=9,
#                          v_x=100, v_y=50,
#                          r_x=60, r_y=30, r_t=20)
#
# plt.clf()
# plt.ylabel('I(t) & R(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time', fontsize=20)
# plt.xlim(0, 150)
# # print fig
# plt.plot(lines_1[0], 'r', label='I(t)')
# plt.plot(lines_1[1], 'b', label='R(t)')
# plt.legend(loc='lower right')
# plt.savefig('fig_4_3_7.png', format='png')
#
# plt.clf()
# plt.ylabel('I(t) & R(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time', fontsize=20)
# plt.xlim(0, 150)
# # print fig
# plt.plot(lines_2[0], 'r', label='I(t)')
# plt.plot(lines_2[1], 'b', label='R(t)')
# plt.legend(loc='lower right')
# plt.savefig('fig_4_3_8.png', format='png')
#
# plt.clf()
# plt.ylabel('I(t) & R(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time', fontsize=20)
# plt.xlim(0, 150)
# # print fig
# plt.plot(lines_3[0], 'r', label='I(t)')
# plt.plot(lines_3[1], 'b', label='R(t)')
# plt.legend(loc='lower right')
# plt.savefig('fig_4_3_9.png', format='png')

# from fig_4_4 import draw_graph_4_4
#
# lines_1 = draw_graph_4_4(density=0.15, side_width=200, side_height=100,
#                          sim_time=150, g_r=5,
#                          v_x=10, v_y=10,
#                          r_x=60, r_y=30, r_t=20,
#                          beta=0.2)
#
# lines_2 = draw_graph_4_4(density=0.15, side_width=200, side_height=100,
#                          sim_time=150, g_r=5,
#                          v_x=60, v_y=30,
#                          r_x=60, r_y=30, r_t=20,
#                          beta=0.2)
#
# lines_3 = draw_graph_4_4(density=0.15, side_width=200, side_height=100,
#                          sim_time=150, g_r=5,
#                          v_x=100, v_y=50,
#                          r_x=60, r_y=30, r_t=20,
#                          beta=0.2)
#
# plt.clf()
# plt.ylabel('I(t) & R(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time', fontsize=20)
# plt.xlim(0, 150)
# # print fig
# plt.plot(lines_1[0], 'r', label='I(t)')
# plt.plot(lines_1[1], 'b', label='R(t)')
# plt.legend(loc='lower right')
# plt.savefig('fig_4_4_1.png', format='png')
#
#
# plt.clf()
# plt.ylabel('I(t) & R(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time', fontsize=20)
# plt.xlim(0, 150)
# # print fig
# plt.plot(lines_2[0], 'r', label='I(t)')
# plt.plot(lines_2[1], 'b', label='R(t)')
# plt.legend(loc='lower right')
# plt.savefig('fig_4_4_2.png', format='png')
#
# plt.clf()
# plt.ylabel('I(t) & R(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time', fontsize=20)
# plt.xlim(0, 150)
# # print fig
# plt.plot(lines_3[0], 'r', label='I(t)')
# plt.plot(lines_3[1], 'b', label='R(t)')
# plt.legend(loc='lower right')
# plt.savefig('fig_4_4_3.png', format='png')
#
# lines_1 = draw_graph_4_4(density=0.15, side_width=200, side_height=100,
#                          sim_time=150, g_r=5,
#                          v_x=10, v_y=10,
#                          r_x=60, r_y=30, r_t=20,
#                          beta=0.4)
#
# lines_2 = draw_graph_4_4(density=0.15, side_width=200, side_height=100,
#                          sim_time=150, g_r=5,
#                          v_x=60, v_y=30,
#                          r_x=60, r_y=30, r_t=20,
#                          beta=0.4)
#
# lines_3 = draw_graph_4_4(density=0.15, side_width=200, side_height=100,
#                          sim_time=150, g_r=5,
#                          v_x=100, v_y=50,
#                          r_x=60, r_y=30, r_t=20,
#                          beta=0.4)
#
# plt.clf()
# plt.ylabel('I(t) & R(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time', fontsize=20)
# plt.xlim(0, 150)
# # print fig
# plt.plot(lines_1[0], 'r', label='I(t)')
# plt.plot(lines_1[1], 'b', label='R(t)')
# plt.legend(loc='lower right')
# plt.savefig('fig_4_4_4.png', format='png')
#
#
# plt.clf()
# plt.ylabel('I(t) & R(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time', fontsize=20)
# plt.xlim(0, 150)
# # print fig
# plt.plot(lines_2[0], 'r', label='I(t)')
# plt.plot(lines_2[1], 'b', label='R(t)')
# plt.legend(loc='lower right')
# plt.savefig('fig_4_4_5.png', format='png')
#
# plt.clf()
# plt.ylabel('I(t) & R(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time', fontsize=20)
# plt.xlim(0, 150)
# # print fig
# plt.plot(lines_3[0], 'r', label='I(t)')
# plt.plot(lines_3[1], 'b', label='R(t)')
# plt.legend(loc='lower right')
# plt.savefig('fig_4_4_6.png', format='png')
#
# lines_1 = draw_graph_4_4(density=0.15, side_width=200, side_height=100,
#                          sim_time=150, g_r=5,
#                          v_x=10, v_y=10,
#                          r_x=60, r_y=30, r_t=20,
#                          beta=0.8)
#
# lines_2 = draw_graph_4_4(density=0.15, side_width=200, side_height=100,
#                          sim_time=150, g_r=5,
#                          v_x=60, v_y=30,
#                          r_x=60, r_y=30, r_t=20,
#                          beta=0.8)
#
# lines_3 = draw_graph_4_4(density=0.15, side_width=200, side_height=100,
#                          sim_time=150, g_r=5,
#                          v_x=100, v_y=50,
#                          r_x=60, r_y=30, r_t=20,
#                          beta=0.8)
#
# plt.clf()
# plt.ylabel('I(t) & R(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time', fontsize=20)
# plt.xlim(0, 150)
# # print fig
# plt.plot(lines_1[0], 'r', label='I(t)')
# plt.plot(lines_1[1], 'b', label='R(t)')
# plt.legend(loc='lower right')
# plt.savefig('fig_4_4_7.png', format='png')
#
#
# plt.clf()
# plt.ylabel('I(t) & R(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time', fontsize=20)
# plt.xlim(0, 150)
# # print fig
# plt.plot(lines_2[0], 'r', label='I(t)')
# plt.plot(lines_2[1], 'b', label='R(t)')
# plt.legend(loc='lower right')
# plt.savefig('fig_4_4_8.png', format='png')
#
# plt.clf()
# plt.ylabel('I(t) & R(t)', fontsize=20)
# plt.xlabel('Time/Unit of Time', fontsize=20)
# plt.xlim(0, 150)
# # print fig
# plt.plot(lines_3[0], 'r', label='I(t)')
# plt.plot(lines_3[1], 'b', label='R(t)')
# plt.legend(loc='lower right')
# plt.savefig('fig_4_4_9.png', format='png')

from Graph import draw_graph

lines = draw_graph(density=0.15, side_width=200, side_height=100,
                   sim_time=150, g_r=5,
                   v_x=100, v_y=50,
                   r_x=0, r_y=0, r_t=151)

plt.clf()
plt.ylabel('I(t)', fontsize=20)
plt.xlabel('Time/Unit of Time', fontsize=20)
plt.xlim(0, 150)
# print fig
plt.plot(lines[0], 'r', label='new_SI')
plt.plot(lines[1], 'b', label='tang_SIS')
plt.plot(lines[2], 'g', label='SI')
plt.legend(loc='lower right')
plt.savefig('fig_three.png', format='png')
