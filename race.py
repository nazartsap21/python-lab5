from lab5 import Race, RaceHorse

if __name__ == '__main__':
    horse1 = RaceHorse(10, 7, "Valkyrie")
    horse2 = RaceHorse(12, 5, "Silver Bullet")
    horse3 = RaceHorse(16, 3, "Hono")
    horse4 = RaceHorse(9, 7, "Roxanne")

    race = Race()
    race.new_participant(horse1)
    race.new_participant(horse2)
    race.new_participant(horse3)
    race.new_participant(horse4)

    print(race.select_winner())

    race.sort_speed()
    print(race.participants)

    race.set_place()
    print(race.participants)

    race.del_participant(horse4)
    print(race.participants)
