#!/usr/bin/env python3
"""CLI-Zahlenratespiel – Phase 3 (Code-Qualität & Feinschliff)."""

from __future__ import annotations

import argparse
import random

def parse_args() -> int:
    """Parst CLI-Argumente und gibt das obere Limit zurück."""
    parser = argparse.ArgumentParser(description="CLI-Zahlenratespiel")
    parser.add_argument(
        "--max", "-m",
        type=int,
        default=100,
        metavar="N",
        help="oberes Limit des Zahlenbereichs (Default: 100)",
    )
    args = parser.parse_args()
    if args.max < 1:
        parser.error("--max muss ≥ 1 sein")
    return args.max

def play_round(max_value: int = 100) -> None:
    """Spielt genau eine Runde Zahlenraten.

    Der*die Spieler*in rät so lange, bis die Zufallszahl getroffen wird.

    Args:
        max_value: Oberes Limit des Zahlenbereichs (einschließlich).

    Raises:
        ValueError: Wenn *max_value* kleiner als 1 ist.
    """
    if max_value < 1:
        raise ValueError("max_value muss ≥ 1 sein")

    secret_number: int = random.randint(1, max_value)
    attempts: int = 0

    print("\nWillkommen zum Zahlenraten-Spiel!")
    print(f"Ich habe eine Zahl zwischen 1 und {max_value} ausgewählt.")
    print("Versuche, sie zu erraten!")

    while True:
        try:
            guess: int = int(input("Gib deinen Tipp ein: "))
        except ValueError:
            print("❌ Ungültige Eingabe – bitte eine ganze Zahl eingeben.")
            continue

        if not 1 <= guess <= max_value:
            print(f"⚠️  Nur Werte von 1 bis {max_value}.")
            continue

        attempts += 1

        if guess < secret_number:
            print("zu niedrig")
        elif guess > secret_number:
            print("zu hoch")
        else:
            plural: str = "versuche" if attempts != 1 else "versuch"
            print(f"richtig! Die Zahl war {secret_number}.")
            print(f"{attempts} {plural}")
            break


def main() -> None:
    max_value = parse_args()            # ← Limit aus CLI
    print("🎲 Zahlenratespiel – viel Spaß!")
    while True:
        play_round(max_value)
        again = input("Nochmal spielen? (j/n) ").strip().lower()
        if again != "j":
            print("Danke fürs Spielen – bis bald!")
            break


if __name__ == "__main__":
    main()