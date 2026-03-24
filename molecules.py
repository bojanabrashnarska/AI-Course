from searching_framework import *



def move_atom(x, y, direction, others, obstacles):
    if direction == 'Right':
        dx, dy = 1, 0
    elif direction == 'Left':
        dx, dy = -1, 0
    elif direction == 'Up':
        dx, dy = 0, 1
    elif direction == 'Down':
        dx, dy = 0, -1

    while True:
        nx = x + dx
        ny = y + dy

        if nx < 0 or nx > 8:
            break
        if ny < 0 or ny > 6:
            break
        if [nx, ny] in obstacles:
            break
        if [nx, ny] in others:
            break
        x = nx
        y = ny

    return x, y



class Molecules(Problem):

    def __init__(self, obstacles, initial, goal=None):
        super().__init__(initial, goal)
        self.obstacles = obstacles

    def successor(self, state):
        h1_x = state[0]
        h1_y = state[1]
        h2_x = state[2]
        h2_y = state[3]
        o_x = state[4]
        o_y = state[5]

        successors = {}

        others = [[h2_x, h2_y], [o_x, o_y]]

        new_x, new_y  = move_atom(h1_x, h1_y, 'Right', others, self.obstacles)
        if new_x != h1_x:
            successors['RightH1'] = (new_x, h1_y, h2_x, h2_y, o_x, o_y)

        new_x, new_y  = move_atom(h1_x, h1_y, 'Left', others, self.obstacles)
        if new_x != h1_x:
            successors['LeftH1'] = (new_x, h1_y, h2_x, h2_y, o_x, o_y)

        new_x, new_y = move_atom(h1_x, h1_y, 'Up', others, self.obstacles)
        if new_y != h1_y:
            successors['UpH1'] = (h1_x, new_y, h2_x, h2_y, o_x, o_y)

        new_x, new_y = move_atom(h1_x, h1_y, 'Down', others, self.obstacles)
        if new_y != h1_y:
            successors['DownH1'] = (h1_x, new_y, h2_x, h2_y, o_x, o_y)


        others = [[h1_x, h1_y], [o_x, o_y]]

        new_x, new_y = move_atom(h1_x, h1_y, 'Right', others, self.obstacles)
        if new_x != h1_x:
            successors['RightH2'] = (h1_x, h1_y, new_x, h2_y, o_x, o_y)

        new_x, new_y = move_atom(h1_x, h1_y, 'Left', others, self.obstacles)
        if new_x != h1_x:
            successors['LeftH2'] = (h1_x, h1_y, new_x, h2_y, o_x, o_y)

        new_x, new_y = move_atom(h1_x, h1_y, 'Up', others, self.obstacles)
        if new_y != h1_y:
            successors['UpH2'] = (h1_x, h1_y, h2_x, new_y, o_x, o_y)

        new_x, new_y = move_atom(h1_x, h1_y, 'Down', others, self.obstacles)
        if new_y != h1_y:
            successors['DownH2'] = (h1_x, h1_y, h2_x, new_y, o_x, o_y)


        others = [[h1_x, h1_y], [h2_x, h2_y]]

        new_x, new_y = move_atom(h1_x, h1_y, 'Right', others, self.obstacles)
        if new_x != h1_x:
            successors['RightO'] = (h1_x, h1_y, h2_x, h2_y, new_x, o_y)

        new_x, new_y = move_atom(h1_x, h1_y, 'Left', others, self.obstacles)
        if new_x != h1_x:
            successors['LeftO'] = (h1_x, h1_y, h2_x, h2_y, new_x, o_y)

        new_x, new_y = move_atom(h1_x, h1_y, 'Up', others, self.obstacles)
        if new_y != h1_y:
            successors['UpO'] = (h1_x, h1_y, h2_x, h2_y, o_x, new_y)

        new_x, new_y= move_atom(h1_x, h1_y, 'Down', others, self.obstacles)
        if new_y != h1_y:
            successors['DownO'] = (h1_x, h1_y, h2_x, h2_y, o_x, new_y)


        return successors


    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        h1_x = state[0]
        h1_y = state[1]
        o_x = state[2]
        o_y = state[3]
        h2_x = state[4]
        h2_y = state[5]

        same_row = h1_y == o_y == h2_y
        h1_left_of_o = h1_x + 1 == o_x
        o_left_of_h2 = o_x + 1 == h2_x

        return same_row and h1_left_of_o and o_left_of_h2


if __name__ == '__main__':
    obstacles_list = [[0, 1], [1, 1], [1, 3], [2, 5], [3, 1], [3, 6], [4, 2],
                      [5, 6], [6, 1], [6, 2], [6, 3], [7, 3], [7, 6], [8, 5]]
    h1_pos = [2, 1]
    h2_pos = [2, 6]
    o_pos  = [7, 2]

    initial_state = (h1_pos[0], h1_pos[1],
                     o_pos[0],  o_pos[1],
                     h2_pos[0], h2_pos[1])

    molecule = Molecules(obstacles_list, initial_state)

    print(breadth_first_graph_search(molecule).solution())


