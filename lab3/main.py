import random
import time

from lab2.tree_of_states import State
from lab3.algorithm import sim_annealing

if __name__ == "__main__":
    avg_time = 0
    avg_iteration = 0
    failure = 0
    for i in range(20):
        print("Algorithm ANNEAL number:{}".format(i+1))
        moves = 20
        final_state = State.get_final_state()
        init_state = State.get_final_state()
        for j in range(moves):
            init_state = random.choice(init_state.get_next_states())
        init_state.depth = 0
        start = time.time()
        search_state = sim_annealing(init_state, final_state)
        end = time.time()
        avg_iteration += search_state.depth
        avg_time += end - start
        if search_state.matrix == final_state.matrix:
            print('I solved your puzzle')
        else:
            print('Sorry, I could not solve it')
            failure += 1
    print("Algorithm ANNEAL\nAvg time:{} Avg iterations:{} Failure:{}".format(avg_time / i,
                                                                              avg_iteration / i,
                                                                              failure))
