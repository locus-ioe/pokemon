"""A Pokemon Game built for Python Workshop, Locus 2016.

The game is simple and text-based. Pokemons data are read
from file. User get to choose a pokemon while the computer
chooses one at random. Then the battle starts with the user
and the computer alternatively choosing attacks for their
respective pokemons. The game ends when one of the pokemon
loses all health.
"""

import random
import difflib


def use_attack(attacker, other, attack_id):
    """Attacker uses attack with given id on other.
    We need to get a random hit point based around the strength of
    the attack, and use it to decrease health
    of the other.
    """

    attack = attacker[1][attack_id-1]
    print("{} uses {}.".format(attacker[0],attack[0]))

    # Gaussian randomness with attack's strength as mean.
    hit = random.gauss(attack[1], 10)

    # Decrease the health by "hit", but don't let it be less than 0.
    other[2] = max(0, other[2] - hit)

    print("It did {:.2f} points damage on {}.".format(hit,other[0]))
    print("{} has now health points {:.2f}\n".format(other[0],other[2]))


""" START
"""

print('Loading pokemons ...')

# Read pokemon data from file and split by the separator 'end'.

pokemon_data = open('pokemon.data', 'r').read()
raw_data = pokemon_data.strip().split('end')[:-1]

# Store all pokemon data as dictionary in format:
# { name: [(attack1, strength), (attack2, strength), ...], ...}

pokemons = {}
pokemon_names = []

for each in raw_data:
    # Split each pokemon data by whitespace.
    # This gives [name, attack1, strength1, attack2, strength2, ...]
    temp = each.split()

    # Get the pokemon name.
    name = temp[0]
    # Get each attack and its strength.
    attacks = []
    for i in range(1, len(temp), 2):
        attack = (temp[i][:-1], int(temp[i+1]))
        attacks.append(attack)
    pokemons[name] = attacks
    pokemon_names.append(name)

# Show pokemon list.
for i, name in enumerate(pokemon_names):
    print("{}. {}".format(i+1,name))

# Get pokemon choice from user.
while(True):
    user_input = input("Choose your pokemon: ")

    # Get the closest matching pokemon name.
    possible_choices = difflib.get_close_matches(user_input, pokemon_names)
    if len(possible_choices) == 0:
        print("Invalid choice")
    else:
        choice = possible_choices[0]
        break

# Find a random pokemon opponent.
opponent = random.choice(pokemon_names)

print("You chose {}".format(choice))
print("Your attacks: ")
i = 1
for attack in pokemons[choice]:
    print("{}. {}".format(i,attack[0]))
    i += 1

print("Opponent chose {}".format(opponent))
print("Opponent's attacks: ")
i = 1
for attack in pokemons[opponent]:
    print("{}. {}".format(i,attack[0]))
    i += 1

# Create the user and opponent data structures:
# [name, attacks, health].
user = [choice, pokemons[choice], 100]
opponent = [opponent, pokemons[opponent], 100]


print("\nBattle !\n")

# The Battle is a loop that ends only with victory or loss.
while True:

    # Let the user decide the first attack.
    while True:
        attack_choice = input("Choose an attack (1-4): ")
        # check if the user has entered non integer value
        try:
            attack_choice = int(attack_choice)
        except:
            print("Please enter integer value")
            continue
        if attack_choice < 1 or attack_choice > 4:
            print("Invalid choice")
        else:
            break

    # Use the choice for attacking the opponent.
    use_attack(user, opponent, attack_choice)

    # Check for victory.
    if opponent[2] == 0:
        print("You won !")
        break

    # Get a random attack choice for opponent and use it on user.
    attack_choice = random.randint(1, 4)
    use_attack(opponent, user, attack_choice)

    # Check for loss.
    if user[2] == 0:
        print("You lost !")
        break

