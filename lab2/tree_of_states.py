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

    def get_heuristic_evaluate(self):
        final_matrix = self.get_final_state().matrix
        estimation = 0
        for i in range(3):
            for j in range(3):
                if self.matrix[i][j] != final_matrix[i][j]:
                    estimation += 1
        return estimation


class Node:
    def __init__(self, current_state):
        self.visited_states = []
        self.current_state = current_state
        self.next_states = current_state.get_next_states()


