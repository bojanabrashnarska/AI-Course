from searching_framework import *

UP = "up"
DOWN = "down"

def move_obstacle(x, y, direction, max_y):
    if direction == UP:
        if y == max_y - 1:
            return x, y-1, DOWN
        else:
            return x, y+1, UP
    else:
        if y == 0:
            return x, y+1, UP
        else:
            return x, y-1, DOWN


class Explorer(Problem):

    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)
        self.grid_size = [8, 6]


    def successor(self, state):

        man_x, man_y = state[0], state[1]
        obs1_x, obs1_y, obs1_dir = state[2], state[3], state[4]
        obs2_x, obs2_y, obs2_dir = state[5], state[6], state[7]

        max_x = self.grid_size[0]
        max_y = self.grid_size[1]

        obs1_x, obs1_y, obs1_dir = move_obstacle(obs1_x, obs1_y, obs1_dir, max_y)
        obs2_x, obs2_y, obs2_dir = move_obstacle(obs2_x, obs2_y, obs2_dir, max_y)

        obstacles = [[obs1_x, obs1_y], [obs2_x, obs2_y]]

        successors = {}

        if man_x < max_x and [man_x + 1, man_y] not in obstacles:
            successors['Right'] = (man_x + 1, man_y, obs1_x, obs1_y, obs1_dir, obs2_x, obs2_y, obs2_dir)

        if man_x > 0 and [man_x - 1, man_y] not in obstacles:
            successors['Left'] = (man_x - 1, man_y, obs1_x, obs1_y, obs1_dir, obs2_x, obs2_y, obs2_dir)

        if man_y < max_y and [man_x, man_y + 1] not in obstacles:
            successors['Up'] = (man_x, man_y + 1, obs1_x, obs1_y, obs1_dir, obs2_x, obs2_y, obs2_dir)

        if man_y > 0 and [man_x, man_y - 1] not in obstacles:
            successors['Down'] = (man_x, man_y - 1, obs1_x, obs1_y, obs1_dir, obs2_x, obs2_y, obs2_dir)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        position = (state[0], state[1])
        return position == self.goal



if __name__ == '__main__':

    goal_state = (7,4)
    initial_state = (0,2)

    obstacle1 = (2, 5, DOWN)
    obstacle2 = (5, 0, UP)

    explorer = Explorer((initial_state[0], initial_state[1],
                         obstacle1[0], obstacle1[1], obstacle1[2],
                         obstacle2[0], obstacle2[1], obstacle2[2]), goal_state)

    print(breadth_first_graph_search(explorer).solution())









