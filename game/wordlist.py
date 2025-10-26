"""
Wordlist Manager Module
Handles loading words from files and random selection.

This module is responsible for:
- Loading words from category files
- Random word selection
- Category management
"""

from pathlib import Path
import random


class WordlistManager:
    """Manages word database and selection."""
    
    def __init__(self):
        """Initialize wordlist manager and load words."""
        self.words_dir = Path("words")
        self.categories_dir = self.words_dir / "categories"
        self.all_words_file = self.words_dir / "words.txt"
        
        self.categories = {}
        self._load_words()
    
    def _load_words(self):
        """Load words from all category files."""
        print("\n📚 Loading word files...")
        
        # Define expected category files based on your structure
        category_files = {
            'Animals': 'animals.txt',
            'Countries': 'countries.txt',
            'Food': 'food.txt',
            'Nature': 'nature.txt',
            'Professions': 'professions.txt',
            'Programming': 'programming.txt',
            'Sports': 'sports.txt'
        }
        
        # Load each category file
        for category, filename in category_files.items():
            filepath = self.categories_dir / filename
            if filepath.exists():
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        words = [line.strip().lower() for line in f if line.strip()]
                        if words:
                            self.categories[category] = words
                            print(f"✅ Loaded {len(words)} words from {category}")
                        else:
                            print(f"⚠️  Warning: {filename} is empty")
                except Exception as e:
                    print(f"❌ Error loading {filename}: {e}")
            else:
                print(f"⚠️  Warning: {filename} not found in words/categories/")
        
        # Load main words.txt file
        if self.all_words_file.exists():
            try:
                with open(self.all_words_file, 'r', encoding='utf-8') as f:
                    all_words = [line.strip().lower() for line in f if line.strip()]
                    if all_words:
                        self.categories['All'] = all_words
                        print(f"✅ Loaded {len(all_words)} total words from words.txt")
                    else:
                        print(f"⚠️  Warning: words.txt is empty")
            except Exception as e:
                print(f"❌ Error loading words.txt: {e}")
        else:
            # If words.txt doesn't exist, combine all category words
            print("ℹ️  words.txt not found. Combining category words...")
            all_words = []
            for words in self.categories.values():
                all_words.extend(words)
            if all_words:
                self.categories['All'] = all_words
                print(f"✅ Combined {len(all_words)} words from all categories")
        
        # Check if any words were loaded
        if not self.categories:
            print("\n❌ ERROR: No word files found!")
            print("Please ensure you have word files in:")
            print(f"   {self.categories_dir.absolute()}")
            print("\nExpected files:")
            for filename in category_files.values():
                print(f"   - {filename}")
            raise FileNotFoundError("No word files found. Please create word files in words/categories/")
        
        # Display summary
        total_words = len(self.categories.get('All', []))
        print(f"\n📊 Total words available: {total_words}")
        print(f"✅ Categories loaded: {len([c for c in self.categories.keys() if c != 'All'])}")
    
    def get_categories(self):
        """
        Get list of available categories (excluding 'All').
        
        Returns:
            list: List of category names
        """
        return sorted([cat for cat in self.categories.keys() if cat != 'All'])
    
    def get_random_word(self, category='All'):
        """
        Get a random word from specified category.
        
        Args:
            category (str): Category name or 'All'
            
        Returns:
            tuple: (word, actual_category)
        """
        if category == 'All':
            # Select from all words
            if 'All' in self.categories and self.categories['All']:
                word = random.choice(self.categories['All'])
                actual_category = self._find_word_category(word)
                return word, actual_category
            else:
                # Fallback: combine all category words
                all_words = []
                for cat, words in self.categories.items():
                    if cat != 'All':
                        all_words.extend(words)
                if all_words:
                    word = random.choice(all_words)
                    actual_category = self._find_word_category(word)
                    return word, actual_category
                else:
                    raise ValueError("No words available in any category")
        
        # Select from specific category
        if category in self.categories and self.categories[category]:
            word = random.choice(self.categories[category])
            return word, category
        else:
            available = ', '.join(self.get_categories())
            raise ValueError(f"Category '{category}' not found. Available: {available}")
    
    def _find_word_category(self, word):
        """
        Find which category a word belongs to.
        
        Args:
            word (str): Word to search for
            
        Returns:
            str: Category name or 'Unknown'
        """
        word = word.lower()
        for category, words in self.categories.items():
            if category != 'All' and word in words:
                return category
        return 'Unknown'
    
    def get_word_count(self):
        """
        Get total word count.
        
        Returns:
            int: Total number of unique words
        """
        if 'All' in self.categories:
            return len(self.categories['All'])
        else:
            all_words = set()
            for words in self.categories.values():
                all_words.update(words)
            return len(all_words)