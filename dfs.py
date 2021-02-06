from helpers import get_path, offsets, is_legal_pos, read_maze
from stack import Stack

def dfs(maze,start,goal):
    stack = Stack()
    stack.push(start)
    predecessors  = {start:None}
    while not stack.is_empty():
        current_cell = stack.pop()
        if current_cell == goal:
            return get_path(predecessors,start,goal)
        for direction in ['up','right','down', 'left']:
            row_offset, col_offset = offsets[direction]
            neighbor = (current_cell[0]+row_offset, current_cell[1] +col_offset)
            print(predecessors)
            if is_legal_pos(maze,neighbor) and  neighbor not in predecessors:
                stack.push(neighbor)
                predecessors[neighbor] = current_cell
    return None



if __name__ == "__main__":
    maze  = [[i+1] * 3 for i in range(1,4) ]
    print(maze)
    start = (0,0)
    goal = (2,2)
    #result = dfs(maze, start, goal)
    predecessors = {(0, 0): None, (1, 0): (0, 0), (0, 1): (0, 0), (1, 1): (0, 1), (0, 2): (0, 1), (1, 2): (0, 2), (2, 2): (1, 2)}
    predecessors[(0,1)]
    print(predecessors[(0,1)])