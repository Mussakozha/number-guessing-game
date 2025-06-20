#!/usr/bin/env python3
# number_guess.py
import random


def play_round(max_value: int = 100) -> None:
    """Eine Runde Zahlenraten."""
    secret_number = random.randint(1, max_value)
    attempts = 0
    print(f"Ich habe eine Zahl zwischen 1 und {max_value} gewählt.")

    while True:
        try:
            guess = int(input("➡️  Dein Tipp: "))
        except ValueError:
            print("❌ Bitte eine ganze Zahl eingeben.")
            continue

        if not 1 <= guess <= max_value:
            print(f"⚠️  Nur Werte zwischen 1 und {max_value}.")
            continue

        attempts += 1

        if guess < secret_number:
            print("zu niedrig")
        elif guess > secret_number:
            print("zu hoch")
        else:
            print(f"richtig! Du brauchtest {attempts} Versuche.")
            break


def main() -> None:
    """Startet das Spiel und fragt nach weiteren Runden."""
    print("🎲 Willkommen beim Zahlenratespiel!")
    while True:
        play_round()
        again = input("Nochmal spielen? (j/n) ").strip().lower()
        if again != "j":
            print("Auf Wiedersehen!")
            break


if __name__ == "__main__":
    main()
