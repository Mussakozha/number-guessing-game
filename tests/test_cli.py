# tests/test_cli.py
#
# Prüft, ob das CLI-Flag --max den Zahlenbereich korrekt ändert.

import builtins
import importlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

def test_max_flag_changes_range(monkeypatch):
    import number_guess

    # randint patchen, um Aufrufgrenzen zu prüfen
    called = {}
    def fake_randint(a: int, b: int) -> int:
        called["a"], called["b"] = a, b
        return b  # gibt sofort die richtige Zahl zurück

    monkeypatch.setattr(number_guess.random, "randint", fake_randint)

    # Eingaben faken: direkt '500' raten, dann 'n' → keine zweite Runde
    inputs = iter(["500", "n"])
    monkeypatch.setattr(builtins, "input", lambda _="": next(inputs))

    # CLI-Aufruf simulieren
    sys.argv = ["number_guess.py", "--max", "500"]
    importlib.reload(number_guess).main()

    # Prüfen, ob randint(1, 500) aufgerufen wurde
    assert called == {"a": 1, "b": 500}