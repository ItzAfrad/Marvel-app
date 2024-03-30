import os
print('\033[32mWelcome to the Marvel app')
class Marvel:

    def info(self):
        print('name')
        print("age")
        print('super power')
        print('height')
        print('weakness')


class Spiderman(Marvel):

    def info(self):
        print('Peter Parker')
        print('21yrs old')
        print('Super Strength \n Spider sense \n agility \n Stick to surfaces')
        print('5ft 8')
        print('Big disadvantage without his web shooters')


class Ironman(Marvel):

    def info(self):
        print('Tony Stark')
        print('53yrs old')
        print('HI-Tech suit')
        print('nothing without suit')


class Dr_Strange(Marvel):

    def info(self):
        print('Stephen Strange')
        print('36yrs old')
        print(
            'Can control time using time stone \n can teleport \n use the multiverse'
        )
        print('6ft')
        print('No weakness')


class CaptainAmerica(Marvel):

    def info(self):
        print('Steve Rogers')
        print('100+ years old (due to super-soldier serum)')
        print('Superhuman strength, agility, and endurance')
        print('6ft 2')
        print('Vibranium shield provides protection')
        print(
            'Vulnerable to mental manipulation and lacks superhuman healing abilities'
        )


class Thor(Marvel):

    def info(self):
        print('Thor Odinson')
        print('Over 1000 years old (as Asgardians age differently)')
        print('God-like strength, control over lightning, flight')
        print('6ft 6')
        print('Vulnerable without Mjolnir (his hammer)')


class Hulk(Marvel):

    def info(self):
        print('Bruce Banner')
        print('Age varies due to transformations')
        print('Incredible superhuman strength, regeneration')
        print('7ft')
        print('Can become vulnerable in human form')


class BlackPanther(Marvel):

    def info(self):
        print('T\'Challa')
        print('30+ years old')
        print(
            'Enhanced strength, agility, and senses due to heart-shaped herb')
        print('6ft')
        print('Vibranium suit provides enhanced durability')
        print('Vulnerable without his suit and herb-induced powers')


class Vision(Marvel):

    def info(self):
        print('Vision')
        print('Ageless (synthetic being)')
        print('Superhuman strength, density manipulation, energy beams')
        print('6ft 3')
        print('Made of Vibranium and has a powerful energy source')
        print('Vulnerable if the Mind Stone is removed')


class BlackWidow(Marvel):

    def info(self):
        print('Natasha Romanoff')
        print('30+ years old')
        print('Expert martial artist, espionage, and marksmanship')
        print('5ft 7')
        print('Highly trained with advanced weaponry')
        print('No superhuman abilities, relies on skill and equipment')


class Hawkeye(Marvel):

    def info(self):
        print('Clint Barton')
        print('40+ years old')
        print('Master archer, exceptional hand-to-hand combatant')
        print('6ft 3')
        print('Highly skilled with various arrows and weapons')
        print('Lacks superhuman abilities, relies on exceptional skills')


class Daredevil(Marvel):

    def info(self):
        print('Matt Murdock (Daredevil)')
        print('30+ years old')
        print('Enhanced senses, expert martial artist')
        print('5ft 10')
        print('Uses a combination of martial arts and his heightened senses')
        print('Blind, but his other senses are enhanced')


class NickFury(Marvel):

    def info(self):
        print('Nick Fury')
        print('Unknown age (classified)')
        print('Master tactician, skilled hand-to-hand combatant')
        print('6ft 1')
        print('Strategic genius and excellent leader')
        print('No superhuman abilities, relies on his skills and intelligence')


class AntMan(Marvel):

    def info(self):
        print('Scott Lang ')
        print('40+ years old')
        print('Can shrink and communicate with ants')
        print('5ft 10')
        print('Wears a suit that allows him to shrink and grow in size')
        print('Vulnerable without his suit and Pym particles')


class Wasp(Marvel):

    def info(self):
        print('Hope van Dyne ')
        print('26 years old')
        print('Can shrink, fly, and fire bio-electric blasts')
        print('5ft 6')
        print('Uses a suit with wings and blasters')
        print('Vulnerable without her suit and Pym particles')


class ScarletWitch(Marvel):

    def info(self):
        print('Wanda Maximoff')
        print('30+ years old')
        print('Reality manipulation, energy projection')
        print('5ft 7')
        print('Harnesses chaos magic')
        print('Emotionally vulnerable, and her powers can be unpredictable')


class Falcon(Marvel):

    def info(self):
        print('Sam Wilson')
        print('30+ years old')
        print('Wingsuit with enhanced strength and flight capability')
        print('6ft 2')
        print('Employs a highly advanced winged suit')
        print('No superhuman abilities, relies on technology')


class WarMachine(Marvel):

    def info(self):
        print('James "Rhodey" Rhodes ')
        print('40+ years old')
        print('Powered combat armor with heavy weaponry')
        print('6ft 1')
        print('Wears a heavily armed suit')
        print('Relies on his suit and weaponry for combat')


# Create instances of the superheroes
ironman = Ironman()
spiderman = Spiderman()
drstrange = Dr_Strange()
captain_america = CaptainAmerica()
thor = Thor()
hulk = Hulk()
black_panther = BlackPanther()
vision = Vision()
black_widow = BlackWidow()
hawkeye = Hawkeye()
daredevil = Daredevil()
nick_fury = NickFury()
ant_man = AntMan()
wasp = Wasp()
scarlet_witch = ScarletWitch()
falcon = Falcon()
war_machine = WarMachine()

# Add these superheroes to the previous ones
superheroes = [
    ironman, spiderman, drstrange, captain_america, thor, hulk, black_panther,
    vision, black_widow, hawkeye, daredevil, nick_fury, ant_man, wasp,
    scarlet_witch, falcon, war_machine
]
while True:
# Get user input
    information = input('Enter superhero>')

# Display information based on user's input
    for hero in superheroes:
        if information.lower().replace(' ', '') == hero.__class__.__name__.lower():
            hero.info()
            break
    else:
        print('Superhero not found')
    exit_condition = input("Press 'q' to quit, or any other key to continue: ")
    if exit_condition == 'q':
        break