# display ASCII art for the title
print(r'''
 _______    ________   ___ __ __   ______       ______   ___   ___   ______   __ __ __     
/______/\  /_______/\ /__//_//_/\ /_____/\     /_____/\ /__/\ /__/\ /_____/\ /_//_//_/\     /__/\     
\::::__\/__\::: _  \ \\::\| \| \ \\::::_\/_    \::::_\/_\::\ \\  \ \\:::_ \ \\:\\:\\:\ \    \.:\ \    
 \:\ /____/\\::(_)  \ \\:.      \ \\:\/___/\    \:\/___/\\::\/_\ .\ \\:\ \ \ \\:\\:\\:\ \    \::\ \   
  \:\\_  _\/ \:: __  \ \\:.\-/\  \ \\::___\/_    \_::._\:\\:: ___::\ \\:\ \ \ \\:\\:\\:\ \    \__\/_  
   \:\_\ \ \  \:.\ \  \ \\. \  \  \ \\:\____/\     /____\:\\: \ \\::\ \\:\_\ \ \\:\\:\\:\ \     /__/\ 
    \_____\/   \__\/\__\/ \__\/ \__\/ \_____\/     \_____\/ \__\/ \::\/ \_____\/ \_______\/     \__\/''')
# Introduce the game with instructions
print("Welcome to Misnomer Names! Our most popular quiz show!")
print()
print("Test your knowledge of commonly used misleading names by answering True or False questions. Please only answer with a 'T' or 'F' when you are prompted for an answer. Good luck!")
print()
print(" = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
# Create first tuple list and variable name to hold questions
Questions = ("Q1. Pencils contain graphite in them.", "Q2. Cotton Candy consists of a network of small, edible, cotton fibers.", "Q3. Ice cream has ice in it.", "Q4. Fireflies are beetles and not flies", "Q5. A cat burglar is someone who steal rare breeds of cats.", "Q6. Buffalo wings contain buffalo meat.", "Q7. Scotch tape was invented in Scotland.", "Q8. Water closet refers to a place where you hang up your wet bathing suit.", "Q9. An ascot is a flag a mascot waves around.", "Q10. Tuppence refers to the original name for tupperware.")
# Create second tuple list and variable name to hold answers
Answers = ("T", "F", "T", "T", "F", "F", "F", "F", "F", "F")
# Create variable name for dummy value for userinput
UserAnswer = ""
# Create variable name for correctly guessed questions 
NumberOfCorrect = 0
# Create variable name for the length of items in the tuple named 'Questions' 
NumberOfQuestions = len(Questions)   
# Set up a 'for' loop to go through each item in the 'question' tuple & create variable name to represent each item
for index in range(NumberOfQuestions):
   # print each question individually (one at a time)
  print(Questions[index])
  #Set up a 'while' loop to check for correct user input: that will repeat the prompt to enter an accepted form of response 
  UserAnswer = input("Please enter a 'T' for true or an 'F' for false: ")
  print()
  while(UserAnswer != 'T' and UserAnswer != 'F'):
    UserAnswer = input("Please enter a 'T' for true or an 'F'for false: ")
  # Create a variable to show that a correct answer lines up with each item in the Answers tuple
    print()
  CorrectAnswer = Answers[index]     
  #'if' statement for when user guesses right answer
  if(UserAnswer == CorrectAnswer):
      # Using already created variable name to keep track of each correct user guess as a total
    NumberOfCorrect += 1
    
print()     
print(f"You got {NumberOfCorrect} out of 3 correct! Thanks for playing!")