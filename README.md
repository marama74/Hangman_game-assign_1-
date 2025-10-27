# Hangman Game - Terminal-Based Implementation

A comprehensive, modular Python implementation of the classic Hangman game featuring intelligent input detection, persistent game statistics, and detailed logging capabilities.

---

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Gameplay Guide](#gameplay-guide)
- [Three Guessing Methods](#three-guessing-methods)
- [Word Database](#word-database)
- [Scoring System](#scoring-system)
- [Game Logging](#game-logging)
- [Code Architecture](#code-architecture)
- [Technical Requirements](#technical-requirements)
- [Assignment Compliance](#assignment-compliance)

---

## Overview

This Hangman game is built as a modular Python application that demonstrates clean code architecture, proper separation of concerns, and comprehensive game mechanics. The project includes over 1400 words across multiple categories and implements three different guessing methods with automatic detection.

---

## Key Features

### Game Mechanics
- **1400+ Word Database**: Extensive collection of words across 7 diverse categories
- **Intelligent Input Detection**: Automatically recognizes whether you're guessing a single letter, multiple letters, or the complete word
- **Three Guessing Methods**: Traditional single-letter guessing, multi-letter sequence guessing, and full-word guessing
- **Maximum 6 Wrong Guesses**: Classic hangman rules with 6 attempts before game over

### User Experience
- **ASCII Art Visualization**: Dynamic hangman drawing with 7 progressive states (0-6 wrong guesses)
- **Clear Game Interface**: Shows word progress, guessed letters, and remaining attempts
- **Real-time Feedback**: Instant visual and textual feedback after each guess

### Data Management
- **Persistent Statistics**: Tracks your performance across all gaming sessions
- **Automatic Game Logging**: Every game is saved with detailed information
- **Score Calculation**: Dynamic scoring based on word difficulty and performance

### Code Quality
- **Modular Architecture**: Clean separation of game logic, display, and word management
- **Error Handling**: Robust input validation and file operation error handling
- **Documentation**: Comprehensive docstrings and inline comments
- **PEP8 Compliance**: Follows Python style guidelines

---

## Project Structure

```
Hangman_game(assign_1)/
│
├── main.py                      # Entry point - orchestrates game flow
│
├── game/                        # Core game logic package
│   ├── __init__.py             # Package initializer
│   ├── engine.py               # Game engine and state management
│   ├── wordlist.py             # Word loading and random selection
│   └── ascii_art.py            # ASCII art hangman drawings
│
├── ui/                          # User interface package
│   ├── __init__.py             # Package initializer
│   └── display.py              # Display formatting and output
│
├── words/                       # Word database directory
│   ├── words.txt               # Combined master wordlist (1400+ words)
│   └── categories/             # Individual category files
│       ├── animals.txt         # 200+ animal names
│       ├── countries.txt       # 200+ country names
│       ├── food.txt            # 200+ food items
│       ├── nature.txt          # 200+ nature words
│       ├── professions.txt     # 200+ job titles
│       ├── programming.txt     # 200+ tech terms
│       └── sports.txt          # 200+ sports words
│
├── game_log/                    # Game logs (auto-created at runtime)
│   ├── stats.txt               # Persistent player statistics
│   ├── game1/                  # First game session
│   │   └── log.txt            # Detailed game 1 log
│   ├── game2/                  # Second game session
│   │   └── log.txt            # Detailed game 2 log
│   └── ...                     # Additional game sessions
│
├── combine_words.py             # Utility script to merge category files
└── README.md                    # This documentation file
```

### Directory Explanations

**game/** - Contains all core gameplay logic
- `engine.py`: Manages game state, processes guesses, calculates scores
- `wordlist.py`: Loads words from files, selects random words
- `ascii_art.py`: Provides ASCII art for visual feedback

**ui/** - Handles all display and formatting
- `display.py`: Formats game state display, word progress, statistics

**words/** - Word database storage
- Category files contain themed word lists
- `words.txt` combines all categories for "All" selection

**game_log/** - Stores game history and statistics
- Each game creates a new numbered folder
- Logs contain complete game information including moves and results

---

## Installation

### Prerequisites
- Python 3.6 or higher
- Terminal or command prompt
- Git (for cloning repository)

### Setup Steps

1. **Clone or Download the Repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/hangman-game.git
   cd hangman-game
   ```

2. **Verify Word Files Exist**
   Ensure the `words/categories/` folder contains all 7 category files with words.

3. **No Additional Installation Required**
   The game uses only Python standard libraries.

---

## How to Run

### Method 1: Direct Execution
```bash
python main.py
```

### Method 2: From Specific Path
```bash
cd C:\Users\LENOVO\Desktop\Python\Hangman_game(assign_1)
python main.py
```

### Method 3: Using Python3 (Mac/Linux)
```bash
python3 main.py
```

### Method 4: From Python Interpreter
```python
import main
main.main()
```

The game will automatically:
- Load word files from categories
- Create necessary directories (game_log)
- Initialize statistics if running for the first time
- Display the main menu

---

## Gameplay Guide

### Starting a New Game

1. **Launch the Application**
   ```bash
   python main.py
   ```

2. **Select a Category**
   ```
   CHOOSE A CATEGORY
   1. Animals
   2. Countries
   3. Food
   4. Nature
   5. Professions
   6. Programming
   7. Sports
   8. All categories (random)
   
   Choose a category (number or name): 3
   ```

3. **Begin Guessing**
   The game displays the hidden word with underscores and you can start making guesses.

### Game Interface

During gameplay, you'll see:

```
============================================================
Word: P _ _ H _ _
Guessed letters: a, e, h, p, t
Remaining attempts: 3/6

        +---+
        |   |
        O   |
       /|\  |
            |
            |
      =========

Your guess: 
```

### Game Rules

- **Objective**: Guess the hidden word before running out of attempts
- **Maximum Wrong Guesses**: 6 incorrect guesses allowed
- **Case Insensitive**: 'A' and 'a' are treated the same
- **No Penalty for Repeats**: Guessing the same letter again doesn't count as wrong
- **Win Condition**: All letters in the word are revealed
- **Lose Condition**: 6 wrong guesses reached

### Available Commands

| Input | Action |
|-------|--------|
| Single letter (e.g., `p`) | Guess one letter |
| Multiple letters (e.g., `thon`) | Guess multiple letters |
| Full word (e.g., `python`) | Guess complete word |
| `quit` | Exit current game |

---

## Three Guessing Methods

The game automatically detects which type of guess you're making based on your input length. You don't need to select a mode.

### Method 1: Single Letter Guessing (Traditional)

**How it works:** Enter one letter at a time. The game checks if that letter exists in the word and reveals all instances.

**Example:**
```
Word: _ _ _ _ _ _
Your guess: p
Result: P _ _ _ _ _

Your guess: y
Result: P Y _ _ _ _
```

**When to use:**
- When you want to play cautiously
- At the start of the game
- To maximize your score (fewer wrong guesses)

**Penalty:** If the letter is not in the word, counts as 1 wrong guess.

---

### Method 2: Multiple Letter Guessing (Sequence)

**How it works:** Enter multiple letters (not equal to word length). Each letter is checked individually, and all matching letters are revealed simultaneously.

**Example:**
```
Word: _ _ _ _ _ _  (word is "python")
Your guess: thon

Checking: t, h, o, n
Correct: t, h, o, n
Result: P Y T H O N  (if 'p' and 'y' were already guessed)
```

**Another Example:**
```
Word: _ _ _ _ _  (word is "apple")
Your guess: ple

Checking: p, l, e
Correct: p, l, e
Wrong: none
Result: A P P L E  (if 'a' was already guessed)
```

**When to use:**
- When you recognize a pattern (like word endings: -tion, -ing)
- To speed up the game
- When you're confident about multiple letters

**Penalty:** Each wrong letter counts as 1 wrong guess separately.

**Example with wrong letters:**
```
Word: _ _ _ _ _  (word is "apple")
Your guess: xyz

Checking: x, y, z
Wrong: x, y, z (3 wrong guesses added)
Result: _ _ _ _ _  (no change, wrong attempts: 3)
```

---

### Method 3: Complete Word Guessing

**How it works:** Enter a word with the same length as the target word. The game compares your guess to the actual word.

**Example:**
```
Word: _ _ _ _ _ _  (6 letters, word is "python")
Your guess: python  (6 letters)

Result: YOU WIN! (instant win)
```

**Wrong Guess Example:**
```
Word: _ _ _ _ _ _  (6 letters, word is "python")
Your guess: coding  (6 letters)

Result: Wrong! (only 1 wrong guess penalty)
```

**When to use:**
- When you're confident you know the word
- Near the end when only 1-2 letters remain
- High-risk, high-reward strategy

**Penalty:** If wrong, counts as only 1 wrong guess (not one per letter).

---

### How the Game Detects Your Input Type

| Word Length | Your Input | Detected As | Reason |
|-------------|------------|-------------|---------|
| 5 letters | `a` | Single letter | Length = 1 |
| 5 letters | `ppl` | Multiple letters | Length = 3 ≠ 5 |
| 5 letters | `apple` | Complete word | Length = 5 = 5 |
| 6 letters | `python` | Complete word | Length = 6 = 6 |
| 6 letters | `pyth` | Multiple letters | Length = 4 ≠ 6 |

---

## Word Database

### Categories Overview

The game includes 7 themed categories with over 200 words each:

| Category | Total Words | Examples | File Location |
|----------|-------------|----------|---------------|
| **Animals** | 200+ | elephant, giraffe, dolphin, penguin | `words/categories/animals.txt` |
| **Countries** | 200+ | australia, brazil, canada, india | `words/categories/countries.txt` |
| **Food** | 200+ | apple, pizza, chocolate, pasta | `words/categories/food.txt` |
| **Nature** | 200+ | mountain, ocean, forest, rainbow | `words/categories/nature.txt` |
| **Professions** | 200+ | doctor, engineer, teacher, chef | `words/categories/professions.txt` |
| **Programming** | 200+ | python, algorithm, database, code | `words/categories/programming.txt` |
| **Sports** | 200+ | basketball, tennis, soccer, hockey | `words/categories/sports.txt` |
| **Total** | **1400+** | Combined from all categories | `words/words.txt` |

### Word File Format

Each word file follows these rules:
- One word per line
- All lowercase letters
- No spaces or special characters
- No duplicate words within a category

**Example from animals.txt:**
```
elephant
giraffe
penguin
dolphin
kangaroo
```

### Adding Your Own Words

1. **Navigate to category folder:**
   ```bash
   cd words/categories/
   ```

2. **Edit the desired category file:**
   ```bash
   notepad animals.txt
   # or
   nano animals.txt
   ```

3. **Add words (one per line):**
   ```
   zebra
   koala
   panda
   ```

4. **Update the combined file (optional):**
   ```bash
   python combine_words.py
   ```
   Or the game will automatically load from category files.

### Combining Category Files

The `combine_words.py` utility script merges all category files into `words.txt`:

```bash
python combine_words.py
```

This creates/updates `words/words.txt` with all words from all categories, which is used when "All categories" is selected.

---

## Scoring System

### Scoring Formula

The game uses a dynamic scoring system that rewards longer words and penalizes wrong guesses:

```
Score = (Word Length × 10) - (Wrong Guesses × 5)

Minimum Score = 0
```

### Components

- **Base Score**: Word length multiplied by 10 points
- **Penalty**: Each wrong guess deducts 5 points
- **Losing**: If you lose the game, score = 0 (regardless of progress)

### Scoring Examples

| Word | Length | Wrong Guesses | Calculation | Final Score |
|------|--------|---------------|-------------|-------------|
| `cat` | 3 | 0 | (3 × 10) - (0 × 5) | **30** |
| `cat` | 3 | 2 | (3 × 10) - (2 × 5) | **20** |
| `cat` | 3 | 6 | Lost the game | **0** |
| `python` | 6 | 0 | (6 × 10) - (0 × 5) | **60** |
| `python` | 6 | 1 | (6 × 10) - (1 × 5) | **55** |
| `python` | 6 | 3 | (6 × 10) - (3 × 5) | **45** |
| `algorithm` | 9 | 2 | (9 × 10) - (2 × 5) | **80** |
| `algorithm` | 9 | 4 | (9 × 10) - (4 × 5) | **70** |
| `programming` | 11 | 1 | (11 × 10) - (1 × 5) | **105** |

### Strategy for High Scores

1. **Choose longer words**: Select categories with longer words for higher base scores
2. **Minimize wrong guesses**: Think carefully before guessing
3. **Use multi-letter method wisely**: Can be faster but riskier
4. **Perfect game bonus**: Zero wrong guesses gives maximum points

---

## Game Logging

### Log Structure

Every game session is automatically saved with complete details:

```
game_log/
├── stats.txt                    # Persistent statistics across all games
├── game1/                       # First game folder
│   └── log.txt                 # Detailed log for game 1
├── game2/                       # Second game folder
│   └── log.txt                 # Detailed log for game 2
├── game3/                       # Third game folder
│   └── log.txt                 # Detailed log for game 3
└── ...                          # More game folders
```

### Individual Game Log Contents

Each `game{N}/log.txt` file contains:

```
Game 3 Log
============================================================
Category: Programming
Word: python
Word Length: 6

Guesses (in order):
1. p → Correct
2. y → Correct
3. z → Wrong
4. t → Correct
5. h → Correct
6. o → Correct
7. n → Correct

Wrong Guesses List: z
Wrong Guesses Count: 1
Remaining Attempts at End: 5
Result: Win
Points Earned: 55
Total Score (after this round): 155

Games Played: 3
Wins: 2
Losses: 1
Win Rate: 66.67%

Date & Time: 2025-10-25 14:30:45
============================================================
```

### Statistics File (stats.txt)

Persistent statistics tracked across all sessions:

```
games_played: 10
wins: 7
losses: 3
total_score: 450
```

### Statistics Tracked

| Statistic | Description |
|-----------|-------------|
| **Games Played** | Total number of games completed |
| **Wins** | Number of games won |
| **Losses** | Number of games lost |
| **Total Score** | Cumulative score from all games |
| **Win Rate** | Percentage of games won (Wins / Games Played × 100) |
| **Average Score** | Average points per game (Total Score / Games Played) |

### Viewing Your Statistics

Statistics are displayed:
- After each game completion
- When you quit the game
- In the `game_log/stats.txt` file

**Example statistics display:**
```
FINAL STATISTICS
============================================================
Games played: 10
Wins: 7
Losses: 3
Win rate: 70.00%
Average score per game: 45.00
Total score: 450
============================================================
```

---

## Code Architecture

### Design Principles

The project follows these software engineering principles:

1. **Separation of Concerns**: Each module has a single, well-defined responsibility
2. **Modular Design**: Code is organized into logical, reusable components
3. **DRY (Don't Repeat Yourself)**: Common functionality is abstracted into functions
4. **Single Responsibility Principle**: Each class/function does one thing well
5. **Encapsulation**: Internal implementation details are hidden from other modules

### Module Responsibilities

| Module | Primary Responsibility | Key Functions/Methods |
|--------|------------------------|----------------------|
| **main.py** | Game flow orchestration and menu management | `main()`, `setup_directories()`, `load_stats()`, `save_stats()` |
| **game/engine.py** | Core gameplay logic and state management | `play_game()`, `_process_guess()`, `_calculate_score()`, `_save_log()` |
| **game/wordlist.py** | Word database loading and selection | `get_random_word()`, `get_categories()`, `_load_words()` |
| **game/ascii_art.py** | Visual ASCII art generation | `get_hangman_art()` |
| **ui/display.py** | User interface formatting and display | `show_game_state()`, `_get_word_progress()` |

### Data Flow Diagram

```
User Input
    ↓
main.py (orchestrates)
    ↓
WordlistManager (selects word)
    ↓
HangmanEngine (processes guess)
    ↓
Display (shows game state)
    ↓
ASCII Art (visual feedback)
    ↓
Logs (saves game data)
```

### Key Classes

#### HangmanEngine
Manages the complete game state and logic.

**Attributes:**
- `word`: The secret word to guess
- `guessed_letters`: Set of all letters guessed
- `correct_letters`: Set of correct letters found
- `wrong_count`: Number of wrong guesses
- `game_won`, `game_lost`: Game state flags

**Key Methods:**
- `play_game()`: Main game loop
- `_process_guess()`: Automatically detects and processes guess type
- `_calculate_score()`: Computes final score
- `_save_log()`: Writes game log to file

#### WordlistManager
Handles word database operations.

**Attributes:**
- `categories`: Dictionary mapping category names to word lists
- `words_dir`: Path to words directory
- `categories_dir`: Path to categories subdirectory

**Key Methods:**
- `get_random_word(category)`: Returns random word from specified category
- `get_categories()`: Lists all available categories
- `_load_words()`: Loads words from text files

#### Display
Formats and displays game information.

**Key Methods:**
- `show_game_state()`: Displays current word, guesses, and attempts
- `_get_word_progress()`: Formats word with revealed letters and underscores

---

## Technical Requirements

### Software Requirements

| Requirement | Specification |
|-------------|---------------|
| **Python Version** | 3.6 or higher |
| **Operating System** | Windows, macOS, or Linux |
| **Terminal** | Any terminal with UTF-8 support |
| **Storage** | Minimum 5 MB for word files and logs |

### Python Standard Libraries Used

All libraries are part of Python's standard library (no external dependencies):

- `pathlib`: Cross-platform file path operations
- `random`: Random word selection
- `datetime`: Timestamp generation for logs
- `sys`: System-level operations and exit handling

### Installation Verification

Check if your Python version is compatible:

```bash
python --version
# Should show: Python 3.6.x or higher
```

---

## Assignment Compliance

This project fulfills all assignment requirements:

### Core Requirements

| Requirement | Status | Implementation |
|-------------|--------|----------------|
| Modular project structure | ✓ | 5 separate modules with clear responsibilities |
| main.py as sole entry point | ✓ | Contains only high-level orchestration logic |
| 1000+ words minimum | ✓ | 1400+ words across 7 categories |
| Multiple categories | ✓ | 7 categories: Animals, Countries, Food, Nature, Professions, Programming, Sports |
| Random word selection | ✓ | Uses Python's random module for fair selection |
| Category-based selection | ✓ | User can choose specific category or "All" |
| Text-based interface | ✓ | Clear terminal-based UI with formatted output |
| Win/Lose conditions | ✓ | Win: all letters guessed; Lose: 6 wrong guesses |
| Input validation | ✓ | Validates letter input, handles repeats, case-insensitive |
| Progress tracking | ✓ | Shows word progress, guessed letters, remaining attempts |
| Clean, documented code | ✓ | PEP8 compliant with comprehensive docstrings |
| Scoring system | ✓ | Formula: (length × 10) - (wrong × 5) |
| Persistent statistics | ✓ | Tracks wins, losses, scores across sessions |
| Game logging | ✓ | Each game saved in separate folder with details |
| ASCII art | ✓ | 7-state hangman visualization |
| Uses pathlib | ✓ | All file operations use pathlib.Path |

### Additional Features

- Three guessing methods with automatic detection
- Comprehensive error handling
- Detailed game logs with timestamps
- Win rate and average score calculation
- Combine words utility script

---

## Author

**Maryam Arshad**  
Student ID: 498506  
Assignment 1 - Hangman Game  
Course: Python Programming  
Submission Date: October 2025

---

## Version History

**Version 1.0.0** - October 2025
- Initial release
- 1400+ words across 7 categories
- Three guessing methods with automatic detection
- Complete logging and statistics system
- Full documentation and code comments

---

## License

This project is developed for educational purposes as part of a course assignment.

---


