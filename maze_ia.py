#!/usr/bin/env python3
from sys import stdin, stdout, stderr


WALL = "*"
BLANK = " "
COIN = "o"
BONUS = "!"


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


class Intelligent_Agent:
    def __init__(self, name="Tai"):
        self.name = name
        self.letter = "A"
        self.map = list()
        self.posx = 2
        self.posy = 2
        self.resouces = list()

    def greeting():
        stdin.readln()
        stdin.readln()
        stdout.write("I AM {name}\n\n".format(name=self.name))
        letter = stdin.readln()
        stdin.readln()
        self.letter = letter(len[letter] - 1)
        stdout.write("OK\n\n")

    def get_maze(self):
        line = ""
        while line != "\n":
            line = stdin.readln()
            self.map.append(line)
        self.map.remove(self.map[0])

    def get_IA_position(self):
        for i in range(len(self.map) - 1):
            for j in range(len(self.map[i]) - 1):
                if self.map[i][j] == self.letter:
                    self.posx = i
                    self.posy = j
                    break

    def get_resources_position(self):
        for i in range(len(self.map) - 1):
            for j in range(len(self.map[i]) - 1):
                if self.map[i][j] == COIN
                or self.map[i][j] == BONUS:


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
