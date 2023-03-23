import random

lottery = set()
while len(lottery) < 6:
    print(lottery)
    ball = random.randint(1,50)
    print(f"Adding {ball}.")
    lottery.add(ball)
    print(len(lottery))
print(sorted(lottery))
print("End")

