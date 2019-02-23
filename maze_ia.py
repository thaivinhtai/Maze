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
        stderr.write("BFS")
        direction = [[y - 1, x], [y + 1, x], [y, x - 1], [y, x + 1]]
        open = Queue([(y, x)])
        while len(open.queue) > 0:
            node = open.dequeue()
            y = node[0]
            x = node[1]

            if Map[y][x] == res:
                return get_path_from_nodes(node)
            if Map[y][x] != Maze().path:
                continue
            Map[y][x] = "Visited"
            for i in direction:
                open.append((i[0], i[1], node))
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
        line = ""
        while line != "\n":
            line = stdin.readline()
            self.maze.append(line)
            #stderr.write("this: " + line)
        self.maze.remove(self.maze[0])
        #stderr.write(self.maze[0])
        return 0


class Intelligent_Agent:
    def __init__(self, name="Tai's IA"):
        self.name = name
        self.letter = "A"
        self.posx = -2
        self.posy = -2

    # Introduce IA to VM
    def greeting(self):
        a = stdin.readline()
        b = stdin.readline()
        stderr.write(a)
        stderr.write(b)
        stdout.write("I AM {IA}\n\n".format(IA=self.name))
        letter = stdin.readline()
        stdin.readline()
        self.letter = letter[len(letter) - 1]
        stdout.write("OK\n\n")
        return 0

    # Figure out the position of IA
    def get_IA_position(self, maze):
        for y in range(len(maze)):
            for x in range(len(maze[i])):
                if maze[y][x] == self.letter:
                    self.posx = x
                    self.posy = y
                    return (y, x)

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
    #while stdin.readline() != "/n":
    maze = Maze()
    maze.get_maze()
    stderr.write(maze.maze[0])
    step_to_bonus = Breadth_First_Search().run(ia.posy, ia.posx,
                                               maze.maze, maze.bonus)
    step_to_coin = Breadth_First_Search().run(ia.posy, ia.posx,
                                              maze.maze, maze.coin)
    #stderr.write(step_to_coin[0])
    # stderr.write(step_to_bonus)
    # if (len(step_to_bonus) <= 20) and
    #    (len(step_to_bonus) < (2 * len(step_to_coin))) and
    #    (len(step_to_bonus) > 0):
    #     for i in step_to_bonus:
    #         IA.move(i[0], i[1])
    # elif len(step_to_coin) > 0:
    #     for i in step_to_coin:
    #         IA.move(i[0], i[1])
    for i in step_to_coin:
        ia.move(i[0], i[1])
    return 0


main()
