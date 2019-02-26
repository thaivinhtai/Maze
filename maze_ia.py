#!/usr/bin/env python3
from sys import stdin, stdout, stderr


class Queue:
    """
    Define Queue data struture
    """

    def __init__(self, elements):
        self.queue = elements

    def enqueue(self, elements):
        """
        Add element to first posotion of queue
        """
        if elements not in self.queue:
            self.queue.insert(0, elements)
            return True
        return False

    def dequeue(self):
        """
        Take the first element out of queue
        """
        if len(self.queue) > 0:
            return self.queue.pop()
        return None

    def size(self):
        """
        Return the lenght of queue
        """
        return len(self.queue)

    def print_queue(self):
        """
        Print the queue
        """
        return self.queue

    def is_empty(self):
        """
        Check the queue is empty or not
        """
        return len(self.queue) == 0

    def peek(self):
        """
        Return fisrt element of the queue
        """
        if len(self.queue) > 0:
            return self.queue[0]
        return None


class Breadth_First_Search:
    """
    Use BFS algorithm to find the way to resources
    """

    def run(self, y, x, Map, resources):
        """
        Run the BFS algorithm
        """
        open = Queue([(y, x, None)])
        root_node = Map[y][x]
        while len(open.queue) > 0:
            node = open.dequeue()
            y = node[0]
            x = node[1]
            if Map[y][x] in resources:
                return self.get_path_from_nodes(node)
            if Map[y][x] != Maze().path and Map[y][x] != root_node:
                continue
            Map[y][x] = "explored"
            direction = [[y - 1, x], [y + 1, x], [y, x - 1], [y, x + 1]]
            for i in direction:
                open.enqueue((i[0], i[1], node))
        return []

    def get_path_from_nodes(self, node):
        """
        Tracking back
        """
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

    def get_maze(self):
        """
        Get the current Maze's status
        """
        self.list_line = []
        line = ""
        while line != "\n":
            line = stdin.readline()
            self.list_line.append(line)
        self.list_line.remove(self.list_line[len(self.list_line) - 1])
        self.list_line.remove(self.list_line[0])
        return 0

    def convert_maze(self):
        """
        Convert list_maze to nested list
        """
        self.maze = [[line[i]
                      for i in range(len(line))] for line in self.list_line]
        return 0


class Intelligent_Agent:
    def __init__(self, name="Tai's IA"):
        self.name = name
        self.letter = "A"
        self.posx = -2
        self.posy = -2

    def greeting(self):
        """
        Introduce IA to VM
        """
        while True:
            stdin.readline()
            if stdin.readline() == "\n":
                break
        stdout.write("I AM {IA}\n\n".format(IA=self.name))
        letter = stdin.readline()
        stdin.readline()
        self.letter = letter[len(letter) - 2]
        stdout.write("OK\n\n")
        return 0

    def get_IA_position(self, maze):
        """
        Figure out the position of IA
        """
        for y in range(len(maze)):
            for x in range(len(maze[y])):
                if maze[y][x] == self.letter:
                    self.posx = x
                    self.posy = y
                    break
        return 0

    def move(self, y, x):
        """
        Generate move command for IA
        """
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
