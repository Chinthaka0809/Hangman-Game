import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
space = []
lives = 6
 

 # Make a space to same lenght of word
for  i in chosen_word:
    space.append("_")

size = len(space)
print(f"Your guessing space : {space}")
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position] 
        if letter == guess:
            if(space[position] == guess):
                position += 1
            else:
                space[position] = guess
    print(space)

    if guess not in chosen_word :
        lives -= 1
        if lives == 0:
            print("You lost") 
            end_of_game = True

    if "_" not in space:
        end_of_game =  True
        print("You win")

    print(stages[lives])      

    

