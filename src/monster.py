class Monster:
    def __init__(self, name, diet):
        self.name = name
        self.diet = diet

    def speak(self):
        pass

    def attack(self, player):
        player.health - 1


class ClosetMonster(Monster):
    def __init__(self, name, diet='egg'):
        super().__init__(name, diet)

    def speak(self):
        print('\nRwarrrgh!!!!!!!!! Rwarrargggghh!!!\n')

    def attack(self, player):

        player.health = player.health - 15
        print(f'{self.name} just bit you with his razor sharp teeth!')
        print(f'Your took damage!\nYour health: {player.health}')
