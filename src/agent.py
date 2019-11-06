from src.environment import Environment
import random


class Agent:
    bump = False
    dirty = False
    msg = ''
    agent_map = []
    last_action = None
    posX = 0
    posY = 0

    def __init__(self, zone):
        self.msg = 'Hello World, i\'m Vacuum'
        self.agent_map = [[zone.maze[col][row] for col in range(zone.size)] for row in range(zone.size)]
        self.posX = zone.positionX
        self.postY = zone.positionY

    def up(self):
        last_action = "UP"
        return "UP"

    def down(self):
        last_action = "DOWN"
        return "DOWN"

    def left(self):
        last_action = "LEFT"
        return "LEFT"

    def right(self):
        last_action = "RIGHT"
        return "RIGHT"

    def suck(self):
        last_action = "SUCK"
        return "SUCK"

    def idle(self):
        last_action = "IDLE"
        return "IDLE"

    def prespective(self, env):
        self.bump = env.bump
        self.dirty = env.dirt_amout(self.posX, self.posY)
        self.posX, self.posY = env.positionX, env.positionY

    def think_random(self, maze):
        if maze[self.posX][self.posY] == 1:
            return self.suck()
        actions = [self.up(), self.down(), self.left(), self.right()]
        return actions[int(random.random() * 4)]

    def think_reflex(self, maze):
        if maze[self.posX][self.posY] == 1:
            return self.suck()
        elif maze[self.posX][self.posY + 1] == 1:
            return self.right()
        elif maze[self.posX][self.posY - 1] == 1:
            return self.left()
        elif maze[self.posX + 1][self.posY] == 1:
            return self.down()
        elif maze[self.posX - 1][self.posY] == 1:
            return self.up()
        elif maze[self.posX - 1][self.posY - 1] == 1:
            if maze[self.posX - 1][self.posY] != -1:
                return self.up()
            else:
                return self.left()
        elif maze[self.posX - 1][self.posY + 1] == 1:
            if maze[self.posX - 1][self.posY] != -1:
                return self.up()
            else:
                return self.right()
        elif maze[self.posX + 1][self.posY + 1] == 1:
            if maze[self.posX + 1][self.posY] != -1:
                return self.down()
            else:
                return self.right()
        elif maze[self.posX + 1][self.posY - 1] == 1:
            if maze[self.posX + 1][self.posY] != -1:
                return self.down()
            else:
                return self.left
        else:
            actions = [self.up(), self.down(), self.left(), self.right(), self.idle()]
            return actions[int(random.random() * 5)]

    def think_model_based(self, maze):
        if maze[self.posX][self.posY] == 1:
            return self.suck()
        actions = [self.up(), self.down(), self.left(), self.right()]
        return actions[int(random.random() * 4)]