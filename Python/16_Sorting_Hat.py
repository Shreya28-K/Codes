G=0
R=0
H=0
S=0
question=int(input('Q1) Do you like Dawn or Dusk?\n1) Dawn\n2) Dusk\n'))
if question==1:
  G+=1
  R+=1
elif question==2:
  H+=1
  S+=1
else:
  print('Wrong input.')

question=int(input('Q2) When I’m dead, I want people to remember me as: \n1) The Good\n2) The Great\n3) The Wise\n4) The Bold\n'))
if question==1:
  H+=2
elif question==2:
  S+=2
elif question==3:
  R+=2
elif question==4:
  G+=2
else:
  print('Wrong input.')

question=int(input('Q3) Which kind of instrument most pleases your ear?\n1) The violin\n2) The trumpet\n3) The piano\n4) The drum\n'))
if question==1:
  S+=4
elif question==2:
  H+=4
elif question==3:
  R+=4
elif question==4:
  G+=4
else:
  print('Wrong input.')

print('Scores')
print('🦁 Gryffindor = ',G,
'\n🦅 Ravenclaw = ',R,
'\n🦡 Hufflepuff = ',H,
'\n🐍 Slytherin = ',S)

m=max(G,H,R,S)

if m==G:
  print('G is mostly scored.')
elif m==H:
  print('H is mostly scored.')
if m==R:
  print('R is mostly scored.')
else:
  print('S is mostly scored.')

  
