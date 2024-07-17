print("START GAME! \n")
#Randomly chosses a word from word_list
import random
from hangman_words import words_list

chosen_word = random.choice(words_list)
#replace the word with blanks
display = []
for _ in range(len(chosen_word)):
  display += "_"
print(display)
#Ask the user to guess a letter
end_game = False
lives = 6
from hangman_art import logo

print(logo)
while not end_game:
  guess = input("Guess a letter: \n").lower()
  if guess in display:
    print(f"You have already guessed {guess} \n")
#You guess a right letter
  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
  print(display)
  #you guess a wrong letter
  if guess not in chosen_word:
    print(f"You guessed: {guess}, that's not in the word. You Lose a life\n")
    lives -= 1
    if lives == 0:
      end_game = True
      print("You lose")
  if "_" not in display:
    end_game = True
    print("Player Wins")
  from hangman_art import stages
  print(stages[lives])
