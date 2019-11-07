from optparse import OptionParser

from src.environment import Environment as env
from src.agent import Agent
from src.evaluator import Evaluator

DEBUG = True


def run(zone, agent, calculus, iteration):
    zone.change()
    agent.prespective(zone)

    #action = agent.think_random(zone.maze)
    #action = agent.think_reflex(zone.maze)
    action = agent.think_model_based(zone.maze,  iteration)
    print(action)
    zone.accept_action(action)
    calculus.evaluete(action, zone)
    zone.print_maze()


def main():
    f = open(map_path)
    zone = env(f)
    bond = Agent(zone)

    current_time = 0
    bond.agent_map[bond.posX][bond.posY] = 1
    calculus = Evaluator()

    while current_time < life_time:
        run(zone, bond, calculus, current_time)
        print('|===|===|===|===|===|===|===|===|===|===|===|===|===|===|===|===|===|')
        for line in bond.agent_map:
            print(['{0:3}'.format(x) for x in line])
        print('|===|===|===|===|===|===|===|===|===|===|===|===|===|===|===|===|===|\n')

        current_time += 1
    print("Cleaned dirty: " + str(calculus.cleaned_dirty))
    print("consumed energy: " + str(calculus.consumed_energy))
    print("Avg dirty: " + str(calculus.total_dirty / life_time))
    print('|===|===|===|===|===|===|===|===|===|===|===|===|===|===|===|===|===|')
    for line in bond.agent_map:
        print(['{0:3}'.format(x) for x in line])
    print('|===|===|===|===|===|===|===|===|===|===|===|===|===|===|===|===|===|\n')


if __name__ == "__main__":
    current_time = 0
    life_time = 1000
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
