#!/usr/bin/env python3
from sys import stdin, stdout, stderr


class Intelligent_Agent:
    def __init__(self, name="Tai", map=[]):
        self.name = name
        self.map = map

    def greeting():
        stdin.readln()
        stdin.readln()
        stdout.write("I AM {name}\n\n".format(name=self.name))
        stdin.readln()
        stdout.write("OK\n\n")

    def get_maze(self):
        self.map = map
        line = ""
        while line != "\n":
            line = stdin.readln()
            self.map.append(line)
        self.map.remove(self.map[0])
        

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
