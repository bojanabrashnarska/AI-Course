from searching_framework import *

def move_knight(x, y, move_type, other_pieces):
    if move_type == 'K1':
        dx, dy = -1, 2
    elif move_type == 'K2':
        dx, dy = 1, 2
    elif move_type == 'K3':
        dx, dy = 2, 1
    elif move_type == 'K4':
        dx, dy = 2, -1
    elif move_type == 'K5':
        dx, dy = 1, -2
    elif move_type == 'K6':
        dx, dy = -1, -2
    elif move_type == 'K7':
        dx, dy = -2, -1
    elif move_type == 'K8':
        dx, dy = -2, 1


    hx = x + dx
    hy = y + dy

    if hx < 0 or hx > 7:
        return None
    if hy < 0 or hy > 7:
        return None
    if [hx, hy] in other_pieces:
        return None


    return hx, hy


def move_bishop(x, y, move_type, other_pieces):

    og_bx = x
    og_by = y

    if move_type == 'B1':
        dx, dy = -1, 1
    elif move_type == 'B2':
        dx, dy = 1, 1
    elif move_type == 'B3':
        dx, dy = -1, -1
    elif move_type == 'B4':
        dx, dy = 1, -1


    bx = x + dx
    by = y + dy

    if bx < 0 or bx > 7:
        return None
    if by < 0 or by > 7:
        return None
    if [bx, by] in other_pieces:
        return None

    return bx, by


class Chess(Problem):

    def __init__(self, state):
        super().__init__(state)

    def successor(self, state):

        kx = state[0]
        ky = state[1]
        bx = state[2]
        by = state[3]

        remaining_stars = state[4]

        successors = {}

        for move in ['K1', 'K2', 'K3', 'K4', 'K5', 'K6', 'K7', 'K8']:
            new_pos = move_knight(kx, ky, move, [[bx, by]])
            if new_pos is not None:
                new_kx, new_ky = new_pos
                new_stars = tuple(s for s in remaining_stars if s != (new_kx, new_ky))
                successors[move] = (new_kx, new_ky, bx, by, new_stars)


        for move in ['B1', 'B2', 'B3', 'B4']:
            new_pos = move_bishop(bx, by, move, [[kx, ky]])
            if new_pos is not None:
                new_bx, new_by = new_pos
                new_stars = tuple(s for s in remaining_stars if s!=(new_bx, new_by))
                successors[move] = (kx, ky, new_bx, new_by, new_stars)

        return successors

    def goal_test(self, state):
        return len(state[4]) == 0

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

if __name__ == '__main__':
    knight = [2, 5]
    bishop = [5, 2]
    stars_pos = ((1, 1), (4, 3), (6,6))

    stars = (Chess((knight[0], knight[1], bishop[0], bishop[1], stars_pos)))

    result = breadth_first_graph_search(stars)
    print(result.solution())

