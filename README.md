# Python Mini Projects

Four small, self-contained command-line programs written in plain Python. They are beginner exercises in control flow, input validation and small functions, and each one runs on its own with no third-party packages.

| Script | What it does |
| --- | --- |
| `dice_rolling_game.py` | Rolls any number of six-sided dice and keeps a running count of dice rolled this session. |
| `guess_the_number.py` | Picks a secret number in a range you choose and tells you whether each guess is too low or too high, and roughly how far off. |
| `name_list_manager.py` | Menu-driven list of names: view, add, remove, clear. |
| `rock_paper_scissors.py` | Rock, paper, scissors against a random computer opponent, round after round. |

## Requirements

- Python 3.9 or newer (CI runs 3.9 and 3.12).
- No runtime dependencies; everything uses the standard library. `requirements.txt` is intentionally empty.

## Running

```bash
git clone https://github.com/ShibilAhamed701212/python_mini_projects.git
cd python_mini_projects
python dice_rolling_game.py      # or any of the other scripts
```

Every program is interactive and reads from the keyboard. `Ctrl+C` or `Ctrl+D` exits cleanly at any prompt.

## How each program behaves

### Dice Rolling Game

Asks `Roll the dice? (y/n)`, then how many dice. Zero, negative and non-numeric counts are rejected with a message.

```text
--- Professional Dice Roller ---

Roll the dice? (y/n): y
How many dice would you like to roll?: 3
Results: (3) (4) (6)
Total dice rolled in this session: 3

Roll the dice? (y/n): n
Thanks for using the Dice Roller. Goodbye!
```

### Number Guessing Game

You enter the start and end of the range (inclusive, negatives allowed; the start must be smaller than the end). After each wrong guess you get one of four hints. A guess that misses by more than a quarter of the range is "not even close" / "way off"; anything nearer is "getting closer" / "in the neighborhood". When you find the number it reports how many attempts you took and offers another round.

### Name List Manager

```text
--- Name List Manager ---
1. View Names
2. Add Name
3. Remove Name
4. Clear All Names
5. Exit
```

Names are kept in memory only and are lost when the program exits. Blank names are rejected, duplicates are allowed, removal matches the exact text (case-sensitive) and removes the first match, and clearing the list asks for confirmation.

### Rock Paper Scissors

Enter `r`, `p` or `s` (case and surrounding spaces are ignored). The program shows both choices and the result, then asks whether to play again.

```text
--- Rock Paper Scissors Game ---
Press r for Rock, p for Paper, s for Scissors: r

You chose: Rock
Computer chose: Paper
You Lose!

Do you want to play again? (y/n): n
Thanks for playing!
```

The sample outputs above were captured from real runs; the dice and the computer's choice are random, so yours will differ.

## Project structure

```text
.
├── dice_rolling_game.py
├── guess_the_number.py
├── name_list_manager.py
├── rock_paper_scissors.py
├── tests/test_mini_projects.py   # pytest suite for the game logic
├── conftest.py                   # puts the repo root on the import path for tests
├── requirements.txt              # empty: no runtime dependencies
├── requirements-dev.txt          # pytest and ruff
└── .github/workflows/ci.yml      # lint + tests on every push and pull request
```

## Testing

```bash
pip install -r requirements-dev.txt
ruff check .
pytest -q
```

The tests cover dice rolling, the rock-paper-scissors rules and input validation, integer input retries, the guessing game's hints, range check and attempt count, and a full scripted session of the name list manager. GitHub Actions runs the same commands on Python 3.9 and 3.12.

## Changes from the audit

- **Guessing game hints were wrong around zero and for negative ranges.** The old check compared a guess with half or double the secret number, so with a secret of `0` a guess of `-1` was called "not even close", and with a secret of `-5` a guess of `-4` was "way off". Hints are now based on the distance relative to the size of the range, with regression tests.
- **Ctrl+C / Ctrl+D crashed every program with a traceback.** They now exit with the program's goodbye message.
- Added the pytest suite, the CI workflow and `requirements-dev.txt`, and removed a stray garbage line from `.gitignore`.

## Known limitations

- The dice roller has no upper limit on the number of dice, so an extremely large count (millions) is slow and uses a lot of memory.
- The guessing game accepts guesses outside the chosen range without saying so.
- Nothing is saved between runs; the name list lives only in memory.

## License

The project is described as MIT-licensed, but the repository does not yet include a `LICENSE` file.
