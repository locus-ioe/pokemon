import random
import difflib


print('pokemon loading...')

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
    print(str(i+1) + ". " + name)

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
opponent = pokemon_names[random.randint(1, len(pokemons)-1)]

print("You chose " + choice)
print("Your attacks: ")
i = 1
for attack in pokemons[choice]:
    print(str(i) + ". " + attack[0])
    i += 1

print("Opponent chose " + opponent)
print("Opponent's attacks: ")
i = 1
for attack in pokemons[opponent]:
    print(str(i) + ". " + attack[0])
    i += 1

# Create the user and opponent data structures:
# [name, attacks, health].
user = [choice, pokemons[choice], 100]
opponent = [opponent, pokemons[opponent], 100]


def attack(attacker, other, attack_id):
    attack = attacker[1][attack_id]
    print(attacker[0] + " uses " + attack[0] + ".")
    hit = random.gauss(attack[1], 10)
    other[2] = max(0, other[2] - hit)
    print("It did " + str(hit) + " points damaage on " + other[0] + ".")
    print(other[0] + " has now health points " + str(other[2]) + ".\n")


print("\nBattle !\n")

while (True):
    # Let the user decide the first attack.
    attack_choice = int(input("Choose an attack (1-4): "))
    # TODO: Validate attack input.
    attack(user, opponent, attack_choice)

    if opponent[2] == 0:
        print("You won !")
        break

    attack_choice = random.randint(1, 4)
    attack(opponent, user, attack_choice)

    if user[2] == 0:
        print("You lost !")
        break
