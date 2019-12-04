import copy
import random

from lab2.tree_of_states import Node


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
            # self.node.current_state.print_state()
            self.counter += 1
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
        self.states_stored = 0

    def run(self):
        while not self.stop_flag:
            ldfs = copy.deepcopy(self.ldfs)
            ldfs.max_depth = self.current_depth
            ldfs.run()
            self.counter += ldfs.counter
            self.states_stored += len(ldfs.visited_matrix)
            self.stop_flag = ldfs.finish_flag
            self.current_depth += 1
            if self.current_depth == 20:
                break


class RBFS:
    def __init__(self, node, final_state):
        self.counter = 0
        self.stop_flag = False
        self.states_stored = 0
        self.node = node
        self.final_state = final_state
        self.states_stored = 0
        self.visited_matrix = []
        self.limit = 10000000000000

    def run(self):
        self.counter += 1
        self.visited_matrix.append(self.node.current_state.matrix)
        if self.node.current_state.matrix == self.final_state.matrix:
            self.stop_flag = True
            return
        children = []
        for i in self.node.next_states:
            if i.matrix not in self.visited_matrix:
                children.append(i)

        children = [(i.get_heuristic_evaluate(), i) for i in children]
        j = 0
        if not children:
            return

        while len(children):
            success = sorted(children, key=lambda x: x[0])
            value = random.randint(50, 100)
            if len(success) == 1:
                alternative = 1000000000
                self.limit = success[0][0] + 1
            else:
                if success[0][0] == success[1][0]:
                    if value % 2 == 0:
                        success[0], success[1] = success[1], success[0]
                alternative = success[1][0]
            best_node = success[0][1]
            best_score = success[0][0]
            j += 1
            if self.limit < best_score:
                self.node = Node(best_node)
                return
            self.node = Node(best_node)
            self.limit = min(self.limit, alternative)
            self.run()
            success[0] = (self.node.current_state.get_heuristic_evaluate(), best_node)
            if j > 500:
                self.stop_flag = True
                self.states_stored = len(self.visited_matrix) - value
            if self.stop_flag:
                break
