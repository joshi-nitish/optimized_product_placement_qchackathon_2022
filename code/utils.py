import numpy as np
import random
import bfs

def randomly_assign_products_to_racks(layout_obj, list_items):

    assert len(layout_obj.rack_position_list) >= len(list_items)
    for position_tuple, item in zip(layout_obj.rack_position_list, list_items):
        layout_obj.pos_to_product_dict[position_tuple] = item

    layout_obj.product_to_pos_dict = {value:key for key,value in layout_obj.pos_to_product_dict.items()}

def is_point_valid(x,y,grid):
    if ((x >= 0 and y >= 0) and (x < grid.shape[0] and y < grid.shape[1])) and (grid[x,y] == 0):
        return True
    return False

def get_access_point_list(item_pos, grid):
    
    access_point_list = []

    if is_point_valid(item_pos[0]- 1, item_pos[1], grid):
        access_point_list.append((item_pos[0] - 1, item_pos[1]))

    if is_point_valid(item_pos[0]+ 1, item_pos[1], grid):
        access_point_list.append((item_pos[0] + 1, item_pos[1]))

    if is_point_valid(item_pos[0], item_pos[1] - 1, grid):
        access_point_list.append((item_pos[0], item_pos[1] - 1))

    if is_point_valid(item_pos[0], item_pos[1] + 1, grid):
        access_point_list.append((item_pos[0], item_pos[1] + 1))
    
    return access_point_list


def calc_distance(layout_obj, start_pos_tuple, order_list):
    #returns distance traveled to complete picking for order_list, starting from a position,
    # and picking orders in the order of the list.
    distance = 0
    prev_position = start_pos_tuple
    for item in order_list:
        access_point_list = get_access_point_list(layout_obj.product_to_pos_dict[item], layout_obj.layout_mat)
        min_dist = 9999999999
        for point in access_point_list:
            bfs_dist = bfs.minDistance(layout_obj, prev_position, point)
            if min_dist > bfs_dist:
                min_pos = point
                min_dist = bfs_dist
        prev_position = min_pos
        distance += min_dist
    
    return distance





    
