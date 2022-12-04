inventory = []
with open('1.txt') as f:
  text = f.read()
  inventory = text.split("\n\n")

sums = []
for value in inventory:
    food = value.split('\n')
    sum = 0
    for calorie in food:
        sum += int(calorie)
    sums.append(sum)
sums.sort()
print(sums[-1]+sums[-2]+sums[-3])