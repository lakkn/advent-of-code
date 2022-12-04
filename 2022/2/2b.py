data = []
with open('2.txt') as f:
  data = f.read().split('\n')

score = 0
for round in data:
  choices = round.split(" ")
  if choices[1] == 'X':
    score += 0
    if choices[0] == 'A':
      score += 3
    elif choices[0] == 'B':
      score += 1
    else:
      score += 2
  elif choices[1] == 'Y':
    score += 3
    if choices[0] == 'B':
      score += 2
    elif choices[0] == 'C':
      score += 3
    else:
      score += 1
  else:
    score += 6
    if choices[0] == 'C':
      score += 1
    elif choices[0] == 'A':
      score += 2
    else:
      score += 3
print(score)