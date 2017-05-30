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
                        if hero[0]==values[0]:
                            hero[1] += (float(values[1])*-1)
                            hero[2].append(100-float(values[2]))
                            hero[3] += int(values[3])
                except KeyError:
                    continue
    return hero_stats


def hero_suggester(stats):
    sorted_stats = sorted(stats, key=lambda x: x[1], reverse=True)
    for hero in sorted_stats:
        if hero[1] >= 0 and True if all(float(x) >= float(50) for x in hero[2]) else False :
            print hero
        elif all(float(x) >= float(50) for x in hero[2]):
            print hero

def main():
    print "Dota 2 Heros Suggester"
    print "Do you want to pull the latest data (y/n)"
    if raw_input()=='y':
        os.system('scrapy runspider matchups_getter.py')
        os.system('scrapy runspider heroes_getter.py')
    print "Starting Hero Suggester"
    heroes = []
    with open('heros.txt', 'r') as f:
        i = 1
        for line in f:
            heroes.append(line.strip())
    hero_stats = []
    for j in range(len(heroes)):
        print "(" + str(j+1) + ':' + heroes[j] + ")    ",
    for i in range(5):
        print "\nChoose No " + str(i+1) + " Enemy Hero"
        print 'Input Hero Number to Select : ',
        hero = int(raw_input())
        print "Hero Selected : " + str(heroes[hero-1])
        hero_stats = load_hero_data_into_suggestions(heroes[hero-1], hero_stats)
        hero_suggester(hero_stats)
if __name__ == "__main__":
    main()
