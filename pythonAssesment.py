def count_specific_word(text, search_word):

    count = 0

    words = text.lower().split()

    for word in words:
        word = word.strip(".,!?")
        if word == search_word.lower():
            count += 1

    return count


def identify_most_common_word(text):

    if text.strip() == "":
        return None

    words = text.lower().split()

    counts = {}

    for word in words:
        word = word.strip(".,!?")

        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return max(counts, key=counts.get)


def calculate_average_word_length(text):

    words = []

    for word in text.split():
        cleaned = word.strip(".,!?")

        if cleaned != "":
            words.append(cleaned)

    if len(words) == 0:
        return 0

    total = 0

    for word in words:
        total += len(word)

    return total / len(words)


def count_paragraphs(text):

    if text.strip() == "":
        return 1

    paragraphs = text.strip().split("\n\n")

    return len(paragraphs)


def count_sentences(text):

    if text.strip() == "":
        return 1

    count = 0

    for character in text:
        if character in ".!?":
            count += 1

    return count

article = ""

if __name__ == "__main__":

    article = ""

    while article.strip() == "":
        article = input("Enter a news article: ")

    search_word = input("Enter a word to search for: ")

    print("\nTEXT ANALYSIS RESULTS")
    print("---------------------")
    print("Occurrences:", count_specific_word(article, search_word))
    print("Most common word:", identify_most_common_word(article))
    print("Average word length:", round(calculate_average_word_length(article), 2))
    print("Paragraphs:", count_paragraphs(article))
    print("Sentences:", count_sentences(article))
