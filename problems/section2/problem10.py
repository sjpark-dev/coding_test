n = int(input())
probs = list(map(int, input().split()))
score = 0
points = 0

for prob in probs:
    if prob:
        points += 1
    else:
        points = 0
    score += points

print(score)