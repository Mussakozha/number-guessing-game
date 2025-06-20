import random

print("Hello World")
# This line will cause an error because 'random' is not imported
x = random.randint(1, 100)
print(f"Zufallszahl: {x}")

zahl = int(input("Gebe eine Zahl ein: "))

print("Deine Zahl ist: ", zahl)
