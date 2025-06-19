guess = 0
tries=0 # number of guessed number

while tries < 5 and   guess != 6 :
  guess = int(input("Guess the number:  "))
  tries+=1

print("You got it!")