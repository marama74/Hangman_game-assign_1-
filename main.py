"""
Hangman Game - Main Entry Point
Assignment 1 - Terminal-based Hangman Game

This file serves as the entry point and contains only high-level game flow logic.
All implementation details are in separate modules.

Author: Your Name
Date: 2025
"""

from pathlib import Path
from game.engine import HangmanEngine
from game.wordlist import WordlistManager
from ui.display import Display
import sys


def setup_directories():
    """
    Create necessary directories if they don't exist.
    Uses pathlib with parents=True and exist_ok=True as per requirements.
    """
    Path("game_log").mkdir(parents=True, exist_ok=True)
    Path("words").mkdir(parents=True, exist_ok=True)
    Path("words/categories").mkdir(parents=True, exist_ok=True)


def load_stats(stats_file):
    """
    Load game statistics from file.
    
    Args:
        stats_file (Path): Path to statistics file
        
    Returns:
        dict: Statistics dictionary with games_played, wins, losses, total_score
    """
    default_stats = {
        'games_played': 0,
        'wins': 0,
        'losses': 0,
        'total_score': 0
    }
    
    if not stats_file.exists():
        return default_stats
    
    try:
        with open(stats_file, 'r', encoding='utf-8') as f:
            stats = {}
            for line in f:
                if ':' in line:
                    key, value = line.strip().split(':', 1)
                    stats[key.strip()] = int(value.strip())
            return stats if stats else default_stats
    except Exception as e:
        print(f"Warning: Could not load statistics: {e}")
        return default_stats


def save_stats(stats_file, stats):
    """
    Save game statistics to file for persistence.
    
    Args:
        stats_file (Path): Path to statistics file
        stats (dict): Statistics dictionary to save
    """
    try:
        with open(stats_file, 'w', encoding='utf-8') as f:
            f.write(f"games_played: {stats['games_played']}\n")
            f.write(f"wins: {stats['wins']}\n")
            f.write(f"losses: {stats['losses']}\n")
            f.write(f"total_score: {stats['total_score']}\n")
    except Exception as e:
        print(f"Warning: Could not save statistics: {e}")


def parse_category_choice(choice, categories):
    """
    Parse user's category choice from input.
    Accepts both number and category name.
    
    Args:
        choice (str): User's input
        categories (list): List of available categories
        
    Returns:
        str or None: Selected category or None if invalid
    """
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(categories):
            return categories[idx]
        elif idx == len(categories):
            return "All"
        else:
            print("❌ Invalid choice. Please try again.")
            return None
    else:
        # Check if it's a valid category name
        for cat in categories:
            if cat.lower() == choice.lower():
                return cat
        if choice.lower() == 'all':
            return "All"
        print("❌ Invalid category. Please try again.")
        return None


def display_welcome():
    """Display welcome banner with game information."""
    print("\n" + "=" * 60)
    print("🎮  WELCOME TO HANGMAN GAME  🎮".center(60))
    print("=" * 60)
    print("\n📝 How to guess:")
    print("   • Single letter: Type 'a' → reveals all 'a' in word")
    print("   • Multiple letters: Type 'apple' → checks each letter")
    print("   • Complete word: Type full word → instant win/lose")
    print("\n💡 The game automatically detects your input type!")
    print("=" * 60)


def display_final_stats(stats):
    """
    Display final game statistics when exiting.
    
    Args:
        stats (dict): Statistics dictionary
    """
    print("\n" + "=" * 60)
    print("📊 FINAL STATISTICS".center(60))
    print("=" * 60)
    print(f"🎮 Games played: {stats['games_played']}")
    print(f"🏆 Wins: {stats['wins']}")
    print(f"💔 Losses: {stats['losses']}")
    
    if stats['games_played'] > 0:
        win_rate = (stats['wins'] / stats['games_played']) * 100
        avg_score = stats['total_score'] / stats['games_played']
        print(f"📈 Win rate: {win_rate:.2f}%")
        print(f"⭐ Average score per game: {avg_score:.2f}")
    
    print(f"🎯 Total score: {stats['total_score']}")
    print("=" * 60)


def show_category_menu(categories):
    """
    Display category selection menu.
    
    Args:
        categories (list): List of available categories
    """
    print("\n" + "=" * 60)
    print("📚 CHOOSE A CATEGORY".center(60))
    print("=" * 60)
    for i, cat in enumerate(categories, 1):
        print(f"   {i}. {cat}")
    print(f"   {len(categories) + 1}. All categories (random)")
    print("\n   Type 'quit' to exit the game")
    print("=" * 60)


def main():
    """
    Main game loop - orchestrates the entire game flow.
    This function only contains high-level logic as per requirements.
    """
    # Setup
    setup_directories()
    display_welcome()
    
    # Initialize managers
    wordlist_manager = WordlistManager()
    
    # Load statistics
    stats_file = Path("game_log/stats.txt")
    stats = load_stats(stats_file)
    
    # Main game loop
    while True:
        # Show available categories
        categories = wordlist_manager.get_categories()
        show_category_menu(categories)
        
        # Get category choice
        choice = input("\n🎯 Choose a category (number or name): ").strip()
        
        if choice.lower() == 'quit':
            print("\n👋 Thanks for playing!")
            display_final_stats(stats)
            break
        
        # Parse category choice
        category = parse_category_choice(choice, categories)
        if category is None:
            continue
        
        # Start new game
        try:
            engine = HangmanEngine(wordlist_manager, category, stats)
            result = engine.play_game()
            
            # Update statistics
            stats = result['stats']
            save_stats(stats_file, stats)
            
            # Ask to play again
            print("\n" + "=" * 60)
            play_again = input("🔄 Play another round? (yes/no): ").strip().lower()
            if play_again not in ['yes', 'y']:
                print("\n👋 Thanks for playing!")
                display_final_stats(stats)
                break
                
        except Exception as e:
            print(f"\n❌ Error starting game: {e}")
            print("Please try again.")
            continue


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Game interrupted. Goodbye!")
        sys.exit(0)