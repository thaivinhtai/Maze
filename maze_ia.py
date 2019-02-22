#!/usr/bin/env python3
from sys import stdin, stdout, stderr


# Define Queue data str
class Queue:
    def __init__(self):
        self.queue = list()

    # Add element to first posotion of queue
    def enqueue(self, elements):
        if elements not in self.queue:
            self.queue.insert(0, elements)
            return True
        return False

    # Take the last element out of queue
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return "Queue Empty!"

    # Return the lenght of queue
    def size(self):
        return len(self.queue)

    # Print the queue
    def print_queue(self):
        return self.queue


class Maze:
    def __init__(self):
        self.maze = list()
        self.wall = "*"
        self.list_resoueces = ["o", "!"]
        self.list_resources_pos = list()

    # Get the current Maze's status
    def get_maze(self):
        line = ""
        while line != "\n":
            line = stdin.readln()
            self.maze.append(line)
        self.maze.remove(self.maze[0])

    # Get list of current resources position
    def get_resources_pos():
        temp_index = -1
        for y in range(len(self.maze)):
            for x in range(len(self.maze[i])):
                if self.maze[i][j] in self.list_resources:
                    temp_index = temp_index + 1
                    self.list_resources_pos.append([])
                    if self.maze[i][j] == "o":
                        self.list_resoueces_pos[temp_index].append("o")
                    elif self.maze[i][j] == "!":
                        self.list_resoueces_pos[temp_index].appen("!")
                    self.list_resoueces_pos[temp_index].append(y)
                    self.list_resoueces_pos[temp_index].append(x)


class Intelligent_Agent:
    def __init__(self, name="Tai's IA"):
        self.name = name
        self.letter = "A"
        self.posx = -2
        self.posy = -2

    # Introduce IA to VM
    def greeting():
        line = ""
        while line != "\n":
            line = stdin.readln()
        stdout.write("I AM {name}\n\n".format(name=self.name))
        letter = stdin.readln()
        stdin.readln()
        self.letter = letter(len[letter] - 1)
        stdout.write("OK\n\n")

    # Figure out the position of IA
    def get_IA_position(self, maze):
        for y in range(len(maze)):
            for x in range(len(maze[i])):
                if maze[y][x] == self.letter:
                    self.posx = x
                    self.posy = y
                    break

    def move_left():
        stdin.write("MOVE LEFT\n\n")
        move = [0, -1]
        return move

    def move_right():
        stdin.write("MOVE RIGHT\n\n")
        move = [0, 1]
        return move

    def move_up():
        stdin.write("MOVE UP\n\n")
        move = [-1, 0]
        return move

    def move_down():
        stdin.write("MOVE DOWN\n\n")
        move = [1, 0]
        return move


if __name__ == "main":
    ia = Intelligent_Agent
    ia.greeting()
    maze = Maze
    maze.get_maze()
