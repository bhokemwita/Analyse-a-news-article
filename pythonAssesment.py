def read_article(filename):
    """Read the article from a file"""
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def count_specific_word(text, word):
    """Count how many times a specific word appears"""
    if not text:
        return 0
    
    # Convert to lowercase for case-insensitive counting
    text_lower = text.lower()
    word_lower = word.lower()
    
    # Split into words (simple way)
    words = text_lower.split()
    
    # Count matches
    count = 0
    for w in words:
        # Remove punctuation from the word
        clean_word = w.strip('.,!?;:"\'()[]{}<>')
        if clean_word == word_lower:
            count = count + 1
    
    return count

def identify_most_common_word(text):
    """Find the word that appears most often"""
    if not text:
        return None
    
    # Convert to lowercase and split
    text_lower = text.lower()
    words = text_lower.split()
    
    # Count each word
    word_counts = {}
    for word in words:
        # Remove punctuation
        clean_word = word.strip('.,!?;:"\'()[]{}<>')
        if clean_word:  # Make sure it's not empty
            if clean_word in word_counts:
                word_counts[clean_word] = word_counts[clean_word] + 1
            else:
                word_counts[clean_word] = 1
    
    # Find the word with highest count
    most_common = None
    highest_count = 0
    
    for word, count in word_counts.items():
        if count > highest_count:
            highest_count = count
            most_common = word
    
    return most_common

def calculate_average_word_length(text):
    """Calculate average length of words (ignoring punctuation)"""
    if not text:
        return 0.0
    
    # Split into words
    words = text.split()
    
    total_length = 0
    word_count = 0
    
    for word in words:
        # Remove punctuation
        clean_word = word.strip('.,!?;:"\'()[]{}<>')
        if clean_word:  # Only count if not empty
            total_length = total_length + len(clean_word)
            word_count = word_count + 1
    
    if word_count == 0:
        return 0.0
    
    average = total_length / word_count
    return average

def count_paragraphs(text):
    """Count paragraphs based on empty lines"""
    if not text:
        return 1
    
    # Split by double newline
    paragraphs = text.split('\n\n')
    
    # Count only paragraphs that have actual text
    count = 0
    for p in paragraphs:
        if p.strip():  # If not just empty spaces
            count = count + 1
    
    if count == 0:
        return 1
    return count

def count_sentences(text):
    """Count sentences using ., !, and ?"""
    if not text:
        return 1
    
    count = 0
    for char in text:
        if char in '.!?':
            count = count + 1
    
    if count == 0:
        return 1
    return count

# Main program
def main():
    print("=" * 50)
    print("NEWS ARTICLE TEXT ANALYSIS")
    print("=" * 50)
    
    # Read the article
    filename = "news_article.txt"
    try:
        article = read_article(filename)
        print(f"\n✓ Loaded article successfully!")
        print(f"  File: {filename}")
        print(f"  Size: {len(article)} characters\n")
    except:
        print(f"\n✗ Error: Could not find '{filename}'")
        print("  Please make sure the file exists in the same folder.")
        return
    
    # Task 1: Count specific word
    print("-" * 50)
    search_word = input("Enter a word to count: ")
    word_count = count_specific_word(article, search_word)
    print(f"  The word '{search_word}' appears {word_count} time(s)")
    
    # Task 2: Most common word
    print("-" * 50)
    common_word = identify_most_common_word(article)
    print(f"  Most common word: '{common_word}'")
    
    # Task 3: Average word length
    print("-" * 50)
    avg_length = calculate_average_word_length(article)
    print(f"  Average word length: {avg_length:.2f} characters")
    
    # Task 4: Number of paragraphs
    print("-" * 50)
    num_paragraphs = count_paragraphs(article)
    print(f"  Number of paragraphs: {num_paragraphs}")
    
    # Task 5: Number of sentences
    print("-" * 50)
    num_sentences = count_sentences(article)
    print(f"  Number of sentences: {num_sentences}")
    
    print("\n" + "=" * 50)
    print("Analysis complete!")
    print("=" * 50)

# Run the program
if __name__ == "__main__":
    main()