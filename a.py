import random
print('Rolling dice...')
total = 0
for i in range(1, 3):
    x = random.randint(1, 6)
    print('Die %d: %d' % (i, x))
    total += x
    time.sleep(0.5)

print('Total value: %d' % total)
