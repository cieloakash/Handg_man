import random
import art_
import words_


chosen_word = random.choice(words_.word_list)


display = []
wrong_letters = []
end_of_game = False
lives = 6

for letter in chosen_word:
  display.append("_")

print(art_.logo)

while not end_of_game:
  print(art_.stages[lives])
  guess = input("Guess the letter: ").lower()  
  
  length_of_display = len(display)
  random_var = -1

  if guess in display:
    print(f"you guess the right: \"{guess}\"")

  for letter in chosen_word:
    random_var += 1
    if letter == guess:
      display[random_var] = guess

  if guess not in chosen_word:
    
    if guess in wrong_letters:
      print(f"your  {guess}, is wrong.")
    else: 
      lives -= 1
      wrong_letters.append(guess)
      string_wrong = ", ".join(wrong_letters)
      print(f"{guess} is not the word")
    

  if len(wrong_letters) != 0:
    print(f"you gussed: {string_wrong}")

  string_display = " ".join(display)
  print(string_display)
