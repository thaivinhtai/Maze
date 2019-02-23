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
            Map[y][x] = "explored"
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
        self.list_line = list()
        self.maze = list()
        self.wall = "*"
        self.path = " "
        self.coin = "o"
        self.bonus = "!"
        self.list_resoueces = ["o", "!"]
        self.list_resources_pos = list()

    # Get the current Maze's status
    def get_maze(self):
        self.list_line = []
        line = ""
        while line != "\n":
            line = stdin.readline()
            self.list_line.append(line)
        self.list_line.remove(self.list_line[len(self.list_line) - 1])
        self.list_line.remove(self.list_line[0])
        return 0

    # convert list_maze to nested list
    def convert_maze(self):
        self.maze = []
        for i in range(len(self.list_line)):
            self.maze.append([])
            for j in range(len(self.list_line[i])):
                self.maze[i].append(self.list_line[i][j])
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


def main():
    ia = Intelligent_Agent()
    ia.greeting()
    maze = Maze()
    maze.get_maze()
    while True:
        maze.convert_maze()
        ia.get_IA_position(maze.maze)
        # step_to_bonus = Breadth_First_Search().run(ia.posy, ia.posx,
        #                                            maze.maze, maze.bonus)
        # step_to_coin = Breadth_First_Search().run(ia.posy, ia.posx,
        #                                           maze.maze, maze.coin)
        # step_to_coin.reverse()
        # step_to_bonus.reverse()
        # len_coin = len(step_to_coin) - 1
        # len_bonus = len(step_to_bonus) - 1
        # if len_bonus > 0 and len_bonus <= 20:
        #     step_to_bonus.remove(step_to_bonus[0])
        #     if len_bonus * 2 <= len_coin:
        #         for i in step_to_bonus:
        #             ia.move(i[0], i[1])
        #             maze.get_maze()
        #         continue
        # if len(step_to_coin) > 0:
        #     step_to_coin.remove(step_to_coin[0])
        #     for i in step_to_coin:
        #         ia.move(i[0], i[1])
        #         maze.get_maze()
        step_to_res = Breadth_First_Search().run(ia.posy, ia.posx,
                                                 maze.maze,
                                                 maze.list_resoueces)
        step_to_res.reverse()
        step_to_res.remove(step_to_res[0])
        for i in step_to_res:
            ia.move(i[0], i[1])
            maze.get_maze()
    return 0


if __name__ == "__main__":
    main()
