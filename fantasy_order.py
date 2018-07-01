import random

wc_teams = ['France', 'Uruguay', 'Spain/Russia', 'Croatia/Denmark', 'Brazil/Mexico', 'Belgium/Japan', 'Sweden/Switzerland', 'Colombia/England']

fantasy_people = ['Andrew Weiser', 'Ben Vitello', 'CJ Aydin', 'Chris Tran', 'Eren Erdogan', 'Eric Revich', 'Mike Themis', 'Pat Nizza', 'Scott Kessler', 'Sean Slavin', 'Sunny Polepalli', 'Tim Sawma']


def print_order(wc_team, fantasy_people):
    print('{}: '.format(wc_team))
    for i in range(0, len(fantasy_people)):
        print('{}.) {}'.format(i+1, fantasy_people[i]))

    print('')

for team in wc_teams:
    random.shuffle(fantasy_people)
    print_order(team, fantasy_people)
