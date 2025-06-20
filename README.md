# 🎲 Zahlenratespiel (Python)

Ein kleines CLI‐Spiel: errate eine zufällig gewählte Zahl – mit
– **robustem Fehler-Handling**  
– frei wählbarem Zahlenbereich `--max`  
– automatisierten Tests (pytest) und Linter (ruff).

## Installation

```bash
git clone https://github.com/<username>/number-guessing-game.git
cd number-guessing-game
python -m venv .venv
.\.venv\Scripts\activate              # macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt       # enthält pytest, ruff, mypy



## 2 · Was gehört in die Abschnitte?

| Abschnitt | Inhalt | Häufige Fehler |
|-----------|--------|----------------|
| **Titel + 1-Satz-Pitch** | Name + Emoji, 120 Zeichen Pitch. | Zu technisch („CLI basierend auf while-Loop…“). |
| **Installation** | 4–6 Terminalzeilen – *kein Roman*. | OS-spezifische Befehle mischen; venv vergessen. |
| **Usage** | Mindestens **Basic** & **Flag-Beispiel**. | Flag unerklärt lassen; Ausgabe abschneiden. |
| **Beispiel-Output** | 4–8 Zeilen reale CLI-Session. | GIF/Screenshot ohne Textalternative. |
| **Lessons Learned** | 3–5 Bulletpoints, „Ich habe gelernt…“. | Absatzweise Tagebuch; keep it short. |
| **Lizenz / Credits** (optional) | MIT License oder CC-0. | Lizenzauswahl skippen. |

---

## 3 · Feinschliff-Tipps

1. **Verb-First**: „Errate eine Zahl…“, nicht „Dieses Projekt ist ein Spiel…“.  
2. **Codeblocks** für Terminal-Befehle → ```bash``` oder ```text```.  
3. **SVG-Badges** (optional) für Tests/ruff-Status:  

4. **Link auf CHANGELOG** und auf **Docs** (später).  
5. **Screenshot/GIF**:  
- asciinema → klein & textbasiert:  
  ```
  asciinema rec demo
  ```  
- PNG‐Screenshot – zuschneiden & beschriften.

