"""
Game Engine Module
Contains the core gameplay logic for Hangman.

This module handles:
- Game state management
- Processing all types of guesses (single letter, multiple letters, full word)
- Score calculation
- Win/lose conditions
- Game logging
"""

from pathlib import Path
from datetime import datetime
from ui.display import Display
from game.ascii_art import get_hangman_art


class HangmanEngine:
    """
    Main game engine for Hangman.
    Manages game state and processes all player actions.
    """
    
    def __init__(self, wordlist_manager, category, stats):
        """
        Initialize game engine.
        
        Args:
            wordlist_manager: WordlistManager instance
            category (str): Selected category
            stats (dict): Current game statistics
        """
        self.wordlist_manager = wordlist_manager
        self.category = category
        self.stats = stats.copy()
        self.max_wrong_guesses = 6
        
        # Select word
        self.word, self.actual_category = wordlist_manager.get_random_word(category)
        self.word = self.word.lower()
        
        # Game state
        self.guessed_letters = set()
        self.correct_letters = set()
        self.wrong_guesses = []
        self.wrong_count = 0
        self.game_won = False
        self.game_lost = False
        
        # Logging
        self.guess_log = []
        self.game_number = self._get_next_game_number()
        
        # Display
        self.display = Display()
    
    def _get_next_game_number(self):
        """
        Calculate the next game number for logging.
        
        Returns:
            int: Next game number
        """
        game_log_dir = Path("game_log")
        existing_games = [
            d for d in game_log_dir.iterdir() 
            if d.is_dir() and d.name.startswith('game')
        ]
        
        if not existing_games:
            return 1
        
        numbers = []
        for game_dir in existing_games:
            try:
                num = int(game_dir.name.replace('game', ''))
                numbers.append(num)
            except ValueError:
                continue
        
        return max(numbers) + 1 if numbers else 1
    
    def play_game(self):
        """
        Main game loop - runs until game is won or lost.
        
        Returns:
            dict: Game result with stats and outcome
        """
        print(f"\n🎲 New word selected from '{self.actual_category}' category")
        print(f"📏 Word length: {len(self.word)} letters")
        print(f"❤️  You have {self.max_wrong_guesses} wrong guesses allowed\n")
        
        # Main game loop
        while not self.game_won and not self.game_lost:
            # Display current state
            self.display.show_game_state(
                self.word,
                self.guessed_letters,
                self.correct_letters,
                self.wrong_count,
                self.max_wrong_guesses
            )
            
            # Show ASCII art
            print(get_hangman_art(self.wrong_count))
            
            # Get user input
            print("💡 Enter your guess:")
            print("   • Single letter (e.g., 'a')")
            print("   • Multiple letters (e.g., 'pple' or 'apple')")
            print("   • Type 'quit' to exit")
            
            user_input = input("\n🎯 Your guess: ").strip().lower()
            
            if user_input == 'quit':
                print("\n🚪 Game terminated by user.")
                self.game_lost = True
                break
            
            # Process input automatically based on length and content
            self._process_guess(user_input)
        
        # Game over
        return self._end_game()
    
    def _process_guess(self, guess):
        """
        Automatically process guess based on input.
        Detects whether it's a single letter, multiple letters, or full word.
        
        Args:
            guess (str): User's guess input
        """
        # Validation
        if not guess:
            print("❌ Empty input. Please enter a guess.")
            return
        
        if not guess.isalpha():
            print("❌ Invalid input. Please enter only letters.")
            return
        
        # Determine guess type and process
        if len(guess) == 1:
            # Single letter guess
            self._handle_single_letter(guess)
        elif len(guess) == len(self.word):
            # Likely a full word guess
            self._handle_full_word_guess(guess)
        else:
            # Multiple letters (partial word)
            self._handle_multiple_letters(guess)
    
    def _handle_single_letter(self, letter):
        """
        Handle a single letter guess.
        
        Args:
            letter (str): Single letter guessed
        """
        # Check if already guessed
        if letter in self.guessed_letters:
            print(f"ℹ️  You already guessed '{letter}'. Try a different letter.")
            return
        
        # Process guess
        self.guessed_letters.add(letter)
        
        if letter in self.word:
            self.correct_letters.add(letter)
            count = self.word.count(letter)
            print(f"✅ Correct! '{letter}' appears {count} time(s) in the word.")
            self.guess_log.append((letter, True))
            
            if self._check_win():
                self.game_won = True
        else:
            self.wrong_guesses.append(letter)
            self.wrong_count += 1
            print(f"❌ Wrong! '{letter}' is not in the word.")
            self.guess_log.append((letter, False))
            
            if self.wrong_count >= self.max_wrong_guesses:
                self.game_lost = True
    
    def _handle_multiple_letters(self, letters):
        """
        Handle multiple letters guess (sequence/adjoining).
        Each letter is checked individually.
        
        Args:
            letters (str): Multiple letters to guess
        """
        print(f"\n🔤 Checking letters: {letters.upper()}")
        
        new_correct = []
        new_wrong = []
        already_guessed = []
        
        for letter in letters:
            if letter in self.guessed_letters:
                already_guessed.append(letter)
                continue
            
            self.guessed_letters.add(letter)
            
            if letter in self.word:
                if letter not in self.correct_letters:
                    self.correct_letters.add(letter)
                    new_correct.append(letter)
            else:
                if letter not in self.wrong_guesses:
                    self.wrong_guesses.append(letter)
                    self.wrong_count += 1
                    new_wrong.append(letter)
        
        # Report results
        if already_guessed:
            print(f"ℹ️  Already guessed: {', '.join(already_guessed)}")
        if new_correct:
            print(f"✅ Correct letters: {', '.join(new_correct)}")
        if new_wrong:
            print(f"❌ Wrong letters: {', '.join(new_wrong)}")
        if not new_correct and not new_wrong and not already_guessed:
            print("ℹ️  No new information.")
        
        # Log as multi-letter guess
        self.guess_log.append((f"MULTI:{letters}", len(new_correct) > 0))
        
        # Check conditions
        if self._check_win():
            self.game_won = True
        elif self.wrong_count >= self.max_wrong_guesses:
            self.game_lost = True
    
    def _handle_full_word_guess(self, guess):
        """
        Handle complete word guess.
        
        Args:
            guess (str): Complete word guess
        """
        print(f"\n📝 Guessing complete word: {guess.upper()}")
        
        if guess == self.word:
            # Correct - instant win
            self.correct_letters = set(self.word)
            self.guessed_letters = set(self.word)
            self.game_won = True
            print(f"🎉 Correct! You guessed the word!")
            self.guess_log.append((f"WORD:{guess}", True))
        else:
            # Wrong - counts as 1 wrong guess
            self.wrong_count += 1
            self.wrong_guesses.append(f"WORD:{guess}")
            print(f"❌ Wrong! '{guess}' is not the word.")
            self.guess_log.append((f"WORD:{guess}", False))
            
            if self.wrong_count >= self.max_wrong_guesses:
                self.game_lost = True
    
    def _check_win(self):
        """
        Check if player has won.
        
        Returns:
            bool: True if all letters guessed
        """
        for letter in self.word:
            if letter not in self.correct_letters:
                return False
        return True
    
    def _calculate_score(self):
        """
        Calculate score using formula: (length * 10) - (wrong * 5).
        
        Returns:
            int: Calculated score (minimum 0)
        """
        if not self.game_won:
            return 0
        
        base_score = len(self.word) * 10
        penalty = self.wrong_count * 5
        score = max(0, base_score - penalty)
        return score
    
    def _end_game(self):
        """
        Handle game end - display results, update stats, save log.
        
        Returns:
            dict: Game result
        """
        score = self._calculate_score()
        
        # Update statistics
        self.stats['games_played'] += 1
        if self.game_won:
            self.stats['wins'] += 1
            self.stats['total_score'] += score
            print(f"\n🎉 YOU WIN! The word was: {self.word.upper()}")
            print(f"⭐ Points earned: {score}")
        else:
            self.stats['losses'] += 1
            print(f"\n💔 YOU LOSE! The word was: {self.word.upper()}")
            print(f"⭐ Points earned: 0")
        
        # Display statistics
        self._display_stats()
        
        # Save log
        self._save_log(score)
        
        return {
            'won': self.game_won,
            'word': self.word,
            'score': score,
            'stats': self.stats
        }
    
    def _display_stats(self):
        """Display current game statistics."""
        print(f"\n📊 Current Statistics:")
        print(f"   Total score: {self.stats['total_score']}")
        print(f"   Games: {self.stats['games_played']} | Wins: {self.stats['wins']} | Losses: {self.stats['losses']}", end="")
        
        if self.stats['games_played'] > 0:
            win_rate = (self.stats['wins'] / self.stats['games_played']) * 100
            avg_score = self.stats['total_score'] / self.stats['games_played']
            print(f" | Win rate: {win_rate:.2f}%")
            print(f"   Average score: {avg_score:.2f}")
        else:
            print()
    
    def _save_log(self, score):
        """
        Save detailed game log to file.
        
        Args:
            score (int): Score for this game
        """
        game_dir = Path(f"game_log/game{self.game_number}")
        game_dir.mkdir(parents=True, exist_ok=True)
        
        log_file = game_dir / "log.txt"
        
        try:
            with open(log_file, 'w', encoding='utf-8') as f:
                f.write(f"Game {self.game_number} Log\n")
                f.write("=" * 60 + "\n")
                f.write(f"Category: {self.actual_category}\n")
                f.write(f"Word: {self.word}\n")
                f.write(f"Word Length: {len(self.word)}\n\n")
                
                f.write("Guesses (in order):\n")
                for i, (guess, correct) in enumerate(self.guess_log, 1):
                    status = "Correct" if correct else "Wrong"
                    f.write(f"{i}. {guess} → {status}\n")
                
                f.write(f"\nWrong Guesses List: {', '.join(self.wrong_guesses) if self.wrong_guesses else 'None'}\n")
                f.write(f"Wrong Guesses Count: {self.wrong_count}\n")
                f.write(f"Remaining Attempts at End: {self.max_wrong_guesses - self.wrong_count}\n")
                f.write(f"Result: {'Win' if self.game_won else 'Loss'}\n")
                f.write(f"Points Earned: {score}\n")
                f.write(f"Total Score (after this round): {self.stats['total_score']}\n\n")
                
                f.write(f"Games Played: {self.stats['games_played']}\n")
                f.write(f"Wins: {self.stats['wins']}\n")
                f.write(f"Losses: {self.stats['losses']}\n")
                
                if self.stats['games_played'] > 0:
                    win_rate = (self.stats['wins'] / self.stats['games_played']) * 100
                    f.write(f"Win Rate: {win_rate:.2f}%\n")
                
                f.write(f"\nDate & Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=" * 60 + "\n")
                
            print(f"Game log saved to: {log_file}")
                
        except Exception as e:
            print(f" Warning: Could not save log: {e}")