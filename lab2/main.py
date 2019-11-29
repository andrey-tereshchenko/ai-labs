import random
import time
from lab2.tree_of_states import State, Node
from lab2.algorithm import LDFS, IDS, RBFS


def test_ids_algorithm(moves, iteration):
    avg_time = 0
    avg_state_generated = 0
    avg_state_storaged = 0
    for i in range(iteration):
        init_state = State.get_final_state()
        for j in range(moves):
            init_state = random.choice(init_state.get_next_states())
        init_state.depth = 0
        root = Node(init_state)
        start = time.time()
        ldfs = LDFS(root, final_state)
        ids = IDS(ldfs)
        ids.run()
        end = time.time()
        avg_time += end - start
        avg_state_generated += ids.counter
        avg_state_storaged += ids.states_stored
        print("Iteration IDS:{}".format(i + 1))
        print("Success depth:{}".format(ids.current_depth))
        print('------------------------------')
    return avg_time / iteration, avg_state_generated / iteration, avg_state_storaged / iteration


def test_rdfs_algorithm(moves, iteration):
    avg_time = 0
    avg_state_generated = 0
    avg_state_storaged = 0
    for i in range(iteration):
        init_state = State.get_final_state()
        for j in range(moves):
            init_state = random.choice(init_state.get_next_states())
        init_state.depth = 0
        root = Node(init_state)
        start = time.time()
        ldfs = LDFS(root, final_state)
        rbfs = RBFS(root, final_state)
        rbfs.run()
        end = time.time()
        avg_time += end - start
        avg_state_generated += rbfs.counter
        avg_state_storaged += rbfs.states_stored
        print("Iteration RDFS:{}".format(i + 1))
        print('------------------------------')
    return avg_time / iteration, avg_state_generated / iteration, avg_state_storaged / iteration


if __name__ == "__main__":
    moves = 30
    iteration = 20
    final_state = State.get_final_state()
    init_state = State.get_final_state()
    for j in range(moves):
        init_state = random.choice(init_state.get_next_states())
    init_state.depth = 0
    root = Node(init_state)
    avg_time_ids, avg_count_ids, avg_stored_ids = test_ids_algorithm(moves, iteration)
    avg_time_rdfs, avg_count_rdfs, avg_stored_rdfs = test_rdfs_algorithm(moves, iteration)
    print("Algorithm IDS\nAvg time:{} Avg generated states:{} Avg stored states:{}".format(avg_time_ids, avg_count_ids,
                                                                                           avg_stored_ids))
    print(
        "Algorithm RDFS\nAvg time:{} Avg generated states:{} Avg stored states:{}".format(avg_time_rdfs, avg_count_rdfs,
                                                                                         avg_stored_rdfs))
