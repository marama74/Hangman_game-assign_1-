"""
Display Module
Handles all game display and user interface elements.

This module is responsible for:
- Displaying game state (word progress, guessed letters, attempts)
- Formatting output for readability
- Showing progress with underscores and revealed letters
"""


class Display:
    """Handles all display-related functions for the game."""
    
    def show_game_state(self, word, guessed_letters, correct_letters, wrong_count, max_wrong):
        """
        Display current game state including word progress and statistics.
        
        Args:
            word (str): The secret word
            guessed_letters (set): All letters guessed so far
            correct_letters (set): Only correct letters
            wrong_count (int): Number of wrong guesses
            max_wrong (int): Maximum wrong guesses allowed
        """
        print("\n" + "=" * 60)
        
        # Show word progress with revealed letters
        progress = self._get_word_progress(word, correct_letters)
        print(f"📝 Word: {progress}")
        
        # Show guessed letters (sorted alphabetically)
        if guessed_letters:
            sorted_guesses = sorted(list(guessed_letters))
            print(f"🔤 Guessed letters: {', '.join(sorted_guesses)}")
        else:
            print("🔤 Guessed letters: None yet")
        
        # Show remaining attempts
        remaining = max_wrong - wrong_count
        hearts = "❤️ " * remaining + "🖤 " * wrong_count
        print(f"💔 Remaining attempts: {remaining}/{max_wrong}")
        print(f"   {hearts}")
        
        print("=" * 60)
    
    def _get_word_progress(self, word, correct_letters):
        """
        Get current word progress with revealed letters and underscores.
        
        Args:
            word (str): The secret word
            correct_letters (set): Letters that have been correctly guessed
            
        Returns:
            str: Word progress (e.g., "P Y _ H O _")
        """
        progress = []
        for letter in word:
            if letter in correct_letters:
                progress.append(letter.upper())
            else:
                progress.append('_')
        return ' '.join(progress)