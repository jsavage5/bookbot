def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    lettercount = count_letter(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()


    for key, value in lettercount.items():
        if key.isalpha():
            print(f"The '{key}' character was found {value} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_letter(text):
    counts = {}

    for char in text:
        char = char.lower()

        if char in counts:
            counts[char] +=1
        else:
            counts[char] = 1
    
    return counts


main()