# combine_words.py
from pathlib import Path

# Paths
base_dir = Path("words")
categories_dir = base_dir / "categories"
output_file = base_dir / "words.txt"

# Collect all words
all_words = []
category_counts = {}

# Loop through each .txt file in categories
for txt_file in categories_dir.glob("*.txt"):
    with open(txt_file, "r", encoding="utf-8") as f:
        lines = [line.strip().lower() for line in f if line.strip()]
        all_words.extend(lines)
        category_counts[txt_file.stem] = len(lines)

# Remove duplicates
unique_words = sorted(set(all_words))

# Write combined list to words.txt
with open(output_file, "w", encoding="utf-8") as f:
    for word in unique_words:
        f.write(word + "\n")

# Summary
print("Combined words successfully.\n")
print("Word counts per category:")
for cat, count in category_counts.items():
    print(f"  - {cat}: {count} words")
print(f"\nTotal unique words: {len(unique_words)}")
print(f"Saved to: {output_file}")
