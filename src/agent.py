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
        self.posY = zone.positionY

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

    def find_min_elements_without_negative(self):
        min = 88888888
        min_x = 0
        min_y = 0
        module = 8888888
        for i in range(len(self.agent_map)):
            for j in range(len(self.agent_map)):
                if int(self.agent_map[i][j]) >= 0 and int(self.agent_map[i][j]) <= min:
                    if int(self.agent_map[i][j]) == min:
                        if module <= abs(self.posX - i) + abs(self.posY - j):
                            min = self.agent_map[i][j]
                            min_x = i
                            min_y = j
                            module = abs(self.posX - i) + abs(self.posY - j)
                    else:
                        min = self.agent_map[i][j]
                        min_x = i
                        min_y = j

        return min_x, min_y

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

    def think_model_based(self, maze, iteration):
        iteration += 2
        if maze[self.posX][self.posY] == 1:
            self.agent_map[self.posX][self.posY] = iteration
            return self.suck()
        elif maze[self.posX][self.posY + 1] == 1:
            self.agent_map[self.posX][self.posY + 1] = iteration
            return self.right()
        elif maze[self.posX][self.posY - 1] == 1:
            self.agent_map[self.posX][self.posY - 1] = iteration
            return self.left()
        elif maze[self.posX + 1][self.posY] == 1:
            self.agent_map[self.posX + 1][self.posY] = iteration
            return self.down()
        elif maze[self.posX - 1][self.posY] == 1:
            self.agent_map[self.posX - 1][self.posY] = iteration
            return self.up()
        elif maze[self.posX - 1][self.posY - 1] == 1:
            if maze[self.posX - 1][self.posY] != -1:
                self.agent_map[self.posX - 1][self.posY] = iteration
                return self.up()
            else:
                self.agent_map[self.posX][self.posY - 1] = iteration
                return self.left()
        elif maze[self.posX - 1][self.posY + 1] == 1:
            if maze[self.posX - 1][self.posY] != -1:
                self.agent_map[self.posX - 1][self.posY] = iteration
                return self.up()
            else:
                self.agent_map[self.posX][self.posY + 1] = iteration
                return self.right()
        elif maze[self.posX + 1][self.posY + 1] == 1:
            if maze[self.posX + 1][self.posY] != -1:
                self.agent_map[self.posX + 1][self.posY] = iteration
                return self.down()
            else:
                self.agent_map[self.posX][self.posY + 1] = iteration
                return self.right()
        elif maze[self.posX + 1][self.posY - 1] == 1:
            if maze[self.posX + 1][self.posY] != -1:
                self.agent_map[self.posX + 1][self.posY] = iteration
                return self.down()
            else:
                self.agent_map[self.posX][self.posY - 1] = iteration
                return self.left
        else:
            x, y = self.find_min_elements_without_negative()
            if int(maze[self.posX + 1][self.posY]) != -1 and self.posX < x:
                self.agent_map[self.posX + 1][self.posY] = iteration
                return self.down()
            elif int(maze[self.posX - 1][self.posY]) != -1 and self.posX > x:
                self.agent_map[self.posX - 1][self.posY] = iteration
                return self.up()
            else:
                if int(maze[self.posX][self.posY + 1]) != -1 and self.posY < y:
                    self.agent_map[self.posX][self.posY + 1] = iteration
                    return self.right()
                elif int(maze[self.posX][self.posY - 1]) != -1 and self.posY > y:
                    self.agent_map[self.posX][self.posY - 1] = iteration
                    return self.left()
                else:
                    actions = [self.up(), self.down(), self.left(), self.right()]
                    return actions[int(random.random() * 4)]
