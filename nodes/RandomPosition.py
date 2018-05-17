import random


# return List[(int, int)...]
def get_random_position(density, side_width, side_height):
    d = density
    # h = side_length
    node_num = int(d*side_width*side_height)
    pos_list = []
    for x in random.sample(range(side_width * side_height), node_num):
        pos_x, pos_y = divmod(x, side_height)
        pos_list.append((pos_x, pos_y))
    return pos_list


# print(get_random_position(0.3, 10))
