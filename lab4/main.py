
class Actions:
    def __init__(self):
        self.hit = False
        self.shine = False
        self.scream = False
        self.enemy = False


class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Sensors:
    def __init__(self):
        self.stink = False
        self.wind = False


class Cave:
    def __init__(self):
        # viy = 1
        # princess = 2
        # gold = 3
        # else = 4
        self.field = [
            [4, 4, 2, 4],
            [4, 4, 2, 4],
            [3, 1, 4, 4],
            [4, 2, 4, 3]
        ]
        self.VIY = True

    def print_cave(self, homa_position):
        for i in range(len(self.field)):
            for j in range(len(self.field[0])):
                if (i, j) == homa_position:
                    print('%10s' % 'homa', sep=' ', end=' ')
                else:
                    if self.field[i][j] == 1:
                        print('%10s' % 'viy', sep=' ', end=' ')
                    if self.field[i][j] == 2:
                        print('%10s' % 'princess', sep=' ', end=' ')
                    if self.field[i][j] == 3:
                        print('%10s' % 'gold', sep=' ', end=' ')
                    if self.field[i][j] == 4:
                        print('%10s' % 'empty', sep=' ', end=' ')
            print()

    def get_info(self, x, y):
        s = Sensors()

        pos1x = x + 1 if x != 3 else -1
        pos1y = y
        pos2x = x - 1 if x != 0 else -1
        pos2y = y
        pos3x = x
        pos3y = y + 1 if y != 3 else -1
        pos4x = x
        pos4y = y - 1 if y != 0 else -1
        if (((pos1x != -1) and (self.field[pos1x][pos1y] == 1)) or
                ((pos2x != -1) and (self.field[pos2x][pos2y] == 1)) or
                ((pos3y != -1) and (self.field[pos3x][pos3y] == 1)) or
                ((pos4y != -1) and (self.field[pos4x][pos4y] == 1))
            ):
            s.stink = True
        if (((pos1x != -1) and (self.field[pos1x][pos1y] == 2)) or
                ((pos2x != -1) and (self.field[pos2x][pos2y] == 2)) or
                ((pos3y != -1) and (self.field[pos3x][pos3y] == 2)) or
                ((pos4y != -1) and (self.field[pos4x][pos4y] == 2))
            ):
            s.wind = True

        return s

    def get_result(self, x, y):
        s = Actions()
        if (not self.VIY):
            s.scream = True
        if (x > 3) or (x < 0) or (y > 3) or (y < 0):
            s.hit = True
            return s
        if ((self.field[x][y] == 1) and self.VIY) or (self.field[x][y] == 2):
            s.enemy = True
            return s
        if self.field[x][y] == 3:
            s.shine = True
            self.field[x][y] = 4
            return s
        return s

    def throw_arm(self, x, y, turn):
        if ((turn == 'l') and (x != 3)):
            for i in range(x + 1, 4):
                if self.field[i][y] == 1:
                    self.VIY = False
        if ((turn == 'r') and (x != 0)):
            for i in range(x - 1, -1, -1):
                if self.field[i][y] == 1:
                    self.VIY = False
        if ((turn == 'u') and (y != 3)):
            for i in range(y + 1, 4):
                if self.field[x][i] == 1:
                    self.VIY = False
        if ((turn == 'd') and (x != 0)):
            for i in range(y - 1, -1, -1):
                if self.field[x][i] == 1:
                    self.VIY = False


