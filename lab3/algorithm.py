import random
import math


def sim_annealing(initial_state, final_state, t_0=10000, max_moves=100000):
    state = initial_state
    moves = 1
    while moves <= max_moves:
        t = t_0 / moves
        new_state = random.choice(state.get_next_states())
        energy = state.get_heuristic_evaluate()
        new_energy = new_state.get_heuristic_evaluate()
        possibility = 1 / (1 + math.exp(new_energy - energy) / t)
        accepted_move = False
        if new_energy < energy:
            accepted_move = True
        elif random.random() < possibility:
            accepted_move = True
        if accepted_move:
            state = new_state
        if state.matrix == final_state.matrix:
            break
        # print("Energy:{}".format(state.get_heuristic_evaluate()))
        # state.print_state()
        moves += 1
    return state


