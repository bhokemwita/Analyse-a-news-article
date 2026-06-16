# Read the article
print("Reading article...")
with open("news_article.txt", "r", encoding='utf-8') as file:
    text = file.read()

print("\n" + "="*50)
print("TEXT ANALYSIS RESULTS")
print("="*50)

# 1. Count a specific word
word_to_count = input("\nEnter a word to count: ")
count = 0
for w in text.lower().split():
    clean = w.strip('.,!?;:')
    if clean == word_to_count.lower():
        count = count + 1
print(f"'{word_to_count}' appears {count} times")

# 2. Find most common word
words = []
for w in text.lower().split():
    clean = w.strip('.,!?;:')
    if clean:
        words.append(clean)

word_counts = {}
for w in words:
    if w in word_counts:
        word_counts[w] = word_counts[w] + 1
    else:
        word_counts[w] = 1

most_common = max(word_counts, key=word_counts.get)
print(f"Most common word: '{most_common}'")

# 3. Average word length
total_length = 0
for w in words:
    total_length = total_length + len(w)
avg = total_length / len(words)
print(f"Average word length: {avg:.2f} characters")

# 4. Count paragraphs
paragraphs = text.split('\n\n')
para_count = 0
for p in paragraphs:
    if p.strip():
        para_count = para_count + 1
print(f"Number of paragraphs: {para_count}")

# 5. Count sentences
sentence_count = 0
for char in text:
    if char in '.!?':
        sentence_count = sentence_count + 1
print(f"Number of sentences: {sentence_count}")

print("="*50)