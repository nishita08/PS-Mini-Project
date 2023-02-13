ROLL 2 !!!
# dice.py
import random

DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "

# ...

import random

input("YOUR GOOD NAME:")



#d = pygame.display.set_mode((size, size))
#d.fill(diecol)
#pygame.display.set_caption("Dice Simulator")


def roll():
  return random.sample([1,2,3,4,5,6,],1)[0]

def chk_odd_or_even(val):
  if val%2==0:
    return True
  else:
    return False

def chk_2_or_4(val):
  if val==2 or val==4:
    return True
  else:
    return False

def chk_2(val):
  if val==2:
    return True
  else:
    return False

def play(level):
  if level == 1:
    val = roll()
    img = DICE_ART[val]
    for line in img:
      print(line)
    return chk_odd_or_even(val)

  elif level==2:
    val = roll()
    img = DICE_ART[val]
    for line in img:
      print(line)
    return chk_2_or_4(val)

  else:
    val = roll()
    img = DICE_ART[val]
    for line in img:
      print(line)
    return chk_2(val)

def main():
  level = 1
  success = play(level)
  if success:
    level = 2
    success = play(level)
    if success:
      level = 3
      success = play(level)
      if success:
        print("You won the game")
      else:
         print("You lost the game")
    else:
         print("You lost the game")
  else:
      print("You lost the game")

main()

print("HAVE A GREAT DAY")
