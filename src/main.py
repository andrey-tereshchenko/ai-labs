from optparse import OptionParser

from src.environment import Environment as env
from src.agent import Agent
from src.evaluator import Evaluator
import matplotlib.pyplot as plt
import numpy as np
import copy

DEBUG = True


def clean_maze(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if int(maze[i][j]) == 1:
                maze[i][j] = 0
    return maze


def show(labels, garbage, energy):
    x = np.arange(len(labels))
    width = 0.45

    fig, ax = plt.subplots()
    ax.bar(x - width / 2, garbage, width, label='garbage')
    ax.bar(x + width / 2, energy, width, label='enegry')

    ax.set_ylabel('Scores')
    ax.set_title('Scores by agents')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    fig.tight_layout()

    plt.show()


def run(zone, agent, calculus, iteration, type):
    zone.change()
    agent.prespective(zone)

    if type == 0:
        action = agent.think_random(zone.maze)
    elif type == 1:
        action = agent.think_reflex(zone.maze)
    elif type == 2:
        action = agent.think_model_based(zone.maze, iteration)
    # print(action)
    zone.accept_action(action)
    calculus.evaluete(action, zone)
    zone.print_maze()


def main():
    energy_list = []
    garbage_list = []
    f = open(map_path)
    z = env(f)
    for i in range(3):
        zone = copy.deepcopy(z)
        zone.maze = clean_maze(zone.maze)
        bond = Agent(zone)
        current_time = 0
        bond.agent_map[bond.posX][bond.posY] = 1
        calculus = Evaluator()

        while current_time < life_time:
            run(zone, bond, calculus, current_time, i)
            current_time += 1
        print("Cleaned dirty: " + str(calculus.cleaned_dirty))
        print("consumed energy: " + str(calculus.consumed_energy))
        print("Avg dirty: " + str(calculus.total_dirty / life_time))
        energy_list.append(calculus.consumed_energy)
        garbage_list.append(calculus.total_dirty / life_time)
    labels = ['random', 'reflex', 'model-based']
    show(labels, garbage_list, energy_list)


if __name__ == "__main__":
    current_time = 0
    life_time = 100
    map_path = '../map/first.map'

    usage = "usage: %prog [options] arg1 arg2"
    parser = OptionParser(usage=usage)
    parser.add_option("-m", "--map", dest="map_path", default=False,
                      help="Path to the map")
    parser.add_option("-l", "--life", dest="life_time", default=False,
                      help="Life time value")
    args = parser.parse_args()
    args = args[0]

    if args.map_path:
        map_path = args.map_path
    if args.life_time:
        life_time = int(args.life_time)

    main()
