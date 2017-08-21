import os


def load_hero_data_into_suggestions(hero_name, hero_stats):
    file_name = hero_name + ' - Matchups - DOTABUFF - Dota 2 Stats.txt'
    with open(file_name, 'r') as f:
        if len(hero_stats) == 0:
            for line in f:
                values = line.split(',')
                hero_stats.append([values[0], (float(values[1])*-1), [100-float(values[2])], int(values[3])])
        else:
            for line in f:
                values = line.split(',')
                try:
                    for hero in hero_stats:
                        if hero[0] == values[0]:
                            hero[1] += (float(values[1])*-1)
                            hero[2].append(100-float(values[2]))
                            hero[3] += int(values[3])
                except KeyError:
                    continue
    return hero_stats


def hero_suggester(stats):
    sorted_stats = sorted(stats, key=lambda x: x[1], reverse=True)
    for hero in sorted_stats:
        if hero[1] >= 0 and True if all(float(x) >= float(50) for x in hero[2]) else False:
            print hero
        elif all(float(x) >= float(50) for x in hero[2]):
            print hero


def get_heroes():
    heroes = []
    with open('heros.txt', 'r') as f:
        for line in f:
            heroes.append(line.strip())
        return heroes


def print_heros(heroes):
    for j in range(len(heroes)):
        print "(" + str(j + 1) + ':' + heroes[j] + ")    ",


def suggest_hero():
    heroes = get_heroes()
    hero_stats = []
    print_heros(heroes)
    for i in range(5):
        print "\nChoose No " + str(i + 1) + " Enemy Hero"
        print 'Input Hero Number to Select : ',
        hero = int(raw_input())
        print "Hero Selected : " + str(heroes[hero - 1])
        hero_stats = load_hero_data_into_suggestions(heroes[hero - 1], hero_stats)
        hero_suggester(hero_stats)


def pull_data():
    print "*Starting Pulling Data*"
    os.system('scrapy runspider matchups_getter.py')
    os.system('scrapy runspider heroes_getter.py')
    print "Data has been Updated"


def team_picks(heroes):
    team = []
    for i in range(5):
        print "\nChoose No " + str(i + 1) + " Enemy Hero"
        print 'Input Hero Number to Select : ',
        hero = int(raw_input())
        print "Hero Selected : " + str(heroes[hero - 1])
        team.append(str(heroes[hero - 1]))
    return team


def compare_teams(radiant, dire):
    radiant_advantage = list(get_team_advantage(radiant, dire))
    dire_advantage = list(get_team_advantage(dire, radiant))
    return radiant_advantage, dire_advantage


def get_team_advantage(team, oponent_team):
    advantage = 0.0
    win_chance = 0.0
    for hero in team:
        file_name = hero + ' - Matchups - DOTABUFF - Dota 2 Stats.txt'
        win_chance_per_hero = 0.0
        with open(file_name, 'r') as f:
            for line in f:
                match_up_stats = line.split(',')
                if match_up_stats[0] in oponent_team:
                    advantage += float(match_up_stats[1])
                    win_chance_per_hero += float(match_up_stats[2])
            win_chance_per_hero = win_chance_per_hero/5
        win_chance += win_chance_per_hero
    return advantage, win_chance/5


def compare_two_teams():
    heroes = get_heroes()
    print "Pick Radiant Team :"
    print_heros(heroes)
    radiant = team_picks(heroes)
    print "Pick Dire Team :"
    print_heros(heroes)
    dire = team_picks(heroes)
    radinat_points, dire_points = compare_teams(radiant, dire)
    print 'Radiant Win Chance :' + str(radinat_points[1])
    print 'Dire Win Chance :' + str(dire_points[1])


def main():
    print "Dota 2 Heros Suggester"
    while True:
        print "1. Hero Suggester"
        print "2. Compare Teams"
        print "3. Pull Data"
        print "4. Close"
        print "Chose Option :"
        option = raw_input()
        if option == '1':
            suggest_hero()
        elif option == '2':
            compare_two_teams()
        elif option == '3':
            # Todo: Later Add patch to updated with respect to latest Patch
            # print "Enter the Patch :"
            # patch = raw_input()
            pull_data()
        elif option == '4':
            break


if __name__ == "__main__":
    main()
