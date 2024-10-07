import random 
dice_art = {1:('┌──────────┐',
               '│          │',
               '│     ●    │',
               '│          │',
               '└──────────┘'),

            2:("┌──────────┐",
               '│ ●        │',
               '│          │',
               '│        ● │',
               '└──────────┘'),

            3:("┌──────────┐",
               '│ ●      ● │',
               "│          │",
               '│     ●    │',
               '└──────────┘'),
            
            4:("┌──────────┐",
               "│ ●      ● │",
               '│          │',
               '│ ●      ● │',
               '└──────────┘'),
               
            5:("┌──────────┐",
               '│ ●      ● │',
               '│     ●    │',
               '│ ●      ● │',
               '└──────────┘'),
               
            6:("┌──────────┐",
               '│ ●      ● │',
               "│ ●      ● │",
               '│ ●      ● │',
               '└──────────┘')}

dice = []
total = 0
numOfDice = int(input('Enter the number of dice: '))

for die in range(numOfDice):
   dice.append(random.randint(1, 6))

for die in range(numOfDice):
   for x in dice_art.get(dice[die]):
      print(x)

# for line in range(5):
#     for die in dice:
#         print(dice_art.get(die)[line],end=' ')
#     print()        

for die in dice:
   total += die
print(f'Total: {total}')