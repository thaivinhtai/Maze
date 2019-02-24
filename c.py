#!/usr/bin/env python3
from sys import stdin, stdout, stderr


# Define Queue data str
class Queue:
    def __init__(self, elements):
        self.queue = elements

    # Add element to first posotion of queue
    def enqueue(self, elements):
        if elements not in self.queue:
            self.queue.insert(0, elements)
            return True
        return False

    # Take the first element out of queue
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return None

    # Return the lenght of queue
    def size(self):
        return len(self.queue)

    # Print the queue
    def print_queue(self):
        return self.queue

    # Check the queue is empty or not
    def is_empty(self):
        return len(self.queue) == 0

    # Return fisrt element of the queue
    def peek(self):
        if len(self.queue) > 0:
            return self.queue[0]
        return None


class Breadth_First_Search:
    def run(self, y, x, Map, res):
        open = Queue([(y, x, None)])
        root_node = Map[y][x]
        while len(open.queue) > 0:
            node = open.dequeue()
            y = node[0]
            x = node[1]
            if Map[y][x] in res:
                return self.get_path_from_nodes(node)
            if Map[y][x] != Maze().path and Map[y][x] != root_node:
                continue
            Map[y][x] = "visited"
            direction = [[y - 1, x], [y + 1, x], [y, x - 1], [y, x + 1]]
            for i in direction:
                open.enqueue((i[0], i[1], node))
        return []

    def get_path_from_nodes(self, node):
        path = []
        while node is not None:
            path.append((node[0], node[1]))
            node = node[2]
        return path


class Maze:
    def __init__(self):
        self.maze = list()
        self.wall = "*"
        self.path = " "
        self.coin = "o"
        self.bonus = "!"
        self.list_resoueces = ["o", "!"]
        self.list_resources_pos = list()

    # Get the current Maze's status
    def get_maze(self):
        self.maze = []
        line = ""
        temp_maze = []
        while line != "\n":
            line = stdin.readline()
            temp_maze.append(line)
        temp_maze.remove(temp_maze[len(temp_maze) - 1])
        temp_maze.remove(temp_maze[0])
        for i in range(len(temp_maze)):
            self.maze.append([])
            for j in range(len(temp_maze[i])):
                self.maze[i].append(temp_maze[i][j])
        return 0


class Intelligent_Agent:
    def __init__(self, name="Tai's IA"):
        self.name = name
        self.letter = "A"
        self.posx = -2
        self.posy = -2

    # Introduce IA to VM
    def greeting(self):
        stdin.readline()
        stdin.readline()
        stdout.write("I AM {IA}\n\n".format(IA=self.name))
        letter = stdin.readline()
        stdin.readline()
        self.letter = letter[len(letter) - 2]
        stdout.write("OK\n\n")
        return 0

    # Figure out the position of IA
    def get_IA_position(self, maze):
        for y in range(len(maze)):
            for x in range(len(maze[y])):
                if maze[y][x] == self.letter:
                    self.posx = x
                    self.posy = y
                    break
        return 0

    def move(self, y, x):
        if y - self.posy == 0 and x - self.posx == 1:
            stdout.write("MOVE RIGHT\n\n")
        elif y - self.posy == 0 and x - self.posx == -1:
            stdout.write("MOVE LEFT\n\n")
        elif y - self.posy == 1 and x - self.posx == 0:
            stdout.write("MOVE DOWN\n\n")
        elif y - self.posy == -1 and x - self.posx == 0:
            stdout.write("MOVE UP\n\n")
        self.posy = y
        self.posx = x
        return 0

    def will_impact_enemy(self, pos, map):
        y = pos[0]
        x = pos[1]
        if map[y][x] not in [Maze().path, Maze().coin,
                             Maze().bonus, 'visited']:
            return True
        return False


def main():
    ia = Intelligent_Agent()
    ia.greeting()
    maze = Maze()
    maze.get_maze()
    while True:
        ia.get_IA_position(maze.maze)
        step_to_res = Breadth_First_Search().run(ia.posy, ia.posx,
                                                 maze.maze,
                                                 maze.list_resoueces)
        step_to_res.reverse()
        # step_to_res.remove(step_to_res[0])
        for i in step_to_res:
            # stderr.write("this: \n")
            # stderr.write(str(maze.maze))
            if ia.will_impact_enemy(i, maze.maze):
                continue
            ia.move(i[0], i[1])
            maze.get_maze()
    return 0


if __name__ == "__main__":
    main()
