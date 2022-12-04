data = []
with open('2.txt') as f:
  data = f.read().split('\n')

score = 0
for round in data:
  choices = round.split(" ")
  if choices[1] == 'X':
    score += 1
    if choices[0] == 'A':
      score += 3
    elif choices[0] == 'B':
      score += 0
    else:
      score += 6
  elif choices[1] == 'Y':
    score += 2
    if choices[0] == 'B':
      score += 3
    elif choices[0] == 'C':
      score += 0
    else:
      score += 6
  else:
    score += 3
    if choices[0] == 'C':
      score += 3
    elif choices[0] == 'A':
      score += 0
    else:
      score += 6
print(score)