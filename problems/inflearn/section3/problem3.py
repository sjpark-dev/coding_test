cards = list(range(1, 21))

for i in range(10):
    s, e = map(int, input().split())

    for j in range((e-s+1)//2):
        cards[s-1+j], cards[e-1-j] = cards[e-1-j], cards[s-1+j]

print(*cards)
