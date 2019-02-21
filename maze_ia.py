#!/usr/bin/env python3
from sys import stdin, stdout, stderr


class Queue:
    def __init__(self):
        self.queue = list()

    def enqueue(self, elements):
        if elements not in self.queue:
            self.queue.insert(0, elements)
            return True
        return False

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return "Queue Empty!"

    def size(self):
        return len(self.queue)

    def print_queue(self):
        return self.queue


class Resources:
    def __init__(self):
        self.coin = "o"
        self.bonus = "!"
        self.wall = "*"


class Maze:
    def __init__(self):
        self.maze = list()

    def get_maze(self):
        line = ""
        while line != "\n":
            line = stdin.readln()
            self.maze.append(line)
        self.maze.remove(self.maze[0])


class Intelligent_Agent:
    def __init__(self, name="Tai"):
        self.name = name
        self.letter = "A"
        self.posx = -2
        self.posy = -2

    def greeting():
        stdin.readln()
        stdin.readln()
        stdout.write("I AM {name}\n\n".format(name=self.name))
        letter = stdin.readln()
        stdin.readln()
        self.letter = letter(len[letter] - 1)
        stdout.write("OK\n\n")

    def get_IA_position(self, maze):
        for i in range(len(maze) - 1):
            for j in range(len(maze[i]) - 1):
                if maze[i][j] == self.letter:
                    self.posx = i
                    self.posy = j
                    break

    def get_resources_position(self, maze):
        for i in range(len(maze) - 1):
            for j in range(len(maze[i]) - 1):
                if maze[i][j] == Resources.coin
                or maze[i][j] == Resources.bonus:
                    temp_pos = []
                    temp_pos.append(i)
                    temp_pos.append(j)
                    if temp_pos not in self.resources:
                        self.resources.append(temp_pos)

    def move_left():
        stdin.write("MOVE LEFT\n\n")

    def move_right():
        stdin.write("MOVE RIGHT\n\n")

    def move_up():
        stdin.write("MOVE UP\n\n")

    def move_down():
        stdin.write("MOVE DOWN\n\n")


if __name__ == "main":
    play = Intelligent_Agent
    play.greeting()
    play.get_maze()
