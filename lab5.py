class RaceHorse:
    """horse characteristics"""

    def __init__(self, speed, age, name):
        self.speed = speed
        self.age = age
        self.name = name
        self.place_in_race = None

    def __repr__(self):
        return f"Racehorse({self.speed}, {self.age}, {self.name}, {self.place_in_race})"


class Race:

    def __init__(self):
        self.participants = []

    def new_participant(self, horse):
        if 3 <= horse.age <= 7:
            self.participants.append(horse)

    def del_participant(self, horse):
        self.participants.remove(horse)

    def select_winner(self):
        avg_age = sum(horse.age for horse in self.participants) / len(self.participants)
        winner = sorted(self.participants, key=lambda horse: horse.speed + abs(horse.age - avg_age), reverse=True)[0]
        winner.place_in_race = 1
        return winner

    def sort_speed(self):
        self.participants.sort(key=lambda horse: horse.speed, reverse=True)

    def set_place(self):
        for i, horse in enumerate(self.participants[:3]):
            horse.place_in_race = i + 1


horse1 = RaceHorse(10, 7, "Valkyrie")
horse2 = RaceHorse(12, 5, "Silver Bullet")
horse3 = RaceHorse(16, 3, "Hono")
horse4 = RaceHorse(9, 7, "Roxanne")

if __name__ == '__main__':

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
