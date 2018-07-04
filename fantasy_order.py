import random
import itertools

wc_teams = ['France/Uruguay', 'Russia/Croatia', 'Brazil/Belgium', 'Sweden/England']

fantasy_people = ['Andrew Weiser', 'Ben Vitello', 'CJ Aydin', 'Chris Tran', 'Eren Erdogan', 'Eric Revich', 'Mike Themis', 'Pat Nizza', 'Scott Kessler', 'Sean Slavin', 'Sunny Polepalli', 'Tim Sawma']

permutations = list(itertools.permutations(wc_teams))

def print_order(order, fantasy_people):
    print('1st {}, 2nd {}, 3rd {}, 4th {}:'.format(order[0], order[1], order[2], order[3]))
    for i in range(0, len(fantasy_people)):
        print('{}.) {}'.format(i+1, fantasy_people[i]))

    print('')

for order in permutations:
    random.shuffle(fantasy_people)
    print_order(order, fantasy_people)
