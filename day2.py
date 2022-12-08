scores = {
    "A X": 1 + 3,   # Rock / Rock (1)         = Draw (3)
    "A Y": 2 + 6,   # Rock / Paper (2)        = Win (6)
    "A Z": 3 + 0,   # Rock / Scissors (3)     = Loss (0)
    "B X": 1 + 0,   # Paper / Rock (1)        = Loss (0)
    "B Y": 2 + 3,   # Paper / Paper (2)       = Draw (3)
    "B Z": 3 + 6,   # Paper / Scissors (3)    = Win (6)
    "C X": 1 + 6,   # Scissors / Rock (1)     = Win (6)
    "C Y": 2 + 0,   # Scissors / Paper (2)    = Loss (0)
    "C Z": 3 + 3,   # Scissors / Scissors (3) = Draw (3)
}
with open('input2.txt', 'r') as f:
    lines = f.readlines()

is_success_or_chess = sum([scores[l.strip()] for l in lines])
print(f'Predict the score: {is_success_or_chess}')


