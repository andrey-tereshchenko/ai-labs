import random
import copy


class State:
    def __init__(self, matrix, depth):
        self.matrix = matrix
        self.depth = depth

    @staticmethod
    def get_final_state():
        numbers = [i for i in range(10)]
        counter = 0
        final_state = []
        for i in range(3):
            row = []
            for j in range(3):
                if i == 0 and j == 0:
                    row.append(' ')
                else:
                    number = numbers[counter]
                    row.append(str(number))
                counter += 1
            final_state.append(row)
        return State(final_state, 0)

    def search_index_empty_field(self):
        for i in range(3):
            for j in range(3):
                if self.matrix[i][j] == ' ':
                    return i, j

    def swap_two_fields(self, i1, j1, i2, j2):
        new_matrix = copy.deepcopy(self.matrix)
        new_matrix[i1][j1], new_matrix[i2][j2] = new_matrix[i2][j2], new_matrix[i1][j1]
        return new_matrix

    def print_state(self):
        for i in range(3):
            for j in range(3):
                print(self.matrix[i][j], sep=' ', end=' ')
            print()
        print("depth: " + str(self.depth))
        print('----------------------------')

    def get_next_states(self):
        row, column = self.search_index_empty_field()
        states = []
        if column >= 1:
            new_matrix = self.swap_two_fields(row, column, row, column - 1)
            states.append(State(new_matrix, self.depth + 1))
        if row >= 1:
            new_matrix = self.swap_two_fields(row, column, row - 1, column)
            states.append(State(new_matrix, self.depth + 1))
        if column <= 1:
            new_matrix = self.swap_two_fields(row, column, row, column + 1)
            states.append(State(new_matrix, self.depth + 1))
        if row <= 1:
            new_matrix = self.swap_two_fields(row, column, row + 1, column)
            states.append(State(new_matrix, self.depth + 1))
        return states


class Node:
    def __init__(self, current_state):
        self.visited_states = []
        self.current_state = current_state
        self.next_states = current_state.get_next_states()


class LDFS:
    def __init__(self, node, final_state, max_depth=None):
        self.counter = 0
        self.node = node
        self.max_depth = max_depth
        self.final_state = final_state
        self.visited_matrix = []
        self.finish_flag = False

    def run(self):
        if not self.finish_flag:
            self.node.current_state.print_state()
            self.counter += 1
            print('Counter:' + str(self.counter))
            self.visited_matrix.append(self.node.current_state.matrix)
            if self.node.current_state.matrix == self.final_state.matrix:
                self.finish_flag = True
                return

            if self.node.current_state.depth < self.max_depth:
                if self.node.next_states:
                    for i in self.node.next_states:
                        if i.matrix not in self.visited_matrix:
                            self.node = Node(i)
                            self.run()
                        else:
                            self.counter += 1
                else:
                    return
            else:
                return
        else:
            return


class IDS:
    def __init__(self, ldfs):
        self.counter = 0
        self.ldfs = ldfs
        self.stop_flag = False
        self.current_depth = 1

    def run(self):
        while not self.stop_flag:
            ldfs = copy.deepcopy(self.ldfs)
            ldfs.max_depth = self.current_depth
            ldfs.run()
            self.counter += ldfs.counter
            self.stop_flag = ldfs.finish_flag
            self.current_depth += 1


moves = 80
init_state = State.get_final_state()
for i in range(moves):
    init_state = random.choice(init_state.get_next_states())
init_state.depth = 0
final_state = State.get_final_state()
root = Node(init_state)
ldfs = LDFS(root, final_state)
ids = IDS(ldfs)
ids.run()
print("Total generated states:" + str(ids.counter))
print("Approached depth search:" + str(ids.current_depth))