class Agent:
    def __init__(self, cave):

        self.VIY = False
        self.arm = False

        self.cave = cave

        self.score = 0
        self.Win = False
        self.Loose = False
        self.predictions = [
            [0, -1, -1, -1],
            [-1, -1, -1, -1],
            [-1, -1, -1, -1],
            [-1, -1, -1, -1]
        ]

        self.pCount = 3
        self.gCount = 2
        self.return_count = 0

        self.current = Coords(0, 0)
        self.visited = [Coords(0, 0)]

    def print_cave(self):
        self.cave.print_cave((self.current.x, self.current.y))

    def set_predict_by_sensors(self, sensor):
        pos1x = self.current.x + 1 if self.current.x != 3 else -1
        pos1y = self.current.y
        pos2x = self.current.x - 1 if self.current.x != 0 else -1
        pos2y = self.current.y
        pos3x = self.current.x
        pos3y = self.current.y + 1 if self.current.y != 3 else -1
        pos4x = self.current.x
        pos4y = self.current.y - 1 if self.current.y != 0 else -1

        if (not sensor.stink) and (not sensor.wind):
            if pos1x != -1:
                self.predictions[pos1x][pos1y] = 0
            if pos2x != -1:
                self.predictions[pos2x][pos2y] = 0
            if pos3y != -1:
                self.predictions[pos3x][pos3y] = 0
            if pos4y != -1:
                self.predictions[pos4x][pos4y] = 0

        if sensor.wind:
            if (pos1x != -1) and (self.predictions[pos1x][pos1y] not in [0, 1, 2, 3, 5]):
                if self.predictions[pos1x][pos1y] == -1:
                    self.predictions[pos1x][pos1y] = 1
                elif self.predictions[pos1x][pos1y] == 2:
                    self.predictions[pos1x][pos1y] = 3
            if (pos2x != -1) and (self.predictions[pos2x][pos2y] not in [0, 1, 2, 3, 5]):
                if self.predictions[pos2x][pos2y] == -1:
                    self.predictions[pos2x][pos2y] = 1
                elif self.predictions[pos2x][pos2y] == 2:
                    self.predictions[pos2x][pos2y] = 3
            if (pos3y != -1) and (self.predictions[pos3x][pos3y] not in [0, 1, 2, 3, 5]):
                if self.predictions[pos3x][pos3y] == -1:
                    self.predictions[pos3x][pos3y] = 1
                elif self.predictions[pos3x][pos2y] == 2:
                    self.predictions[pos3x][pos2y] = 3
            if (pos4y != -1) and (self.predictions[pos4x][pos4y] not in [0, 1, 2, 3, 5]):
                if self.predictions[pos4x][pos4y] == -1:
                    self.predictions[pos4x][pos4y] = 1
                elif self.predictions[pos4x][pos4y] == 2:
                    self.predictions[pos4x][pos4y] = 3
        else:
            if (pos1x != -1) and (self.predictions[pos1x][pos1y] in [1, 3]):
                if self.predictions[pos1x][pos1y] == 3:
                    self.predictions[pos1x][pos1y] = 2
                elif self.predictions[pos1x][pos1y] == 1:
                    self.predictions[pos1x][pos1y] = -1
            if (pos2x != -1) and (self.predictions[pos2x][pos2y] in [1, 3]):
                if self.predictions[pos2x][pos2y] == 3:
                    self.predictions[pos2x][pos2y] = 2
                elif self.predictions[pos2x][pos2y] == 1:
                    self.predictions[pos2x][pos2y] = -1
            if (pos3y != -1) and (self.predictions[pos3x][pos3y] in [1, 3]):
                if self.predictions[pos3x][pos3y] == 3:
                    self.predictions[pos3x][pos3y] = 2
                elif self.predictions[pos3x][pos3y] == 1:
                    self.predictions[pos3x][pos3y] = -1
            if (pos4y != -1) and (self.predictions[pos4x][pos4y] in [1, 3]):
                if self.predictions[pos4x][pos4y] == 3:
                    self.predictions[pos4x][pos4y] = 2
                elif self.predictions[pos4x][pos4y] == 1:
                    self.predictions[pos4x][pos4y] = -1

        if sensor.stink and self.VIY:
            if (pos1x != -1) and (self.predictions[pos1x][pos1y] not in [0, 2, 3, 4]):
                if self.predictions[pos1x][pos1y] == -1:
                    self.predictions[pos1x][pos1y] = 2
                elif self.predictions[pos1x][pos1y] == 1:
                    self.predictions[pos1x][pos1y] = 3
            if (pos2x != -1) and (self.predictions[pos2x][pos2y] not in [0, 2, 3, 4]):
                if self.predictions[pos2x][pos2y] == -1:
                    self.predictions[pos2x][pos2y] = 2
                elif self.predictions[pos2x][pos2y] == 1:
                    self.predictions[pos2x][pos2y] = 3
            if (pos3y != -1) and (self.predictions[pos3x][pos3y] not in [0, 2, 3, 4]):
                if self.predictions[pos3x][pos3y] == -1:
                    self.predictions[pos3x][pos3y] = 2
                elif self.predictions[pos3x][pos2y] == 1:
                    self.predictions[pos3x][pos2y] = 3
            if (pos4y != -1) and (self.predictions[pos4x][pos4y] not in [0, 2, 3, 4]):
                if self.predictions[pos4x][pos4y] == -1:
                    self.predictions[pos4x][pos4y] = 2
                elif self.predictions[pos4x][pos4y] == 1:
                    self.predictions[pos4x][pos4y] = 3
        else:
            if (pos1x != -1) and (self.predictions[pos1x][pos1y] in [2, 3]):
                if self.predictions[pos1x][pos1y] == 3:
                    self.predictions[pos1x][pos1y] = 1
                elif self.predictions[pos1x][pos1y] == 2:
                    self.predictions[pos1x][pos1y] = -1
            if (pos2x != -1) and (self.predictions[pos2x][pos2y] in [2, 3]):
                if self.predictions[pos2x][pos2y] == 3:
                    self.predictions[pos2x][pos2y] = 1
                elif self.predictions[pos2x][pos2y] == 2:
                    self.predictions[pos2x][pos2y] = -1
            if (pos3y != -1) and (self.predictions[pos3x][pos3y] in [2, 3]):
                if self.predictions[pos3x][pos3y] == 3:
                    self.predictions[pos3x][pos3y] = 1
                elif self.predictions[pos3x][pos3y] == 2:
                    self.predictions[pos3x][pos3y] = -1
            if (pos4y != -1) and (self.predictions[pos4x][pos4y] in [2, 3]):
                if self.predictions[pos4x][pos4y] == 3:
                    self.predictions[pos4x][pos4y] = 1
                elif self.predictions[pos4x][pos4y] == 2:
                    self.predictions[pos4x][pos4y] = -1

    def make_move(self):

        def check(arr, pos_x, pos_y):
            counter = 0
            for a in arr:
                if (a.x == pos_x) and (a.y == pos_y):
                    counter += 1
            return counter

        def find_index(arr, pos_x, pos_y):
            for a in arr:
                if (a.x == pos_x) and (a.y == pos_y):
                    return arr.index(a)
            return -1

        self.predictions[self.current.x][self.current.y] = 0

        pos1x = self.current.x + 1 if self.current.x != 3 else -1
        pos1y = self.current.y
        pos2x = self.current.x - 1 if self.current.x != 0 else -1
        pos2y = self.current.y
        pos3x = self.current.x
        pos3y = self.current.y + 1 if self.current.y != 3 else -1
        pos4x = self.current.x
        pos4y = self.current.y - 1 if self.current.y != 0 else -1

        not_visited = []

        if (pos1x != -1) and check(self.visited, pos1x, pos1y) == 0:
            not_visited.append(Coords(pos1x, pos1y))
        if (pos2x != -1) and check(self.visited, pos2x, pos2y) == 0:
            not_visited.append(Coords(pos2x, pos2y))
        if (pos3y != -1) and check(self.visited, pos3x, pos3y) == 0:
            not_visited.append(Coords(pos3x, pos3y))
        if (pos4y != -1) and check(self.visited, pos4x, pos4y) == 0:
            not_visited.append(Coords(pos4x, pos4y))

        exist_safe = [v for v in not_visited if (self.predictions[v.x][v.y] == 0)]
        exit_unknown = [v for v in not_visited if (self.predictions[v.x][v.y] == -1)]

        if len(exist_safe) > 0:
            self.return_count = 0
            c = Coords(exist_safe[0].x, exist_safe[0].y)
            self.current.x = c.x
            self.current.y = c.y
            self.score -= 1
            self.visited.append(c)
        elif (self.return_count <= 4 and (check(self.visited, self.current.x, self.current.y) > 0)):
            id_ = find_index(self.visited, self.current.x, self.current.y)
            self.return_count += 1
            c = Coords(self.visited[id_].x, self.visited[id_].y)
            self.current.x = c.x
            self.current.y = c.y
            self.score -= 1
        elif self.arm:
            for i in range(4):
                for j in range(4):
                    if (self.predictions[i][j] == 3) and self.arm:
                        pos1x = i + 1 if i != 3 else -1
                        pos1y = j
                        pos2x = i - 1 if i != 0 else -1
                        pos2y = j
                        pos3x = i
                        pos3y = j + 1 if j != 3 else -1
                        pos4x = i
                        pos4y = j - 1 if j != 3 else -1

                        if (pos1x != -1) and (self.predictions[pos1x][pos1y] == 0):
                            self.score -= 100
                            self.score -= abs(self.current.x - pos1x)
                            self.score -= abs(self.current.y - pos1y)

                            self.current.x = pos1x
                            self.current.y = pos1y

                            self.cave.throw_arm(self.current.x, self.current.y, 'r')
                        elif (pos2x != -1) and (self.predictions[pos2x][pos2y] == 0):
                            self.score -= 100
                            self.score -= abs(self.current.x - pos2x)
                            self.score -= abs(self.current.y - pos2y)

                            self.current.x = pos2x
                            self.current.y = pos2y

                            self.cave.throw_arm(self.current.x, self.current.y, 'r')
                        elif (pos3y != -1) and (self.predictions[pos3x][pos3y] == 0):
                            self.score -= 100
                            self.score -= abs(self.current.x - pos3x)
                            self.score -= abs(self.current.y - pos3y)

                            self.current.x = pos3x
                            self.current.y = pos3y

                            self.cave.throw_arm(self.current.x, self.current.y, 'r')
                        elif (pos4y != -1) and (self.predictions[pos4x][pos4y] == 0):
                            self.score -= 100
                            self.score -= abs(self.current.x - pos4x)
                            self.score -= abs(self.current.y - pos4y)

                            self.current.x = pos4x
                            self.current.y = pos4y

                            self.cave.throw_arm(self.current.x, self.current.y, 'r')

        elif (self.return_count > 4) and (len(exit_unknown) > 0):
            self.return_count = 0
            c = Coords(exit_unknown[0].x, exit_unknown[0].y)
            self.current.x = c.x
            self.current.y = c.y

            self.score -= 1
            self.visited.append((c))
        elif self.gCount < 2:
            self.Loose = True
        else:
            move = False
            for i in range(4):
                for j in range(4):
                    if (self.predictions[i][j] in [1, 2]) and (not move):
                        move = True
                        self.score -= abs(self.current.x - i)
                        self.score -= abs(self.current.y - j)
                        self.current.x = i
                        self.current.y = j
            if (not move):
                self.Loose = True

    def set_predict_by_actions(self, a):
        if a.shine:
            self.score += 1000
            self.gCount -= 1
        if (a.scream and self.VIY):
            self.VIY = False
            for i in range(4):
                for j in range(4):
                    if self.predictions[i][j] == 3:
                        self.predictions[i][j] = 1
                    elif self.predictions[i][j] == 2:
                        self.predictions[i][j] = -1
        if (a.enemy):
            self.score -= 1000
            self.Loose = True
        if self.gCount == 0:
            self.Win = True


cave = Cave()
Homa = Agent(cave)

while ((not Homa.Win) and (not Homa.Loose)):
    print()
    print(Homa.current.x, Homa.current.y)
    Homa.print_cave()

    sence = Homa.cave.get_info(Homa.current.x, Homa.current.y)

    Homa.set_predict_by_sensors(sence)
    Homa.make_move()
    act = Homa.cave.get_result(Homa.current.x, Homa.current.y)
    Homa.set_predict_by_actions(act)

print('Homa win' if Homa.Win else 'Homa lose' if Homa.score < 0 else 'Gold received')
print('Viy killed' if Homa.VIY else 'Viy is not killed')
print('Score:', Homa.score)
