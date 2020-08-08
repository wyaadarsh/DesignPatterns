# Game for adults or kids: To be decided at the runtime of application based on the inputs

# Kid's Game


class Frog:

    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name

    def interact_with(self, obstacle):
        print("{} the frog encounters {} and {}".format(self, obstacle, obstacle.action()))


class Bug:

    def __str__(self):
        return "a bug"

    def action(self):
        return "Eats it."


class FrogWorld:

    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return "\n --------------Frog World------------- \n"

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


# Adult's Game

class Wizard:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, enemy):
        print("{} the wizard encounters {} and {}".format(self, enemy, enemy.action()))


class Ork:

    def __str__(self):
        return "Ork"

    def action(self):
        return "Kills it."


class WizardWorld:

    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return "\n --------------Wizard World------------- \n"

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork()


class GameEnvironment:
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)

