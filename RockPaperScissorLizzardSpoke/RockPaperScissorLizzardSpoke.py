# Write code below 💖
import random

player = 0
computer = 0
option = ['✊', '✋', '✌️', '🦎', '🖖']
winTable =  [[0, -1, 1, 1, -1],[1, 0, -1, -1, 1],[-1, 1, 0, 1, -1],
            [-1, 1, -1, 0, 1],[1, -1, 1, -1, 0]]

print("================================")
print("Rock Paper Scissors Lizard Spock")
print("================================")
for i in range(5):
  print(f'{i + 1}) {option[i]}')

while player < 1 or player > 5:
  player = int(input('Pick a number: '))
  if player < 1 or player > 5:
    print("Not a valid choice, try again")
  else:
    print(f'\nYou chose: {option[player - 1]}')

computer = random.randint(1,5)
print(f'CPU chose: {option[computer -1]}')

if winTable[player - 1][computer -1] == 1:
  print("The player won!")
elif winTable[player - 1][computer -1] == -1:
  print("The CPU won!")
else:
  print("It's a tie!")