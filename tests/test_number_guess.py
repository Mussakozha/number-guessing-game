# tests/test_number_guess.py
import builtins, importlib, random, sys
from types import ModuleType
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))          # ← stellt Import sicher

MODULE = "number_guess"                     # Dateiname ohne .py


def run_game(fake_inputs: list[str], secret: int = 42) -> list[str]:
    """Führt play_round() mit vorgegebenen Eingaben aus
       und sammelt alle Ausgaben."""
    outputs: list[str] = []
    inputs_iter = iter(fake_inputs)

    def fake_input(prompt: str = "") -> str:
        outputs.append(prompt)
        return next(inputs_iter)

    def fake_print(*args, **kwargs) -> None:
        outputs.append(" ".join(map(str, args)))

    # Modul frisch laden
    mod: ModuleType = importlib.import_module(MODULE)
    importlib.reload(mod)

    # Zufallszahl patchen
    original_randint = random.randint
    random.randint = lambda a, b: secret

    # builtins patchen
    builtin_in, builtin_out = builtins.input, builtins.print
    builtins.input, builtins.print = fake_input, fake_print
    try:
        mod.play_round()
    finally:
        builtins.input, builtins.print = builtin_in, builtin_out
        random.randint = original_randint

    return outputs


# ---------- eigentliche Tests -----------------------------------------

def test_correct_first_try() -> None:
    out = run_game(["42"])
    assert "richtig" in " ".join(out).lower()


def test_too_low_then_correct() -> None:
    out = run_game(["10", "42"])
    joined = " ".join(out).lower()
    assert "zu niedrig" in joined
    assert "richtig" in joined
    assert "2 versuch" in joined           # Prüft Zähler


def test_invalid_input_then_success() -> None:
    out = run_game(["x", "42"])
    joined = " ".join(out).lower()
    assert any(word in joined for word in ("ungültig", "invalid"))
    assert "richtig" in joined
