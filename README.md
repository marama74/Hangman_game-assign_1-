
# Hangman Game - Terminal-Based Implementation

A modular Python Hangman game with multiple guessing methods, persistent statistics, and automatic logging.

---

## Features

- 1000+ words across 7 categories  
- Automatic input detection: single letter, multiple letters, full word  
- Scoring based on word length and wrong guesses  
- Persistent statistics and game logs  
- ASCII art hangman (7 states)  
- Modular architecture

---

## Project Structure

```

Hangman_game(assign_1)/
├── main.py
├── game/
│   ├── **init**.py
│   ├── engine.py
│   ├── wordlist.py
│   └── ascii_art.py
├── ui/
│   ├── **init**.py
│   └── display.py
├── words/
│   ├── words.txt
│   └── categories/
├── game_log/
│   ├── stats.txt
│   └── game{N}/log.txt
└── README.md

````



## Installation & Run

```bash
python main.py
````

or

```bash
cd /path/to/Hangman_game(assign_1)
python main.py
```

Supports Windows, Mac, Linux.

---

## Gameplay

1. Run the game and select a category or "All"
2. Guess letters, sequences, or full words
3. Game ends after 6 wrong guesses or when word is guessed

**Game Display Example**

```
Word: _ _ _ _ _
Guessed: a, e, l
Remaining: 4/6
ASCII Hangman displayed
```

---

## Guessing Methods

* **Single Letter:** Reveals all instances
* **Multiple Letters:** Checks each letter individually
* **Full Word:** Correct → win, Incorrect → 1 wrong guess

---

## Wordlist

* Categories: Animals, Countries, Food, Nature, Professions, Programming, Sports
* 150+ words per category, total 1050+ words
* Files: `words/categories/*.txt`, combined in `words.txt`

---

## Scoring

```
Score = (Word Length × 10) - (Wrong Guesses × 5)
Minimum = 0
```

---

## Logging

* Each game saved in `game_log/game{N}/log.txt`
* Tracks guesses, result, points, and statistics

---

## Requirements

* Python 3.6+
* Standard libraries: pathlib, random, datetime, sys
* No external dependencies

---

## Module Responsibilities

| Module            | Purpose                    |
| ----------------- | -------------------------- |
| main.py           | Game flow and menu         |
| game/engine.py    | Gameplay logic             |
| game/wordlist.py  | Word loading and selection |
| game/ascii_art.py | Hangman drawings           |
| ui/display.py     | Formatting and output      |

---

## Author

Maryam Arshad(498506) – Assignment 1, October 2025

---

## License

Educational project.


